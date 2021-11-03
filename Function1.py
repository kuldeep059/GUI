def user_age_in_seconds():                                                          #function defined or made
    user_age=int(input("Enter your age !"))                                         #function bodyKulde
    age_in_seconds=user_age*365*24*60*60                                            #calculation part of function 

    print(f"Your age in seconds is:{age_in_seconds}")                               #For PRinting the output of function        

def user_name():
    user_name_input=(input("What is your name ?"))
    print(f"Your name is :{user_name_input} ")

user_name()                                                                          #function called
user_age_in_seconds()                                                               #function called



