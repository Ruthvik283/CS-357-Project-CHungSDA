#!/bin/bash
# A bash script to simplify the running of code with the redirection of input and output.

# Ensure a test case number is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <testcase_number>"
    exit 1
fi

# Variables
testcase_num=$1
input_file="./testcases/testcase${testcase_num}.txt"
output_file="./testcases/outputs/output${testcase_num}.txt"
source_file="code.cpp"
binary_file="code"

# Compile the C++ code
g++ "$source_file" -o "$binary_file"
if [ $? -ne 0 ]; then
    echo "Compilation failed."
    exit 2
fi

# Check if the input file exists
if [ ! -f "$input_file" ]; then
    echo "Input file $input_file does not exist."
    exit 3
fi

# Run the binary with the input and output redirection
./"$binary_file" < "$input_file" > "$output_file"
if [ $? -eq 0 ]; then
    echo "Execution successful. Output written to $output_file"
else
    echo "Execution failed."
    exit 4
fi
