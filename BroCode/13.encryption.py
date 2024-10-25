import random
import string

print("---------------------------------------------------------------")
chars = " " + string.punctuation + string.digits + string.ascii_letters
#there are alot extra things in string.whitespace
# print(chars)

chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print("chars:", chars)
# print("key:", key)

# ENCRYPT
plain_txt = input("Enter a message to encrypt: ")
cipher_text = ""

for letter in plain_txt:
     index = chars.index(letter)
     cipher_text += key[index]

print(f"Original message: {plain_txt}")
print(f"Encrypted message: {cipher_text}")

#DECRYPT
cipher_text1 = input("Enter a message to encrypt: ")
plain_txt1 = ""

for letter in cipher_text1:
     index = key.index(letter)
     plain_txt1 += chars[index]

print(f"Encrypted message: {cipher_text1}")
print(f"Original message: {plain_txt1}")