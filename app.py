import streamlit as st
import pandas as pd

st.title("favourite things")

# Инициализация на данните
if "subjects" not in st.session_state:
    st.session_state.subjects = {
        "Math": 0,
        "English": 0,
        "Science": 0,
        "Biology": 0
    }

if "sports" not in st.session_state:
    st.session_state.sports = {
        "Football": 0,
        "Basketball": 0,
        "Volleybal": 0,
        "Swimming": 0
    }

st.subheader("Select your favourite from the following: ")

subjects = st.selectbox("Favourite subject:", list(st.session_state.subjects.keys()))
sport = st.selectbox("Favourite sports:", list(st.session_state.sports.keys()))

if st.button("Save"):
    st.session_state.subjects[color] += 1
    st.session_state.sports[sport] += 1
    st.success("Saved")

st.divider()

st.subheader("Results")

# Графика за цветовете
st.write("Favourite subjects")
colors_df = pd.DataFrame.from_dict(
    st.session_state.subjects, orient="index", columns=["Брой"]
)
st.bar_chart(colors_df)

# Графика за спортовете
st.write("Favourite sports")
sports_df = pd.DataFrame.from_dict(
    st.session_state.sports, orient="index", columns=["Брой"]
)
st.bar_chart(sports_df)

