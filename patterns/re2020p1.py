def solution(a):
    max_len = 0
    j = 1
    for i in range(0, len(a)-1):
        cd =  a[i+1] - a[i]     
        j = i
        while (j < (len(a)-1) and a[j+1] - a[j] == cd):
                j += 1
        max_len = max(j - i + 1, max_len)
    return max_len

"""
    max_len = 2
    #j = 0
    #temp_max_len = 2
    #while j < len(a)-2:
    #    if a[j+1]-a[j] == a[j+2]-a[j+1]:
    #        temp_max_len += 1
    #        if temp_max_len > max_len:
    #            max_len = temp_max_len
    #        j += 1
    #    else:
    #        j += 1
    #        temp_max_len  = 2
    
    #return max_len
"""

if __name__ == '__main__':
    result = []
    T = int(input())
    for i in range(0, T):
        N = int(input())
        if N >= 2:
            arr = input().split()
            arr = [int(arr[i]) for i in range(0, len(arr))]
            result.append(solution(arr))
        else:
            print()

    """start_time = time.time()
    print(longest_arithmetic_array(range(1, 1000)))
    print(time.time()- start_time)"""
    if N >= 2:
        for j in range(0, T):
            print(f'Case #{j+1}: {result[j]}')