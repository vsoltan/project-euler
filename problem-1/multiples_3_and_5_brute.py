def euler1(n):
    """Sums all the integers that are multiple of 3 or 5 between 0 and n"""
    u = 0
    for i in range(n):
        if i % 3 == 0 or i % 5 == 0:
            u = i + u
    print(u)


euler1(1000)
