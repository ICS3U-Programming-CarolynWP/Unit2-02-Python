#!/usr/bin/env python3
# Created by: Carolyn Webster Pless
# Created on: 2022/09/22
# Takes user input for the length and width and displays the area
# and perimeter back to the user


import math


def main():

    print("Area and Perimeter of a Rectangle")
    length = int(input("Enter the length here (cm): "))
    width = int(input("Enter the width here (cm): "))

    area = length * width
    perim = 2 * (length + width)

    print("The area is : {}cm^2".format(area))
    print("The perimeter is : {}cm".format(perim))


if __name__ == "__main__":
    main()
