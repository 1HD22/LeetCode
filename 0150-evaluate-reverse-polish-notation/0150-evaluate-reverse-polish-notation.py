class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        moving = 0
        while True:
            if moving == len(tokens):
                break
            
            if tokens[moving] == '+':
                tokens[moving] = str(int(tokens[moving - 2]) + int(tokens[moving - 1]))
            elif tokens[moving] == '-':
                tokens[moving] = str(int(tokens[moving - 2]) - int(tokens[moving - 1]))
            elif tokens[moving] == '*':
                tokens[moving] = str(int(tokens[moving - 2]) * int(tokens[moving - 1]))
            elif tokens[moving] == '/':
                tokens[moving] = str(math.trunc(int(tokens[moving - 2]) / int(tokens[moving - 1])))
            else:
                moving += 1
                continue
            
            for _ in range(2):
                tokens.pop(moving - 2)
            
            moving -= 1
        
        return int(tokens[0])
                
                
                
                
            