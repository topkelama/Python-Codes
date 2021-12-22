
import random
print("well come to the wrold of while loop")
number = random.randint(1,5)
isGuessRight = False
while isGuessRight != True:
    guess = input("guess a number between 1 and 10: ")
    if int(guess) == number:
        print("you guessed {}. that is correct! you win!".format(guess))
            
        
    
