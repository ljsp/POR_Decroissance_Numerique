
import matplotlib.pyplot as plt

clock = 0
vss_data = []
map_data = []
unmap_data = []
time = []

current_vss = 0 
total_map = 0
total_unmap = 0

with open("trace.log", "r") as f: # ouverture du fichier de log en mode lecture
    for line in f:
        if "mmap(" in line: # vérification si la ligne contient un appel mmap
            match = line.split(",")
            total_map += int(match[1])
            current_vss += int(match[1]) # si une taille est trouvée, on l'ajoute à la somme actuelle de VSS
      
        elif "munmap(" in line:
            match = line.split(",")
            match = match[1].split(")")
            current_vss -= int(match[0]) # si une taille est trouvée, on la retire de la somme actuelle de VSS
            total_unmap += int(match[0])
    
        # ajout des valeurs actuelles à chaque itération de la boucle
        vss_data.append(current_vss)
        map_data.append(total_map)
        unmap_data.append(total_unmap)
        time.append(clock)
        clock += 1
        
print(vss_data)

# tracé du graphe en utilisant matplotlib
plt.plot(time, vss_data, label='VSS')
plt.plot(time, map_data, label='Mapped')
plt.plot(time, unmap_data, label='Unmapped')
plt.xlabel('Temps (en secondes)')
plt.ylabel('Utilisation de la mémoire (en octets)')
plt.title('Evolution de l\'utilisation de la mémoire au cours du temps')
plt.legend()
plt.show()