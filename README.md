# AGENDA MANAGE
    ### Video Demo:  https://youtu.be/yWmVQG9Li5k
    ### Description:
The Agenda Manager is a versatile and efficient command-line tool designed to help users organize their daily tasks, notes, and contacts seamlessly. With a user-friendly interface and modular functionalities, this Python-based project offers a simple yet effective solution for maintaining a well-structured agenda.

# Project Overview
## Main Files
project.py: The primary script that acts as the central hub for managing tasks, notes, and contacts. It handles user interactions, delegating actions to specific functions within the file.
test_project.py: A dedicated file for unit tests, ensuring the reliability and correctness of each function in the Agenda Manager. The tests cover various scenarios to maintain robust code quality.


# Getting Started
## Prerequisites
Ensure Python 3.x is installed on your machine.
Install dependencies:
pip install -r requirements.txt


# Usage
Run the Agenda Manager with:  python agenda.py
Use pytest to test the application :pytest test_project.py


# Key Features
Date and Time: View the current date and time for effective time management.
Task and Note Management: Create, update, and delete tasks and notes .
Contact List: Maintain a comprehensive list of contacts with names and telephone numbers.

# Design Principles
CLI Approach: The project adopts a Command-Line Interface (CLI) for simplicity, providing an easy-to-use interface without the need for a graphical user interface.
Modular Design: Each function within agenda.py focuses on a specific agenda management aspect, enhancing code readability and maintainability.
Testing Focus: Inclusion of unit tests in test_agenda.py to ensure the reliability of the application. Thorough testing covers various scenarios for early issue detection.

# License
This project is licensed under the MIT License. Refer to the LICENSE file for details.
