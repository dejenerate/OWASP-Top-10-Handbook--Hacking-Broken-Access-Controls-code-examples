import requests
import time

clientId = 1
iterations = 100

# Loop through client IDs as many times as iterations specifies (100 in this example)
for i in range(iterations):
    print ("Checking clientId " + str(clientId))
    url = "https://your-test-url.com/api/orders/" + str(clientId)

    # Get a response from the URL and parameter. We assume that the
    # response is JSON and the authentication message is in the 'Message'
    # element
    response = requests.get(url)
    statusMessage = str(response['Message'])

    # Print the response to the console with the server response
    print (clientId + " " + statusMessage)
    clientId += 1
    time.sleep(10)
