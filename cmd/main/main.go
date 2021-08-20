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

func main() {
	connectionTypes := map[string]connections.Connection{
		pagerduty: {
			Name:      pagerduty,
			Fields:    nil,
			Reference: pagerduty,
		},
	}

	metadata := openapi_sdk.PluginMetadata{
		Name:           pagerduty,
		Provider:       pagerduty,
		MaskFile:       "mask.yaml",
		OpenApiFile:    "pagerduty-openapi.yaml",
		Tags:           []string{pagerduty},
		HeaderPrefixes: map[string]string{"AUTHORIZATION":"Token token="},
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

func AuthTest(ctx *plugin.ActionContext) (bool,[]byte) {

	var data map[string]interface{}

	req, _ := http.NewRequest(http.MethodGet, "https://api.pagerduty.com/services", nil)

	response, err := openapi_sdk.ExecuteRequest(ctx, req, pagerduty, map[string]string{"AUTHORIZATION":"Token token="},30 )
	if err != nil {
		return false, []byte(err.Error())
	}

	json.Unmarshal(response, &data)

	return Validate(data)

}

func Validate(json openapi_sdk.JSONMap)(bool, []byte){
	m := json.(map[string]interface{})["error"]

	if m != nil {
		m := m.(map[string]interface{})
		return false, []byte(m["message"].(string))
	}

	return true, nil
}