"""
Problem Statement​ ​1:
Write a Python Program(with class concepts) to find the area of the triangle using the below
formula.
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
Function to take the length of the sides of triangle from user should be defined in the parent
class and function to calculate the area should be defined in subclass.
"""

class Triangle:
 def __init__(self, side1, side2, side3):
  self.side1 = side1
  self.side2 = side2
  self.side3 = side3
  print ("Initialised Triagle super class [" +  str(side1) + "," + str(side2) + "," + str(side3) + "]")

class Triangle_Utilities(Triangle):
 
 def __init__(self, side1, side2, side3):
  print ("Initialised Utils Child class" )
  super(Triangle_Utilities, self).__init__(side1, side2, side3)

 def get_area(self):
  s = (self.side1 + self.side2 + self.side3)/2
  print (str(s))
  return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5

instance = Triangle_Utilities(3,4,5)
print ("Area of triangle = " + str(instance.get_area()) )

