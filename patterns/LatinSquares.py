""""Problem Vestigium: 
To Calculate the trace 
and number of rows and columns
with repeated values """

def inputs():
    T = int(input().strip())
    output = []
    for k in range(0, T):
        M = []
        N = int(input().strip())
        for _ in range(0, N):
            temp  = list(map(int, input().strip().split()))[0:N]
            M.append(temp)
        ans = repeated_row_columns(M, N)
        output.append(f"Case #{k+1}: {calcuate_trace(M, N)} {ans[0]} {ans[1]}")
    for i in range(0, T):
        print(output[i])

def calcuate_trace(M, N):
    trace = sum([M[i][i] for i in range(0, N)])
    return trace

def repeated_row_columns(M, N):
    counter_rows = 0
    counter_columns = 0
    M_transpose = []
    for i in range(0, N):
            M_transpose.append([M[j][i] for j in range(0, N)])
    for i in range(0, N):
        if len(set(M[i])) != N:
            counter_rows += 1
        if len(set(M_transpose[i])) != N:
            counter_columns += 1
    return counter_rows, counter_columns

inputs()