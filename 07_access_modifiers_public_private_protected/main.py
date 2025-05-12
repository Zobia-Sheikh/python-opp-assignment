class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name        #pubic variable
        self._salary = salary   #protected variable
        self.__ssn = ssn        #private variable
        
if __name__ == "__main__":
    emp = Employee("Saad", 8000, "42401-24-8493")
    
    #Access public variable
    print("Public variable:", emp.name)
    
    #Access protected variable
    print("Protected variable:", emp._salary)
    
    #Access private variable
    print("Private variable:", emp.__ssn)