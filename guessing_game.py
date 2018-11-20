#Guessing game to pick a number between 1-10

import random

print("***********  Welcome to the guessing game! *********** " )

random_number= random.randint(1, 10) 

#function of guesing game

def start_game():

    random_number= random.randint(1, 10) 

    attempt=0

    while True:
        try:
            choice=int(input("Guess a number between 1 through 10. "))        
            if random_number > choice:
                print("it's higher")
                attempt+=1
            elif choice > 10:            
                print("Your number is to high")
                attempt+=1
            elif random_number < choice:            
                print("it's lower")
                attempt+=1                     
            else:
                attempt+=1
                print("You got it! That took",attempt, "attempt(s).")
                answer=input("Would you look to keep playing? Pick Y/N ")
                if answer.lower()=="y":
                    start_game()
                else:
                    print("Thank you for playing!")
                    break
        except ValueError as error:
            print("ERROR. Please insert a numerical number instead")

#run game function

start_game()



    

    
 



