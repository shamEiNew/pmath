def countTriangles(p): 

    store =[]

    if p % 2 != 0 : return 0
    else : 
        c = 0
        for b in range(1, p // 2): 
  
            a = p / 2 * ((p - 2 * b) / (p - b)) 
            inta = int(a) 
            if (a == inta ): 
   
                ab = tuple(sorted((inta, b))) 

                if ab not in store : 
                    c += 1 
                    store.append(ab) 
        return c
  
lst = []
for p in range(1, 1001):
	lst.append(countTriangles(p))

print(lst.index(max(lst)) + 1)
