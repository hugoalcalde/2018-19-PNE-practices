import http.client
import json

# -- API information
HOSTNAME = "www.metaweather.com"
city = input("please input the capital: ")
ENDPOINT = "/api/location/search/?query=" + city

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
weather = json.loads(text_json)
woeid = weather[0]["woeid"]
ENDPOINT = "/api/location/search/location/" + str(woeid) + "/"
conn = http.client.HTTPSConnection(HOSTNAME)

# -- Send the request. No body (None)
# -- Use the defined headers
conn.request(METHOD, ENDPOINT, None, headers)

# -- Wait for the server's response
r1 = conn.getresponse()
text_json = r1.read().decode("utf-8")
conn.close()
weather = json.loads(text_json)
print("the time is : {}".format(weather["time"]))
print("the temperature is : {}".format(weather["consolidated_weather"][0]["the_temp"]))
print("the sunset is : {}".format(weather["sun_set"]))



