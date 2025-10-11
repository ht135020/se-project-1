# part 1

username = "admin"
password = "1234"



for i in range(3):
    print("Attempt", i + 1)
    
    usernameInput = input("Enter username: ")
    passwordInput = input("Enter password: ")

    if usernameInput == username and passwordInput == password:
                break
    

if i == 2:
    print("Account locked")
else:
    print("login successful") 