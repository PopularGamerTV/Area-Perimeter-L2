print("Chose a shape to calculate the area and perimeter of. #1: Circle, #2: Square, #3: Rectangle, #4: Triangle, #5: Parrelelogram, #6: Trapezium\n")

shapechoice = input("Please select number for shape to find area and perimeter:")
shapechoice = int(shapechoice)

if shapechoice == 1:
  r=float(input("Input Radius : "))
  carea=3.14*r*r
  cperemiter=2*3.14*r
  print("Area of the circle: ",carea)
  print("Perimeter of the circle: ",cperemiter)

if shapechoice == 2:
  l=float(input("Input Length : "))
  w=float(input("Input Width : "))
  sarea=l*w
  sperimeter=2*(l+w)
  print("Area of a square: ",sarea)
  print("Peremiter of a square: ",sperimeter)