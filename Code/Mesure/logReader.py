
import matplotlib.pyplot as plt
import re
import sys
import matplotlib.ticker as tkr  
import pandas as pd

def sizeof_fmt(x, pos):
    if x < 0:
        return ""
    for x_unit in ['bytes', 'kB', 'MB', 'GB', 'TB']:
        if x < 1024.0:
            return "%3.1f %s" % (x, x_unit)
        x /= 1024.0

clock = 0
vss_data = []
time_data = []

current_vss = 0     #
max_vss = 0

prev_brk_alloc = 0
prev_vss = 0

trace = sys.argv[1]
program_path = trace.split("/")
program_name = program_path[-1].removesuffix(".log")

with open(trace, "r") as f: # ouverture du fichier de log en mode lecture
    
    for line in f:
        
        if "mmap(" in line: # vérification si la ligne contient un appel mmap
            match = line.split(",")
            current_vss += int(match[1])
      
        elif "munmap(" in line:
            match = line.split(",")
            match = match[1].split(")")
            match = match[0].split(" ")
            current_vss -= int(match[1])
            
        elif "sbrk(" in line:
            raise Exception("Unexpected sbrk call")
            
        elif "brk(" in line:
            match = re.search(r"brk\((0x[a-fA-F0-9]+|NULL+)\).*=\s*(0x[a-fA-F0-9]+)", line)
            if match:
                alloc = int(match.group(2), base=16)
                if(match.group(1) == "NULL"):
                    prev_brk_alloc = alloc
                else:
                    current_vss += alloc - prev_brk_alloc
                    prev_brk_alloc = alloc
        
        if current_vss > max_vss:
            max_vss = current_vss
            
        if vss_data:
            prev_vss = vss_data[-1]

        vss_data.append(prev_vss)
        vss_data.append(current_vss)
        
        clock += abs(current_vss - prev_vss)
        time_data.append(clock)
        time_data.append(clock)

# Graph
df = pd.DataFrame(list(zip(time_data, vss_data)), columns=['Time', 'VSS'])
print("VSS peak : {:.1f} Mo".format(max_vss / 1000000))
ax = df.plot(x='Time', y='VSS', label='VSS')
ax.yaxis.set_major_formatter(tkr.FuncFormatter(sizeof_fmt))
plt.xlabel('Temps (en octets/par allocations)')
plt.ylabel('Utilisation de la mémoire (en octets)')
plt.title('logReader : ' + program_name)
plt.legend()
plt.show()