password = input("Enter your password: ")
pass_list = list(password)
check = 0
if len(pass_list) < 16:
    print("Your password should be at least 16 letters")
else:
    for i in pass_list:
        if i.isnumeric() == True:
            check = 1
    if check == 0:
        print("Your password should include at least one numeric value")
    else:
        for i in pass_list:
            if i.isupper() == True:
                check = 2
        if check == 1:
            print("Your password should include at least one uppercase letter")
        else:
            for i in pass_list:
                if i.isalnum() == False:
                    check = 3
            if check == 2:
                print("Your password should include at least one non-alphanumeric letter")
            else:
                print("Your password is true")

