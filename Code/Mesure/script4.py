import sys
import subprocess
import matplotlib.pyplot as plt
    
def launchCommandFor(command):
    try:
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
    except:
        res = -1
    return res

if __name__ == "__main__":
    # python3 script3.py min max pas
    # sudo password will be ask
    # example : python3 test_base/script.py "python3 test_base/python/code/void.py" 24000000
    # return the cgroup peak
    try:
        assert len(sys.argv) == 4
        minX = int(sys.argv[1])
        maxX = int(sys.argv[2])
        pas = int(sys.argv[3])
    except:
        print("Abort args")
        exit(1)

    pathC = "c/exe/char_alloc_n_write_m 100000000 "
    pathCpp = "c++/exe/char_alloc_n_write_m 100000000 "
    pathJava = "java char_alloc_n_write_m 100000000 "
    pathPython = "python3 python/code/char_alloc_n_write_m.py 100000000 "
    
    X = [i for i in range(minX, maxX + 1, pas)]
    Yc = [launchCommandFor(pathC + str(i)) for i in X]
    Ycpp = [launchCommandFor(pathCpp + str(i)) for i in X]
    Yjava = [launchCommandFor(pathJava + str(i)) for i in X]
    Ypython = [launchCommandFor(pathPython + str(i)) for i in X]

    plt.loglog(X, Yc, 'black', X, Ycpp, 'b', X, Yjava, 'r', X, Ypython, 'g')
    plt.show()
