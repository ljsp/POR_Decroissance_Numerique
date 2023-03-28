#!/bin/bash

tool="$1"

if [ $tool = "cgroup" ]; then
    gcc ../Tests/C/char_alloc_n_write_m.c -o ../Tests/C/c_char_alloc_n_write_m
    g++ ../Tests/C++/char_alloc_n_write_m.cpp -o ../Tests/C++/cpp_char_alloc_n_write_m 
    python3 script3.py $2 $3 $4
    rm ../Tests/C/c_char_alloc_n_write_m
    rm ../Tests/C++/cpp_char_alloc_n_write_m 
fi

if [[ $# -ne 2 ]]; then
    echo "Invalid number of arguments"
    echo "Usage: $0 <memTool|logReader> <file_path>"
    exit 1 
fi


file_path="$2"
extension="${file_path##*.}"
file_name="${file_path%.*}"

if [ "$extension" = "$file_path" ]; then
    extension="no_extension"
fi

if [ $tool = "memTool" ]; then

    if [ $extension = "cpp" ]; then
        g++ $file_path -o compiled_file
        python3 memTool ./compiled_file
        rm compiled_file

    elif [ $extension = "py" ]; then
        python3 memTool python3 $file_path

    elif [ $extension = "no_extension" ]; then
        python3 memTool $file_path

    else
        echo "Error : unknown file type"

    fi

elif [ $tool = "logReader" ]; then

    if [ $extension = "cpp" ]; then
        g++ $file_path -o compiled_file
        strace -e trace=memory -f -o trace.log ./compiled_file
        rm compiled_file

    elif [ $extension = "py" ]; then
        strace -e trace=memory -f -o trace.log python3 $file_path

    elif [ $extension = "no_extension" ]; then
        strace -e trace=memory -f -o trace.log $file_path

    else
        echo "Error : unknown file type"

    fi

    python3 logReader.py
    rm trace.log

else
    echo "Error: Invalid argument."
fi
