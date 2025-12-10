# try:
#     num = int(input("Enter a number: "))
#     print(num + 5)
# except Exception as e:
#     print("Something went wrong", e)
# finally:
#     print("I will always be executed")

# try:
#     print("Hello")
#     # print(a)
#     print(5 / 0)
# except NameError:
#     print("undefined variable")
# except ZeroDivisionError:
#     print("Cannot divide by 0")

class AgeError(Exception):
    def __init__(self, *args):
        self.age = age
        self.name = args[0]
        super().__init__(*args)


def handle_age(age):
    if age < 0:
        raise AgeError(age, "Hello", 50, "Tolu")

try:
    age = int(input("Enter your age: "))
    handle_age(age)
except AgeError as e:
    print("Age error executing", e)


# def my_func(*args):
#     total = 0
#     for val in args:
#         total = total + val
#     return total

# print(my_func(9, 10))
# print(my_func(3, 6, 9, 12, 15))
