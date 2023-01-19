import re

vss = 0 
rss = 0

with open("trace.log", "r") as f: # ouverture du fichier de log en mode lecture
    for line in f:
        if "mmap(" in line: # vérification si la ligne contient un appel mmap
            match = re.search(r"mmap\(.*, (\d+)", line) # recherche de la taille de mémoire allouée (VSS)
            if match:
                vss += int(match.group(1)) # si une taille est trouvée, on l'ajoute à la somme de VSS

            match = re.search(r"\[(\d+)\]", line) # recherche de la taille de mémoire utilisée (RSS)
            if match:
                rss += int(match.group(1))
                
        elif "munmap(" in line:
            match = re.search(r"munmap\(.*, (\d+)", line) # recherche de la taille de mémoire libérée (VSS)
            if match:
                vss -= int(match.group(1))
        
        elif "brk(" in line:
            match = re.search(r"brk\((\d+)", line) # recherche de la nouvelle taille de la zone de mémoire utilisable (VSS)
            if match:
                vss = int(match.group(1))

print("VSS: ", vss, "bytes")
print("RSS: ", rss, "bytes")