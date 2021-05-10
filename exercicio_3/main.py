import os
import math


def pede_pasta():
    while True:
        pathName = input("Insira o caminho para um pasta: ")
        # verifica se existe esse caminho
        if os.path.isdir(pathName):
            return pathName
        # se não exister ver se o input é a pasta atual
        elif os.path.basename(os.getcwd()) == pathName:
            return os.getcwd()
        else:
            print("Caminho Não Encontrado")


def calcula_tamanho_pasta(path):
    amount = 0
    folder = os.listdir(path)
    for file in folder:
        # juntar o path com o file para o .isfile funcionar
        usablePath = os.path.join(path, file)
        if os.path.isfile(usablePath):
            amount += os.path.getsize(usablePath) / (1024 * 1024)  # converter de bytes par MBytes
        elif os.path.isdir(usablePath):
            amount += calcula_tamanho_pasta(usablePath)
    return amount


def main():
    path = pede_pasta()
    MBytes = math.ceil(calcula_tamanho_pasta(path))  # math.ceil para arrendondar valores
    print(f"Tamanho Total: {MBytes} MBytes")


if __name__ == "__main__":
    main()
