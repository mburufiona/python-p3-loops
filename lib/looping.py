#!/usr/bin/env python3

def happy_new_year():
    for x in range(10, 0, -1):
        print(x)
        print("Happy New Year!")
        
def square_integers(int_list):
    square_list = [x * x for x in int_list]
    return square_list

def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz")
        elif x % 3 == 0:
            print("Fizz")
        elif x % 5 == 0:
            print("Buzz")
        else:
            print(x)

    
