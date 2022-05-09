coll_address_info = {}

while True:
    college_name = input("Enter college name: ")
    college_address = input("Enter college address: ")

    coll_address_info[college_name] = college_address

    next = input("Continue inputting? (Y/N): ")

    if next == "N" or next == "n":
        break

print("\n" + str(coll_address_info))
