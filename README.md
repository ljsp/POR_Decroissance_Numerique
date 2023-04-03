# Outils de mesure de la mémoire

## Description

Ce dépôt contient plusieurs outils de mesure de la mémoire pour analyser l'utilisation de la mémoire de programmes en C, C++ et Python. Le script principal est `mesure.sh` qui lance l'outil souhaité en fonction des arguments entrés. Ce script lance les outils suivants :

1. `cgroup` : Mesure à l'aide des cgroup
2. `memTool` : échantillonnage à l'aide de psutil
3. `logReader` : lecture d'un fichier log crée par strace

## Prérequis

- Java openjdk 17.0.5
- Compilateurs GCC et G++ 11.3.0
- cgroup v2
- strace
- Python 3.10.6
    - matplotlib
    - psutil
    - numpy
    - pandas


## Installation

1. Clonez le dépôt :

``` shell
git clone https://github.com/ljsp/POR_Decroissance_Numerique.git
```

2. Accéder au répertoire des outils de mesure :

``` shell
cd POR_Decroissance_Numerique/Code/Mesure/
```

## Utilisation

### mesure.sh

Pour exécuter le script `mesure.sh`, fournissez le nom de l'outil souhaité en tant que premier argument, suivi de tout argument supplémentaire spécifique à l'outil. La syntaxe pour exécuter le script est :

``` shell
./mesure.sh <nom_de_loutil> <chemin_du_fichier|paramètres>
```

Par exemple :

#### cgroup

Pour exécuter l'outil `cgroup`, utilisez la commande suivante :

```shell
./mesure.sh cgroup <memoire_min> <memoire_max> <pas>
```

#### memTool && logReader 

Pour exécuter l'outil `memTool`, utilisez la commande suivante :

```shell
./mesure.sh <memTool|logReader> <chemin_du_fichier>
```
