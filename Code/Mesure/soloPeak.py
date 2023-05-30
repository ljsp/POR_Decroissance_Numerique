import sys
import csv
from cgroup import launchCommandFor

if __name__ == "__main__":

    # return the cgroup peak of a command
    #
    # type : python3 script.py "command"
    # sudo password will be ask
    #
    # example when root is ./Code folder :
    # python3 Mesure/script2.py "gcc Tests/C++/char_alloc_n_write_m.cpp -o Tests/C++/char_alloc_n_write_m.exe"

    try:
        assert len(sys.argv) == 3
        command = str(sys.argv[1])
        outputFilename = str(sys.argv[2])
    except:
        print("Abort args")
        exit(1)
    
    #res = launchCommandFor(command)
    res = command
    
    print("Result is " + str(res) + " bytes")

    outputFilename = outputFilename.strip()
    if ".csv" not in outputFilename :
        outputFilename += ".csv"
    with open("../Resultats/cgroup/solo/" + outputFilename, 'w', newline='') as mf:
        wr = csv.writer(mf, quoting=csv.QUOTE_ALL)
        wr.writerow([res])

    print("Result was stored in Resultats/cgroup/solo/ folder")