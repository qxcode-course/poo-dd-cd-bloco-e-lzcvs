from abc import ABC, abstractmethod
import math

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
    def __init__(self, nome:str, center: Point2D, radius:float):
        self.radius = radius
        self.center = center
        self.nome = 'Circ'
        
    def getarea(self):
        return math.pi * math.pow(self.radius, 2) 
        
    def getname(self):
        return super().getname()
        
    def getpertimeter(self):
        return 2 * math.pi * self.radius
        
    def __str__(self) -> str:
        return f'Circ: C=({self.center}), R={self.radius:.2f}'

class Rect(Shapes):
    def __init__(self, nome:str, p1: Point2D, p2: Point2D):
        self.p1 = p1
        self.p2 = p2
        self.nome = 'Rect'
        
    def getarea(self):
        largura = abs(self.p1.x - self.p2.x)
        altura = abs(self.p1.y - self.p2.y)
        return largura * altura
    def getname(self):
        return super().getname()
    def getpertimeter(self):
        largura = abs(self.p1.x - self.p2.x)
        altura = abs(self.p1.y - self.p2.y)
        return 2 * (largura + altura)
    def __str__(self) -> str:
        return f'Rect: P1=({self.p1}) P2=({self.p2})'
        
def info(shape: Shapes):
    nome = shape.getname()
    area = shape.getarea()
    perimeter = shape.getpertimeter()
    return f"{nome}: A={area:.2f} P={perimeter:.2f}"
    
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
                circle = Circle('',center, r)
                forms.append(circle)
            elif args[0] == 'rect':
                x1 = int(args[1])
                y1 = float(args[2])
                x2 = float(args[3])
                y2 = float(args[4])
                p1 = Point2D(x1, y1)
                p2 = Point2D(x2, y2)
                rect = Rect('',p1, p2)
                forms.append(rect)
            elif args[0] == 'show':
                for i in forms:
                    print(i)
            elif args[0] == 'info':
                for i in forms:
                    print(info(i))
    except ValueError as error:
        print(error)
main()
# pontos = Point2D(2, 3)      
# circulos = Circle(pontos, 5)
# print("$circle 2 3 5")
# print("$show")
# print(circulos)
# print("$end")