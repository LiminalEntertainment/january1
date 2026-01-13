import streamlit as st
import pandas as pd

st.title("Favourite things")

# Initialize data
if "subjects" not in st.session_state:
    st.session_state.subjects = {
        "Math": 0,
        "English": 0,
        "Science": 0,
        "Biology": 0
    }

if "grades" not in st.session_state:
    st.session_state.grades = {
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0
    }

st.subheader("Select from the following:")

subject = st.selectbox("Favourite subject:", list(st.session_state.subjects.keys()))
grades = st.selectbox("Favourite grades:", list(st.session_state.grades.keys()))

if st.button("Save"):
    st.session_state.subjects[subject] += 1
    st.session_state.sports[grades] += 1
    st.success("Saved")

st.divider()

st.subheader("Results")

# Subjects chart
st.write("Favourite subjects")
subjects_df = pd.DataFrame.from_dict(
    st.session_state.subjects, orient="index", columns=["Count"]
)
st.bar_chart(subjects_df)

# Sports chart
st.write("Favourite sports")
grades_df = pd.DataFrame.from_dict(
    st.session_state.grades, orient="index", columns=["Count"]
)
st.bar_chart(grades_df)
