from abc import ABC, abstractmethod


class Veiculo(ABC):
    def __init__(self, id: str, tipo: str):
        self.id = id
        self.tipo = tipo
        self.entrada = 0

    @abstractmethod
    def calcularvalor(self, horaSaida: int):
        pass

    def setentrada(self, horaEntrada: int):
        self.entrada = horaEntrada

    def getentrada(self):
        return self.entrada

    def getTipo(self):
        return self.tipo

    def getId(self):
        return self.id

    def __str__(self):
        resultado = f"{self.tipo:>10}-:-{self.id:>10}-:-{self.entrada}"
        return resultado.replace(" ", "_").replace("-", " ")


class Carro(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Carro")

    def calcularvalor(self, horaSaida: int):
        diferenca = horaSaida - self.entrada
        valor = diferenca / 10
        if valor < 5:
            valor = 5
        return valor


class Bike(Veiculo):
    def __init__(self, id:str):
        super().__init__(id, "Bike")

    def calcularvalor(self, horaSaida: int):
        valor = "R$ 3.00"
        return valor


class Moto(Veiculo):
    def __init__(self, id: str):
        super().__init__(id, "Moto")

    def calcularvalor(self, horaSaida: int):
        diferenca = horaSaida - self.entrada
        valor = diferenca / 10
        return valor


class Estacionamento:
    def __init__(self):
        self.veiculos: list[Veiculo] = []
        self.horaAtual: int = 0

    def procurarveiculo(self, id: str):
        for veiculo in self.veiculos:
            if veiculo.getId() == id:
                return veiculo
        return None
        
    def setHora(self, nova_hora: int):
        self.horaAtual = nova_hora
    
    def estacionar(self, veiculo: Veiculo):
        if self.procurarveiculo(veiculo.getId()) is not None:
            return
        veiculo.setentrada(self.horaAtual)
        self.veiculos.append(veiculo)
        
    def passartempo(self, tempo: int):
        self.horaAtual += tempo
        
    def __str__(self) -> str:
        if self.veiculos != []:
                txt = ""
                for v in self.veiculos:
                    txt += str(v) + "\n"
                    txt += f"Hora atual: {self.horaAtual}"
                return txt
        else:
            return f"Hora atual: {self.horaAtual}"

    def show(self):
        print(self)


def main():
    estacionamento = Estacionamento()
    while True:
        linha = input()
        args = linha.split(" ")
        print("$" + linha)
        if args[0] == "end":
            break
        elif args[0] == "show":
            estacionamento.show()
        elif args[0] == "estacionar":
            tipo = args[1]
            id = args[2]

            if tipo == 'bike':
                veiculo_obj = Bike(id)
                estacionamento.estacionar(veiculo_obj)
            if tipo == 'moto':
                veiculo_obj = Moto(id)
                estacionamento.estacionar(veiculo_obj)
            if tipo == 'carro':
                veiculo_obj = Carro(id)
                estacionamento.estacionar(veiculo_obj)
        elif args[0] == 'tempo':
            tempo = int(args[1])
            estacionamento.passartempo(tempo)

main()