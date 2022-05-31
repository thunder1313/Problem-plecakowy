def function(problem, i, l):
    if i == -1 or l == 0:
        return 0
    if problem[0][i] > l:
        return function(problem, i-1, l)
    if problem[0][i] <= l:
        return max(function(problem, i-1, l), function(problem, i-1, l-problem[0][i]) + problem[1][i])
    
def main():
    problem = [ [5,3,2,4,3],
                [6,2,1,4,3] ]
    print(function(problem, 4, 10))
    
main()