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

#print(capitals)

user_input = 0

r = [random.choice(list(capitals)) for i in range(10)]
#needs to be printed as a loop

print(r)

def guess():
    #then work on the user input guess 
    if user_input in capitals:
        print("Correct!")
    else:
        print("Incorrect.")

def main():
    pass

executionTime = (time.time() - startTime)
print("Time taken in seconds: " + str(format(executionTime, ".2f")))