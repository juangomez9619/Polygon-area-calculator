class Rectangle:

    def __init__(self, width, height):
        self.__width = width 
        self.__height = height

    def set_width(self, width):
        self.__width = width
    
    def set_height(self, height):
        self.__height = height

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def get_area(self):
        return self.get_height() * self.get_width()

    def get_perimeter(self):
        return self.get_height() * 2 + self.get_width() * 2

    def get_diagonal(self):
        return (self.get_width() ** 2 + self.get_height() ** 2) ** .5

    def __str__(self):
        return f"Rectangle(width={self.get_width()}, height={self.get_height()})"
    
    def get_picture(self):
        if (self.get_height() > 50) | (self.get_width() > 50):
            return "Too big for picture."
        return ('*'*self.get_width()+'\n')*self.get_height()

    def get_amount_inside(self, shape = None):
        if shape == None:
            return 0
        return int((self.get_width() / shape.get_width()) * (self.get_height() / shape.get_height()))

class Square(Rectangle):

    def __init__(self, side):
        super().__init__(side, side)

    def set_side(self, side):
        self.set_height(side)
        self.set_width(side)

    def __str__(self):
        return f"Square(side={self.get_width()})"


    