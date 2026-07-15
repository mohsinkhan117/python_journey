class Circle:
    def __init__(self, radius): #constructor
      self.radius=radius

    def area(self):
       return 3.14*(self.radius)*(self.radius)


class Rectangle:
    def __init__(self,hight, width):
       self.hight=hight
       self.width=width

    def area(self):
       return (self.hight)*(self.width)
    

print(Circle(3),'\n')
print(Circle(4).area(),'\n')
print(Rectangle(5,4),'\n')
print(Rectangle(5,4).area(),'\n')