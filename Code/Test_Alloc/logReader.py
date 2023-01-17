import re # importation de la librairie de gestion des expressions régulières

vss = 0 # variable pour stocker la somme de la mémoire virtuelle allouée (VSS)
rss = 0 # variable pour stocker la somme de la mémoire physique utilisée (RSS)

with open("trace.log", "r") as f: # ouverture du fichier de log en mode lecture
    for line in f: # boucle qui lit chaque ligne du fichier
        if "mmap(" in line: # vérification si la ligne contient un appel mmap
            match = re.search(r"mmap\(.*, (\d+)", line) # recherche de la taille de mémoire allouée (VSS) dans la ligne
            if match:
                vss += int(match.group(1)) # si une taille est trouvée, on l'ajoute à la somme de VSS

            match = re.search(r"\[(\d+)\]", line) # recherche de la taille de mémoire utilisée (RSS) dans la ligne
            if match:
                rss += int(match.group(1)) # si une taille est trouvée, on l'ajoute à la somme de RSS
                
        elif "munmap(" in line: # vérification si la ligne contient un appel munmap
            match = re.search(r"munmap\(.*, (\d+)", line) # recherche de la taille de mémoire libérée (VSS) dans la ligne
            if match:
                vss -= int(match.group(1)) # si une taille est trouvée, on la retire de la somme de VSS

print("VSS: ", vss, "bytes") # affichage de la somme de VSS
print("RSS: ", rss, "bytes") # affichage de la somme de RSS