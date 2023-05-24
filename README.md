# Lab Automation Scripts

This repository contains scripts for automating lab processes in a course project.

## create_lab.py

The `create_lab.py` script is used to create a new project for each student in the course.

### Prerequisites

- Python 3.x
- Requests library (Install using `pip install requests`)

### Usage

1. Set the following variables in the script:
    - `admin_username`: Course project admin username
    - `token`: Private token for authentication
    - `course_name`: Name of the course
    - `template`: Path to the exported template file
    - `student_list`: Path to the file containing the list of students' WatIAM usernames
    - `group_name`: Name of the course project
    - `subgroup_name`: Name of the assignment group
    - `namespace_id`: Assignment group ID

2. Run the script:
    ```
    python create_lab.py
    ```

## process.py

The `process.py` script is used to process the student assignments.

### Prerequisites

- Python 3.x
- Git (installed and configured)
- CMake

### Usage

1. Set the following variables in the script:
    - `admin_username`: Course project admin username
    - `token`: Private token for authentication
    - `local_path`: Path to the student assignment folder on your local computer
    - `course_name`: Name of the course
    - `student_list`: Path to the file containing the list of students' WatIAM usernames
    - `group_name`: Name of the course project
    - `subgroup_name`: Name of the assignment group
    - `due_date`: Due time of the current assignment

2. Run the script:
    ```
    python process.py
    ```

## grade.py

The `grade.py` script is used to generate a report for the students' grades.

### Prerequisites

- Python 3.x
- Pandas library (Install using `pip install pandas`)

### Usage

1. Set the following variables in the script:
    - `admin_username`: Course project admin username
    - `token`: Private token for authentication
    - `local_path`: Path to the student assignment folder on your local computer
    - `course_name`: Name of the course
    - `student_list`: Path to the file containing the list of students' WatIAM usernames
    - `group_name`: Name of the course project
    - `subgroup_name`: Name of the assignment group
    - `due_date`: Due time of the current assignment

2. Run the script:
    ```
    python grade.py
    ```

The generated grades report will be saved as `grades_final.csv` in the current directory.


