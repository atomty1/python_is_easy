# a = 2
# if (a < 12):
#     print("First")
# elif(a < 5):
#     print("Second")
# elif( a < 3):
#     print("Third")
# if(a == 2):
#     print("Fourth")

# b = 7
# if (b != 4):
#     print("Welcome")
# else:
#     print("Heeey")

# c = 4
# d = 8
# e = 5

# if( c < 10 or d == 8 and e > 15):
#     print("Hello")
# else:
#     print("HI")
print("Signup")
username = input("Enter your username: ")

print("Signup successful.")
repeat_username = input("Enter your username: ")

if(username == repeat_username):
    password = input("Enter your password: ")
    repeat_password = input("Enter your password: ")
    if(password == repeat_password):
        print("Password match")
    
    else:
        print("Password do not match")
else:
    print("Incorrect username")

# 70 - 100 - Excellent
# 60 - 69 - Good
# 50 - 59 - average 
# 45 - 49 - Fair
# 40 - 44 - Poor
# 0 - 39 - Fail
# More than 100 or less than 0 - Out of range