import requests
requests.packages.urllib3.disable_warnings()
from requests.auth import HTTPBasicAuth
import json
import base64


def main():
   print("*********************************************************");
   print("* Cisco CMX Command Line REST API Python Utility        *");
   print("* Please provide the input in the following format      *");
   print("*                                                       *");
   print("* REST URL: https://[ip]/api/location/v1/clients/count  *");
   print("* Username: [username]                                  *");
   print("* Password: [password]                                  *");
   print("*                                                       *");
   print("*                                                       *");
   print("* Control C to exit                                     *");
   print("*********************************************************");

   storedCredentials = False


try:
   
   username = 'learning'
   password = 'learning'
   ##Form the request as a post
   request = requests.post('https://msesandbox.cisco.com:8081/api/analytics/v1/deviceCount', json={"granularity": "hourly","period":"yesterday","timeRange":"07:00-13:30", "areas":""}, auth = HTTPBasicAuth(username,password),verify=False)
   ##Print the response from the API
   print request.json()

except requests.exceptions.RequestException as e:
           print(e)

