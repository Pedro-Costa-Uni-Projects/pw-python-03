import analise_pasta


def main():
    path = analise_pasta.pede_pasta()
    print(path)
    dictionary = analise_pasta.faz_calculos(path)
    analise_pasta.guarda_resultados(dictionary, path)
    analise_pasta.faz_grafico_barras(dictionary, path)
    analise_pasta.faz_grafico_queijos(dictionary, path)


if __name__ == "__main__":
    main()
