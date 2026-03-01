import streamlit as st
import pandas as pd
from datetime import date
import os

st.title("🎉 Birthday & Special Events Dashboard")
st.write("Welcome to your Cloud Event Dashboard!")

event_type = st.selectbox("Select Event Type", ["Birthday", "Anniversary", "Special Event"])
name = st.text_input("Enter Name")
event_date = st.date_input("Select Date")

if st.button("Save Event"):
    data = {"Name": name, "Event": event_type, "Date": event_date}
    df = pd.DataFrame([data])

    if os.path.exists("events.csv"):
        old_df = pd.read_csv("events.csv")
        df = pd.concat([old_df, df], ignore_index=True)

    df.to_csv("events.csv", index=False)
    st.success("Event Saved Successfully!")

st.write("----")
st.subheader("All Events")

if os.path.exists("events.csv"):
    df = pd.read_csv("events.csv")
    st.dataframe(df)
