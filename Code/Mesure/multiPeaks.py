import sys
import csv
from time import time
from cgroup import launchCommandFor

if __name__ == "__main__":

    # return the cgroup peaks of a command with changing parameters
    #
    # type : python3 multiPeaks.py [-p "<pre-command>"] "<command>" <outputFilename> [<nbTrials>] [-o] [-c <val> ]* -v <min> <max> <pos> [-c <val> |-v <min> <max> <pos> ]*
    # sudo password will be ask
    #
    # if we assume that char_alloc_n_write_m.cpp and char_alloc_n_write_m.java are already compiled,
    # examples :
    # python3 multiPeaks.py "../Tests/C++/char_alloc_n_write_m.exe" test1 -o -c 1000000 -v 0 1000000 100000
    # python3 multiPeaks.py -p "cd ../Tests/Java" "java ../Tests/Java/char_alloc_n_write_m" test2 3 -c 1000000 -v 0 1000000 200000

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

        nbTrials = 1
        if str(sys.argv[i]) != "-o" and str(sys.argv[i]) != "-c" and str(sys.argv[i]) != "-v":
            nbTrials = int(sys.argv[i])
            i+=1

        isOut = False
        if str(sys.argv[i]) == "-o":
            isOut = True
            i += 1

        parameters = []
        nbParam = 0
        var = []
        nbVar = 0
        while i < len(sys.argv):
            if sys.argv[i] == "-c":
                l = [int(sys.argv[i + 1])]
                parameters.append(l)
                i += 2
            else :
                assert int(sys.argv[i + 1]) + int(sys.argv[i + 3]) <= int(sys.argv[i + 2])
                assert int(sys.argv[i + 3]) >= 0
                l = [j for j in range(int(sys.argv[i + 1]), int(sys.argv[i + 2]) + 1, int(sys.argv[i + 3]))]
                parameters.append(l)
                i += 4
                var.append(len(parameters) - 1)
                nbVar += 1
            nbParam += 1
        doneTab = [False for i in range(nbVar)]
        isDone = False
        isVar = var[0]
        X = [parameters[i][0] for i in range(nbParam)]
        X2 = [0 for i in range(nbParam)]
        Y = []
    except:
        print("Error with args")
        exit(1)
    
    start = round(time() * 1000)
    while not isDone:
        x = ""
        for i in X:
            x += str(i) + " "
        x.strip()

        res = 0
        for i in range(nbTrials):
            res += launchCommandFor(command + " " + x, precommand=precommand, isOut=isOut)
        res = int(res / nbTrials)

        Y.append(x + str(res))

        if X2[isVar] < len(parameters[isVar]) - 1:
            X2[isVar] += 1
            X[isVar] = parameters[isVar][X2[isVar]]
        else:
            doneTab[0] = True
            isDone = True
            for i in range(nbVar):
                if not doneTab[i]:
                    isDone = False
                    X2[var[i]] += 1
                    X[var[i]] = parameters[var[i]][X2[var[i]]]
                    for j in range(var[i]):
                        X2[j] = 0
                        X[j] = parameters[j][0]
                    for j in range(i):
                        doneTab[j] = False
                    if X2[var[i]] == len(parameters[var[i]]) - 1:
                        doneTab[i] = True
                    break
    stop = round(time() * 1000)

    outputFilename = outputFilename.strip()
    if ".csv" not in outputFilename :
        outputFilename += ".csv"
    with open("../Resultats/cgroup/multi/" + outputFilename, 'w', newline='') as mf:
        wr = csv.writer(mf, quoting=csv.QUOTE_ALL)
        wr.writerow(Y)
    
    print("Results were stored in Resultats/cgroup/multi/ folder (" + str(stop - start) + "ms)")