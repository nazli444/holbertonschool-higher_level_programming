#!/usr/bin/python3
def fizzbuzz():
    for n in range(1,100):
        if n % 3 == 0 and n % 5 == 0:
            return FizzBuzz
        elif n % 3 == 0:
            return Fizz
        elif n % 5 == 0:
            return Buzz
        else:
            return n
