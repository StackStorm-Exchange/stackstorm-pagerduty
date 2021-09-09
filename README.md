
## blink-pagerduty

> PagerDuty&#39;s REST API.
[Documentation.](https://developer.pagerduty.com/docs/get-started/getting-started/)



## CreateIncident
* Create an Incident
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Priority</td>
           <td></td>
       </tr>
       <tr>
           <td>Title</td>
           <td>A succinct description of the nature, symptoms, cause, or effect of the incident.</td>
       </tr>
       <tr>
           <td>service</td>
           <td></td>
       </tr>
    </tr>
  </tbody>
</table>

## CreateIncidentNote
* Create a note on an incident
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## CreateService
* Create a service
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Description</td>
           <td>The user-provided description of the service.</td>
       </tr>
       <tr>
           <td>Escalation policy ID</td>
           <td></td>
       </tr>
       <tr>
           <td>Escalation policy type</td>
           <td></td>
       </tr>
       <tr>
           <td>Name</td>
           <td>The name of the service.</td>
       </tr>
    </tr>
  </tbody>
</table>

## CreateStatusUpdate
* Create a status update on an incident
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## DeleteService
* Delete a service
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## GetAlert
* Get an alert
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Alert ID</td>
           <td>The id of the alert to retrieve.</td>
       </tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## GetIncident
* Get an incident
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## GetLogEntry
* Get a log entry
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
       <tr>
           <td>Include</td>
           <td>Array of additional Models to include in response.</td>
       </tr>
       <tr>
           <td>Timezone</td>
           <td>Time zone in which dates in the result will be rendered.</td>
       </tr>
    </tr>
  </tbody>
</table>

## GetOutlierIncident
* Get Outlier Incident
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## GetPastIncidents
* Get Past Incidents
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## GetRelatedIncidents
* Get Related Incidents
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## ListAlerts
* List alerts for an incident
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Alert key</td>
           <td>Alert de-duplication key.</td>
       </tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
       <tr>
           <td>Sort by</td>
           <td>Used to specify both the field you wish to sort the results on (created_at/resolved_at), as well as the direction (asc/desc) of the results. The sort_by field and direction should be separated by a colon. A maximum of two fields can be included, separated by a comma. Sort direction defaults to ascending.</td>
       </tr>
       <tr>
           <td>Status codes</td>
           <td>Return only alerts with the given statuses. (More status codes may be introduced in the future.)</td>
       </tr>
    </tr>
  </tbody>
</table>

## ListEscalationPolicies
* List escalation policies
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    </tr>
  </tbody>
</table>

## ListIncidentLogEntries
* List log entries for an incident
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## ListIncidentNotes
* List notes for an incident
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## ListIncidents
* List incidents
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    </tr>
  </tbody>
</table>

## ListLogEntries
* List log entries
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Include</td>
           <td>Array of additional Models to include in response.</td>
       </tr>
       <tr>
           <td>Is overview</td>
           <td>If `true`, will return a subset of log entries that show only the most important changes to the incident.</td>
       </tr>
       <tr>
           <td>Since</td>
           <td>The start of the date range over which you want to search.</td>
       </tr>
       <tr>
           <td>Team IDs</td>
           <td>An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.</td>
       </tr>
       <tr>
           <td>Timezone</td>
           <td>Time zone in which dates in the result will be rendered.</td>
       </tr>
       <tr>
           <td>Until</td>
           <td>The end of the date range over which you want to search.</td>
       </tr>
    </tr>
  </tbody>
</table>

## ListServices
* List services
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Include</td>
           <td>Array of additional details to include.</td>
       </tr>
       <tr>
           <td>Limit</td>
           <td>The number of results per page.</td>
       </tr>
       <tr>
           <td>Offset</td>
           <td>Offset to start pagination search results.</td>
       </tr>
       <tr>
           <td>Query</td>
           <td>Filters the result, showing only the tags whose labels match the query.</td>
       </tr>
       <tr>
           <td>Sort by</td>
           <td>Used to specify the field you wish to sort the results on.</td>
       </tr>
       <tr>
           <td>Team IDs</td>
           <td>An array of team IDs. Only results related to these teams will be returned. Account must have the `teams` ability to use this parameter.</td>
       </tr>
       <tr>
           <td>Timezone</td>
           <td>Time zone in which dates in the result will be rendered.</td>
       </tr>
       <tr>
           <td>Total</td>
           <td>By default the `total` field in pagination responses is set to `null` to provide the fastest possible response times. Set `total` to `true` for this field to be populated.

See our [Pagination Docs](https://developer.pagerduty.com/docs/rest-api-v2/pagination/) for more information.
</td>
       </tr>
    </tr>
  </tbody>
</table>

## ListSubscribers
* List Notification Subscribers
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## SnoozeIncident
* Snooze an incident
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## UnsubscribeFromIncident
* Remove Notification Subscriber
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
       <tr>
           <td>Subscribers</td>
           <td></td>
       </tr>
    </tr>
  </tbody>
</table>

## UpdateAlert
* Update an alert
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Alert ID</td>
           <td>The id of the alert to retrieve.</td>
       </tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## UpdateIncident
* Update an incident
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## UpdateMultipleAlerts
* Manage alerts
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
       <tr>
           <td>Incident ID</td>
           <td>The ID of the resource.</td>
       </tr>
    </tr>
  </tbody>
</table>

## UpdateMultipleIncidents
* Manage incidents
<table>
<caption>Action Parameters</caption>
  <thead>
    <tr>
        <th>Param Name</th>
        <th>Param Description</th>
    </tr>
  </thead>
  <tbody>
    <tr>
    </tr>
  </tbody>
</table>
