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

def main():
    for i in range(10):
        r = random.choice(list(capitals))
    print(r)

    user_input = input("What is the capital of: ", r)
    if user_input in capitals:
        global count
        count += 1
        print("Correct!")
        return count
    else:
        print("Incorrect.")

#turn above into input
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

    #print("You answered", total, "questions with" , count "correct")
    #print("Your score is", percentage, "%")
    return result

    


main()



executionTime = (time.time() - startTime)
print("Time taken in seconds: " + str(format(executionTime, ".2f")))