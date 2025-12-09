from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}")
    @abstractmethod
    def fazer_som(self):
        pass
    @abstractmethod
    def mover(self):
        pass


class Gatinho(Animal):
    
    def __init__(self, nome:str):
        super().__init__(nome)
    
    def apresentar_nome(self):
        return super().apresentar_nome()
    
    def fazer_som(self):
        print("Miauuuuu")
    
    def mover(self):
        print("pat pat pat pat")
        
class Elefante(Animal):
    
    def __init__(self, nome: str):
        super().__init__(nome)
    
    def apresentar_nome(self):
        return super().apresentar_nome()
    
    def fazer_som(self):
        print("FUUUUUUUUUUUUUUUOON")
    
    def mover(self):
        print("flop flop flop flop")

class Cachorro(Animal):
    def __init__(self, nome:str):
        
        super().__init__(nome)
    
    def apresentar_nome(self):
        return super().apresentar_nome()
    
    def fazer_som(self):
        print("AU AU AU AU")
    
    def mover(self):
        print("scrach scrach scrach")

class Esponja(Animal):
    def __init__(self, nome:str):
        super().__init__(nome)
    
    def apresentar_nome(self):
        return super().apresentar_nome()
    
    def fazer_som(self):
        print("----------")
        
    # def mover(self):
    #     pass
        
def apresentarAnimal(animais: list):
    for animal in animais:
        print(f"{animal.__class__.__name__}")
        animal.apresentar_nome()
        animal.fazer_som()
        animal.mover()


animais = [
    Gatinho("Gatinho"),
    Elefante("Dumbo"),
    Cachorro("Alfredo"),
    Esponja("BOB")
]

apresentarAnimal(animais)