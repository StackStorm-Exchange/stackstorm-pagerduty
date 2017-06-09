# PagerDuty

This action enables the integration of PagerDuty into StackStorm. It is capable of performing the following actions:

1. List all the open incidents on PD (for a given api key)

```
st2 run pagerduty.get_open_incidents
```

2. Launch an incident by giving its details and description

```
st2 run pagerduty.launch_incident from_email='<email>' title='<incident title>' [incident_key='<incident_key>']
```

3. Send acknowledgment of any incident(s)

```
st2 run pagerduty.ack_incident from_email='<email>' ids=<comma separated list of incident ids>
```

4. Snooze incident(s)

```
st2 run pagerduty.snooze_incident from_email='<email>' duration=<seconds> ids=<comma separated list of incident ids>
```

5. Create note for incident(s)

```
st2 run pagerduty.create_note_incident from_email='<email'> content='<note content>' ids=<comma separated list of incident ids>
```

6. Log entries for incident(s)

```
st2 run pagerduty.log_entries_incident is_overview=<boolean> time_zone=<string> fetch_all=<boolean> \
    include=<string>
```

7. View notes forlog_entries incident(s)

```
st2 run .view_notes_incident ids=<comma separated list of incident ids>
```

8. Resolve acknowledged incident(s)

```
st2 run pagerduty.resolve_incident from_email='<email>' ids=<comma separated list of incident ids>
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
* `service_key:` SERVICE-KEY
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

# ChatOps

The following chatops action aliases are defined:

* `get open incidents`
* `create incident {{description}}`
* `ack incident ids {{ids}} with {{email}}`
* `resolve incident ids {{ids}} with {{email}}`

`{{ids}}` is a comma separated list of incident ids, and `{{email}}` is the email address of the
user acknowledging or resolving the incident. `{{description}}` is the title of the incident.
