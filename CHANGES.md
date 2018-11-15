# Change Log

# 0.6.0
- Complete pack redesign (*No backwards compatibility*)
- Extensive new list of actions
- Single `action.py` for all `action.yaml` to reference.
- Raw and Simple versions of most create actions
  - Raw - Intended for programatic uses. Inputs JSON Blob with all possible inputs.
  - Simple - Intended for Humans, Form based, minimum inputs
- Create Events via REST V2 API or Events V1 API
- Default Action Aliases modified to work with new actions
  - `ack_incident.yaml`
    - Renamed to `acknowled_incident.yaml`
    - Only acknowledges 1 ID at a time
    - format string changed
    - Changes to response formatting
  - `get_open_incidents.yaml`
    - Renamed to `find_incidents.yaml`
    - Can specify `triggered` or `acknowledged` for `statuses=[]` (Default is both)
  - `launch_incident.yaml`
    - Small changes to response formatting
  - `resolve_incident.yaml`
    - format string changed
    - Only resolves 1 ID at a time
    - Changes to response formatting
- Action `team.remove_user.yaml` has been created but marked disabled.
  - There is a typo in pypd preventing this from working. Can be reenabled after pending PR is merged
    -  https://github.com/PagerDuty/pagerduty-api-python-client/pull/53

# 0.5.0
- Add actions for user management (Fixes: #15):
  - `list_users`.
  - `create_user`.
  - `delete_user`.

# 0.4.2
- Updated launch_incident action metadata `details` parameter needs to be object

# 0.4.0

- Updated action `runner_type` from `run-python` to `python-script`

# 0.3.0

- Migrate from pygerduty (APIv1) to pypd (APIv2)

# 0.2.0

- Rename `config.yaml` to `config.schema.yaml` and update to use schema.

# 0.1.0

- First release 
