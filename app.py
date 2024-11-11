import streamlit as st
from linkedin_api import Linkedin

# Title
st.title("LinkedIn Profile Info Viewer")

# LinkedIn Login
st.header("Enter LinkedIn Credentials")
username = st.text_input("Username (Email)")
password = st.text_input("Password", type="password")

# Options to select information type
st.header("Select Information to Retrieve")
profile_option = st.checkbox("Profile Information")
contact_info_option = st.checkbox("Contact Information")

# Profile ID input
profile_id = st.text_input("Enter LinkedIn Profile ID")

# Fetch and display information on button click
if st.button("Fetch Information"):
    if username and password and profile_id:
        try:
            # Authenticate LinkedIn API
            api = Linkedin(username, password)
            st.success("Authenticated successfully")

            # Retrieve and display profile information if selected
            if profile_option:
                profile = api.get_profile(profile_id)
                st.subheader("Profile Information")
                st.write(profile)

            # Retrieve and display contact information if selected
            if contact_info_option:
                contact_info = api.get_profile_contact_info(profile_id)
                st.subheader("Contact Information")
                st.write(contact_info)

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter all required fields (Username, Password, and Profile ID).")
