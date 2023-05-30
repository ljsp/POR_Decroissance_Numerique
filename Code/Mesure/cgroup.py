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