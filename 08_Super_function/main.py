#step1: parent class
class Person:
    def __init__(self, name):
        self.name = name
            
#step2: chils class
class Teacher(Person):      #inheriting person
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject
        
    #step 3 display
    def display(self):
        print(f"Name: {self.name}, Subject: {self.subject}")
        
if __name__ == "__main__":
    teacher = Teacher("Miss jia", "Maths")
    teacher.display()