#!/bin/bash

if [ "$1" = "memTool" ]; then

  if [ "$2" = "cpp" ]; then 

    g++ Tests/$3.cpp -o compiled_file

    python3 Outils/memTool ./compiled_file

    rm compiled_file

  elif [ "$2" = "python" ]; then
  
    python3 Outils/memTool -t "python3 Tests/$3.py"

  else

    echo "Error : unknown file type"
  
  fi

elif [ "$1" = "logReader" ]; then

  if [ "$2" = "cpp" ]; then 

    g++ Tests/$3.cpp -o compiled_file
    strace -e trace=memory -f -o trace.log ./compiled_file
    # --status=successful,failed 
    rm compiled_file
  
  elif [ "$2" = "python" ]; then

    strace -e trace=memory -f -o trace.log python3 Tests/$3.py

  else 

    echo "Error : unknown file type"
  
  fi

  python3 Outils/logReader.py
  
  rm trace.log

else
  echo "Error: Invalid argument."
fi
