import random
import time

startTime = time.time()

capitals = {"France":"Paris",
                "United Kingdom":"London",
                "United States":"Washington DC",
                "Spain":"Madrid", "Italy":"Rome",
                "Mexico":"Mexico City",
                "Germany":"Berlin",
                "Sweden":"Stockholm",
                "Iceland":"Reykjavik",
                "Ireland":"Dublin",
                "Australia":"Canberra",
                "New Zealand":"Wellington",
                "Japan":"Tokyo",
                "China":"Beijing",
                "South Korea":"Seoul",
                "Brazil":"Brasilia",
                "Canada":"Ottawa",
                "Portugal":"Lisbon",
                "Morocco":"Rabat",
                "Russia":"Moscow",
                "Ukraine":"Kiev",
                "Serbia":"Belgrade",
                "Namibia":"Windhoek",
                "Kenya":"Nairobi",
                "Belarus":"Minsk",
                "India":"New Delhi",
                "Norway":"Oslo"} #26

user_input = 0
count = 0
total = 0
score = 0

def guess(r):
    print("What is the capital of: ", r) 
    user_input = input("Enter answer: ")

    key_list = list(capitals.keys())
    val_list = list(capitals.values())
    answer = key_list.index(r)
    
    if user_input == val_list[answer]:
        
        global count
        count += 1
        print("Correct!")
        return count
    else:
        print("Incorrect.")
    return user_input

def score():
    if total == 10:
        global result
        result = count / total
        global percentage
        percentage = round((result * 100),2)
        if percentage >= 75:
            print("Excellent")
        elif percentage >=50:
            print("Good")
        else:
            print("Need to improve")

    print("You answered", total, "questions with" , count, "correct")
    print("Your score is", percentage, "%")
    return result

def main():
    print("Welcome to Guess the Capital!")

    global user_input
    global score
    global total
    global capitals
     
    for i in range(10):
        r = random.choice(list(capitals))
        user_input = guess(r)
        total += 1

    score()


def continueLoop():
    again = "y"

    while again == "y":
        main()
        again = input("Continue? y/n")
    else:
        print("You have chosen to end the quiz. Close program window")

continueLoop()

executionTime = (time.time() - startTime)
print("Time taken in seconds: " + str(format(executionTime, ".2f")))