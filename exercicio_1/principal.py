import sys
import analisa_ficheiro
import json

if __name__ == "__main__":
    try:
        dict = {}
        nameFile = analisa_ficheiro.pede_nome()
        newFile = analisa_ficheiro.gera_nome(nameFile)
        print(f"New File Name -> {newFile}")
        dict["Number Lines"] = analisa_ficheiro.calcula_linhas(nameFile)
        dict["Number Chars"] = analisa_ficheiro.calcula_carateres(nameFile)
        dict["Biggest One"] = analisa_ficheiro.calcula_palavra_comprida(nameFile)
        dict["Number of Chars Occurrences"] = analisa_ficheiro.calcula_ocorrencia_de_letras(nameFile)
        with open(newFile, 'w') as jFile:
            json.dump(dict, jFile, indent=4)
        jFile.close()
    except:
        sys.exit("Error Writing File")
