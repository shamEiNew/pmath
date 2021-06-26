def permute(nums):
    result_perms = [[]]
    for n in nums:
        print(n)
        new_perms = []
        for perm in result_perms:
            print(perm)
            for i in range(len(perm)+1):
                new_perms.append(perm[:i]+[n]+perm[i:])
                print(new_perms)
                result_perms=new_perms
    return result_perms

if __name__=='__main__':
    my_nums = [1, 2, 3]
    #print(my_nums)
    print(permute(my_nums))