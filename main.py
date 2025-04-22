import os
import subprocess

# Define the project directory
print("Git Auto Push Program\nThis is intended for Windows")
print("""
When prompted, enter the file path and remove the quotations around it, press enter.
    -(To get the file location right click on the file and select copy path.)

Enter a commit message without quotations, press enter.
    -(Example:added a feature to a .py file)
    
Enter the name of the branch, press enter
    -(Exampl:main)
""")

# Get the project directory form input
proj_directory = input('Enter file path: ')

# Convert the path to a normal path due to slashes
proj_directory_norm_path = os.path.normpath(proj_directory)

# Check if the location exists
if not os.path.isdir(proj_directory_norm_path):
    print('File location does not exist.')
    exit()

# Change the directory
os.chdir(proj_directory_norm_path)

# Get commit message and branch name form input
commit_msg = input("Enter A Commit Message: ")
branch = input("Enter Branch Name (ex: main): ")

# Execute the git commands in command prompt (windows)
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", commit_msg])
subprocess.run(["git", "push", "origin", branch])

# Print message to show end of program.
print('Git push command successful')