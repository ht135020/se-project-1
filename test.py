# part 1

username = "admin"
password = "1234"

usernameInput = input("Enter username: ")
passwordInput = input("Enter username: ")

for i in range(3):
    print("Attempt", i)
    if usernameInput == username and passwordInput == password:
                break
    

if i == 2:
    print("Access denied")
else:
    print("Access granted") 