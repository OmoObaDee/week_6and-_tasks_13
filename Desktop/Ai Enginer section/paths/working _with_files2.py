#1. setting up
# its cleaner to work inside a folder so files dnt clutter your desktop.

from pathlib import Path

workspace = Path(" workingspace_files")
workspace.mkdir(exist_ok=True)
file_path = workspace/"notes.txt"
file_path

# 2. Create a file

#    There are two common ways to “create”:

#  - `w` (write): creates the file if it doesn’t exist; overwrites if it does.

# #  - `x` (exclusive create): creates the file only if it doesn’t exist; errors if it does (safer if you don’t want to overwrite by mistake).

# #  - Use `w` when you’re okay with replacing old content; use `x` when you want to avoid accidental overwrites.

# # A) create or overwrite using 'w'

# f= open(file_path, 'w', encoding="utf-8")
# f.write(" This is the first line in notes.text\n")
# f.close()


# # (B) Safe-create using 'x' (uncomment to try once)

# f = open(workspace / "created_once.txt", "x", encoding="utf-8")
# f.write("This file will only be created if it doesn't exist.\n")
# f.close()


#   3. Open a file

# - Opening a file prepares it for reading or writing.

# Open for writing again (this will overwrite!)
# f = open(file_path, "w", encoding="utf-8")
# f.write("Replaced the old content with this line.\n")
# f.close()

# Note: If you only want to add new content, don’t use 'w' ...
#  use 'a' (append).


# 4. Write to a file

# - Writing puts text into the file. 
#   write() does not add newlines automatically (you add `\n` yourself).

# f = open(file_path, "w", encoding="utf-8")
# f.write("Shopping List:\n")
# f.write(" - Rice\n")
# f.write(" - Beans\n")
# f.write(" - Garri\n")
# f.close()


# 5. Append to a file

# - Append adds to the end without deleting what’s already there.

# f = open(file_path, "a", encoding="utf-8")
# f.write(" - Groundnut oil\n")
# f.write(" - Maggi\n")
# f.close()

# 6. Read from a file

#      There are four common ways:

#   - read() - whole file as one string

#   - read(n)  - first n characters

#   - readline()  - one line

#   - readlines()  - list of all lines


# Read the whole file
f = open(file_path, "r", encoding="utf-8")
content = f.read()
f.close()
print(content)
# output:
# Shopping List:
#  - Rice
#  - Beans
#  - Garri
#  - Groundnut oil
#  - Maggi


# Read line-by-line

f = open(file_path, "r", encoding="utf-8")
print("First line:", f.readline().rstrip())
print("Second line:", f.readline().rstrip())
f.close()
#output: First line: Shopping List:
                    # Second line:  - Rice

# Read as a list of lines

f = open(file_path, "r", encoding="utf-8")
lines = f.readlines()
f.close()
print("Lines list:", [line.rstrip() for line in lines])
#output: Lines list: ['Shopping List:', ' - Rice', ' - Beans', ' - Garri', ' - Groundnut oil', ' - Maggi']


# Iterate over lines (memory-friendly)

f = open(file_path, "r", encoding="utf-8")
for line in f:
    print("->", line.rstrip())
f.close()

#output: -> Shopping List:
        # ->  - Rice
        # ->  - Beans
        # ->  - Garri
        # ->  - Groundnut oil
        # ->  - Maggi


# 7.       Close the file

#  - Always close files opened with open(...).

#   - It flushes (saves) any buffered data to disk.

#   - It releases the OS handle so other programs can use the file.

#   - It avoids weird bugs (especially on Windows).

#     You have seen f.close() above. But there’s a better way…


# 8. Use with `open(...) as f:` (best practice)

# The 'with' statement automatically closes the file even if an error happens. 
# This is the recommended way.


# Write safely

with open(file_path, "w", encoding="utf-8") as f:
    f.write("My Todo List:\n")
    f.write(" - Revise Python file handling\n")
    f.write(" - Practice error handling within a function")
    f.write(" - Practice JSON & CSV\n")
#output :
# First line: My Todo List:
# Second line:  - Revise Python file handling
# Lines list: ['My Todo List:', ' - Revise Python file handling', ' - Practice error handling within a function - Practice JSON & CSV']
# -> My Todo List:
# ->  - Revise Python file handling
# ->  - Practice error handling within a function - Practice JSON & CSV


# Append safely

with open(file_path, "a", encoding="utf-8") as f:
    f.write(" - Build a small project\n")
#output:
# irst line: My Todo List:
# Second line:  - Revise Python file handling
# Lines list: ['My Todo List:', ' - Revise Python file handling', ' - Practice error handling within a function - Practice JSON & CSV', ' - Build a small project']
# -> My Todo List:
# ->  - Revise Python file handling
# ->  - Practice error handling within a function - Practice JSON & CSV
# ->  - Build a small project


