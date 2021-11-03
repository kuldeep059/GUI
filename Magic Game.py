number=8

user_input=input("If you wanna play press 'y'").lower()

if user_input=="y":

 user_number=int(input("Guess any Number"))

if user_number==number:
  print("You guessed correctly")

elif abs (user_number)==1:

    print("You were off by one")

else:
    print("Sorry!It's Wrong!")    


