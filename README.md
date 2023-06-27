Folder and File Renaming Utility

The Folder and File Renaming Utility is a Python script designed to automate the process of renaming folders and files within a specified directory. This utility is useful for situations where you have a large number of folders and files that need to be renamed according to predefined rules.

Features:

Renaming Folders: The script can scan a directory and rename folders based on a provided list of folder name pairs. Each pair consists of an old folder name and a new folder name. The utility uses regular expression pattern matching to identify folders to be renamed.

Renaming Files: The utility can also rename files within the specified folders based on a provided list of renaming mappings. Each mapping consists of an original prefix and a new file name. The utility scans each file within the folders and renames them if their names start with the specified prefixes.

Logging: The utility provides logging functionality to keep track of the renaming process. It logs messages when switching to a new folder, renaming a file, and when encountering errors or skipped files.

Usage:

Specify the directory path: Set the folder_path variable to the path of the directory where the renaming operation should be performed. By default, it is set to the current directory using the ./ notation.

Define folder renaming rules: Create a list of folder name pairs in the folders_to_rename variable. Each pair consists of an old folder name and a new folder name. The utility uses pattern matching to identify folders to be renamed.

Define file renaming rules: Create a dictionary of renaming mappings in the renaming_list variable. Each mapping consists of an original prefix and a new file name. The utility scans each file within the folders and renames them if their names start with the specified prefixes.

Run the script: Execute the script, and it will automatically rename the folders and files within the specified directory based on the provided rules. The script will log the renaming process, including any errors or skipped files.
