# Task 1
list_of_num = [13, 252, 33]
print(f"The highest number from the list is {max(list_of_num)}")

# task 2
list_of_num_2 = [8, 2, 3, 0, 7]
total_sum = 0
for i in list_of_num_2:
    total_sum += i
print(f"\nThe sum of the list is {total_sum}")

# task 3
list_of_num_3 = [8, 2, 3, -1, 7]
total_product = 1
for i in list_of_num_3:
    total_product *= i
print(f"\nThe product of the list is {total_product}")

# task 4
my_string = "1234abcd"
print(f"\nThe reverse of {my_string} is {my_string[::-1]}")

# task 5
factorial_number = int(input("\nType in a number: "))
total_factorial = 1
for i in range(1, factorial_number+1):
    total_factorial *= i
print(f"The factorial of {factorial_number} is {total_factorial}")

# task 6
number_input = int(input("\nType a number: "))
if number_input in range(35, 51):
    print("Your number is within range!")
else:
    print("Your number is NOT within range!")

# task 7
my_string_2 = "The quick Brown Fox"
upper_case = 0
lower_case = 0
for i in my_string_2.strip():
    if i.isupper():
        upper_case += 1
    elif i.islower():
        lower_case += 1

print(f"\nNo. of upper case characters: {upper_case}")
print(f"No. of lower case characters: {lower_case}")

# task 8
sample_list = [1, 2, 3, 3, 3, 3, 4, 5]
unique_list = list(dict.fromkeys(sample_list))
print("\n" + str(unique_list))

# task 9
check_prime_input = int(input("Type a number: "))
is_prime = False
prime_count = 0

if check_prime_input > 1:
    for i in range(2, check_prime_input + 1):
        if (check_prime_input % i) == 0:
            prime_count += 1
        else:
            continue
    if prime_count == 1:
        is_prime = True
    else:
        pass

if is_prime:
    print(f"{check_prime_input} is a prime number")
else:
    print(f"{check_prime_input} is NOT a prime number")

# task 10
sample_list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
new_list = []

for i in sample_list_2:
    if (i%2) == 0:
        new_list.append(i)
    else:
        pass

print(new_list)