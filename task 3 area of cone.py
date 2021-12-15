#Task 3
#Collect radius and height from user,calculate Area of cone (area of cone = pi * r * r * h) (float)print output in integer data type and formatted way

pi = 3.14
radius = float(input("enter the radius here:"))
height = float(input("enter the height here :"))
area = int(pi * radius * radius * height)
print ("area of the cone if radius {} , height {} and pi {} is {} " .format(radius , height , pi ,area))


