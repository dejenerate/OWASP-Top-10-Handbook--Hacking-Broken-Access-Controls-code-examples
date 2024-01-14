import requests

# Open file of URLs to test
fileURLs = open("inputfiles/urls.txt", "r")

# Open file with testing input
fileInput = open("inputfiles/fileinput.txt", "r")

# Loop through each URL and then for each URL loop through
# the testing inputs
for url in fileURLs:
    for input in fileInput:
        testUrl = url + input
        print(testUrl)
        response = requests.get(testUrl)
        print (response.text)