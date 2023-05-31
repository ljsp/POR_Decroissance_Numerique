import subprocess
import os

FNULL = open(os.devnull, 'w')

def launchCommandFor(command, precommand="", isOut=False):

    cmdCreate = "sudo cgcreate -g memory:max"
    cmdSetSwapMax = "echo \"" + str(0) + "\" | sudo dd of=/sys/fs/cgroup/max/memory.swap.max"
    cmdExec = "sudo cgexec -g memory:max " + command
    cmdDelete = "sudo cgdelete -g memory:max"

    if isOut:
        subprocess.run(cmdCreate, shell=True)
        subprocess.run(cmdSetSwapMax, shell=True)
        if precommand != "":
            subprocess.run(precommand + " && " + cmdExec, shell=True)
        else:
            subprocess.run(cmdExec, shell=True)
    else:
        subprocess.run(cmdCreate, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        subprocess.run(cmdSetSwapMax, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        if precommand != "":
            subprocess.run(precommand + " && " + cmdExec, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)
        else:
            subprocess.run(cmdExec, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)

    res = -1
    with open("/sys/fs/cgroup/max/memory.peak", "r") as f:
        res = int(f.readline())
    
    if isOut:
        subprocess.run(cmdDelete, shell=True)
    else:
        subprocess.run(cmdDelete, shell=True, stdout=FNULL, stderr=subprocess.STDOUT)

    return res