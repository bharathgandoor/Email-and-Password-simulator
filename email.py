emailaddress=input("To register, you need to provide an email address: ")
password=input("Please enter a password: ")
retypepassword=input("Please re-enter the same password for verification: ")
if "@gmail.com" in emailaddress or "@outlook.com" in emailaddress or "@hotmail.com" in emailaddress:
    if "_" in password[0]:
        print("Invalid password, passwords cannot start with '_'")
    elif password!=retypepassword:
        print("Passwords do not match")
    else:
        print("Your account has been created")
else:
    print("Invalid Email")

