# PagerDuty

#Pending rewrite

This pack enables the integration of PagerDuty into StackStorm. 

# Configuration

To create and install the config file, you can run:

`st2 pack config pagerduty`

Alternatively, you can copy the example configuration in
[pagerduty.yaml.example](./pagerduty.yaml.example)
to `/opt/stackstorm/configs/pagerduty.yaml` and edit as required.

* `api_key:` API-KEY
* `service_key:` SERVICE-KEY
* `debug:` optional debug flag. Set to True for additional logging

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

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

# ChatOps

The following chatops action aliases are defined:

* `get open incidents`
* `create incident {{description}}`
* `ack incident ids {{ids}} with {{email}}`
* `resolve incident ids {{ids}} with {{email}}`

`{{ids}}` is a comma separated list of incident ids, and `{{email}}` is the email address of the
user acknowledging or resolving the incident. `{{description}}` is the title of the incident.

# Running Create actions

Create actions require a JSON object with the details for the resource being created. 
A JSON Schema is present on all `create` actions to help enforce requirements and inform structure.
These schemas match the PagerDuty API 'request schema' documentation.