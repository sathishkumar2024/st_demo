import streamlit as st

# Title of the app
st.title("Basic Streamlit App")

# Input text from the user
user_input = st.text_input("Enter some text:")

# Button to submit the input
if st.button("Submit"):
    st.write(f"You entered: {user_input}")
