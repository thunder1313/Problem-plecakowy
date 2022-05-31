def BF2(problem, size):
    def checkElement(i, weight, value):
        nonlocal problem, size, max_value
        if i > len(problem)-1 or weight > size:
            return
        if max_value < value:
            max_value = value
        element = problem[i]
        checkElement(i+1, weight+element[0], value+element[1])
        checkElement(i+1, weight, value)
    
    max_value = 0
    checkElement(0,0,0)
    print(max_value)

problem = [(5,3), (3,4), (2,2), (4,6), (3,1)]
problem2 = [(8, 8), (7, 1), (2, 9), (1, 6), (6, 2), (8, 7)]
BF2(problem2, 16)