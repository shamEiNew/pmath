import math

def pascalstriangle(n, limit):
    print(" "*(limit-n), end=' ')
    if n >= 1:
        for i in range(n+1):
            print(f'{math.comb(n, i)}', end=' ')
        print("\n")
            #return pascalstriangle(n-1)

if __name__ == '__main__':
    n = 10
    for i in range(1, n+1):
        pascalstriangle(i, n)