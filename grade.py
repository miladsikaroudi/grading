import os.path
import re
import pandas as pd

admin_username = "admin_user"  # Course project admin username
token = "private_token"  # Private token
local_path = "C:/path/to/assignment_folder"  # Location of student assignment folder on your local computer
course_name = "mte140"  # Course name
student_list = "./student_list_filtered.txt"  # List of students' WatIAM
group_name = "course_project"  # Name of the course project
subgroup_name = "assignment_group"  # Name of the assignment group
due_date = '"master@{2023-03-24 23:59:59}"'  # Due time of current assignment

def generate_report(watiam):
    """
    Generate a report for the student's grade.

    Args:
        watiam (str): WatIAM username of the student.

    Returns:
        tuple: A tuple containing the student's grade (int) and description (str).
    """
    student_path = os.path.join(local_path, watiam)
    with open(os.path.join(student_path, "grade.txt"), "r") as grade_file:
        text = grade_file.read()
        pattern = r'Total grade: (\d+)'
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            total_grade = int(match.group(1))
            description = re.sub(match[0], '', text)
            print(watiam)
            return total_grade, description
        else:
            return 0, "Not compiled"

df = pd.DataFrame(columns=["Student", "Grade", "Description"])

with open(student_list, "r") as f:
    for watiam in f:
        watiam = watiam.strip()
        grade, description = generate_report(watiam)
        df = df.append(
            {"Student": watiam, "Grade": grade, "Description": description},
            ignore_index=True,
        )

df.to_csv("./grades_final.csv")
