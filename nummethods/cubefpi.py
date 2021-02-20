def cubic_root(radicand, initial_value, iterations):
    fixed_point = initial_value
    for _ in range(0, iterations):
        fixed_point = 2/3*fixed_point + radicand/(3*(fixed_point)**2)
    return fixed_point

if __name__ == "__main__":
    print(cubic_root(6, 2, 3))