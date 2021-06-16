FROM blinkops/blink-stackstorm-base:1.0.9 AS plugin

ENV PACK_NAME=pagerduty

COPY plugin.yaml config.yaml config.schema.yaml requirements.txt ./
COPY actions/ actions/
