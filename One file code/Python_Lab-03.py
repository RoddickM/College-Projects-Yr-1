#area of a rectangle
rec_1 = int(input("Input your length: "))
rec_2 = int(input("Input your width: "))

rec_area = rec_1 * rec_2

print("The area of the rectangle is:", int(rec_area))

#area of a triangle
tri_base = int(input("\nInput your base: "))
tri_height = int(input("Input your height: "))

tri_area = (tri_base * tri_height) / 2

print("The area of the triangle is:", int(tri_area))

#area of a circle
radius = int(input("\nInput your radius: "))

circle_area = (radius * radius) * 3.14159

print("The area of the circle is:", float(circle_area))
