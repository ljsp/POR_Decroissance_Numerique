import re 

vss = 0
unVss = 0

with open("trace.log", "r") as f: # ouverture du fichier de log en mode lecture
    for line in f:
        if "mmap(" in line: # vérification si la ligne contient un appel mmap
            match = line.split(",")
            vss += int(match[1]) # Récupération de la mémoire alloué
      
        elif "munmap(" in line:
            match = line.split(",")
            match = match[1].split(")")
            unVss += int(match[0]) # Récupération de la mémoire désalloué

print("VSS: ", vss, "bytes")
print("Unmapped VSS: ", unVss, "bytes")