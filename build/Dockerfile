FROM blinkops/blink-stackstorm-base:1.0-add-default-action-param-value.13 AS plugin

ENV PACK_NAME=pagerduty

COPY plugin.yaml config.yaml config.schema.yaml requirements.txt ./
COPY actions/ actions/

RUN pip install -r requirements.txt
