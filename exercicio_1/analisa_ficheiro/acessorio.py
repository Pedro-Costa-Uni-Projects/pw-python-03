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
    newName = inFile[:-4] + ".json"
    return newName
