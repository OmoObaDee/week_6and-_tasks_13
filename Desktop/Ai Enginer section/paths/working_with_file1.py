import os

print("Current working directory:", os.getcwd())

#      PYTHON FILE HANDLING

#   A file
#   is a place on your computer where data is stored.

# - Files can be of different types: text files (.txt, .csv, .json) or binary files (.jpg, .exe, .mp3).

# - In this notebook, we will focus mainly on text files, but the concepts also apply to binary files.
# - To get a better understanding of how to handle files in python, lets imagine a file as a notebook, you can open a book(open), write inside a book(write), read a book(read), add to what you have written(append), then close the note when you are done(close).

            #  MORESO..!!!!
# - So, to get started with working with files or handling files, we must first have a good understanding of `paths`.

# - A path is simply the "address" of a file or folder on your computer, just like a home address tells you where someone lives. 



# 1. Current Working Directory (CWD)

# - When Python runs a program, it always has a current working directory, this is the folder where it looks for files by default.

# - Create a folder, go to your vscode and open the folder from there.
# - Create a .py file and name it, "my_path.py". Then write the codes below inside it and run.


# now how it works
# using os.getcwd()


# import os
#  Get the current working directory

# print(" Current working directory:", os.getcwd())
# Ensure to check the output  :PS C:\Users\ncc\Desktop\paths> & C:/Users/ncc/Desktop/paths/new_env/Scripts/Activate.ps1
            # & : File C:\Users\ncc\Desktop\paths\new_env\Scripts\Activate.ps1 cannot be loaded because running scripts is disabled on this system. For more information, see about_Execution_Policies at 
            # https:/go.microsoft.com/fwlink/?LinkID=135170.
            # At line:1 char:3
            # + & C:/Users/ncc/Desktop/paths/new_env/Scripts/Activate.ps1
            # +   ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            #     + CategoryInfo          : SecurityError: (:) [], PSSecurityException
            #     + FullyQualifiedErrorId : UnauthorizedAccess
            # PS C:\Users\ncc\Desktop\paths> & C:/Users/ncc/Desktop/paths/new_env/Scripts/python.exe c:/Users/ncc/Desktop/paths/my_paths.py
            # Current working directory: C:\Users\ncc\Desktop\paths
            # PS C:\Users\ncc\Desktop\paths> 




# 2. Absolute vs. Relative Paths


# - I believe you saw something like this in the previous class, when you were activating your environment, right?

# - **Absolute Path** the full address of a file (like a complete GPS location).


#  - Example:

# Windows: C:\Users\Chris\Desktop\my_path.py`

# Mac/Linux: /home/chris/Desktop/my_path.py`

# Relative Path** a shortcut that starts from the current working directory.

#   - Example:

# - If your current working directory is C:\Users\Chris\Desktop,
# then "my_path.py" will point to C:\Users\Chris\Desktop\my_path.py.


# Absolute path example
absolute_path =r"c:\Users\Oludayo\Desktop\my_paths.py"

# Relative path example
relative_path = "my_path"

print("Absolute Path :", absolute_path)
print("Relative Path:", relative_path)


# 3. Joining Paths (The Right Way)

# A time will come when the need to join paths will arise.
# The lines of codes should give the understanding of how to.

import os
folder = "C/Users/Oludayo/Desktop"
filename = "my_path"

path = os.path.join(folder, filename)
print("Full path:", path)
# output : Full path: C/Users/Oludayo/Desktop\my_path

# note this way, python handles slashes (/ vs\) automatically.



# 4. Checking If a File or Folder Exists

# - Sometimes we want to make sure a file is really there before we try to open it.
# We can check using `os.path.exists`.

import os
path = "my_path.py"
if os.path.exists(path):
    print("Yes, the file exists!!!")
else:
    print("File not found.")
# ouput: File not found.


# 5. Using pathlib (Modern Way)

# - Python has a modern library called `pathlib`, which is easier to use than `os`.

from pathlib import Path

# current working directory
print("Current directory:", Path.cwd())

#create a path object
file = Path("myfile.txt")

# check if it exists
print(" File exists:", file.exists())

# combine paths
folder = Path("C:/Users/Oludayo/Desktop")
full_path = folder /"myfile.txt"
print("Full path:", full_path)
# output : Full path: C:\Users\ncc\Desktop\myfile.txt

#  6. Navigating Folders with pathlib

from pathlib import Path

# Get parent folder of current file
print("Parent folder:", Path.cwd().parent)
# output: Full path: C:\Users\Oludayo\Desktop\myfile.txt
                    #Parent folder: C:\Users\ncc\Desktop

# List all files in a directory
for file in Path.cwd().iterdir():
    print(file)
#output: C:\Users\ncc\Desktop\paths\my_paths.py
        # C:\Users\ncc\Desktop\paths\new_env
        # PS C:\Users\ncc\Desktop\paths>  


