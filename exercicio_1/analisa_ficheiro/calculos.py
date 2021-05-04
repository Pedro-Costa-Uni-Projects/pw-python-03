def calcula_linhas(nameFile):
    file = open(nameFile, "r")
    countLines = len(file.readlines())
    file.close()
    return countLines


def calcula_carateres(nameFile):
    file = open(nameFile, "r")
    countChar = len(file.read())
    file.close()
    return countChar


def calcula_palavra_comprida(nameFile):
    bigLine = ""
    file = open(nameFile, "r")
    list = file.readlines()
    for line in list:
        if len(line) > len(bigLine):
            bigLine = line
    file.close()
    return bigLine


def calcula_ocorrencia_de_letras(nameFile):
    dict = {}
    file = open(nameFile, "r")
    chars = file.read()
    chars.lower()
    for char in chars:
        if char.isalpha():
            dict[char] += 1
    return dict
