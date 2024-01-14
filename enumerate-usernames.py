import requests
import json

# Open file of usernames to test
fileUsernames = open("inputfiles/account_names.txt", "r")
url = "https://your-test-url.com/api/passwordreset"
headers = {'Content-type': 'application/json'}

# Used to contain users found to exist on the API
# while we iterate through each user in the file and test it
bingo = []
negHit = "Username not found."

for username in fileUsernames:
    username = username.strip()  # strip any leading or trailing spaces
    print("Testing user " + username)
    userJson = {'user':username}
    jsonData = json.dumps(userJson)
    response = requests.post(url, data=jsonData, headers=headers)
    # print (response.text)
    # exit(0)

    if response.text.find(negHit) < 0:
        print(username + " exists!\n")
        bingo.append(username)




