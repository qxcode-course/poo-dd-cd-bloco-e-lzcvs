from abc import ABC, abstractmethod



class Veiculo(ABC):
    def __init__(self, id: str, tipo: str, entrada: int):
        self.id = id
        self.tipo = tipo
        self.entrada = entrada

    @abstractmethod
    def calcularvalor(self, horaSaida: int):
        pass

    def setentrada(self, horaEntrada: int):
        self.horaEntrada = horaEntrada

    def getentrada(self):
        return self.horaEntrada

    def getTipo(self):
        return self.tipo

    def getId(self):
        return self.id

    def __str__(self):
        resultado = f"{self.tipo:>10}-:-{self.id:>10}-:-{self.entrada}"
        return resultado.replace(' ', '_').replace('-', ' ')

class Carro(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, "Carro", entrada)

    def calcularvalor(self, horaSaida: int):
        return super().calcularvalor(horaSaida)

class Bike(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, "Bike", entrada)

    def calcularvalor(self, horaSaida: int):
        return super().calcularvalor(horaSaida)

class Moto(Veiculo):
    def __init__(self, id: str, entrada: int):
        super().__init__(id, "Moto", entrada)
    
    
    def calcularvalor(self, horaSaida: int):
        print(f"f{self.tipo} chegou {self.entrada} saiu {horaSaida}. Pagar R$ 9.00")
        return super().calcularvalor(horaSaida)

moto = Moto("elias", 20)
bike = Bike("elias", 30)
print(bike)
print(moto)