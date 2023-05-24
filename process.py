import os
import os.path
import subprocess

admin_username = ' '  # Course project admin username
token = ' '  # Private token
local_path = ' '  # Location of student assignment folder on your local computer
course_name = ' '  # Course name
student_list = "./student_list.txt"  # List of students' WatIAM
group_name = ' '  # Name of the course project
subgroup_name = 'a3'  # Name of the assignment group
due_date = '"master@{2023-04-03 23:59:59}"'  # Due time of current assignment

def pull_repo(watiam):
    """
    Clone the student's repository from the remote Git server.
    
    Args:
        watiam (str): WatIAM username of the student.
    """
    student_path = os.path.join(local_path, watiam)
    if not os.path.exists(student_path):
        os.makedirs(student_path)
    os.chdir(local_path)
    repo_url = f'https://{admin_username}:{token}@git.example.com/{group_name}/{subgroup_name}/{watiam}'
    os.system(f'git clone {repo_url}')
    os.chdir(student_path)
    os.system('git checkout ' + due_date)


def copy_testcase(watiam):
    """
    Copy the test case files to the student's assignment folder.
    
    Args:
        watiam (str): WatIAM username of the student.
    """
    student_path = os.path.join(local_path, watiam)
    subprocess.run(['cp', os.path.join(local_path, 'test.cpp'), student_path])
    subprocess.run(['cp', os.path.join(local_path, 'test.h'), student_path])
    subprocess.run(['cp', os.path.join(local_path, 'CMakeLists.txt'), student_path])


def compile_proj(watiam):
    """
    Compile the student's project using CMake and make.
    
    Args:
        watiam (str): WatIAM username of the student.
    """
    student_path = os.path.join(local_path, watiam)
    os.chdir(student_path)
    os.system('rm -rf ./*/')
    os.system('mkdir build && cd build && cmake -G "Unix Makefiles" -DCMAKE_C_COMPILER=gcc -DCMAKE_CXX_COMPILER=g++ ../ && make')


def grade_student(watiam):
    """
    Grade the student's project.
    
    Args:
        watiam (str): WatIAM username of the student.
    """
    grade = 10
    print(watiam)
    student_path = os.path.join(local_path, watiam)
    grade_file_path = os.path.join(student_path, "grade.txt")
    if os.path.exists(grade_file_path):
        open(grade_file_path, "w").close()
    with open(grade_file_path, 'a+') as grade_file:
        exe_path = os.path.join(student_path, 'build', f'{course_name}-L3.exe')
        if os.path.exists(exe_path):
            result = subprocess.run([exe_path], stdout=subprocess.PIPE)
            grade_file.write(result.stdout.decode("utf-8"))
        else:
            grade_file.write("Cannot compile.\n")


def generate_report(watiam):
    """
    Generate a report for the student's grade.
    
    Args:
        watiam (str): WatIAM username of the student.
    """
    student_path = os.path.join(local_path, watiam)
    grade_file_path = os.path.join(student_path, "grade.txt")
    grade_report = open(os.path.join(local_path, 'report.txt'), "w")  # Location of grade report
    with open(grade_file_path, 'r') as grade_file:
        lines = grade_file.read().splitlines()
        if len(lines) > 1:
            print(watiam + ' ' + lines[-1])
        else:
            print(watiam + ' No result')


def remove_testcase(watiam):
    """
    Remove the test case files from the student's assignment folder.
    
    Args:
        watiam (str): WatIAM username of the student.
    """
    student_path = os.path.join(local_path, watiam)
    subprocess.run(['rm', os.path.join(student_path, 'test.cpp')])
    subprocess.run(['rm', os.path.join(student_path, 'test.h')])


def push_grade(watiam):
    """
    Push the graded project to the student's repository.
    
    Args:
        watiam (str): WatIAM username of the student.
    """
    student_path = os.path.join(local_path, watiam)
    os.chdir(student_path)
    os.system('git checkout -b grade')
    os.system('git add test.cpp')
    os.system('git add test.h')
    os.system('git add grade.txt')
    os.system('git commit -m "Grade."')
    os.system('git push -u origin grade')


with open(student_list, "r") as f:
    for watiam in f:
        watiam = watiam.strip()
        pull_repo(watiam)
        copy_testcase(watiam)
        compile_proj(watiam)
        grade_student(watiam)
        generate_report(watiam)
        remove_testcase(watiam)
        push_grade(watiam)
