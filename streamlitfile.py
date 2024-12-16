import streamlit as st
import hashlib

# Initialize a dictionary to store usernames and passwords
users = {
    "admin": hashlib.sha256("password".encode()).hexdigest(),
    "user1": hashlib.sha256("user1_password".encode()).hexdigest(),
    # Add more users as needed
}

def authenticate(username, password):
    """Check if the username and password are correct"""
    if username in users:
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        if hashed_password == users[username]:
            return True
    return False

def main():
    """Create the login page using Streamlit"""
    st.title("Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Login successful! You can now access the application.")
            # Add code here to grant access to the application
        else:
            st.error("Incorrect username or password. Please try again.")

if __name__ == "__main__":
    main()