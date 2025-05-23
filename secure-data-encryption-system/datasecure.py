import streamlit as st
import hashlib
import json
import os
import time
from cryptography.fernet import Fernet
from base64 import urlsafe_b64encode
from hashlib import pbkdf2_hmac

# === data information of user ===
DATA_FILE = "secure_data.json"
SALT = b"secure_salt_value"
LOOKOUT_DURATION = 60


# === section login details ===
if "authenticated" not in st.session_state:
    st.session_state.authenticated_user = None

if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = 0

# === if data is load ===
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
        return{}

def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

def generate_key(passkey):
    key = pbkdf2_hmac(
        'sha256',
        passkey.encode(),
        SALT,
        100000,
    )
    return urlsafe_b64encode(key)

def hash_password(password):
    return hashlib.pbkdf2_hmac('sha256', password.encoder(), SALT, 100000).hex()

# === cryptography.fernet used ===
def encrypt_data(data, key):
    cipher = Fernet(generate_key(key))
    return cipher.encypt(data.encode()).decode()
    
def decrypt_data(encrypt_data, key):
    try:
        cipher = Fernet(generate_key(key))
        return cipher.decrypt(encrypt_data.encode()).decode()
    except:
        return None

stored_data = load_data()

# === navigation bar ===
st.title(" 🔐 Secure Data Encryption System")
menu = ["Home", "Register", "Login", "Store Data", "Retrieve Data"]
choice = st.sidebar.selectbox("Navigation", menu)

if choice == "Home":
    st.subheader("Welcome to My 🔐 Data Encryption System !")
    st.markdown(
        """
        This is a simple data encryption system that allows you to securely store and retrieve sensitive information.
        You can register, log in, and manage your data with ease.
        """
    )

# === user registration ===
elif choice == "Register":
    st.subheader("Create a New Account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Register"):
        if username and password:
            if username in stored_data:
                st.warning("Username already exists. Please choose a different one.")
            else:
                stored_data[username] = {
                    "password": hash_password(password),
                    "data": []
                }
                save_data(stored_data)
                st.success("Account created successfully! You can now log in.")
        else:
            st.error("Both fields are required.")

elif choice == "Login":
    st.subheader("User Login")
    
    if  time.time() < st.session_state.lockout_time:
        remaining = int(st.session_state.lockout_time - time.time())
        st.error(f"Too many failed attempts. Please wait {remaining} seconds.")
        st.stop()

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username in stored_data and stored_data[username]["password"] == hash_password(password):
            st.session_state.authenticated_user = username
            st.session_state.failed_attempts = 0
            st.success(f"Welcome, {username}!")  
        else:
            st.session_state.failed_attempts += 1
            remaining_attempts = 3 - st.session_state.failed_attempts
            st.error(f"Invalid Crdentials! Attempts left: {remaining_attempts}")
                
            if st.session_state.failed_attempts >= 3:
               st.session_state.lockout_time = time.time()
               st.error("To many failed attempts. Locked for 60 seconds")
               st.stop()

# === data store section ===
elif choice == "Store Data":
    if not st.session_state.authenticated_user:
        st.warning("Please Login first.")
    else:
        st.subheader("Store Encrypted Data")
        data = st.text_area("Enter data to encrypt")
        passkey = st.text_input("Encryption Key (passphrase)", type="password")

        if st.button("Encrypt And Save"):
            if data and passkey:
                encrypted = encrypt_data(data, passkey)
                stored_data[st.session_state.authenticated_user]["data"].append(encrypted)
                save_data(stored_data)
                st.success("Data encrypted and saved successfully!")
            else:
                st.error("All fields are required to fill.")
            
# === data retrieve section ===
elif choice == "Retrieve Data":
    if not st.session_state.authenticated_user:
        st.warning("Please Login first.")
    else:
        st.subheader("Retrieve Encrypted Data")
        user_data = stored_data.get(st.session_state.authenticated_user, {}).get("data", [])

        if not user_data:
            st.info("No Data Found!")
        else:
            st.write("Encrypted Data Entries")
            for i, item in enumerate(user_data):
                st.code(item,language="text")
            encrypted_input = st.text_area("Enter encrypted text")
            passkey = st.text_input("Enter Passkey To Decrypt", type="password")

            if st.button("Decrypt"):
                result = decrypt_data(encrypted_input, passkey)
                if result:
                    st.success(f"Decrypted : {result}:")
                else:
                    st.error("Incorrect passkey or corrupted data.")