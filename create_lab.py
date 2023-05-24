import requests
import time

admin_username = " "  # Course project admin username
token = " "  # Private token
course_name = ""  # Course name
template = "mte140_a2.tar.gz"  # Exported template file
student_list = "./student_list.txt"  # List of students' WatIAM
group_name = "mte140-2301"  # Name of the course project
subgroup_name = "a2"  # Name of the assignment group
namespace_id = "88858"  # Assignment group ID


def create_project(watiam):
    """
    Create a new project for the student.

    Args:
        watiam (str): WatIAM username of the student.
    """
    url = "https://example.com/api/v4/projects/import"  # Replace with the appropriate domain
    data = {"path": watiam, "namespace": namespace_id}  # Project name/path
    headers = {"Private-Token": token}
    files = {"file": open(template, "rb")}
    r = requests.post(url, headers=headers, data=data, files=files)
    print(r.content)


def get_user_id(watiam):
    """
    Get the user ID for the given WatIAM username.

    Args:
        watiam (str): WatIAM username of the student.

    Returns:
        str: User ID of the student.
    """
    url = f"https://example.com/api/v4/users?username={watiam}"  # Replace with the appropriate domain
    headers = {"Private-Token": token}
    r = requests.get(url, headers=headers)
    end = r.text.find(',"name"')
    return r.text[7:end]


def assign_member(watiam):
    """
    Assign the student as a member to the project.

    Args:
        watiam (str): WatIAM username of the student.
    """
    url = (
        f"https://example.com/api/v4/projects/{group_name}%2F{subgroup_name}%2F{watiam}/members"
    )  # Replace with the appropriate domain
    data = {"user_id": get_user_id(watiam), "access_level": "30"}
    headers = {"Private-Token": token}
    r = requests.post(url, headers=headers, data=data)
    print(r.content)


def branch_access(watiam):
    """
    Set branch access permissions for the student's project.

    Args:
        watiam (str): WatIAM username of the student.
    """
    url = (
        f"https://example.com/api/v4/projects/{group_name}%2F{subgroup_name}%2F{watiam}/protected_branches/master"
    )  # Replace with the appropriate domain
    headers = {"Private-Token": token}
    r = requests.delete(url, headers=headers)
    url = f"https://example.com/api/v4/projects/{group_name}%2F{subgroup_name}%2F{watiam}/protected_branches"
    data = {"push_access_level": "30", "name": "master"}
    headers = {"Private-Token": token}
    r = requests.post(url, headers=headers, data=data)
    print(r.content)


with open(student_list, "r") as f:
    for watiam in f:
        watiam = watiam.strip()
        create_project(watiam)
        time.sleep(5)
        assign_member(watiam)
        time.sleep(5)
        branch_access(watiam)
        time.sleep(5)