import sys
import subprocess
    
def launchCommandFor(command):
    cmdCreate = "sudo cgcreate -g memory:max"
    cmdSetSwapMax = "echo \"" + str(0) + "\" | sudo dd of=/sys/fs/cgroup/max/memory.swap.max"
    cmdExec = "sudo cgexec -g memory:max " + command
    cmdDelete = "sudo cgdelete -g memory:max"

    subprocess.run(cmdCreate, shell=True)
    subprocess.run(cmdSetSwapMax, shell=True)
    subprocess.run(cmdExec, shell=True)

    res = -1
    with open("/sys/fs/cgroup/max/memory.peak", "r") as f:
        res = int(f.readline())
    
    subprocess.run(cmdDelete, shell=True)

    return res

if __name__ == "__main__":
    # python3 script.py "command"
    # sudo password will be ask
    # example : python3 test_base/script.py "python3 test_base/python/code/void.py" 24000000
    # return the cgroup peak
    try:
        assert len(sys.argv) == 2
        command = str(sys.argv[1])
    except:
        print("Abort args")
        exit(1)
    
    res = launchCommandFor(command)
    if res == -1:
        print("Abort result")
    print("Result is " + str(res) + " bytes")