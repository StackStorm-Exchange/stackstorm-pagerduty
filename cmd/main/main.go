package main

import (
	openapi_sdk "github.com/blinkops/blink-openapi-sdk/plugin"
	plugin_sdk "github.com/blinkops/blink-sdk"
	"github.com/blinkops/blink-sdk/plugin/connections"
	log "github.com/sirupsen/logrus"
)

const (
	pagerduty = "pagerduty"
)

func main() {
	pagerdutyOpenApi := "pagerduty-openapi.yaml"
	maskFile := "mask.yaml"
	connectionTypes := map[string]connections.Connection{
		pagerduty: {
			Name:      pagerduty,
			Fields:    nil,
			Reference: pagerduty,
		},
	}

	pagerdutyPlugin, err := openapi_sdk.NewOpenApiPlugin(pagerduty, pagerduty, []string{pagerduty}, connectionTypes, pagerdutyOpenApi, maskFile)

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
