import matplotlib.pyplot as plt
import matplotlib.ticker as tkr
import csv

def sizeof_fmt(x, pos):
    if x < 0:
        return ""
    for x_unit in ['bytes', 'kB', 'MB', 'GB', 'TB']:
        if x < 1024.0:
            return "%3.1f %s" % (x, x_unit)
        x /= 1024.0

if __name__ == "__main__":

    # Exec Alloc 100Mo Write 25Mo
    # fig, ax = plt.subplots()
    # x = ["C++"]
    # y = [25341952]
    # bar_colors = ['tab:purple']
    # ax.bar(x, y, width=0.2, edgecolor="white", color=bar_colors)
    # ax.yaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))
    # ax.set_title('RSS used to alloc 100Mo and write 25Mo in C++')
    # plt.show()
    
    # Compile helloworld
    # fig, ax = plt.subplots()
    # x = ["C (gcc)", "C++ (g++)", "Java (openJDK)", "CSharp", "Rust"]
    # y = [6160547, 40473067, 45082542, 28157378, 74058465]
    # bar_colors = ['tab:blue', 'tab:purple', 'tab:red', 'tab:orange', 'tab:green']
    # ax.bar(x, y, width=0.8, edgecolor="white", color=bar_colors)
    # ax.yaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))
    # ax.set_title('RSS used to compile "helloword" programs by langages')
    # plt.show()


    # Execute helloworld
    # fig, ax = plt.subplots()
    # x = ["C", "C++", "Java", "CSharp", "Rust", "Python", "JS (Node)"]
    # y = [370933, 387317, 9595289, 3316449, 381583, 2908979, 8646983]
    # bar_colors = ['tab:blue', 'tab:purple', 'tab:red', 'tab:orange', 'tab:green', 'tab:pink', 'tab:olive']
    # ax.bar(x, y, width=0.8, edgecolor="white", color=bar_colors)
    # ax.yaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))
    # ax.set_title('RSS used to execute "helloword" programs by langages')
    # plt.show()


    # Execute char_alloc_100000000_write_n for n from 0 to 100000000 by 1000000
    # xc = []
    # yc = []
    # with open("cgroup/multi/CAlloc100MBWriteNC.csv", 'r') as file:
    #     L = csv.reader(file).__next__()
    #     p = L[0]
    #     p = p[2:-2].split("], [")
    #     p[1] = p[1].split(", ")
    #     xc = [i for i in range(int(p[1][0]), int(p[1][1]) + 1, int(p[1][2]))]
    #     L = L[1:]
    #     yc = []
    #     for i in L:
    #         yc.append(int(i.split(" ")[2]))
    # xcpp = []
    # ycpp = []
    # with open("cgroup/multi/CAlloc100MBWriteNC++.csv", 'r') as file:
    #     L = csv.reader(file).__next__()
    #     p = L[0]
    #     p = p[2:-2].split("], [")
    #     p[1] = p[1].split(", ")
    #     xcpp = [i for i in range(int(p[1][0]), int(p[1][1]) + 1, int(p[1][2]))]
    #     L = L[1:]
    #     ycpp = []
    #     for i in L:
    #         ycpp.append(int(i.split(" ")[2]))
    # xjava = []
    # yjava = []
    # with open("cgroup/multi/CAlloc100MBWriteNJava.csv", 'r') as file:
    #     L = csv.reader(file).__next__()
    #     p = L[0]
    #     p = p[2:-2].split("], [")
    #     p[1] = p[1].split(", ")
    #     xjava = [i for i in range(int(p[1][0]), int(p[1][1]) + 1, int(p[1][2]))]
    #     L = L[1:]
    #     yjava = []
    #     for i in L:
    #         yjava.append(int(i.split(" ")[2]))
    # xpython = []
    # ypython = []
    # with open("cgroup/multi/CAlloc100MBWriteNPython.csv", 'r') as file:
    #     L = csv.reader(file).__next__()
    #     p = L[0]
    #     p = p[2:-2].split("], [")
    #     p[1] = p[1].split(", ")
    #     xpython = [i for i in range(int(p[1][0]), int(p[1][1]) + 1, int(p[1][2]))]
    #     L = L[1:]
    #     ypython = []
    #     for i in L:
    #         ypython.append(int(i.split(" ")[2]))
    # fig, ax = plt.subplots()
    # ax.plot(xc, yc, label="C", color='tab:blue')
    # ax.plot(xcpp, ycpp, label="C++", color='tab:purple')
    # ax.plot(xjava, yjava, label="Java", color='tab:red')
    # ax.plot(xpython, ypython, label="Python", color='tab:pink')
    # ax.xaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))
    # ax.yaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))
    # ax.set_title('RSS used to write char by size of write and by langages')
    # plt.legend()
    # plt.show()

    
    # Execute char_alloc_n_write_0 for n from 0 to 100000000 by 1000000
    # xc = []
    # yc = []
    # with open("cgroup/multi/EAllocNWrite0C.csv", 'r') as file:
    #     L = csv.reader(file).__next__()
    #     p = L[0]
    #     p = p[2:-2].split("], [")
    #     p[0] = p[0].split(", ")
    #     xc = [i for i in range(int(p[0][0]), int(p[0][1]) + 1, int(p[0][2]))]
    #     L = L[1:]
    #     yc = []
    #     for i in L:
    #         yc.append(int(i.split(" ")[2]))
    # xcpp = []
    # ycpp = []
    # with open("cgroup/multi/EAllocNWrite0C++.csv", 'r') as file:
    #     L = csv.reader(file).__next__()
    #     p = L[0]
    #     p = p[2:-2].split("], [")
    #     p[0] = p[0].split(", ")
    #     xcpp = [i for i in range(int(p[0][0]), int(p[0][1]) + 1, int(p[0][2]))]
    #     L = L[1:]
    #     ycpp = []
    #     for i in L:
    #         ycpp.append(int(i.split(" ")[2]))
    # xjava = []
    # yjava = []
    # with open("cgroup/multi/EAllocNWrite0Java.csv", 'r') as file:
    #     L = csv.reader(file).__next__()
    #     p = L[0]
    #     p = p[2:-2].split("], [")
    #     p[0] = p[0].split(", ")
    #     xjava = [i for i in range(int(p[0][0]), int(p[0][1]) + 1, int(p[0][2]))]
    #     L = L[1:]
    #     yjava = []
    #     for i in L:
    #         yjava.append(int(i.split(" ")[2]))
    # xpython = []
    # ypython = []
    # with open("cgroup/multi/EAllocNWrite0Python.csv", 'r') as file:
    #     L = csv.reader(file).__next__()
    #     p = L[0]
    #     p = p[2:-2].split("], [")
    #     p[0] = p[0].split(", ")
    #     xpython = [i for i in range(int(p[0][0]), int(p[0][1]) + 1, int(p[0][2]))]
    #     L = L[1:]
    #     ypython = []
    #     for i in L:
    #         ypython.append(int(i.split(" ")[2]))
    # fig, ax = plt.subplots()
    # ax.plot(xc, yc, label="C", color='tab:blue')
    # ax.plot(xcpp, ycpp, label="C++", color='tab:purple')
    # ax.plot(xjava, yjava, label="Java", color='tab:red')
    # ax.plot(xpython, ypython, label="Python", color='tab:pink')
    # ax.xaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))
    # ax.yaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))
    # ax.set_title('RSS used to allocate char by size of allocation and by langages')
    # plt.legend()
    # plt.show()

    SystemExit()