class Employee:
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary
    
    def give_raise(self, sraise = 5000):
        self.salary += sraise
        return self.salary 
    
    def details(self):
        print("You are: ")
        print(f"{self.first} {self.last} with a salary of ${self.salary}")