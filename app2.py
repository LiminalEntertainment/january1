import streamlit as st
import pandas as pd




st.title("Just questions")


if "subjects" not in st.session_state:
    st.session_state.subjects = {
        "Math": 0,
        "English": 0,
        "Science": 0,
        "Biology": 0,
        "History": 0,
        "Geography": 0,
        "Physics": 0,
        "Chemistry": 0
    }

if "grades" not in st.session_state:
    st.session_state.grades = {"6": 0, "5": 0, "4": 0, "3": 0, "2": 0}

if "hwWeekCounts" not in st.session_state:
    st.session_state.hwWeekCounts = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0}


if "classWeekCnt" not in st.session_state:
    st.session_state.classWeekCnt = {"1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0}


st.subheader("Select from the following:")


gradeNow = st.selectbox("Your grade:", list(st.session_state.grades.keys()))
selectedGrade = gradeNow
favSubj = st.selectbox("Favourite subject:", list(st.session_state.subjects.keys()))
selectedSubject = favSubj
hwPerWeek = st.selectbox("Amount of homework per week:", list(st.session_state.hwWeekCounts.keys()))
selectedHw = hwPerWeek

clsPerWeek = st.selectbox("Classes per week:", list(st.session_state.classWeekCnt.keys()))
selectedCls = clsPerWeek


if st.button("Save"):

    tempSubj = st.session_state.subjects[selectedSubject]
  
    st.session_state.subjects[selectedSubject] = tempSubj + 1
    tempGrade = st.session_state.grades[selectedGrade]
    st.session_state.grades[selectedGrade] = tempGrade + 1
    tempHw = st.session_state.hwWeekCounts[selectedHw]
    st.session_state.hwWeekCounts[selectedHw] = tempHw + 1
    tempCls = st.session_state.classWeekCnt[selectedCls]
    st.session_state.classWeekCnt[selectedCls] = tempCls + 1

    st.success("Saved")


st.divider()
st.subheader("Results")

st.write("Favourite subjects")
subjDf = pd.DataFrame.from_dict(st.session_state.subjects, orient="index", columns=["Count"])
subjDfCopy = subjDf.copy()
st.bar_chart(subjDfCopy)

st.write("Grades")
grDf = pd.DataFrame.from_dict(st.session_state.grades, orient="index", columns=["Count"])

st.write("")

grDfCopy = grDf.copy()
st.bar_chart(grDfCopy)


st.write("Homework per week")
hwDf = pd.DataFrame.from_dict(st.session_state.hwWeekCounts, orient="index", columns=["Count"])
hwDfCopy = hwDf.copy()
st.bar_chart(hwDfCopy)

st.write("Classes per week")
clsDf = pd.DataFrame.from_dict(st.session_state.classWeekCnt, orient="index", columns=["Count"])
clsDfCopy = clsDf.copy()
st.bar_chart(clsDfCopy)




