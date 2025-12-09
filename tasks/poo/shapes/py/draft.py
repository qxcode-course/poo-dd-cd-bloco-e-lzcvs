from abc import ABC, abstractmethod

class Shapes(ABC):
    def __init__(self, nome:str):
        self.nome = nome
    
    @abstractmethod
    def getarea(self):
        pass
    @abstractmethod
    def getpertimeter(self):
        pass
    @abstractmethod    
    def getname(self):
        return self.nome

class Point2D:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
    
    def __str__(self) -> str:
        return f"{self.x:.2f}, {self.y:.2f}"
        
class Circle(Shapes):
    def __init__(self, center: Point2D, radius:float):
        self.radius = radius
        self.center = center
    
    def getarea(self):
        return super().getarea()
        
    def getname(self):
        return super().getname()
        
    def getpertimeter(self):
        return super().getpertimeter()
        
    def __str__(self) -> str:
        return f'Circ: C=({self.center}), R={self.radius:.2f}'


def main():
    forms: list[Shapes] = []
    try:
        while True:
            linha = input()
            args = linha.split(' ')
            print("$" + linha)
            if args[0] == 'end':
                break
            elif args[0] == 'circle':
                x = int(args[1])
                y = int(args[2])
                r = float(args[3])
                center = Point2D(x, y)
                circle = Circle(center, r)
                forms.append(circle)
            elif args[0] == 'show':
                for i in forms:
                    print(i)
    except ValueError as error:
        print(error)
main()
# pontos = Point2D(2, 3)      
# circulos = Circle(pontos, 5)
# print("$circle 2 3 5")
# print("$show")
# print(circulos)
# print("$end")