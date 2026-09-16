# Student Attendance Management System

## Overview
This is a command-line based Python application that helps manage student 
records and track daily attendance. It allows adding students, marking 
attendance, viewing records, and generating attendance reports with 
percentage calculations. This project was built as part of the 
Python Essentials course.

## Features
- Add new student records (name, roll number, class)
- Mark daily attendance (Present/Absent) for all students
- View all registered students
- View attendance history for a specific student
- Generate an attendance report showing percentage and defaulters 
  (students below 75% attendance)
- Data is saved permanently in text files, so records persist between runs

## Technologies Used
- Python 3
- Built-in file handling (no external libraries required)

## Project Structure
student-attendance-system/
├── main.py          # Program entry point, menu and logic
├── storage.py        # Handles saving/loading data to text files
├── students.txt        # Stores student records (auto-created)
├── attendance.txt        # Stores attendance records (auto-created)
├── README.md
└── statement.md

## How to Install & Run

### Prerequisites
Python 3 must be installed on your system. Check by running: python --version

### Steps
1. Clone or download this repository:
   git clone https://github.com/siddhantfx/student-attendance-system.git

2. Navigate into the project folder:
   cd student-attendance-system

3. Run the program:
   python main.py

4. Follow the on-screen menu to add students, mark attendance, and view reports.

## How to Test
1. Run python main.py
2. Choose option 1 to add 2-3 sample students
3. Choose option 2 to mark their attendance for a sample date
4. Choose option 3 to confirm students were saved
5. Choose option 4 to view a specific student's attendance
6. Choose option 5 to generate the report and check percentage calculation
7. Choose option 6 to exit, then re-run the program to confirm data was saved 
   correctly (records should still be there)

## Author
Siddhant