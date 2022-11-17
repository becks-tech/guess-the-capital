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
rev_capitals = {
    city: country for country,
    city in capitals.items()
}

user_input = 0
count = 0
total = 0
score = 0

def guess(r):
    print("What is the capital of: ", r)
    user_input = input("Enter answer: ")
    l = [k for k, v in capitals.items() if v == user_input]
    if user_input in capitals.items() == capitals.values():
        #if user_input is the value to the random key
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
    #global continueLoop

     

    for i in range(10):
        r = random.choice(list(capitals.keys())) 
        user_input = guess(r)
        total += 1

main()

def continueLoop():
    continueLoop = "y"

    while continueLoop == "y":
        main()
        continueLoop = input("Continue? y/n")
    else:
        print("You have chosen to end the quiz. Close program window")


executionTime = (time.time() - startTime)
print("Time taken in seconds: " + str(format(executionTime, ".2f")))