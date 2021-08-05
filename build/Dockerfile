FROM golang:1.16.3 AS builder

WORKDIR /go/src/github.com/blinkops/blink-pagerduty
COPY .. .

RUN go build -tags netgo -ldflags '-w -extldflags "-static"' -o /go/bin/blink-pagerduty ./cmd/main

FROM alpine:3.14.0 AS plugin

WORKDIR /blink-pagerduty
COPY --from=builder /go/bin/blink-pagerduty .
COPY --from=builder /go/src/github.com/blinkops/blink-pagerduty/pagerduty-openapi.yaml .
COPY --from=builder /go/src/github.com/blinkops/blink-pagerduty/mask.yaml .

# Expose the gRPC port
EXPOSE 1337

RUN chmod a+x blink-pagerduty

ENTRYPOINT ./blink-pagerduty
