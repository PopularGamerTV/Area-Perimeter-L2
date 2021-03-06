import math

print("Area/Perimeter Calculator")

#Coding for area/perimeter of a circle
def circle():
  r=float(input("Input Radius : "))
  carea= math.pi*r*r
  cperemiter=2* math.pi*r
  print("Area of the circle: ",carea)
  print("Perimeter of the circle: ",cperemiter)
#Coding for area/perimeter of a square
def square():
  l=float(input("Input Length : "))
  w=float(input("Input Width : "))
  sarea=l*w
  sperimeter=2*(l+w)
  print("Area of a square: ",sarea)
  print("Peremiter of a square: ",sperimeter)
#Coding for area/perimeter of a rectangle
def rectangle():
  l=float(input("Input Length : "))
  w=float(input("Input Width : "))
  rarea=l*w
  rperimeter=2*(l+w)
  print("Area of a rectangle: ",rarea)
  print("Peremiter of a rectangle: ",rperimeter)
#Coding for area/perimeter of a triangle
def triangle():
  b=float(input("Input Base : "))
  h=float(input("Input height : "))
  a=float(input("Input Side 1 : "))
  b=float(input("Input Side 2 : "))
  c=float(input("Input Side 3 : "))
  triarea=0.5*b*h
  triperimeter=a+b+c
  print("Area of a triangle: ",triarea)
  print("Perimeter of a triangle: ",triperimeter)
#Coding for area/perimeter of a parraleleogram
def parrelelogram():
  l=float(input("Input Length : "))
  w=float(input("Input Width : "))
  parea=l*w
  pperimeter=2*(l+w)
  print("Area of a parrelelogram: ",parea)
  print("Perimeter of a parrelelogram: ",pperimeter)
#Coding for area/perimeter of a trapezium
def trapezium():
  b=float(input("Input Base : "))
  t=float(input("Input Top : "))
  h=float(input("Input Height : "))
  a=float(input("Input Side 1 : "))
  c=float(input("Input Side 2 : "))
  traparea=0.5*(b+t)*h
  trapperimeter=b+t+a+c
  print("Area of a trapizium: ",traparea)
  print("Perimeter of a trapizium: ",trapperimeter)
#Coding for when users select what shape they wish to calculate
def choice(shapechoice):
  if shapechoice == 1:
    circle()

  if shapechoice == 2:
    square()

  if shapechoice == 3:
    rectangle()

  if shapechoice == 4:
    triangle()

  if shapechoice == 5:
    parrelelogram()

  if shapechoice == 6:
   trapezium()

keep_going = ""
while keep_going == "":
  #Coding for asking the user if the wish to repeat the code to calculate another shape or wish to exit.
  print("\nChose a shape to calculate the area and perimeter of. #1: Circle, #2: Square, #3: Rectangle, #4: Triangle, #5: Parrelelogram, #6: Trapezium\n")

  shapechoice = input("Please select number for shape to find area and perimeter:")
  shapechoice = int(shapechoice)

  choice(shapechoice)
  
  keep_going=input("\nPress 'Enter' to continue or 'Any key' to quit>>")
#Coding for when the users are finished calculating
print("Thank you for using this calculator. Hope to see you again!")