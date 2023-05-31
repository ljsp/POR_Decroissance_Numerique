#!/bin/bash

tool="$1"

if [ $tool = "cgroup" ]; then
    if [ $# -lt 4 ]; then
        echo "Invalid number of arguments"
        echo "Usage: $0 cgroup <solo|multi> <command> <outputFileName> otherArgs..."
        exit 1
    fi

    option="$2"

    shift 2
    args=""
    for arg in "$@"; do
        quoted_arg="\"$arg\""
        args="$args $quoted_arg"
    done

    if [ $option = "solo" ]; then
        python3 soloPeak.py $args
    elif [ $option = "multi" ]; then
        python3 multiPeaks.py $args
    else
        echo "Wrong args"
    fi
else
    if [ $# -ne 2 ]; then
        echo "Invalid number of arguments"
        echo "Usage: $0 <memTool|logReader> <file_path>"
        exit 1
    fi

    file_path="$2"
    extension="${file_path##*.}"
    file_name="${file_path%.*}"

    if [ $tool = "memTool" ]; then

        if [ $extension = "cpp" ]; then
            g++ $file_path -o $file_name
            python3 memTool ./$file_name
            rm $file_name

        elif [ $extension = "py" ]; then
            python3 memTool "python3 $file_path"

        else
            python3 memTool $file_path

        fi

    elif [ $tool = "logReader" ]; then

        if [ $extension = "cpp" ]; then
            g++ $file_path -o compiled_file
            strace -e trace=memory -f -o $file_name.log ./compiled_file
            rm compiled_file

        elif [ $extension = "py" ]; then
            strace -e trace=memory -f -o $file_name.log python3 $file_path

        else
            strace -e trace=memory -f -o $file_name.log $file_path

        fi

        python3 logReader.py $file_name.log
        rm $file_name.log

    else
        echo "Error: Invalid argument."
    fi
fi
