import analise_pasta

if __name__ == "__main__":
    path = analise_pasta.pede_pasta()
    print(path)
    dictionary = analise_pasta.faz_calculos(path)
    print(dictionary)
    analise_pasta.guarda_resultados(dictionary, path)
