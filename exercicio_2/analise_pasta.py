import csv
import os
import math
from matplotlib import pyplot as plt


def pede_pasta():
    print("Este programa analisa o tipo de ficheiros presente numa pasta.")
    while (True):
        pathName = input("Insira o caminho para um pasta: ")
        if os.path.isdir(pathName):
            return pathName
        else:
            print("Caminho não valido")


def faz_calculos(path):
    dictionary = {}
    folder = os.listdir(path)
    for file in folder:
        # juntar o path com o file para o .isfile funcionar
        if os.path.isfile(os.path.join(path, file)):
            # separar o nome do ficheiro com a sua extensão
            splitName = os.path.splitext(file)
            ext = splitName[1][1:]
            sizeBytes = os.path.getsize(os.path.join(path, file))
            sizeKB = math.ceil(sizeBytes / 1024)
            if ext in dictionary:
                dictionary[ext]["volume"] += sizeKB
                dictionary[ext]["quantidade"] += 1
            else:
                dictionary[ext] = {}
                dictionary[ext]["volume"] = sizeKB
                dictionary[ext]["quantidade"] = 1
    return dictionary


def guarda_resultados(dictionary, path):
    name = os.path.basename(path)
    name += ".csv"
    try:
        file = open(name, 'w', newline='')
        fields = ["Extensao", "Quantidade", "Tamanho[kByte]"]
        writer = csv.DictWriter(file, fields)
        writer.writeheader()
        for ext in dictionary:
            newLine = [ext, str(dictionary[ext]["quantidade"]), str(dictionary[ext]["volume"])]
            writer = csv.DictWriter(file, newLine)
            writer.writeheader()
        print(f"Os Resultados Foram Guardados No Ficheiro {name}")
    except OSError:
        print("Error Creating CSV File")
