from password_utils import encrypt_password
from cryptography.fernet import Fernet

def generate_key():
    key=Fernet.generate_key()
    with open("secret.key","wb") as f:
        f.write(key)
    print("key is generated and saved")

if __name__ == "__main__":
    generate_key()

    password=input("Enter password:")
    encrypted=encrypt_password(password)
    print("encrypted password:" , encrypted)
