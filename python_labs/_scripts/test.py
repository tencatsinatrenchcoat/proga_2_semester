for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            print("a", ((not x) and (not y)))
            print("b", (not(x and y)))