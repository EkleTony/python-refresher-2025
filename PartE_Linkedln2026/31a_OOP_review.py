"""Object Oriented Programming... review

    Class

"""


class Computer:
    # 1. Class and Instance Attributes
    """method is the initializer for a class. It is often referred to as a constructor"""

    def __init__(self, type, ram, color):
        self.type = type
        self.ram = ram
        self.color = color

    # 2. Instance Methods
    """Instance methods are functions that you define inside a class"""
    # and can only call on an instance of that class .

    def __str__(self):
        return f"==========Welcome to Computer {self.type} with ram of {self.ram}=============="

    def printAll(self):
        print(
            f'This computer type is {self.type}, with Ram {self.ram} and color is {self.ram}')

    def gpuSize(self, gpu):
        print(f'Computer {self.type} has gpu size of {gpu}')


comp1 = Computer("MacBook Air", "12GB", "Gray")
comp2 = Computer("Dell", "5GB", "black")
print(comp1)
print(comp2)
comp1.printAll()
comp1.gpuSize(10)


"""===Types of Methods=="""


class Student:

    # contructor method
    def __init__(self, score1, score2, score3):
        self.s1 = score1
        self.s2 = score2
        self.s3 = score3

    # instance methods....
    def avg(self):
        return (self.s1 + self.s2 + self.s3)/3
    
    
    # get methods get the values
    def get_s1(self):
        return self.s1

    # setters sets the values....reaassinging..
    def set_s1(self, value):
        self.s1 = value


s1 = Student(23, 46, 89)
s2 = Student(44, 55, 76)

print(f'Student 1: {s1.avg()}')
print()
print(f'Student2 : {s2.avg()}')
