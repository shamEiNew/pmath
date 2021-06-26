import math
def g(n):
	s = 0
	for i in range(1, n+1):
		s += 9*(10**(i-1))*i
	return s

def digit_f(d):
	i = 1
	while True:
		if g(i) <= d <= g(i+1):
			a = d - g(i)
			print(a % (i+1))
			p = math.ceil(a/(i + 1))
			if p == 1:
				return 1
			else:
				return ((10**i + p)-1)
		i+=1

if __name__ == "__main__":
	#v = int(input("Enter the number of digits: "))
	#print("The number of numbers with " + str(v) + " digits" + " is equal to " + str(g(v)))
	d = int(input("Enter the digit number to be found: "))
	#s = digit_f(d)
	print(digit_f(d))
