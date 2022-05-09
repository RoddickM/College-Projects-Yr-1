my_file = open("my_file.txt", "x")

def questions(question):
    answer = input("Answer: ")
    my_file = open("my_file.txt", "a")
    my_file.write(question)
    my_file.write("\n" + answer)
    my_file.write("\n")
    my_file.close()


while True:
    question = input("Question: ")
    questions(question)

    quit = input("Finish?")
    if quit == "y" or quit == "Y":
        break
    else:
        continue
