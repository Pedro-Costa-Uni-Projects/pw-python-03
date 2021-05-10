from automovel import automovel


def main():
    a1 = automovel(60, 10, 15)
    print(f"Autonomia: {a1.autonomia()}")
    print(a1.abastece(45))
    print(a1.percorre(150))
    print(a1.percorre(250))


if __name__ == "__main__":
    main()