# Summary

# | Mode   | Meaning                       | Typical use     |
# | ------ | ----------------------------- | --------------- |
# | 'r'  | Read (file must exist)        | Reading text    |
# | 'w'  | Write (overwrite/create)      | Start fresh     |
# | 'a'  | Append (create if missing)    | Add to end      |
# | 'x'  | Create (error if exists)      | Safe create     |
# | `b'  | Binary (combine, e.g. 'rb') | Images/videos   |
# | 't'  | Text (default)                | Human-readable  |
# | 'r+' | Read & write (no truncate)    | Update in place |


# More Context 

# What Happens When Things Go Wrong?

# Sometimes files don't exist, or we don't have permission to read them. 
# Python will give us an error, but we can catch and handle these errors gracefully.
#  Let's see how to do that.


from pathlib import Path

workspace = Path("workspace_files")
workspace.mkdir(exist_ok=True)

# Try to read a file that doesn't exist
try:
    with open(workspace / "missing_file.txt", "r") as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("Oops! That file doesn't exist yet.")
    print("Let's create it first!")
    
    # Now create the file
    with open(workspace / "missing_file.txt", "w") as f:
        f.write("Now I exist!")
    print("File created successfully!")


# If you write this correctly, you should see something like this...
# output:
        # """
        # Oops! That file doesn't exist yet.
        # Let's create it first!
        # File created successfully!


# Running cells with 'Python 3.13.7' requires the ipykernel package.

# Create a Python Environment with the required packages.

# Or install 'ipykernel' using the command: 'c:/Users/ncc(Admin)/AppData/Local/Microsoft/WindowsApps/python3.13.exe -m pip install ipykernel -U --user --force-reinstall'


# **Checking If Files Exist Before Using Them
# - Before trying to read or write files, it's smart to check if they exist first.


from pathlib import Path

workspace = Path("workspace_files")
file_path = workspace / "notes.txt"

# Check if our file exists
if file_path.exists():
    print(f"Found the file: {file_path.name}")
    
    # Get some information about the file
    file_size = file_path.stat().st_size
    print(f"File size: {file_size} bytes")
    
    # Read and show the content
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
        print(f"Content preview: {content[:50]}...")  # First 50 characters
else:
    print(f"File {file_path.name} doesn't exist")
    print("You might want to create it first!")

# If notes.txt exists

#output:
# Found the file: notes.txt
# File size: 67 bytes
# Content preview: Todo:
#  - Revise Python file handling
#  - Practice J...


# # if notes.txt does not exist

# """
# File notes.txt doesn't exist
# You might want to create it first!


# Working with JSON Files (Storing Data)**

# - JSON files are great for storing structured data like dictionaries and lists. 
#    Think of them as a way to save Python data to a file.


import json
from pathlib import Path

workspace = Path("workspace_files")

# Create some student data (like a mini database)
student_data = {
    "name": "Oyindamola",
    "age": 16,
    "courses": ["Python", "Data Science", "Web Development"],
    "grades": {"Python": "A", "Data Science": "B+", "Web Development": "A-"},
    "is_graduated": False
}

# Save the data to a JSON file
json_file = workspace / "student_data.json"
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(student_data, f, indent=2)  # indent=2 makes it pretty and readable

print("Student data saved to JSON file!")

# Now read it back
with open(json_file, "r", encoding="utf-8") as f:
    loaded_data = json.load(f)

print("\nData read from JSON file:")
print(f"Student name: {loaded_data['name']}")
print(f"Age: {loaded_data['age']}")
print(f"Courses: {', '.join(loaded_data['courses'])}")
print(f"Python grade: {loaded_data['grades']['Python']}")


import csv
from pathlib import Path
workspace = Path("workspace_files")
csv_file = workspace /"students.csv"


# create sample student data
students = [
    ["Name", "Age"," Course", "Grade"],
    ["Oludayo",48, "Python", "A"],
    ["Favour", 30, "Javascript", "B+"],
    ["Precious", 20, "Python", "A-"],
    ["Ore", 25, "Python", "A"],
    ["Oluayo", 18, "Python", "A"]
]

#  write data to csv file
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(students)  #write all rows at once

print("student data written to csv file!!!")

# Read the csv file back
print("\nReading CSV file:")
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    
    for row_number, row in enumerate(reader):
        if row_number == 0:  # Header row
            print(f"Headers: {' | '.join(row)}")
            print("-" * 40)
        else:  # Data rows
            name, age, course, grade = row
            print(f"{name} ({age} years) - {course}: {grade}")



#   Working with Multiple Files at Once

# - Sometimes you need to read from one file and write to another at the same time.

