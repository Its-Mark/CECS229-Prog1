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
        self.width = 1.0
        self.height = 1.0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def getArea(self):
        return self.width * self.height

    def getPerimeter(self):
        return 2 * self.width + 2 * self.height


def euclidean(a, b):
    print("A: " + str(a) + ", B: " + str(b))
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a > b:
        return euclidean(a % b, b)
    elif b > a:
        return euclidean(b % a, a)


def binToDec(bins):
    binSplit = list(bins)
    decimal = 0
    for i in range(len(binSplit)):
        decimal += int(binSplit[i]) * 2**(i+1)
    return decimal


def main():
    r1 = Rectangle(4, 40)
    r2 = Rectangle(3.5, 35.9)
    print("Rectangle 1: \nWidth: " + str(r1.width) + "\nHeight: " + str(r1.height) + "Perimeter: " + str(
        r1.getPerimeter()) + "\nArea: " + str(r1.getArea()))
    print("Rectangle 2: \nWidth: " + str(r2.width) + "\nHeight: " + str(r2.height) + "Perimeter: " + str(
        r2.getPerimeter()) + "\nArea: " + str(r2.getArea()))
    a = int(input("a = "))
    b = int(input("b = "))
    print("EUCLIDEAN ALGO FOR " + str(a) + " & " + str(b))
    print(euclidean(a, b))
    c = "1001010010"
    print("Decimal representation of: " + str(c))
    print(binToDec(c))

    exit = input("Press any key to exit")

main()
