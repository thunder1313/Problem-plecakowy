import randomProblem
from copy import deepcopy
import random
from re import I
class Knapsack:
    """
    Solving Knapsack Problem

    item => [(size, value)]
    """
    size = 0
    items = []

    def __init__(self, percentage, items):
        self.items = items
        for x in items:
            self.size += percentage * x[0]

    def dynamic(self, i, l):
        """
        Dynamic programing solution for knapsack problem
        """
        if i == -1 or l == 0:
            return 0
        if self.items[i][0] > l:
            return self.dynamic(i-1, l)
        else:
            return max(self.dynamic(i-1, l), self.dynamic(i-1, l-self.items[i][0]) + self.items[i][1])

    def getbin(self, n, s=['']):

        """
        Util funtion to generate all combinantions
        """

        if n > 0:
            return [
                *self.getbin(n - 1, [i + '0' for i in s]),
                *self.getbin(n - 1, [j + '1' for j in s])
            ]
        return s

    def BF1(self):
        binNums = self.getbin(len(self.items))
     
        res = []
        maxProfit = 0
        maxWeight = 0
        for binary in binNums:
            arr = deepcopy(self.items)
            partialValue = 0
            partialWeight = 0
            partialRes =  [0 for x in range(len(self.items))]
            while len(arr) > 0:
                if(binary[len(arr)-1] == '1'):

                    partialWeight += arr[len(arr)-1][0]
                    partialValue += arr[len(arr)-1][1]
                    partialRes[len(arr)-1] = 1
              
                binary[:-1]
                arr.pop()
            if(partialWeight <= self.size and partialValue > maxProfit):
                res = partialRes
                maxProfit = partialValue
                maxWeight = partialWeight

        return res
    
    def BF2(self, problem):
        def checkElement(i=0, weight=0, value=0):
            nonlocal problem, max_value
            if max_value < value:
                max_value = value
            if i > len(problem)-1:
                return
            element = problem[i]
            if weight+element[0] <= self.size:
                checkElement(i+1, weight+element[0], value+element[1])
            checkElement(i+1, weight, value)
        
        max_value = 0
        checkElement()
        return max_value

    def HRandom(self):
        rand_i = [i for i in range(len(self.items))]
        random.shuffle(rand_i)
        current_size  = self.size
        w = 0
        result = []
        
        for x in rand_i:
            if current_size == 0:
                return result, w
            elif current_size - self.items[x][0] >= 0:
                current_size -= self.items[x][0]
                result.append(x)
                w += self.items[x][1]
        return result, w
        
    def HMinS(self):
        arr = sorted(deepcopy(self.items))
        current_size = self.size
        w = 0
        result = []
        
        for x in arr:
            if(current_size - x[0] >= 0):
                current_size -= x[0]
                result.append(x)
                w += x[1]
        return result, w
    
    def HMaxW(self):
        arr = sorted(deepcopy(self.items), key = lambda tup: tup[1], reverse = True)
        current_size = self.size
        w = 0
        result =  []
        
        for x in arr:
            if(current_size - x[0] >= 0):
                current_size -= x[0]
                result.append(x)
                w += x[1]
        return result, w

    def HMaxWS(self):
        arr = sorted(deepcopy(self.items), key = lambda tup: (tup[1]/tup[0]), reverse=True)
        current_size = self.size
        w = 0
        result =  []
        
        for x in arr:
            if(current_size - x[0] >= 0):
                current_size -= x[0]
                result.append(x)
                w += x[1]
        return result, w
