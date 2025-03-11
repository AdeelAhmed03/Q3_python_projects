import streamlit as st # Importing streamlit library for creating web app
import random # Importing random library for generating random characters
import string # Importing string library for generating string characters

# Function to generate a password based on the selected length and character options
def generate_password(length, use_digits, use_special):
    characters = string.ascii_letters # Adds letters (a-z, A-Z)

    if use_digits:
        characters += string.digits # Adds numbers (0-9) if selected

    if use_special:
        characters += string.punctuation # Adds special characters (e.g., !, @, #, $, %, ^, &, *) if selected
    
    # Generate a random password of the specified length using the selected characters
    return ''.join(random.choice(characters) for _ in range(length))

st.title("Password Generator")

length = st.slider("Select Password length", min_value=6, max_value=32, value=12)

use_digits = st.checkbox("Include Digits")

use_special = st.checkbox("Include Special Characters")

if st.button("Generate Password"):
    password = generate_password(length, use_digits, use_special)
    st.write(f"Generated Password: `{password}`")
    
st.write("--------------------------------")

st.write("Made with ❤️ by [AdeelAhmed](https://github.com/AdeelAhmed03)")