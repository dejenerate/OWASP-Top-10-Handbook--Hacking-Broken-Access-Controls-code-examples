import requests
import time

clientId = 1
iterations = 100

# Loop through client IDs as many times as iterations specifies (100 in this example)
for i in range(iterations):
    print ("Checking clientId " + str(clientId))
    url = "https://pinkhatcode.com/index?client_id=" + str(clientId)

    # Get a response from the URL and parameter. I want to see if it returns a
    # 200OK response, which indicates we have an IDOR vulnerability
    response = requests.get(url)

    # Print the response to the console with the server response
    print (url + " " + str(response.status_code))
    clientId += 1
    time.sleep(10)

