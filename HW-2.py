class Figure:
    unit = 'cm'
    def __init__(self):
        pass
    def calculate_area(self):
        pass
    def info(self):
        pass

class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        return (f"Квадрат с длиной стороны {self.__side_length} {self.unit}. "
                f"Площадь: {self.calculate_area()} {self.unit}")

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        return f'length: {self.__length} {self.unit}, width: {self.__width} {self.unit}, area: {self.calculate_area()} {self.unit}²'

squares = [
    Square(6),
    Square(9)
]

rectangles = [
    Rectangle(6, 3),
    Rectangle(9,4),
    Rectangle(10, 5)
]

figures = squares + rectangles

for figure in figures:
    print(figure.info())

