#Taks 2

#(print output in int)
#write a programme to calculate area of circle with radius (float)(collect using input function )

radius = float (input("enter the radius:"))
pi = 3.14
area = int(pi * radius * radius)
print ("Area of the circle with radius {} and pi {} is {} " .format(radius , pi , area))


#(print output in int)
#write a programme to calculate perimeter of a circle with radius (float), (collect using output)

radius = float(input("enter the radius:"))
pi = 3.14
perimeter = int(2 * pi * radius)
print ("perimter of the circle with radius {} and pi {} is {} :" .format(radius , pi , perimeter))
