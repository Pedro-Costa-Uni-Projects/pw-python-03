import sys
import analisa_ficheiro
import json


def main():
    try:
        dictionary = {}
        nameFile = analisa_ficheiro.pede_nome()
        newFile = analisa_ficheiro.gera_nome(nameFile)
        print(f"New File Name -> {newFile}")
        dictionary["Number Lines"] = analisa_ficheiro.calcula_linhas(nameFile)
        dictionary["Number Chars"] = analisa_ficheiro.calcula_carateres(nameFile)
        dictionary["Biggest One"] = analisa_ficheiro.calcula_palavra_comprida(nameFile)
        dictionary["Number of Chars Occurrences"] = analisa_ficheiro.calcula_ocorrencia_de_letras(nameFile)
        with open(newFile, 'w') as jFile:
            json.dump(dictionary, jFile, indent=4)
        jFile.close()
    except OSError:
        sys.exit("Error Writing File")


if __name__ == "__main__":
    main()
