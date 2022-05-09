my_bool = 6 > 5
# Bad
if my_bool == True:
    print("YAY")

# Good
if my_bool:
    print("YAY")


my_list = []
# Bad
if not len(my_list):
    print("Empty")

# Good
if not my_list:
    print("Empty")


x = 1
# Bad
if not x is None:
    print("X is real")

# Good
if x is not None:
    print("X is real")


file = "file.jpg"
# Bad
if file[-3:] == "jpg":
    print("It is a JPEG file")

# Good
if file.endswith("jpg"):
    print("It is a JPEG file")
