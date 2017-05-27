# PagerDuty

This action enables the integration of PagerDuty into StackStorm. It is capable of performing the following actions:

1. List all the open incidents on PD (for a given api key)

```
st2 run pagerduty.get_open_incidents
```

2. Launch an incident by giving its details and description

```
st2 run pagerduty.launch_incident description='<incident title>'
```

3. Send acknowledgment of any incident(s)

```
st2 run pagerduty.ack_incident email='<email>' ids=<comma separated list of incident ids>
```

4. Resolve acknowledged incident(s)

```
st2 run pagerduty.resolve_incident email='<email>' ids=<comma separated list of incident ids>
```

# Configuration

To create and install the config file, you can run:

```
st2 pack config pagerduty
```

Alternatively, you can copy the example configuration in
[pagerduty.yaml.example](./pagerduty.yaml.example)
to `/opt/stackstorm/configs/pagerduty.yaml` and edit as required.

* `api_key:` API-KEY
* `service_api:` SERVICE-API
* `debug:` optional debug flag. Set to True for additional logging

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

## Retrieving API Key from PagerDuty

* Sign into PagerDuty
* Head to `API Access` tab and navigate to the `New API` section
* Enter a description for the API key, and click `Create API Key`.
* Copy and paste the API key into `pagerduty.yaml`

## Retrieving Service Key from PagerDuty

* Sign into PagerDuty
* Head to the `Services` tab and click on `Add New Service`.
* Enter a name for the new service, and ensure the `Use our API directly` radio button is selected.
* Click `Add Service`.
* Copy and paste the service key into `pagerduty.yaml`
