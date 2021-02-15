import random
import operator

name = input("What is your name?")
score = 0

def random_problem():
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
    }
    num_1 = random.randint(0, 10)
    num_2 = random.randint(0, 10)
    operation = random.choice(list(operators.keys()))
    answer = operators.get(operation)(num_1, num_2)
    print(f"What is {num_1} {operation} {num_2}?")
    return answer

def ask_question():
    answer = random_problem()
    guess = float(input())
    return guess == answer

def game():
    print("How well do you know math?\n")

for i in range (10):
    if ask_question == True:
        score += 1
        print("correct!")
    else: 
        print("incorrect")
        score -= 1
        if score < 0:
        

print (f"{name} your score is {score}")
game()

