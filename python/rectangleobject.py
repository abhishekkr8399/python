class Rectangle():
 def __init__(self, width, height):
  self.width = width
  self.height = height
 def getArea(self):
  return self.width * self.height
n = int(input("Enter the number of rectangles : "))
rectangles = []
for i in range(n):
 print("Rectangle-%d:" % (i + 1))
 width = int(input("Width : ")) #You can specify as float for reading decimal values
 height = int(input("Height : "))
 obj = Rectangle(width, height)
 rectangles.append(obj)
sorted_rects=sorted(rectangles,key=lambda x: x.getArea()) #Sort base on area
min_area = sorted_rects[0]
max_area = sorted_rects[n - 1]
print("\nMinimum area Rectangles :")
for i in rectangles:
 if i.getArea() == min_area.getArea():
  print("Height=", i.height, "\tWidth=", i.width, "\tArea=", i.getArea())
print("\nMaximum area Rectangles :")
for i in rectangles:
 if i.getArea() == max_area.getArea():
  print("Height=", i.height, "Width=", i.width, "Area=", i.getArea())