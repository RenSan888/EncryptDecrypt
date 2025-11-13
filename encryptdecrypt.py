#importing
from cryptography.fernet import Fernet

#user input
message = input("Please enter your message: ")

#use fernet to generate key
key = Fernet.generate_key()
fernet = Fernet(key)

#encrpting message
encMess = fernet.encrypt(message.encode())
print("This is your encrypted message: ", encMess)

#decrypting message
quest = input("Would you like to decrypt your message? (Y/N): ")
decMess = fernet.decrypt(encMess).decode()

#asking user if they would like to decrypt encrypted message
if quest == "Y":
    print("This is your decrypted message: ", decMess)
elif quest == "N":
    print("Thank you")
else:
    print("Please type 'Y' or 'N'")