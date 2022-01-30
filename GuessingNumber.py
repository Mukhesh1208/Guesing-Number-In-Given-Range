import random
Number = int(input("Enter The Range : ")) #Taking Input From User To Generate Random Number
Genered_Number = random.randrange(0,Number) #Generating Random Numbers In Given Range

count = 1 # To Check In How Many Rounds Does A User Guessed The Number
print("Hello User You Have 10 Chances To Guess A Number :")

while True: #To Take Input From User Multiple Times

    if count <=10: #Allowing Users To Guess The Number in 10 Rounds
        Guessing_Number = int(input("Enter Your Guessing Number : "))

        # checking User Enterd Number With Computer Generated Random Number
        if Guessing_Number == Genered_Number: 
            
            print("Hurry You Own :) ")
            print(f"You Guessed The Number In {count} Rounds :)..")
            break

        elif Guessing_Number < Genered_Number :
            print("You'r Guessed Number Is Less Than Guessing Number :)")
            count+=1
            continue
            
        else:
            print("You'r Guessed Number Is Greater Than Guessing Number :)")
            count+=1
            continue
    else:
        print("Sorry You Exceed The Limit ... Better Luck Try Again Next Time ")
        break

print("Thanks For Playing ..:) ")



