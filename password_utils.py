from cryptography.fernet import Fernet

class FakeStr(str):
    def __str__(self):
        return "****"
    def __repr__(self):
        return "****"

def load_key():
    return open("secret.key","rb").read()
def encrypt_password(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())
def decrypt_password(encrypt_password):
    key = load_key()
    f = Fernet(key)
    decrypted = f.decrypt(encrypt_password).decode()
    return FakeStr(decrypted)
def get_decrypted_password():
    encrypted_password = input("Enter encrypted password:")
    return decrypt_password(encrypted_password)
if __name__ == "__main__":
    password = get_decrypted_password()
    print(password)
