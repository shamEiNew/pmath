## Still not resolved
def maxproduct(A):
    max_product=1
    n = len(A)
    for i in range(n):
        for j in range(n):
            if (j-3)>=0:
                product = A[i][j]*A[i][j-1]*A[i][j-2]*A[i][j-3]
                max_product=max(product, max_product)
            if (i-3)>=0:
                product = A[i][j]*A[i-1][j]*A[i-2][j]*A[i-3][j]
                max_product=max(product, max_product)
            if ((i-3)>=0 and (j-3)>=0):
                product = A[i][j]*A[i-1][j-1]*A[i-2][j-2]*A[i-3][j-3]
                max_product=max(product, max_product)
            #if ((i-3)>=0 and (j-3)>=0):
            #    product = A[i][j]*A[i+1][j-1]*A[i+2][j-2]*A[i+3][j-3]
            #    max_product=max(product, max_product)
    return max_product
if __name__=="__main__":
    A =[]
    with open('grid.txt', 'r') as grid:
        B = grid.readlines()
        for i in range(0, len(B)):
            A.append(list(map(int, B[i].strip().split())))
    print(maxproduct(A))