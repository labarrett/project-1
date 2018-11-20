import random

print("Welcome to the guessing game! ")

random_number= random.randint(1, 10) 

def start_game():  

    attempt=0

    while True:
        choice=int(input("Guess a number between 1 through 10. "))  
        if random_number > choice:
            print("it's higher")
            attempt+=1
        elif random_number < choice:            
            print("it's lower")
            attempt+=1
        else:
            attempt+=1
            print("You got it! That took",attempt, "attempts. Game Over.")
            break
                     
start_game()


    

    
 



