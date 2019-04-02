# Example of getting information stored in github

import http.client
import json

# -- API information
HOSTNAME = "api.github.com"
ENDPOINT = "/users/"
GITHUB_ID = input("Enter the user : ")
METHOD = "GET"

# -- Here we can define special headers if needed
headers = {'User-Agent': 'http-client'}

# -- Connect to the server
# -- NOTICE it is an HTTPS connection!
# -- If we do not specify the port, the standar one
# -- will be used
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT + GITHUB_ID, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()
# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
user = json.loads(text_json)
print("the real name of the user is : {}".format(user["name"]))
total_number = user["public_repos"]
# -- Get some data
REPOS = "/repos"
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, ENDPOINT + GITHUB_ID+REPOS, None, headers)


# -- Wait for the server's response
r1 = conn.getresponse()
# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()
hola = json.loads(text_json)
counter = 1
for element in hola :
    print("The repository number {} is: {}".format(counter, element["name"]))
    counter += 1
REPOS = "/repos/{}/2018-19-PNE-practices/commits".format(GITHUB_ID)
conn = http.client.HTTPSConnection(HOSTNAME)
conn.request(METHOD, REPOS, None, headers)


# -- Wait for the server's response
r1 = conn.getresponse()
# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()
commit = json.loads(text_json)
print("The number of commits is : {}".format(len(commit)))
