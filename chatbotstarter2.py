,,# --- Define your functions below! ---
def intro():
    print("Hello! I'm chatbot, what's your name?")
    username = input("Enter your name: ")
    print("", username," ,that's such a nice name! Nice to meet you!")


from random import*


def game():
    RPC=["rock", "paper", "scissors"]
    aRandomIndex=randint(0, len(RPC)-1)
    answer=input("Do you want to play rock, paper, scissors? yes or no: ")
    if (answer=="yes"):
        print("Great! Lets play.")
        choice=input("choose rock, paper, or scissors: ")
        print("", choice, "")
        print(RPC[aRandomIndex])
        if(choice=="rock" and RPC[aRandomIndex]=="rock"):
            print("we tied!")
        elif (choice=="paper" and RPC[aRandomIndex]=="paper"):
            print("we tied!")
        elif (choice=="scissors" and RPC[aRandomIndex]=="scissors"):
            print("we tied!")
        elif (choice=="rock" and RPC[aRandomIndex]=="paper"):
            print("I won!!")
        elif (choice=="rock" and RPC[aRandomIndex]=="scissors"):
            print("You won!!")
        elif (choice=="paper" and RPC[aRandomIndex]=="rock"):
            print("You won!!")
        elif (choice=="paper" and RPC[aRandomIndex]=="scissors"):
            print("I won!!")
        elif (choice=="scissors" and RPC[aRandomIndex]=="rock"):
            print("I won!!")
        elif (choice=="scissors" and RPC[aRandomIndex]=="paper"):
            print("You won!!")
    if(answer=="no"):
        print("Aww that's ok, maybe next time!")
        print("bye!")

def convo():
    food=["sushi", "pizza", "chinese", "thai", "pasta", "sandwiches", "chinese food", "thai food", "poke", "chicken", "burritos"]
    drink=["coffee", "boba", "bubble tea", "smoothies", "tea", "coconut water", "water"]
    hobbies=["hiking", "watching tv", "going to the lake", "traveling", "swimming", "designing", "writing", "hanging out with friends"]
    sports=["swimming", "running", "pole vault", "skiing", "kayaking"]
    print("I'd like to get to know you better!")
    ask=input("Want to play a question game? yes or no: ")
    if (ask=="yes"):
        print("Let's do our favorite drinks!")
        askdrink=input("What's your favorite drink: ")
        print("OOH,"+ askdrink, +" I could really go for one of those right now")
        print("Now it's your turn to guess again! *hint* they have wide straws in order to drink the bubbles....!")
        guessdrink=input("Guess what my favorite drink is: ")
        if (guessdrink in drink):
            print("True")
            print("You guessed correctly!! Nice job.")
        elif (guessdrink is not drink):
            print("Oops, that's not one of my favorite drinks")
    if(ask=="no"):
        print("Oh that's ok, one of my favorite drinks is bubble tea though!")


# --- Put your main program below! ---
def main():
    intro()
    answer = input("(What will you say?) ")
    print("That's cool!")
    userwantstoplay=True
    while userwantstoplay==True:
        game()
        playagain=input("Want to replay? yes or no: ")
        if (playagain=="no"):
            userwantstoplay=False
            print("Ok! Maybe next time :)")
    userwantstoguess=True
    while userwantstoguess==True:
        convo()
        guessagain=input("Want to guess again? yes or no: ")
        if (guessagain=="no"):
            userwantstoguess=False
            print("Ok, lets play some other time!")








# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
