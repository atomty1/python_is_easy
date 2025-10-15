print("welcome to a new session")
print("Find out your grade")
user_score = int(input("Enter your score: "))
if(user_score < 0 or user_score > 100):
    print("Out of range")
elif(user_score <= 39):
    print("fail")
elif(user_score <= 44):
    print("Poor")
elif(user_score <= 49):
    print("Fair")
elif(user_score <= 59):
    print("Average")
elif(user_score <= 69):
    print("Good")
elif(user_score <= 100):
    print("Excellent")
