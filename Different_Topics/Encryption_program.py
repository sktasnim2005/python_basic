import random
import string

#Part 1
print("Part 1")
# lets create a list of all the characters we want to use
# in our encryption
# we will use all the printable characters
# string.punctuation module contains all the punctuation characters
# string.digits module contains all the digits
# string.ascii_letters module contains all the letters

# here insted of string.whitespace we will use a space (" ")
chars = " " + string.punctuation + string.digits + string.ascii_letters

# it will show one long string of characters
print(chars)
print()

#Part 2
print("Part 2")
#I'm going to turn this string into a list where each character is an individual element
# for that I'm going to typecast the string into a list

chars = list(chars)
# this will create a list of all the characters we want to use in our encryption

print(chars) 
print()

#Part 3
print("Part 3")
# now I want to create a random which will shuffle the list of characters

key = chars.copy()
# this will create a copy of the list of characters
print(f"chars = {chars}")
print(f"key = {key}")
print()

# now we have two identical lists one is original characters and the other is for the key
# now we will shuffle the key

random.shuffle(key)
# this will shuffle the key list

#Part 4 Encryption
print("Part 4 Encrypt")
#plain_text is the original message
plain_text = input("Enter a message to encrypt: ")

#cipher_text is the encrypted message
cipher_text = ""
# this will create an empty string

for letter in plain_text:
    # this will loop through each letter in the plain_text
    # and encrypt it by replacing it with the corresponding letter in the key
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")
print()

#Part 5 Decryption
print("Part 5 Decrypt")
# now we will decrypt the message
# we will use the same key to decrypt the message
# we will create a new empty string for the decrypted message

cipher_TEXT = input("Enter a message to decrypt: ")
decrypted_text = ""
# this will create an empty string
for l in cipher_TEXT:
    # this will loop through each letter in the cipher_text
    # and decrypt it by replacing it with the corresponding letter in the chars
    index = key.index(l)
    decrypted_text += chars[index]

print("ORIGINAL MESSAGE: ", cipher_TEXT)
print("DECRYPTED MESSAGE: ", decrypted_text)
print()