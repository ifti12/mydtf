from .shape import Shape


class Circle(Shape):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14

    def perimeter(self):
        return 2 * self.radius * 3.14

    def func(self):
        return self.radius + 1


NewCircle = Circle(9) #master branch changes to commit commit2.  ----------
print(NewCircle.area())
print(NewCircle.perimeter())


