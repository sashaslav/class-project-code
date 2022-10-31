import random
#lets you use random function

wasCorrect = False

def TellTruth():
    print("My mistake, I was just messing with you, you did get that last one right")

def ChooseCard(answer):
    global wasCorrect
    #allows you to access wascorrect variable that is outside of the function, so able to edit global variable inside func
    cardList = ["circle", "plus sign", "wavy lines", "square", "star"]
    num = random.randrange(0,5)
    if(wasCorrect == True):
        TellTruth()
    if(answer.lower() == cardList[num]):
        while(answer.lower() == cardList[num]):
            num = random.randrange(0,5)
        #the while function checks if the answer is correct, and it says while the answer is equal to the card that was chosen, then choose a new card
        wasCorrect = True
        return "Incorrect, the correct answer was " + cardList[num]
    else:
        wasCorrect = False
        return "Incorrect, the correct answer was " + cardList[num]

name = input("What is your name?\n")
print("Hello " + name + ". Welcome to the Ghostbusters Zener Bot, made to test your psychic abilities. This bot is programmed to tell the absolute truth, so don't worry, you're in good hands.")
print("There are five Zener Cards that the bot will choose from: A circle, a plus sign, wavy lines, a square, and a star. The bot will choose a card at random, and you must say which card you believe the bot has picked. It will tell you whether or not it was correct.")
print("The test will begin momentarily. Good luck!")
for i in range(500):
    answer = input("Which card am I holding up?\n")
    response = ChooseCard(answer) 
    print(response)
    
