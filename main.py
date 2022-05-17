class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.widht = width
        self.height = height

    def __str__(self):
        return f'Rectangle : {self.x}, {self.y}, {self.widht}, {self.height}.'

    def get_area(self):
        return self.widht * self.height


