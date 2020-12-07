class Rectangle:
    width = 0
    height = 0

    def __init__(self, w, h):
        self.width = w
        self.height = h

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.height * self.width

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    def get_picture(self):
        if max(self.width, self.height) > 50:
            return "Too big for picture."
        return ('*'*self.width + '\n') * self.height

    def get_amount_inside(self, rect):
        fit_rows = int(self.width / rect.width)
        fit_column = int(self.height / rect.height)
        return fit_rows * fit_column

    def __str__(self):
        return "Rectangle(width=" +str(self.width)+ ", height=" + str(self.height) + ")"


class Square(Rectangle):

    def __init__(self, a):
        self.width = a
        self.height = a

    def set_side(self, a):
        self.width = self.height = a

    def set_width(self, width):
        self.width = self.height = width

    def set_height(self, height):
        self.width = self.height = height

    def __str__(self):
        return "Square(side=" + str(self.height) + ')'
