import math
class Shape():
    def __init__(self,color,name):
        self.name = name
        self.color = color
    
    def say_name(self):
        return f"My name is {self.name}."

class Rectangle(Shape):
    def __init__(self,color,name,width,height):
        super().__init__(color,name ) #Üst sınıfın name ve color değerlerini başlattı
        self.width = width
        self.height = height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return self.width * 2 + self.height * 2
    def say_name(self):
        return f"My name is {self.name} and I am a rectangle."
    
class Circle(Shape):
    def __init__(self,name,color,radius):
        super().__init__(name,color)
        self.radius = radius
    def say_name(self):
        return f"My name is {self.name} and I am a circle."
    def area(self):
        return math.pi * self.radius ** 2
    def perimeter(self):
        return 2 * math.pi * self.radius