from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome: str):
        self.nome = nome

    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}")

    def fazer_som(self):
        pass

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
        
def apresentarAnimal(animal: Animal):
    print(f"{animal.__class__.__name__}")
    print(f"{type(animal)}")
    animal.apresentar_nome()
    animal.fazer_som()
    animal.mover()



apresentarAnimal(Gatinho("Gatinho"))
apresentarAnimal(Elefante("Dumbo"))
apresentarAnimal(Cachorro("Alfredo"))