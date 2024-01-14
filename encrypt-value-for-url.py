import cryptocode
import webbrowser

clientId = 1

# Encrypt the clientId value and store it in a new variable
key = "1234567891234567"
ciphertext = cryptocode.encrypt(str(clientId), key)

# With the clientId encrypted, now build the URL
# and redirect users to the URL with the encrypted clientId
url = "https://pinkhatcode.com/index?client_id=" + str(ciphertext)
webbrowser.open(url, new=0, autoraise=True)




