from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
class Rectangle(Shape):
    def __init__(self, width, height):
        self.widht = width
        self.height = height
        
    def area(self):
        return self.widht * self.height
    
if __name__ == "__main__":
    rect = Rectangle(4,6)
    
print("Area of Rectangle:", rect.area())
