# PagerDuty 
The action to integrate PD into stackstorm. This action is capable fof perofrming the following actions
1. List all the open incidents on PD for a subdomain
2. Send acknowledgment of any incident or you can even send ACK for multiple events using comma seprated values
3. Close and open incident or you can even close multiple open incidents by providing comma sperated values
4. Launch an incident by giving its details and description

# Confgiuration

You need the following parmters to be in the config.yaml file
`subdomain: `'name of subdomain '
`api_key:` MmzGEJKsqmq7DrmE4w1R
`service_Api:` 1148e87e51fe4688aaba21b88b264692

##How to get API key
Once you sign in to you PD subdomain go to the API access tab and under create New API key give the key name in description and click on create key that will create API key, copy and paste that API key in the config.yaml file.
![Alt text](/st2contrib/_images/api_access_key.png?raw=true "add API key")



##How to get Service Key
Now to get the service key you need to go to the services tab and click on `add new service` give any name and then select `Use our API directly ` radio buton and then click on Add Service. That will give you a service key add that to config.yaml and you are allset to go.

![Alt text](/st2contrib/_images/add_service.png?raw=true "add serive key")
![Alt text](/st2contrib/_images/services_api.png?raw=true "service api key")
