import random

"""The only even prime number is 2. All other even numbers can be divided by 2. If the sum of a number's digits is a 
multiple of 3, that number can be divided by 3. No prime number greater than 5 ends in a 5. Any number greater than 5 
that ends in a 5 can be divided by 5. Zero and 1 are not considered prime numbers. Except for 0 and 1, a number is 
either a prime number or a composite number. A composite number is defined as any number, greater than 1, that is not 
prime. """


def prime_checking(number_in):
    flag_variable = False
    if number_in == 0 or number_in == 1:
        print(f"{number_in} is not considered a prime number")
    else:
        for case in range(2, number_in):
            if number_in % case == 0:  # check remainder in prime
                flag_variable = True  # break out condition for NO reminder is found
                break

            # print("It is a prime number")
    if flag_variable:
        print(f"{number_in} is a composite number")
    elif not flag_variable:
        print(f"{number_in} is a prime number")


Number_Choice = int(input("Enter a Number: "))
prime_checking(Number_Choice)
