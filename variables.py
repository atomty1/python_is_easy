first_num = int(input("Enter the first number: ")) # 6
second_num = int(input("Enter the second number: ")) # 30
def check_nums():
    global second_num
    if(second_num < first_num):
        print("You did not get it right, enter a higher number")
        second_num = int(input("Enter the second number again: "))
        check_nums()
    else:
        print("Correct.")
        print("BYE!")

check_nums()

