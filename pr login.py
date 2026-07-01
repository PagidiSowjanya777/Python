username = "Sowjanya"
password = "1234"
username = "aynjwos"
password = "4321"
while True:

    print("\n LOGIN PAGE ")

    user = input("Enter Username: ")
    pwd = input("Enter Password: ")

    if user == username and pwd == password:
        print("Login Successful!")
        break

    else:
        print("Invalid Username or Password")

        choice = input("Try Again? (yes/no): ")

        if choice.lower() == "no":
            print("Thank You!")
            break
