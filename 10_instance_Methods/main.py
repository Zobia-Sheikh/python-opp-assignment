class Dog:
    def __init__(self, name, breed):
        # instance variables
        self.name = name
        self.breed = breed 
    def bark(self):       # instance methods
        
     print(f"{self.name} is barking!")
     
    #creating an object(instance)
if __name__ == "__main__":
    my_dog = Dog ("Lucky", "bulldog")
#calling the method
    my_dog.bark()
    