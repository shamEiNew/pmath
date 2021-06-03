def collatzsequence(n):

    if n==1:return True

    if (n % 2 == 0):
        return collatzsequence(n//2)

    else:
        return collatzsequence((3*n+ 1)//2)

if __name__ =='__main__':
    print(all([collatzsequence(i) for i in range(2, 1000000)]))