This is a sample application using python, xlrd and xlwt as a teaching material.

# Purpose of sample application

Extracting some values from many Excel files and aggregate them.

# Pre-condition

- There are a lot of excel files in a directory (`resources/input_files`).
- The file format is Excel and has same layout.
- Each files include scores of a student.
- the file name pattern is `student_[0-9]+\.xlsx`. The number after "student_" is student id.

# Process

- 1. Get input files.
- 2. Make output file.
- 3. Loop for input files in the directory.
	- 3.1. Open the input file.
	- 3.2. Pick up the values needed.
	- 3.3. Write the values into the output file.
- 4. Save output file.

# Post-condition

- An output file (`resources/output_YYYYmmdd_HHMMSS.xls`) which includes result value.
