import cryptocode

# In your code, you would use the urlparse library to retrieve
# the ciphtertext value from the variable clientId. We're hardcoding it for simplicity.

# Decrypt the clientId so that it can be processed
key = "1234567891234567"
decryptedId = cryptocode.decrypt("8Q==*Vo/baBXhaGuL7QFPX+09Qg==*O9DhyGeTrlVnsjfWZVDc4w==*rYK8brUdxC8UVzrBREQ3kg==", key)

print(decryptedId)