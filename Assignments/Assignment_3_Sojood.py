correct_username = "sojoodas"
correct_password = "NoHint0-0"
user_role = "user"

username = input("Enter username: ")

if username == correct_username:
    password = input("Enter password: ")
    if password == correct_password:
        if user_role == "admin":
            print("Welcome Admin")
        elif user_role == "moderator":
            print("Welcome Moderator")
        elif user_role == "user":
            print("Welcome User")
        else:
            print("Unknown role")
    else:
        print("Wrong password")
else:
    print("User not found")                   
    
#DONE_SOJOOD_ABUSAADA :)