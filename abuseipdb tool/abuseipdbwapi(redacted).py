import requests
import json

input =''

# Defining the api-endpoint
url = 'https://api.abuseipdb.com/api/v2/check'

querystring = {
    'ipAddress': "8.8.8.8",
    'maxAgeInDays': '90'
}

headers = {
    'Accept': 'application/json',
    'Key': 'b805668b00a4a2fb72f2d554d51aacc93a7941d9a8f6ac58eb2d94b37094a1c06caa939d677b0798'
}

response = requests.request(method='GET', url=url, headers=headers, params=querystring)

# Formatted output
decodedResponse = json.loads(response.text)
# print (json.dumps(decodedResponse, sort_keys=True, indent=4))

raw_output = decodedResponse["data"] 
#Extract 
formatted_output = {
                    "IP address": raw_output.get("ipAddress"),
                    "ISP": raw_output.get("isp"), 
                    "Country code": raw_output.get("countryCode"),
                    "Domain": raw_output.get("domain"),
                    "Abuse rating":raw_output.get("abuseConfidenceScore")} 

print(formatted_output)