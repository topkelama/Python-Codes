print("welcome to mygame called choices!")
name = input("what is your name? ")
print(name)
age = int(input("what is your age? "))
# putting int in front of your input question will convert it into an integer automatically and also for the remainder of you code.

health = 10
#We have assigned a health system for this game

if age >= 18:
    print("you are old enough to play this game!")
    wantToPlay = input("Do you want to play: ").lower()
    if wantToPlay == "yes":
        print("Let's play together")
        print("You are starting with", health, "health")
        up_or_down = input("First choice --up or down(up/down)?")
        if up_or_down == "yes":
            ans = input("Nice, you follow the path and reach a lake...Do you swim across or go around(across/around)?")
            if ans == "around":
                print("you went around and reached the other side of the lake")
            elif ans == "across":
                print("you managed to get across but ran into an alligator who bit your leg and lost 5 health")
                health-= 5
            ans = input("you noticed a house and a river. Which do you go to (river/house)")
            if ans  == "house":
                print("you go to house and are greeted by the owner who shows his shot gun and shoots you in the arm and you lose 5 health")
                health -=5
                if health <= 0:
                    print("you now have 0 health and you lose the game... ")
                else:
                    print("You are survived for now but lets work on that.")
                    ans =input("You run away from house and see a car and a boat, where do you go(car/boat)?")
                    if ans =="car":
                        print("Car key is under the front right tire, drive safe. You survived and won the game.")
                    else:
                        print("Jump on the boat but someone may come out of house and blow out the boat..game over")
            else:
                print("Get into the Canoe and cross safely... you are survived, you win")

        else:
            print("you went down into the pits of hell  and lost..try again")
    else:
        print("input yes or no else you dont get to play")

            
else:
    print("You are too young to play")
