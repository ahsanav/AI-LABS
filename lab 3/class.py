class shape:
    @staticmethod
    def printype():
        print("print here")
    def draw(self):
        print("draw your world here")
    def area(self):
        print("the area is 222km")

class Rectangle(shape):
    def __init__(self):
        self.length = 0
        self.width = 0

    def draw(self):
        print("draw your world here")

    def area(self):
        print("the area is 222km")
class Triangle(shape):
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0

    def draw(self):
            print("draw your world here")

    def area(self):
            print("the area is 222km")


a=Triangle()
a.draw()
b=Triangle()
b.area()


