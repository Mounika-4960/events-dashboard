import streamlit as st
import pandas as pd
from datetime import date

st.set_page_config(page_title="Events Dashboard", layout="wide")

st.title("🎉 Birthday & Special Events Dashboard")

# Initialize session storage
if "events" not in st.session_state:
    st.session_state.events = []

# Input Section
st.subheader("➕ Add New Event")

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Enter Name")
    event_type = st.selectbox(
        "Select Event Type",
        ["Birthday", "Anniversary", "Wedding", "Achievement", "Other"]
    )

with col2:
    event_date = st.date_input("Select Event Date")
    uploaded_image = st.file_uploader(
        "Upload Person's Image",
        type=["jpg", "jpeg", "png"]
    )

if st.button("Save Event"):
    if name and uploaded_image:
        event_data = {
            "name": name,
            "type": event_type,
            "date": event_date,
            "image": uploaded_image
        }
        st.session_state.events.append(event_data)
        st.success("Event Saved Successfully! 🎉")
    else:
        st.warning("Please enter name and upload image.")

st.divider()

# Display Section
st.subheader("📅 All Events")

if len(st.session_state.events) == 0:
    st.info("No events added yet.")
else:
    for event in st.session_state.events:
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(event["image"], width=150)
        with col2:
            st.markdown(f"### {event['name']}")
            st.write(f"Event: {event['type']}")
            st.write(f"Date: {event['date']}")

            # Show celebration if today
            if event["date"] == date.today():
                st.success("🎊 Today is the Special Day!")
                st.balloons()

        st.divider()
