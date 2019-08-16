#press run to start code

#player 1 inputs a word of choice

#display number of letters in word
#display number of lives (7)
#player 2 guesses a letter - if letter guessed is in word of choice, display letter on screen-
#elif letter is NOT in word, lives = -1

print("Welcome to the Guess the Secret Word Game!!")
p1name=input("Enter your name: ")
p1name
print("hello, " + p1name," Time to play hangman!")
print("choose a word for a player 2 to guess")
word=input("enter your word of choice: ")

underscores = []
length = len(word)
guess=[]

for letter in word:
    underscores.append("_ ")
print("".join(underscores))

letter=input("enter a letter: ")
