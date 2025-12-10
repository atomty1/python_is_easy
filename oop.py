
# class Person:
#     def __init__(self, new_name, new_dept):
#         self.name = new_name
#         self.dept = new_dept
#         print(self.name, self.dept)
#         self.greet()


#     def say_hi(self):
#         print(f"{self.name} How are you doing today?")
    
#     def change_name(self, new_name):
#         self.name = new_name
    
#     def greet(self):
#         print("Good evening everyone")


# a = Person("Rukayat", "CSC")
# a.say_hi()
class Human:
    eyes = 2
    head = 1
    ears = 2
    def __init__(self, eyes, head, ears):
        self.eyes = eyes
        self.head = head
        self.ears = ears
    def talk(self):
        print("I am talking")
    
    def display_head_info(self):
        print(f"I have {self.eyes} eyes in my {self.head} head")


class Man(Human):
   
    def __init__(self, voice, eyes, head, ears):
        super().__init__(eyes=eyes, head=head, ears=ears)
        self.voice = voice
        
    def talk(self):
        super().talk()
        print("I am not talking")

class Woman(Human):
    hair = "plenty"

adam = Man(ears=4, head=1, eyes=2, voice="deep")
adam.talk()
adam.display_head_info()



