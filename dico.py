# person = {"school": "UI", "dept": "CSC", "name": "Kenny", "names": ["Taye", "Kenny", "Idowu"]}
# person.clear()
# print(person)
# person["age"] = 20
# person = {}
# key = input("Enter the key: ") # "dept"
# value = input(f"Enter the value of {key}: ") #BCH
# person[key] = value
# print(person)



# 1. To add new data
# 2. To see data values
# 3. To see all data info
# 4. To clear all info

# 1. Enter the key
#     Enter the value for key
#     print(key added successfully)

# 2. Taye, CSC

# 3. 

# 4. 

# Do you want to do anything else?
# 1. Yes 2. No
print("Welcome to my dictionary")
info = {}
def dico():
    print("What do you want to do? ")
    menu = input("1. Add new data 2. See all data values 3. See all data info. 4. To clear all info: ")
    if(menu == "1"):
        key = input("Enter the key: ")
        value = input(f"Enter the value for {key}: ")
        info[key] = value
        print(f"{key} added successfully.")
    elif( menu == "2"):
        print(info.values())
    elif(menu == "3"):
        print(info)
    elif(menu == "4" ):
        info.clear()
    print("Do you want to anything else?")
    repeat = input("1. Yes 2. No: ")
    if(repeat == "1"):
        dico()
    else:
        print("BYE!")

dico()