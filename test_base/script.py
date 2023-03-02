import sys
import subprocess

def launchCommandForDev(nbBytes, command):
    #footer = " > /dev/null"
    cmdCreate = "sudo cgcreate -g memory:" + str(nbBytes)
    cmdSetMax = "echo \"" + str(nbBytes) + "\" | sudo dd of=/sys/fs/cgroup/" + str(nbBytes) + "/memory.max"
    cmdSetSwapMax = "echo \"" + str(0) + "\" | sudo dd of=/sys/fs/cgroup/" + str(nbBytes) + "/memory.swap.max"
    cmdExec = "sudo cgexec -g memory:" + str(nbBytes) + " " + command
    cmdDelete = "sudo cgdelete -g memory:" + str(nbBytes)

    subprocess.run(cmdCreate, shell=True)
    #print("created")
    subprocess.run(cmdSetMax, shell=True)
    #print("set max")
    subprocess.run(cmdSetSwapMax, shell=True)
    #print("set swap max")
    #print("begin running")
    subprocess.run(cmdExec, shell=True)
    #print("end running")

    res = -1
    with open("/sys/fs/cgroup/" + str(nbBytes) + "/memory.events", "r") as f:
        res = int(f.readlines()[2].split(" ")[1][:-1])
    #print("read value")
    
    subprocess.run(cmdDelete, shell=True)
    #print("deleted")

    return res

def launchCommandFor(nbBytes, command):
    cmdCreate = "sudo cgcreate -g memory:" + str(nbBytes)
    cmdSetMax = "echo \"" + str(nbBytes) + "\" | sudo dd of=/sys/fs/cgroup/" + str(nbBytes) + "/memory.max"
    cmdSetSwapMax = "echo \"" + str(0) + "\" | sudo dd of=/sys/fs/cgroup/" + str(nbBytes) + "/memory.swap.max"
    cmdExec = "sudo cgexec -g memory:" + str(nbBytes) + " " + command
    cmdDelete = "sudo cgdelete -g memory:" + str(nbBytes)

    subprocess.run(cmdCreate, shell=True)
    subprocess.run(cmdSetMax, shell=True)
    subprocess.run(cmdSetSwapMax, shell=True)
    subprocess.run(cmdExec, shell=True)

    res = -1
    with open("/sys/fs/cgroup/" + str(nbBytes) + "/memory.events", "r") as f:
        res = int(f.readlines()[2].split(" ")[1][:-1])
    
    subprocess.run(cmdDelete, shell=True)

    return res

if __name__ == "__main__":
    # python3 script.py "command" memMin memMax precision
    # all in bytes
    # sudo password will be ask
    # example : python3 test_base/script.py "python3 test_base/python/code/void.py" 1000000 5000000 100000
    # return an interval of the max memory value
    try:
        assert len(sys.argv) == 5
        command = str(sys.argv[1])
        memMin = int(sys.argv[2])
        memMax = int(sys.argv[3])
        precision = int(sys.argv[4])
        assert memMin >= 50_000 and memMax <= 4_000_000_000 and precision >= 10_000
        assert memMin + precision <= memMax
    except:
        print("Abort args")
        exit(1)
    
    res = launchCommandFor(memMax, command)
    print("res = " + str(res))
    if res == -1 :
        print("Abort max")
        exit(1)
    elif res > 0 :
        print("Solution is above " + str(memMax))
        exit(1)

    res = launchCommandFor(memMin, command)
    print("res = " + str(res))
    if res == -1 :
        print("Abort min")
        exit(1)
    elif res == 0 :
        print("Solution is under " + str(memMin))
        exit(1)

    count = 1
    while memMax - memMin > precision:
        nextVal = int((memMax + memMin) / 2)
        #print("Max is " + str(memMax) + ", min is " + str(memMin) + ", next max is " + str(nextVal))
        res = launchCommandFor(nextVal, command)
        #print("res = " + str(res))
        if res == -1 :
            print("Abort at iteration " + str(count))
            exit(1)
        elif res > 0:
            memMin = nextVal
        else:
            memMax = nextVal
        count += 1

    print("Solution is between " + str(memMax) + " and " + str(memMin))