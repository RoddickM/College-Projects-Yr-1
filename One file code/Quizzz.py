score = 0

def right_wrong(user_input, answer):
    if user_input == answer:
        return "Correct!"
    else:
        return "Wrong!"

q1 = int(input("What is 4 + 3? "))
right_wrong(q1, 7)
q2 = int(input("What is 4 * 3? "))
right_wrong(q2, 12)
q3 = int(input("What is 23 // 5? "))
right_wrong(q3, 4)
q4 = int(input("What is 50 % 3? "))
right_wrong(q4, 2)
q5 = input("Is 4 == 3?(T/F) ")
right_wrong(q5, "F")
q6 = input("Is 5 >= 20?(T/F) ")
right_wrong(q1, 7)
q7 = input("Is 40 > 42?(T/F) ")
right_wrong(q1, 7)
q8 = input("Is 4 == 3 and 5 >= 3 correct?(T/F) ")
right_wrong(q1, 7)
q9 = input("Is 5 >= 20 or 5 <= 3 correct?(T/F) ")
right_wrong(q1, 7)
q10 = input("Is 4 == 3 and 50 >= 25 correct?(T/F) ")
right_wrong(q1, 7)
q11 = input("Is (not 4 == 3) and 5 >= 3 correct?(T/F) ")
right_wrong(q1, 7)
