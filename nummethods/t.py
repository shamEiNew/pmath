def laugh(x):
    if x == 0:
        print("lol")
    else:
        laugh(x-1)
        print(x)
        print("aye")
        
laugh(5)