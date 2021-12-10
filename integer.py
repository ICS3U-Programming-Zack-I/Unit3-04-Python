#!/usr/bin/env python3
# Created by: Zack isingoma
# Created on: Dec 9th , 2021
# This program makes users guess a random

num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")
