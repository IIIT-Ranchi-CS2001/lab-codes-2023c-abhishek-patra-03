import streamlit as st
import numpy as np
import pandas as pd

# Initialize students and attendance
if "students" not in st.session_state:
    st.session_state.students = ["Alice", "Bob", "Charlie", "David", "Eve"]

if "attendance" not in st.session_state:
    st.session_state.attendance = np.zeros((0, len(st.session_state.students)), dtype=int)

# Function to add a new student
def add_new_student():
    new_student = st.text_input("Enter the name of the new student:", key="new_student_name")
    if st.button("Add Student"):
        if new_student:
            st.session_state.students.append(new_student)
            # Add a new column (all zeros) for the new student in the attendance matrix
            st.session_state.attendance = np.hstack(
                [st.session_state.attendance, np.zeros((st.session_state.attendance.shape[0], 1), dtype=int)]
            )
            st.success(f"Student '{new_student}' added successfully!")
        else:
            st.warning("Please enter a valid student name.")

# Function to mark attendance
def mark_attendance():
    today = np.zeros(len(st.session_state.students), dtype=int)  # Initialize today's attendance
    st.write("### Mark attendance for today:")

    for i, student in enumerate(st.session_state.students):
        status = st.radio(f"Is {student} present?", ["Yes", "No"], key=f"attendance_{student}")
        if status == "Yes":
            today[i] = 1

    if st.button("Save Today's Attendance"):
        # Append today's attendance
        st.session_state.attendance = np.vstack([st.session_state.attendance, today])
        st.success("Today's attendance saved successfully!")
        st.write("### Today's Attendance:")
        today_df = pd.DataFrame([today], columns=st.session_state.students)
        st.dataframe(today_df)

# Function to display attendance
def display_attendance():
    st.write("### Attendance Record")
    if st.session_state.attendance.shape[0] == 0:
        st.warning("No attendance data available.")
        return
    attendance_df = pd.DataFrame(st.session_state.attendance, columns=st.session_state.students)
    st.dataframe(attendance_df)

# Function to calculate attendance statistics
def attendance_statistics():
    st.write("### Attendance Statistics")
    if st.session_state.attendance.shape[0] == 0:
        st.warning("No attendance data available.")
        return
    percentages = np.sum(st.session_state.attendance, axis=0) / st.session_state.attendance.shape[0] * 100
    for student, percent in zip(st.session_state.students, percentages):
        st.write(f"{student}: {percent:.2f}% attendance")

# Sidebar for navigation
st.sidebar.title("Attendance Marker")
menu = st.sidebar.radio("Menu", ["Mark Attendance", "Display Attendance", "Attendance Statistics", "Add Student", "Save/Load Data"])

# Main app
if menu == "Mark Attendance":
    mark_attendance()
elif menu == "Display Attendance":
    display_attendance()
elif menu == "Attendance Statistics":
    attendance_statistics()
elif menu == "Add Student":
    st.write("### Add a New Student")
    add_new_student()
elif menu == "Save/Load Data":
    st.write("### Save or Load Attendance")
    if st.button("Save Attendance"):
        np.savetxt("attendance.csv", st.session_state.attendance, delimiter=",", fmt="%d")
        with open("students.txt", "w") as f:
            f.write("\n".join(st.session_state.students))
        st.success("Attendance and student list saved successfully!")
    if st.button("Load Attendance"):
        try:
            st.session_state.attendance = np.loadtxt("attendance.csv", delimiter=",", dtype=int)
            with open("students.txt", "r") as f:
                st.session_state.students = f.read().splitlines()
            st.success("Attendance and student list loaded successfully!")
        except FileNotFoundError:
            st.error("No saved files found.")
