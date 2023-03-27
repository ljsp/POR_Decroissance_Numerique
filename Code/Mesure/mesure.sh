#!/bin/bash

if [[ $# -ne 2 ]]; then
    echo "Invalid number of arguments"
    echo "Usage: $0 <memTool|logReader> <file_path>"
    exit 1 
fi

tool="$1"
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
