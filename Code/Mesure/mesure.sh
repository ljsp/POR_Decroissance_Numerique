#!/bin/bash

if [ "$1" = "memTool" ]; then

  g++ Tests/$2.cpp -o compiled_file

  python3 Outils/memTool ./compiled_file

  rm compiled_file

elif [ "$1" = "logReader" ]; then

  g++ Tests/$2.cpp -o compiled_file

  strace -e trace=memory -f -o trace.log ./compiled_file

  rm compiled_file

  python3 Outils/logReader.py

  rm trace.log

elif [ "$1" = "alloc-write-start" ]; then

  strace -e trace=memory -f -o trace.log ./Outils/alloc-write-start.sh $2 $3

  python3 Outils/logReader.py

  rm trace.log

else
  # sinon, on affiche un message d'erreur
  echo "Error: Invalid argument."
fi
