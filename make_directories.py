'''
| os.mkdir() is used to create a directory named "path" with the specified numeric mode.
| This method raises a "FileExistsError" if the directory to be created already exists.
|
| Syntax: 
|   os.mkdir(path, mode = 0o777, *, dir_fd = None)
|
| Parameters:
|   Name            | Definition
|   ----------------|------------------------------------------------------
|   path            | A path-like object representing a file system path
|                   | A path-like object is either a string or bytes object
|                   | representing a path.
|   ----------------|------------------------------------------------------             
|   mode(optional)  | A Integer value representing the mode of the
|                   | directory to be created. If this parameter is 
|                   | omitted, then its default value is Oo777
|   ----------------|------------------------------------------------------
|   dir_fd(optional)| A file descriptor referring to a directory. 
|                   | The default value of this parameter is None.
|                   | If the specified path is absolute, then dir_fd     
|                   | is ignored.
|   ----------------|------------------------------------------------------
|
| NOTE: the "*" in the parameter list indicates that all of the following 
|       parameters (here in our case 'dir_fd') are keyword-only parameters
|       and they can be provided using their name, not as a positional 
|       parameter.
|
| Return Type: Does not return a value.
'''

import os
import sys

num_args = len(sys.argv)
args = sys.argv

if num_args not in (3, 4):
    print("Use the script in the following ways:")
    print("Usage 1: python make_directories.py <prefix> <number_of_files>")
    print("Usage 2: python make_directories.py <prefix> <starting_file_number> <ending_file_number>")
    sys.exit(1)

current_directory = os.path.dirname(os.path.abspath(__file__))

try:
    if num_args == 4:
        start = int(args[2])
        end = int(args[3])

        if start < 0 or end < 0 or (end < start):
            raise ValueError
        
        max_num_chars = max(len(args[2]), len(args[3])) # for getting the right amount of numbers to format e.g., 01 100 will format the numbers like this: 001, 002, 003 ... 100
    else:
        start = 1
        end = int(args[2])
        max_num_chars = (len(args[2]))
except ValueError:
    print("The number of files, starting file number (if included), and ending file number must all be positive integers.")
    print("The ending file number must be greater than the starting file number.")
    sys.exit(1)

for i in range(start, end + 1):  # Fix: Include end value in the loop range
    # You can now create directories or perform other actions here using the iterator variable
    directory_name = f"{args[1]}{i:0{max_num_chars}d}"  # Using the max_num_chars to format the leading 0s

    # Check if the directory already exists
    if not os.path.exists(os.path.join(current_directory, directory_name)):
        os.makedirs(os.path.join(current_directory, directory_name))
        print(f"Directory '{directory_name}' created.")
    else:
        print(f"Directory '{directory_name}' already exists. Skipping.")



'''
| 1. __file__:
| -----------------------------------------------------------------------
| - __file__ is a built-in variable in Python that represents the path of
|   the currently executing script.
| - It contains the path to the script from which it is executed.
|
| 2. os.path.abspath(__file__):
| -----------------------------------------------------------------------
| - os.path.abspath() is a method from the os.path module that returns 
|   the absolute version of the specified path.
| - __file__ is passed to os.path.abspath(), and it converts the script's
|   path to an absolute path.
|
| 3. os.path.dirname(os.path.abspath(__file__)):
| -----------------------------------------------------------------------
| - os.path.dirname() is a method from the os.path module that returns
|   the directory name of a path.
| - It is applied to the absolute path obtained from the previous step.
| - This extracts the directory part of the absolute path, leaving you 
|   with the directory where the script is located.
|
| 4. current_directory = ...:
| -----------------------------------------------------------------------
| - The result of the entire expression is assigned to the variable 
|   current_directory.
| - Therefore, current_directory now holds the absolute path to the 
|   directory containing the currently executing script.
'''