from time import *
import random as r


def mistake(par_test, user_test):
    error = 0
    for i in range(len(par_test)):
        try:
            if par_test[i] != user_test[i]:
                error = error + 1
        except:
            error = error + 1
    return error


def speed_time(time_start, time_end, user_input):
    time_delay = time_end - time_start
    time_R = round(time_delay, 2)
    speed = len(user_input) / time_R
    return round(speed)


if __name__ == '__main__':
    while True:
        ck = input("Ready to test : Yes / No : ")
        if ck == "Yes":
            test = [
                "A paragraph is a self-contained unit of discourse in writing dealing with a particular point or idea. ",
                "My name is Muneeb ", "wellcome to my github 99muneeb"]
            test1 = r.choice(test)
            print("**********Typing speed************")
            print(test1)
            print()
            print()
            time_1 = time()

            testinput = input(" Enter : ")
            time_2 = time()

            print("Speed :  ", speed_time(time_1, time_2, testinput), "w/sec")
            print("Error: ", mistake(test1, testinput))
        elif ck == "No":
            print("Thank you")
            break
        else:
            print("wrong input: ")
