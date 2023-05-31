import matplotlib.pyplot as plt
import matplotlib.ticker as tkr

def sizeof_fmt(x, pos):
    if x < 0:
        return ""
    for x_unit in ['bytes', 'kB', 'MB', 'GB', 'TB']:
        if x < 1024.0:
            return "%3.1f %s" % (x, x_unit)
        x /= 1024.0

if __name__ == "__main__":
    
    # Compile helloworld
    # fig, ax = plt.subplots()
    # x = ["C (gcc)", "C++ (g++)", "Java (openJDK)", "CSharp", "Rust"]
    # y = [6160547, 40473067, 45082542, 28157378, 74058465]
    # bar_colors = ['tab:blue', 'tab:purple', 'tab:red', 'tab:orange', 'tab:green']
    # ax.bar(x, y, width=0.8, edgecolor="white", color=bar_colors)
    # ax.yaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))
    # ax.set_title('RSS used to compile "helloword" programs by langages')
    # plt.show()

    # Exec helloworld
    # fig, ax = plt.subplots()
    # x = ["C", "C++", "Java", "CSharp", "Rust", "Python", "JS (Node)"]
    # y = [370933, 387317, 9595289, 3316449, 381583, 2908979, 8646983]
    # bar_colors = ['tab:blue', 'tab:purple', 'tab:red', 'tab:orange', 'tab:green', 'tab:pink', 'tab:olive']
    # ax.bar(x, y, width=0.8, edgecolor="white", color=bar_colors)
    # ax.yaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))
    # ax.set_title('RSS used to execute "helloword" programs by langages')
    # plt.show()

    SystemExit()