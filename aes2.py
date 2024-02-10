from Cryptodome.Cipher import AES

######### BASIC ENCRYPTION ###########

# The key (must be 16 bytes)
key = b'Sixteen byte key'

# Set up the AES encryption class
encCipher = AES.new(key, AES.MODE_ECB)

# AES requires plain/cipher text blocks to be 16 bytes

file = open("aes.txt",'rb')
cipherText = encCipher.encrypt(file.read())

print("Cipher text: ", cipherText)

file = open("myEncFile.bin", "wb").write(cipherText)
