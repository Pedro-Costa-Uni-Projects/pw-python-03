import analise_pasta

if __name__ == "__main__":
    path = analise_pasta.pede_pasta()
    print(path)
    dir = analise_pasta.faz_calculos(path)
    print(dir)

