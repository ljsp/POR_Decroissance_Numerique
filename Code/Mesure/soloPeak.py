import sys
import csv
from time import time
from cgroup import launchCommandFor

if __name__ == "__main__":

    # return the cgroup peak of a command
    #
    # type : python3 soloPeaks.py [-p "<pre-command>"] "<command>" <outputFilename> [<nbTrials>] [-o]
    # sudo password will be ask
    #
    # example :
    # python3 soloPeak.py "gcc Tests/C++/char_alloc_n_write_m.cpp -o Tests/C++/char_alloc_n_write_m.exe" test1 5 -0
    # python3 soloPeak.py -p "cd ../Tests/Java" "javac char_alloc_n_write_m.java" test2

    try:
        i = 1

        precommand = ""
        if str(sys.argv[i]) == "-p":
            precommand = str(sys.argv[i + 1])
            i += 2

        command = str(sys.argv[i])
        i += 1

        outputFilename = str(sys.argv[i])
        i += 1

        isOut = False
        nbTrials = 1
        if i < len(sys.argv) and str(sys.argv[i]) != "-o":
            nbTrials = int(sys.argv[i])
            i += 1
        if i < len(sys.argv) and str(sys.argv[i]) == "-o":
            isOut = True
            i += 1
        
    except:
        print("Error with args")
        exit(1)
    
    start = round(time() * 1000)
    res = 0
    for i in range(nbTrials):
        res += launchCommandFor(command, precommand=precommand, isOut=isOut)
    res = int(res / nbTrials)
    stop = round(time() * 1000)
    
    print("Result is " + str(res) + " bytes")

    outputFilename = outputFilename.strip()
    if ".csv" not in outputFilename :
        outputFilename += ".csv"
    with open("../Resultats/cgroup/solo/" + outputFilename, 'w', newline='') as mf:
        wr = csv.writer(mf, quoting=csv.QUOTE_ALL)
        wr.writerow([res])

    print("Result was stored in Resultats/cgroup/solo/ folder (" + str(stop - start) + "ms)")