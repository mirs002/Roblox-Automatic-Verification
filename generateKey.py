from cryptography.fernet import Fernet

key = Fernet.generate_key()
print("--------------------------------------------")
print(key.decode())
print("--------------------------------------------")
input()