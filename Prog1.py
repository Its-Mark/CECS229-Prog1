# Mark Garcia
# Programming Assignment 1
# CECS 229-05
# Due:
# 1. Given two integers, use the Euclidean algorithm to find their greatest common divisor.
# 2. Convert Binary String to Decimal
# Design a class named Rectangle to represent a rectangle. The class contains:
# • Two double data fields named width and height that specify the width and height
# of the rectangle.
# • A no-arg constructor that creates a rectangle with width 1 and height 1.
# • A constructor that creates a rectangle with the specified width and height.
# • A function named getArea()that returns the area of this rectangle.
# • A function named getPerimeter() that returns the perimeter.
# Implement the class. Write a test program that creates two Rectangle objects. Assign
# width 4 and height 40 to the first object and width 3.5 and height 35.9 to the second.
# Display the width, height, area, and perimeters of the first object and then the second
# object.

class Rectangle:
    def __init__(self):
        self.width = 1
        self.height = 1

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * self.width + 2 * self.height
