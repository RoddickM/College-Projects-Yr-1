event = {}
cost = {}

def validation(message):
  while True:
    try:
       userInput = float(input(message))
    except ValueError:
       print("Not an integer! Try again.")
       continue
    else:
       return userInput
       break

def costs():
    global total
    total = 0
    while True:
        name_of_material = input("Name of cost: ")
        price = validation("Price of cost: ")
        total += price
        cost[name_of_material] = price
        print(cost)

        next = input("Continue?(Y/N): ")

        if next == "n" or next == "N":
            break

name_of_event = input("Name of event:")
event["Event"] = name_of_event
budget = int(input("How much is the budget?"))
event["Budget"] = budget
costs()
event["Total Costs"] = total

if total <= budget:
    print("You are withing the budget!")
    print(event)
else:
    print("You are over budget!")
    print(event)
