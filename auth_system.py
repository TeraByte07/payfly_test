import json
import os
import hashlib

credentials_file = 'credentials.json'

def load_credentials():
    if os.path.exists(credentials_file):
        with open(credentials_file) as file:
            return json.load(file)
    return {}

def save_credentials(credentials):
    with open(credentials_file, 'w') as file:
        json.dump(credentials, file, indent=4)
        
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user(username, password):
    credentials = load_credentials()
    
    if username in credentials:
        raise ValueError("Username already exists!!!")
    hashed_password = hash_password(password)
    credentials[username] = hashed_password
    save_credentials(credentials)
    print(f"User '{username}' registered successfully.")
    
def login_user(username, password):
    credentials = load_credentials()
    if username not in credentials:
        raise ValueError("Username does not exist!!")
    hashed_password = hash_password(password)
    if credentials[username] == hashed_password:
        print(f"User '{username}' logged in successfully")
    else:
        raise ValueError("Incorrect password")

def main():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                register_user(username, password)
            except ValueError as e:
                print(e)
        
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            try:
                login_user(username, password)
            except ValueError as e:
                print(e)
                
        elif choice == '3':
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()