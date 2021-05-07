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
            bigLine = line[:-1]  # [-1] para retirar o /n
    file.close()
    return bigLine


def calcula_ocorrencia_de_letras(nameFile):
    dict = {}
    file = open(nameFile, "r")
    chars = file.read()
    for char in chars:
        char = char.lower()
        if char.isalpha():
            if char in dict:
                dict[char] += 1
            else:
                dict[char] = 1
    return dict
