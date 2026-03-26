#!/usr/bin/python3
def fizzbuzz():
    for n in range(1,100):
        if n % 3 == 0 and n % 5 == 0:
            print("{}".format(FizzBuzz))
        elif n % 3 == 0:
            print("{}".format(Fizz))
        elif n % 5 == 0:
            print("{}".format(Buzz))
        else:
            print(n)
    return 
