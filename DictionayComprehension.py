users =[
    (0,"Honey","password"),
    (1,"Nanny","boble"),
    (2,"Grann","Hijack"),
    (3,"Manny","Oye"),
    (4,"Chang","Yt"),
]

username_mapping={user[1]:user for user in users}

username_input= raw_input("Enter Your Username=")

password_input= raw_input("Enter Your Password=")

_,username,password=username_mapping[username_input]  #Error shown in this line of command

if password_input==password :

  print("Your have succefully logged in")

else:
    print("Your credentials are wrong! Try again")

#not running 
