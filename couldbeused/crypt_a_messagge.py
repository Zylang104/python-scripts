from cryptography.fernet import Fernet #you need to install it first
import base64
def valitationkey(key):
    if isinstance(key, str):
        key = key.encode()
    if len(key) != 44:
        return False
    try:
        base64.urlsafe_b64decode(key)
        return True
    except Exception:
        return False
while True:
    inputstart = input("encrypt or decrypt? (or exit): ").lower()
    if inputstart == "exit":
        break
    elif inputstart == "encrypt":
        message = input("enter message: ")
        key_option = input("Enter your existing Fernet key, or type 'GENERATE' to create one: ").strip()
        if key_option.upper() == "GENERATE":
            key = Fernet.generate_key()
            print("Generated key: " + key.decode())
        elif valitationkey(key_option):
            key = key_option.encode()
        else:
            print("Error: The entered key is not a valid 32-byte Fernet key. Generating a new key instead.")
            key = Fernet.generate_key()
            print("Generated key: " + key.decode())
            
        fernet = Fernet(key)
        encrypted = fernet.encrypt(message.encode())
        print("encrypted: " + encrypted.decode())
        print()   
    elif inputstart == "decrypt":
        message = input("enter encrypted message: ")
        key_input_decrypt = input("enter key: ").strip()
        if not valitationkey(key_input_decrypt):
            print("Error: The provided key is not a valid 32-byte Fernet key.")
            print("Decryption failed.")
            print()
            continue
        try:
            key = key_input_decrypt.encode()
            fernet = Fernet(key)
            decrypted = fernet.decrypt(message.encode()).decode()
            print("decrypted: " + decrypted)
        except Exception as e:
            print("Error: Invalid key or message. Decryption failed.")
        print()
    else:
        print("invalid option")
        print()