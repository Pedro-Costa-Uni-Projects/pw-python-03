class automovel:
    def __init__(self, cap_dep, quant_comb, consumo):
        self.capacidade = cap_dep
        self.quantidade = quant_comb
        self.consumo = consumo

    def combustivel(self):
        return f"Têm: {self.quantidade} Litros de Combustível no Deposito"

    def autonomia(self):
        return int(self.quantidade / self.consumo * 100)

    def abastece(self, nLitros):
        if self.quantidade + nLitros > self.capacidade:
            return Exception("Abastecimento Excede a Capacidade do Deposito")
        else:
            self.quantidade += nLitros
            return f"Têm Agora Uma Autonomia de: {automovel.autonomia(self)}"

    def percorre(self, nKm):
        if nKm * (self.consumo / 100) > self.quantidade:
            return Exception(f"Erro Quantidade de Combustível Insuficiente Para: {nKm}km")
        else:
            self.quantidade -= nKm * (self.consumo / 100)
            return f"Têm Agora Uma Autonomia de: {automovel.autonomia(self)}"
