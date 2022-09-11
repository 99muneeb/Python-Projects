
# Method 01
email = input("Enter Your Email: ")  # g@g.in
k, d, j = 0, 0, 0
if len(email) >= 6:
    if email[0].isalpha():
        if ("@" in email) and (email.count("@") == 1):
            if (email[-4] == ".") ^ (email[-3] == "."):
                for i in email:
                    if i == i.isspace():
                        k = 1
                    elif i.isalpha():
                        if i == i.upper():
                            j = 1
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email 5")
                else:
                    print("Write Email: ")
            else:
                print("Wrong Email 4")
        else:
            print("Wrong Email 3")

    else:
        print("Wrong Email 2")
else:
    print("Wrong Email 1 ")

# Method 2
# Email Validation in python (using RegEx Model)

import re
email_condition ="^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email=input("Enter your Email : ")
if re.search(email_condition,user_email):
    print("Write Email :) ")
else:
    print("Wrong Email : ")
