import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore
import json
import time

st.set_page_config(layout="wide")

# Load Firebase credentials from Streamlit secrets

# Fix newline issue
st.write("App Started ✅")

try:
    firebase_config = st.secrets["firebase"]
    st.write("Secrets Loaded ✅")

    if not firebase_admin._apps:
        cred = credentials.Certificate(firebase_config)
        firebase_admin.initialize_app(cred)

    st.write("Firebase Initialized ✅")
    db = firestore.client()
    st.write("Firestore Connected ✅")

except Exception as e:
    st.error(f"Error: {e}")

st.title("🎉 Events Dashboard")

# ---------- ADD EVENT ----------
st.subheader("Add Event")

name = st.text_input("Name")
event_type = st.selectbox("Event Type", ["Birthday", "Anniversary", "Festival", "Other"])
event_date = st.date_input("Event Date")
image_url = st.text_input("Image URL (paste public image link)")

if st.button("Save Event"):
    db.collection("events").add({
        "name": name,
        "type": event_type,
        "date": str(event_date),
        "image": image_url
    })
    st.success("Event Added to Database!")

st.divider()

# ---------- DISPLAY EVENTS ----------
st.subheader("Live Display")

events_ref = db.collection("events").stream()
events = [event.to_dict() for event in events_ref]

placeholder = st.empty()

while True:
    for event in events:
        with placeholder.container():
            st.markdown("""
                <style>
                .main-box {
                    background: linear-gradient(135deg,#667eea,#764ba2);
                    padding: 60px;
                    border-radius: 20px;
                    text-align: center;
                    color: white;
                }
                .name {font-size:50px;font-weight:bold;}
                .event {font-size:35px;}
                </style>
            """, unsafe_allow_html=True)

            st.markdown('<div class="main-box">', unsafe_allow_html=True)
            st.image(event["image"], width=250)
            st.markdown(f'<div class="name">{event["name"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="event">Happy {event["type"]} 🎉</div>', unsafe_allow_html=True)
            st.markdown("</div>", unsafe_allow_html=True)

        time.sleep(5)
