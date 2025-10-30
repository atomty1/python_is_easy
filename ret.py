# def double(val):
#     return val * 2

# a = double(10)
# print(a)

# b = double(80)
# print(b)

def divideTwo(first, second):
    if(second != 0):
        return first/second
    else:
        print("You cannot divide by 0")

# a = divideTwo(50, 5)
# if(a == 100):
#     print("Success")
# else:
#     print("Wrong")
b = divideTwo(8, 0)
if(b is None):
    print("Correct")
