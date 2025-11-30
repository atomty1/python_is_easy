print("Welcome")
everyone = []
def start_work():
    print("What do you wnat to do?")
    menu = input("1. Add new person 2. To Get oldest person 3. Average age 4. To greet everyone 5. Edit person 6. Delete person: ")
    if(menu == "1"):
        add_new_person()
    elif(menu == "2"):
        get_oldest()
    elif menu == "3":
        
        get_average_age()
    elif menu == "4":
        greet_everyone()
    elif menu == "5":
        edit_person()
    elif menu == "6":
        delete_person()

    print("Do you want to do anything else?")
    go_back = input("1. Yes 2. No: ")
    if(go_back == "1"):
        start_work()
    else:
        print("Bye!!!")


def add_new_person():
    f_name = input("Enter the firstname: ")
    l_name = input("Enter the lastname :")
    user_age = int(input("Enter the age: "))
    new_person =  {"firstname": f_name, "lastname": l_name, "age": user_age}
    everyone.append(new_person)
    print(f"{f_name} {l_name} added successfully.")

def get_oldest():
    oldest = 0
    oldest_person = {}
    for person in everyone:
        current_age = person["age"]
        if( current_age > oldest):
            oldest = current_age
            oldest_person = person
    print(f"{oldest_person["firstname"]} {oldest_person["lastname"]} is the oldest with the age of {oldest}")

def get_average_age():
    total_persons = len(everyone)
    total_age = 0
    for person in everyone:
        current_age = person["age"]
        total_age = total_age + current_age

    average_age = total_age / total_persons
    print(f"The average age of the persons is {average_age:.2f}")

def greet_everyone():
    for person in everyone:
        print(f"Good morning {person["firstname"]}  {person["lastname"]}")

def edit_person():
    index = int(input("Enter the index you want to edit: "))
    key = input("Enter the key you want to edit: ")
    value = input(f"Enter the value for {key}: ")
    everyone[index][key] = value
    print("Edited successfully")

def delete_person():
    index = int(input("Enter the index you want to delete: "))
    person = everyone[index]
    del everyone[index]
    print(f"{person["firstname"]} {person["lastname"]} deleted successfully.")


# start_work()

val = 4.7543356999643222
print(f"{val:.3f}")




