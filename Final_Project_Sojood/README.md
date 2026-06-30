# Clinic Patient Management System

Final Project Assignment  
Python Basics Training | Beginner-Friendly Capstone Project

## Project description

This is my final project for the Python Basics training. I built a simple command-line clinic system to manage patient records and visit notes.

The project is beginner-friendly, but it helped me practice many important Python concepts in one complete program. It also helped me understand how a small program can organize real-life data in a simple and useful way.

## Main features

- Add new patients with name, age, phone number, symptoms, and patient ID
- View all saved patients
- Search for patients by name or ID
- Handle cases where more than one patient has a similar name
- Update patient information
- Add visit notes for a patient
- View patient visit history
- Save patient data to `patients.json`
- Load saved data when the program starts
- Save data automatically before exit
- Validate empty inputs
- Handle invalid age and ID input

## Files

- `Project_Sojood.py` - the main Python program
- `patients.json` - the saved patient data
- `README.md` - project explanation

## What concepts I used

In this project, I used:

- Variables
- Input and output
- Conditional statements
- Loops
- Functions
- Lists
- Dictionaries
- Strings and text processing
- File handling
- JSON
- Error handling using `try/except`

## What I learned

I learned how to connect different Python concepts together in one working application. I practiced storing data, searching through records, updating information, validating input, and saving data to a file.

I also learned that helper functions are very useful because they make the code cleaner and reduce repeated logic.

## What was difficult

The most difficult part at the beginning was saving and loading data using JSON. I needed to understand how the program could keep the patient records after closing and running it again.

I overcame this by searching more, practicing, and testing the program several times. After that, I understood how `json.dump()` and `json.load()` work, and I made sure that the patient data and visit history were saved and loaded correctly.

## What I would improve later

In the future, I would like to improve the project by adding:

- Delete patient option
- Search patients by symptom
- Export a simple report to a text file
- A version using OOP/classes

## Acknowledgment

Special thanks to our instructor, Mohamad Shoman, for explaining the Python basics clearly, sharing helpful slides, and guiding us through the project step by step.
