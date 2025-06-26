import streamlit as st
import smtplib
from email.message import EmailMessage

st.set_page_config(page_title="Info Submission", layout="centered")
st.title("Submit Your Info")
st.write("Please fill out the form below.")

with st.form("user_form"):
    name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    message = st.text_area("Your Message")
    submitted = st.form_submit_button("Send")

    if submitted:
        if name and email and message:
            try:
                sender_email = "your_email@gmail.com"
                sender_password = "your_app_password"
                receiver_email = "your_email@gmail.com"

                subject = f"New Submission from {name}"
                body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

                msg = EmailMessage()
                msg['Subject'] = subject
                msg['From'] = sender_email
                msg['To'] = receiver_email
                msg.set_content(body)

                with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                    smtp.login(sender_email, sender_password)
                    smtp.send_message(msg)

                st.success("✅ Message sent successfully!")


