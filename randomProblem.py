from random import randint
def generateRandomProblem(n):
    return [(randint(1, 10), randint(1, 10)) for i in range(n)]