import streamlit as st

st.set_page_config(page_title="Password Validator", page_icon="🔐")

st.title("🔐 Password Validator")

password = st.text_input("Enter Your Password", type="password")

if st.button("Validate Password"):

    if len(password) < 8:
        st.error("❌ Password must contain at least 8 characters.")

    elif password.islower():
        st.warning("⚠️ Add at least one uppercase letter.")

    elif password.isalpha():
        st.warning("⚠️ Add at least one number.")

    else:
        st.success("✅ Strong Password!")
        st.balloons()
