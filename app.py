import streamlit as st
from linkedin_api import Linkedin

# Sidebar for LinkedIn login credentials
st.sidebar.title("LinkedIn Authentication")
username = st.sidebar.text_input("Username (Email)")
password = st.sidebar.text_input("Password", type="password")

# Main page title
st.title("LinkedIn Profile Info Viewer")

# State variable for authentication
if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False

# Authentication button
if st.sidebar.button("Authenticate"):
    if username and password:
        try:
            # Authenticate LinkedIn API
            st.session_state["api"] = Linkedin(username, password)
            st.session_state["authenticated"] = True
            st.success("Authenticated successfully")
        except Exception as e:
            st.session_state["authenticated"] = False
            st.error(f"Authentication failed: {e}")
    else:
        st.warning("Please enter both username and password to authenticate.")

# Main page content
if st.session_state["authenticated"]:
    st.subheader("Select Information to Retrieve")

    # Options to select information type
    profile_option = st.checkbox("Profile Information")
    contact_info_option = st.checkbox("Contact Information")

    # Profile ID input
    profile_id = st.text_input("Enter LinkedIn Profile ID")

    # Fetch and display information based on selection
    if st.button("Fetch Information"):
        if profile_id:
            try:
                # Display profile information if selected
                if profile_option:
                    profile = st.session_state["api"].get_profile(profile_id)
                    st.subheader("Profile Information")
                    st.write(profile)

                # Display contact information if selected
                if contact_info_option:
                    contact_info = st.session_state["api"].get_profile_contact_info(profile_id)
                    st.subheader("Contact Information")
                    st.write(contact_info)

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a LinkedIn Profile ID.")
else:
    st.info("Please authenticate using the sidebar to retrieve LinkedIn information.")
