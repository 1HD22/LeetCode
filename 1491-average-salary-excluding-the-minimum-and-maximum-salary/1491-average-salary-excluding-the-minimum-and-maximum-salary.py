class Solution:
    def average(self, salary: List[int]) -> float:
        sum = 0
        length = len(salary) - 2
        minimum = math.inf
        maximum = -math.inf
        
        for i in salary:
            sum += i
            if i > maximum:
                sum -= i
                if maximum != -math.inf:
                    sum += maximum
                maximum = i
            if i < minimum:
                sum -= i
                if minimum != math.inf:
                    sum += minimum
                minimum = i
        
        return sum / length
                
        