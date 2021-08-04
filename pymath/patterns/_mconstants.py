import math

"""
The Champernowne constant is real transcendental real number,
In base 10 it is 0.12345678910121314151617....

"""
def g(n):
    """
    The constant has the form
    Each level is a set of integers, 1-9, 10-99, 100-999, ...
    0.123456789
      1011121314151617181920....

    g(n) determines the whether the n is in 1-9, 10-99, ...
    """
    s = 0
    for i in range(1, n+1):
        s += 9*(10**(i-1))*i
    return s
 
def digit_function(d):

    def print_function(value):

        """
        d is a non-local variable and it is accessed by the nested function.

        """
        print(f"The {d}th digit in the constant is {value}")  

    i = 1
    while True:
        if g(i) <= d <= g(i+1):
            a = d - g(i)
            p = math.ceil(a/(i + 1))
            if p == 1:
                return print_function(1)
            else:
                return print_function((10**i + p)-1)
        i+=1
    
 
if __name__ == "__main__":
    d = int(input("Enter the digit number to be found: "))
    digit_function(d)