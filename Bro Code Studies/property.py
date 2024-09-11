#property = Decorator that allows you to define a method that can be accessed like an attribute.

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height

    @property
    def width(self):
        return f"{self._width:.1f}cm"

    @property
    def height(self):
        return f"{self._height:.1f}cm"
    
    @width.setter
    def width(sel, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be positive")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be positive")
    
    @width.deleter
    def width(self):
        print("Deleting width")
        del self._width

    @height.deleter
    def height(self):
        print("Deleting height")
        del self._height
        


rectangle = Rectangle(3,4)

rectangle.width = 0
rectangle.height = 10

del rectangle.width
del rectangle.height

'''print(rectangle.width)
print(rectangle.height)
'''

