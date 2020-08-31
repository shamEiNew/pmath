def check_pandigital(str):
	flag = [0]*len(str)
	str1 = sorted(str)
	for i in range(0, len(str)):
		if int(str1[i]) == i + 1:
			flag[i] = 1
	
	for i in range(0, len(str)):
		if (flag[i] == 0):
			return False
	
	return True

if __name__ == "__main__":
	n = input("Enter the number:\n")
	print(check_pandigital(n))
