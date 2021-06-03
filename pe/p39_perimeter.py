import math

def max_righttraingle():
	maximum_p = 0
	num = 0
	for p in range(10, 1002, 2):
		i = 0
		for m in range(1, math.ceil(math.sqrt(p/2))):
			for n in range(1, m + 1):
				if p == 2*m*(m + n):
					i+=1
		if i >= maximum_p:
			maximum_p = i
			num = p
	return maximum_p, num

if __name__ == "__main__":
	print(max_righttraingle())
