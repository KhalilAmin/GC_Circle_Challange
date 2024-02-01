"""
Prompt the user to enter a radius; the user may enter a number with decimals (double).
Display an error if the user enters invalid data and asks the user again for a radius.
When the user enters valid data, create an instance of a Circle and then use its methods to display the Diameter, Circumference and Area.
Ask the user if the circle should grow.
If the user says yes, call the grow method and then loop back to the method calls for the formulas.
The grow method will double radius.
If the user says no, display a “goodbye” message and the radius of the circle.

Build Specifications:
Create a class named Circle to store the data about this circle. This class should contain the following:
Initialization (self, radius)
Sets the radius property
"""
import math

validInput = True
while validInput:
    radius = float(input(f'Enter the radius of the circle: '))
    if (type(radius) != float):
        print(f'Invalid input, please enter a positive number!')
    elif (radius <= 0):
        print(f'Invalid input, please enter a positive number!')
    else:
        validInput = False

class circle:
    def __init__(self, radius):
        self.radius = radius

# Methods
# calculate_diameter()
# Returns the calculated diameter
    def calculate_diameter(self):
        diameter = self.radius*2
        return diameter

#calculate_circumference()
#Returns the calculated circumference
    def calculate_circumference(self):
        circumference = (self.radius*2)*math.pi
        return circumference

#calculate_area()
#Returns the calculated area
    def calculate_area(self):
        area = math.pi*(self.radius**2)
        return area
# grow()
# Doubles the radius property
    def grow(self):
        self.radius*=2
# get_radius()
# Returns the radius value
    def get_radius(self):
        return self.radius

c1= circle(radius)
print(f"Diameter: {c1.calculate_diameter()}")
print(f"Circumference: {c1.calculate_circumference()}")
print(f"Area: {c1.calculate_area()}")
growChoice=input("Would you like your circle to grow?(y/n) ")
while growChoice=='y':
    c1.grow()
    print(f"Diameter: {c1.calculate_diameter()}")
    print(f"Circumference: {c1.calculate_circumference()}")
    print(f"Area: {c1.calculate_area()}")
    growChoice = input("Would you like your circle to grow?(y/n) ")
    if growChoice=='n':
        print("Goodbye")
    elif(growChoice=='y'):
        pass
    else:
        print("Invalid input, please")
        growChoice=input("Would you like your c1 to grow?(y/n) ")

"""
For the value of pi, use the pi constant of the math module (import math).
Get the user input, create a Circle object, and display the diameter, circumference and area.
"""