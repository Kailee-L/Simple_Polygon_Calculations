#Read Me
#This appliation does simple mathematics with Rectangles and Squares
#A square inherits from the rectangle class
#Author: Kailee Lesko
#Version: 1.0

import math

#requires both width and height
class Rectangle:
    def __init__(self, width, height=None):
        self.width = width

        if height == None:
            self.height = width
        else:
            self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ', height=' + str(self.height) + ')'

    def set_width(self, width):

        self.width = width

    def set_height(self, height):
        if (self.width == self.height):
            self.height = self.set_width(height)
        else:
            self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        drawing = ''
        i = 1
        while i <= self.height:
            j = 1
            while j <= self.width:
                drawing += '*'
                j = j + 1

            drawing += '\n'
            i = i + 1

        return drawing

    def get_amount_inside(self, rect):
        rect_height = rect.height
        rect_width = rect.width
        if (rect_height < self.height and rect_width < self.width):
            return math.floor((-self.height / rect_height) * (-self.width / rect_width))
        else:
            return 0

#Square class inherits from rectangles.
#Squares only need one side
class Square(Rectangle):
    def __innit__(self, side):
        self.side = side
        super().__init__(self, side, side)

    def __str__(self):
        return 'Square(side=' + str(self.width) + ')'

    def set_side(self, side):
        self.height = side
        self.width = side


if __name__ == '__main__':
    #sample rectangle problems
    rectangle = Rectangle(4,6)
    print("Rectagnle:")
    print("Area is :",rectangle.get_area())
    print("Picture of the Rectangle:\n"+rectangle.get_picture())
    print("Diagonal:",rectangle.get_diagonal())
    print("Perimeter:",rectangle.get_perimeter())

    #sample square problems
    square = Square(2)
    print("Square:")
    print("Area is :", square.get_area())
    print("Picture of the square:\n" + square.get_picture())
    print("Diagonal:", square.get_diagonal())
    print("Perimeter:",square.get_perimeter())

    #2 object problems
    print("How many of instance square can fit in instance rectangle")
    print(rectangle.get_amount_inside(square))

