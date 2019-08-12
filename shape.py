
#First class: shape
class Shape:

    def __init__(self, x, y, description):
        self.x = x
        self.y = y
        self.description = description
        
    def area(self):
        return self.x * self.y

    def perimeter(self):
        return 2 * self.x + 2 * self.y

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale

    def setDescription(self, description):
        self.description = description

#create instance of a object
rectangle = Shape(100, 45, "Rect")

#find the area of your rectangle:
print("Area: ", rectangle.area())

#find the perimeter of your rectangle:
print("Perimeter", rectangle.perimeter())

#making the rectangle 50% smaller
rectangle.scaleSize(0.5)

#re-printing the new area of the rectangle
print("Scaled down area" , rectangle.area())

rectangle.setDescription ("Rectangle Shape is awesome")

print(rectangle.description)

#create two more instances of the Shape object
long_rectangle = Shape(120,10, "Long Rect")






