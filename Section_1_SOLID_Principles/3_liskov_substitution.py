""" 3е правило основных принципов - LSP
Принцип подстановки Барбары Лисков
Классы наследники не должны противоречить базовому классу"""

class Rectangle:
    def __init__(self, width, height):
        self.height = height
        self._width = width
    
    @property 
    def area(self):
        return self._width * self.height
     
    def __str__(self):
        return f'Width: {self.width}, height: {self.height}'
       
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        self._width = value
        
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        self._height = value

# создадим новый класс-наследник. который не будет следовать
# принципу Лисков, то есть создаем квадрат, коорый наследуется от 
# треугольника, что уже не правильно
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)
    
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value
        
    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value
        
def use_it(rc):
    w = rc.width
    rc.height = 10
    expected = int(w * 10)
    print(f'Expected {expected}, got {rc.area}')
 
   
rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)