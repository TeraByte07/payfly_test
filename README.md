# User Registration and Login System

This project is a simple user registration and login system implemented in Python. It uses JSON files to store user credentials and hashes passwords using SHA-256 for security.

## Features

- Register a new user with a username and password.
- Login with a username and password.
- Passwords are securely hashed.

## Requirements

- Python 3.x

## Setup

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    ```

2. Navigate to the project directory:
    ```bash
    cd your-repository
    ```

3. (Optional) Create a virtual environment:
    ```bash
    python -m venv venv
    venv\Scripts\activate
    ```

4. Install any necessary dependencies (if applicable):
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```bash
    python auth_system.py
    ```

2. Follow the on-screen instructions to register or login.

## Approach

The approach to developing this user registration and login system was as follows:
1. **Data Storage**: User credentials are stored in a JSON file named `credentials.json`. This allows for simple and easy retrieval of user data.
2. **Password Hashing**: Passwords are hashed using SHA-256 before being stored. This enhances security by ensuring that plaintext passwords are never saved.
3. **Functions**: Modular functions were created for loading credentials, saving credentials, hashing passwords, registering users, and logging in users. This makes the code more organized and reusable.
4. **User Interaction**: A simple command-line interface was implemented to allow users to register, login, or exit the application.

## Challenges

1. **Password Security**: Ensuring that passwords are securely stored was a primary concern. Implementing SHA-256 hashing helped address this.
2. **File Handling**: Properly reading from and writing to the JSON file required careful handling to avoid data corruption or loss.
3. **User Experience**: Providing clear and informative messages for registration, login success, and error conditions was important for a good user experience.
4. **Error Handling**: Implementing appropriate error handling to manage cases like existing usernames, non-existent users, and incorrect passwords was crucial for the robustness of the application.

## File Structure

- `auth_system.py` - Main script to run the application.
- `credentials.json` - JSON file where user credentials are stored.
- `README.m
