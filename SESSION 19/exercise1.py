import http.client
import json
import random

# -- API information
HOSTNAME = "api.icndb.com"
ENDPOINT = "/jokes"
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
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()

# -- Print the status
print()
print("Response received: ", end='')
print(r1.status, r1.reason)

# -- Read the response's body and close
# -- the connection
text_json = r1.read().decode("utf-8")
conn.close()

# -- Optionally you can print the
# -- received json file for testing
# print(text_json)

# -- Generate the object from the json file
cn = json.loads(text_json)

# -- Print the received URL
print("the number of jokes of Chuck Norris in this database is: {}".format(len(cn["value"])))
list_categories = list()
for element in cn["value"] :
    if element["categories"] not in list_categories:
        list_categories.append(element["categories"])
print("The number of categories is : {}".format(len(list_categories)))
print("The name of the categories are : ")
for element in list_categories :
    print(" -{}".format(element))
joke_number = random.randint(1,len(cn["value"]))
print("This is a random joke: ")
print(cn["value"][joke_number]["joke"])