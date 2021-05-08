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
    dir = os.listdir(path)
    for file in dir:
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

def guarda_resultados(dir, path):
