import math
class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(self.height) + ")"
    
    def set_width(self, width):
        self.width = width
        return self.width
        #print("width =", self.width)

    def set_height(self, height):
        self.height = height
        return self.height
        #print("height =", self.height)

    def get_area(self):
        area = self.height * self.width
        return area
        #print("area =", area)

    def get_perimeter(self):
        perimeter = 2 * (self.height + self.width)
        return perimeter
        #print("perimeter =", perimeter)

    def get_diagonal(self):
        diagonal = (self.width ** 2 + self.height ** 2) ** .5
        return diagonal
        #print("diagonal =", diagonal)

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        picture = ""
        for i in range(self.height):
            picture += "*" * self.width + "\n"
        return picture
        #print(picture)

    def get_amount_inside(self, shape):
        amount = 0
        print("self.width =", self.width)
        print("self.height =", self.height)
        print("shape.width =", shape.width)
        print("shape.height =", shape.height)
        if shape.width > self.width or shape.height > self.height:
            return amount
        amount = math.floor(self.width / shape.width) * math.floor(self.height / shape.height)
        
        return amount
        #print("amount =", amount)

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

    def __str__(self):
        return "Square(side=" + str(self.side) + ")"

    def set_side(self, side):
        self.side = side
        Rectangle.width = self.side
        Rectangle.height = self.side
        Rectangle.set_height(self, self.side)
        Rectangle.set_width(self, self.side)
        return self.side

    def set_width(self, side):
        self.side = side
        return self.side

    def set_height(self, side):
        self.side = side
        return self.side
