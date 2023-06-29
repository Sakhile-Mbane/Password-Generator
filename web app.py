import sqlite3
import streamlit as st

# Connect to the database
conn = sqlite3.connect('/Users/sakhile/Documents/Projects/Pass/DB/passwords.db')
c = conn.cursor()

# Function to retrieve password and username by platform
def get_password_and_username_by_platform(platform):
    c.execute("SELECT password, username FROM passwords WHERE platform=?", (platform,))
    result = c.fetchone()
    if result:
        return result[0], result[1]
    else:
        return None, None

# Function to update password and username by platform
def update_password_and_username(platform, new_password, new_username):
    c.execute("UPDATE passwords SET password=?, username=? WHERE platform=?", (new_password, new_username, platform))
    conn.commit()
    st.success("Password and username updated successfully.")

# Streamlit app
def main():
    st.title("Password Retrieval and Update App")

    # User input for platform
    platform = st.text_input("Enter the platform to retrieve or update the password and username:")

    if platform:
        password, username = get_password_and_username_by_platform(platform)

        if password and username:
            st.success("Platform: {}".format(platform))
            st.write("Password: {}".format(password))
            st.write("Username: {}".format(username))
            
            st.subheader("Update Password and Username")
            new_password = st.text_input("Enter new password:")
            new_username = st.text_input("Enter new username:")
            update_button = st.button("Update")
            
            if update_button and (new_password or new_username):
                update_password_and_username(platform, new_password, new_username)

        else:
            st.warning("No password found for the given platform.")

if __name__ == "__main__":
    main()

# Close the database connection
conn.close()
