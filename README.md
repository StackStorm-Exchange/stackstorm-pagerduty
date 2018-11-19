# PagerDuty

This pack enables the integration of PagerDuty into StackStorm. 

# Configuration

To create and install the config file, you can run:

`st2 pack config pagerduty`

Alternatively, you can copy the example configuration in
[pagerduty.yaml.example](./pagerduty.yaml.example)
to `/opt/stackstorm/configs/pagerduty.yaml` and edit as required.

* `api_key:` API-KEY
* `service_key:` SERVICE-KEY (Used as default for incident creation via the Events API)
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

The following ChatOps action aliases are defined:

launch_incident: Launch a new Incident via the Events API
* `create incident {{description}}`
get_open_incidents: Find incidents by Status (Default is effectively 'open incidents')
* `get open incidents {{statuses=[triggered,acknowledged]}}`
acknowledge_incident: Acknowledge an Incident via the REST API
* `ack incident id {{entity_id}} from {{from_email}}`
resolve: Resolve an Incident via the REST API
* `resolve incident id {{entity_id}} from {{from_email}}`

 `{{description}}` is the title of the incident.  
 `{{from_email}}` is the email address of a valid user on your PD account for `acknowledge` or `resolve`  
 * Recommended: Create your own Alias/workflow that ties the API (chat) user to this field automatically.

# Running Create actions

All Create actions require a JSON object with the details for the resource being created. 
A JSON Schema is present on all `create` actions to help enforce requirements and inform structure.
These schemas match the PagerDuty API 'request schema' documentation. These are intended to be used by workflows and in programmatic ways.

Some create actions also have a similarly named `.simple` version which provides a more form based input of required fields and commonly used optional fields. These will cover many use cases and provide a preformatted version of the non `simple` action. These are intended to be used by Action Aliases and Humans

# Rest API Vs Events API

Pagerduty has two primary types of API; A traditional RESTful API and an Events API.

The Events API was designed specifically for handling Incident creation, acknowledgment, and resolution. 
Read more about the Events API [here.](https://v2.developer.pagerduty.com/docs/events-api)

Currently pypd only supports the mode `trigger` (create) on only the Events V1 API. Once pypd is updated to support the Events V2 API, corresponding actions can be updated.

# Creating Incidents

Because incidents can be created via both APIs, actions have been included that can be used to create incidents in the way that makes the most sense for you. Read about the differences between these APIs to help influence your decision.
