
import matplotlib.pyplot as plt
import re
import time

clock = 0
vss_data = []
map_data = []
unmap_data = []
time_data = []

current_vss = 0 
total_map = 0
total_unmap = 0

prev_alloc = 0
prev_vss = 0
prev_time = time.time()

with open("trace.log", "r") as f: # ouverture du fichier de log en mode lecture
    for line in f:
        
        if "mmap(" in line: # vérification si la ligne contient un appel mmap
            match = line.split(",")
            current_vss += int(match[1]) # si une taille est trouvée, on l'ajoute à la somme actuelle de VSS
      
        elif "munmap(" in line:
            match = line.split(",")
            match = match[1].split(")")
            current_vss -= int(match[0]) # si une taille est trouvée, on la retire de la somme actuelle de VSS
            
        elif "sbrk(" in line:
            raise Exception("Unexpected sbrk call")
            
        elif "brk(" in line:
            match = re.search(r"brk\((0x[a-fA-F0-9]+|NULL+)\).*=\s*(0x[a-fA-F0-9]+)", line)
            if match:
                alloc = int(match.group(2), base=16)
                if(match.group(1) == "NULL"):
                    prev_alloc = alloc
                else:
                    current_vss += alloc - prev_alloc
                    prev_alloc = alloc
        
        if vss_data:
            prev_vss = vss_data[-1]

        vss_data.append(prev_vss)
        vss_data.append(current_vss)
        
        time_data.append(clock - 1.0e-19)
        time_data.append(clock)
        
        current_time = time.time()
        elapsed_time = current_time - prev_time
        
        prev_time = current_time
        clock += current_vss / elapsed_time
        
# tracé du graphe en utilisant matplotlib
plt.plot(time_data, vss_data, label='VSS')
plt.xlabel('Temps (en octets/secondes)')
plt.ylabel('Utilisation de la mémoire (en octets)')
plt.title('Evolution de l\'utilisation de la mémoire au cours du temps')
plt.legend()
plt.show()