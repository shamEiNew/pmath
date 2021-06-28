def riemannsum(
    f,
    lower_bound, 
    upper_bound ,
    subintervals, 
    method="left",
    ):

    delta_x = abs(upper_bound-lower_bound)/subintervals

    while method in "midpoint right":
        if method == "midpoint":
            return sum([f(lower_bound + (2*i+1)*delta_x/2) for i in range(1, subintervals)])*delta_x 
        elif method == "right":
            return sum([f(lower_bound + i*delta_x) for i in range(1, subintervals+1)])*delta_x
        else:
            break
        
    return sum([f(lower_bound + i*delta_x) for i in range(0, subintervals+1)])*delta_x


if __name__=="__main__":
    print(riemannsum(lambda x: x**2, 0, 1, 120, "midpoint"))
