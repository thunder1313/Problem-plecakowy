from randomProblem import generateRandomProblem
from knapsackClass import Knapsack
from sys import setrecursionlimit
setrecursionlimit(100_000_000)

n = 22
p = 0.5 # b = p * sum(ai)

problem1 = generateRandomProblem(n)
problem2 = generateRandomProblem(n)
K1 = Knapsack(p, problem1)
#K2 = Knapsack(0.5, problem2)
print(problem1, end = ' ')
print(K1.dynamic(n-1, K1.size))
print(K1.BF2(problem1))
#print(K1.BF1())
#print(problem2, end = ' ')
#print(K2.dynamic(4, 10))
#print("Random: ", K1.HRandom())
#print("Min Si: ", K1.HMinS())
#print("Max Wi: ", K1.HMaxW())
#print("Max Wi/Si: ", K1.HMaxWS())