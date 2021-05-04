import json

def pede_nome():
    while (True):
        try:
            nameFile = input("File Name: ")
            file = open(nameFile, 'r')
            file.close()
            return nameFile
        except OSError:
            print("File Not Found | Try Again")


def gera_nome(inFile):
    dict = {}
    with open(inFile, 'r') as file:
        for line in file:
            dict[line.split(":")[0]] = int(line.split(":")[1])
    inFile = inFile[:-4] + ".json"
    outFile = open(inFile, 'w')
    file.close()
    json.dump(dict, outFile, indent=4, sort_keys=True)
    outFile.close()

