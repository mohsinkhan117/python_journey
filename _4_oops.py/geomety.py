import matplotlib.pyplot as plt
class Circle:
    def __init__(self, radius,clr): #constructor
      self.radius=radius
      self.clr=clr
    def area(self):
       return 3.14*(self.radius)*(self.radius)
    
    def drawCircle(self):

        fig, ax = plt.subplots()

        circle = plt.Circle(
            (0, 0),
            radius=self.radius,
            color=self.clr
        )

        ax.add_patch(circle)

        ax.set_xlim(-self.radius-1, self.radius+1)
        ax.set_ylim(-self.radius-1, self.radius+1)

        ax.set_aspect("equal")

        plt.show()
class Rectangle:
    def __init__(self,hight, width,clr):
       self.hight=hight
       self.width=width
       self.clr=clr
    def area(self):
       return (self.hight)*(self.width)
    
    def drawRectangle(self):
        plt.gca().add_patch(plt.Rectangle((0, 0), self.width, self.hight ,fc=self.clr))
        plt.axis('scaled')
        plt.show()
    
c = Circle(4, "red")
print(c,'\n')
print(c.area(),'\n')
c.drawCircle()

r=Rectangle(5,4,"green")
print(r,'\n')
print(r.area(),'\n')
r.drawRectangle()