def generate(k, A):
    if k == 1:
        print(A)
    else:
        generate(k-1, A)

        for i in range(0, k-1):
            if k%2 == 0:
                temp  = A[i]
                A[i] = A[k-1]
                A[k-1] = temp
            else:
                temp  = A[0]
                A[0] = A[k-1]
                A[k-1] = temp
            generate(k-1, A)

A = [1, 2, 3, 4, 5]
generate(len(A), A)