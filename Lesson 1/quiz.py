import random 
score = 0
Type_

while True:
    try: a = int(input("How many questions do you want?")) 
    break
    except:
        print("Please type in number")

while True: 
    try:
        a = int(input("How many questions do you want?"))
        Type_of_math = input(""" Choose between \na)  Addition \nb) Subtraction \nc) Multiplication""")       
        Type_of_math == "a"
        break 
    except:
        print("a,b or c")

import random
for i in range (3):
    a = int(random.randint(0,100)) 
    b = int(random.randint(0,100))

    answer = a*b
    user = int(input(f"what is the answer to {a} * {b} ?"))

    if user == answer:
        print("good job!!")

    else: 
        print("try again")
