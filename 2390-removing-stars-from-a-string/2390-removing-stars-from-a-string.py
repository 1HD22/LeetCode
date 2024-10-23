class Solution:
    class Stack:
        def __init__(self):
            self.l: list[str] = []
                
        def append(self, s: str) -> None:
            self.l.append(s)
            
        def pop(self) -> str:
            if len(self.l) <= 0:
                return ''
            return self.l.pop(-1)
        
        def flush(self) -> str:
            return ''.join(self.l)
        
    def removeStars(self, s: str) -> str:
        
        stack: Stack = self.Stack()
        for c in s:
            if c == '*':
                stack.pop()
                continue
            
            stack.append(c)
        
        return stack.flush()
            
                
        