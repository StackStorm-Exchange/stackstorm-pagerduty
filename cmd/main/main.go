package main

import (
	"encoding/json"
	openapi_sdk "github.com/blinkops/blink-openapi-sdk/plugin"
	plugin_sdk "github.com/blinkops/blink-sdk"
	"github.com/blinkops/blink-sdk/plugin"
	"github.com/blinkops/blink-sdk/plugin/connections"
	log "github.com/sirupsen/logrus"
	"net/http"
)

const (
	pagerduty = "pagerduty"
)

var prefixes = openapi_sdk.HeaderValuePrefixes{"AUTHORIZATION": "Token token="}
var headerAlias = openapi_sdk.HeaderAlias{"API ACCESS KEY": "AUTHORIZATION"}

func main() {
	connectionTypes := map[string]connections.Connection{
		pagerduty: {
			Name:      pagerduty,
			Fields:    nil,
			Reference: pagerduty,
		},
	}

	metadata := openapi_sdk.PluginMetadata{
		Name:                pagerduty,
		Provider:            pagerduty,
		MaskFile:            "mask.yaml",
		OpenApiFile:         "pagerduty-openapi.yaml",
		Tags:                []string{pagerduty},
		HeaderValuePrefixes: prefixes,
		HeaderAlias:         headerAlias,
	}
	checks := openapi_sdk.PluginChecks{
		TestCredentialsFunc:
		func(ctx *plugin.ActionContext) (*plugin.CredentialsValidationResponse, error) {
			value, err := AuthTest(ctx)

			return &plugin.CredentialsValidationResponse{
				AreCredentialsValid:   value,
				RawValidationResponse: err,
			}, nil
		},

		ValidateResponse: Validate,
	}

	pagerdutyPlugin, err := openapi_sdk.NewOpenApiPlugin(connectionTypes, metadata, checks)

	if err != nil {
		log.Error("Failed to create pagerduty integration: ", err)
		panic(err)
	}

	err = plugin_sdk.Start(pagerdutyPlugin)
	if err != nil {
		log.Error("Failed to start pagerduty integration: ", err)
		panic(err)
	}
}

func AuthTest(ctx *plugin.ActionContext) (bool, []byte) {

	req, _ := http.NewRequest(http.MethodGet, "https://api.pagerduty.com/services", nil)

	response, err := openapi_sdk.ExecuteRequest(ctx, req, pagerduty, prefixes, headerAlias, 30)
	if err != nil {
		return false, []byte(err.Error())
	}

	return Validate(response)

}

func Validate(res openapi_sdk.Result) (bool, []byte) {
	var data map[string]interface{}

	if res.StatusCode == http.StatusBadRequest {
		return false, res.Body
	}

	err := json.Unmarshal(res.Body, &data)
	if err != nil {
		return false, []byte("error validating json")
	}
	m := data["error"]

	if m != nil {
		m := m.(map[string]interface{})
		return false, []byte(m["message"].(string))
	}

	return true, nil
}
