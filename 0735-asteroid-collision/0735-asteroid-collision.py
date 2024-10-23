class Solution:
    class Stack:
        
        def __init__(self) -> None:
            self.stack: list[int] = []
        
        @property
        def last(self) -> int | None:
            if len(self.stack) == 0:
                return None
            
            return self.stack[-1]
        
        @property
        def length(self) -> int:
            return len(self.stack)
        
        def add(self, n: int) -> None:
            self.stack.append(n)
            
        def pop(self) -> int:
            
            return self.stack.pop(-1)
        
        def collide_add(self, n:int) -> None:
            
            if (self.length <= 0):
                self.add(n)
                return
            
            if (self.last * n > 0):
                self.add(n)
                return
            
            if (self.last < 0 and n > 0):
                self.add(n)
                return
            
            if (abs(self.last) == abs(n)):
                self.pop()
                return
            
            if (abs(self.last) > abs(n)):
                return 
            
            self.pop()
            self.collide_add(n)
            
            return
        
        def flush(self) -> list[int]:
            return self.stack
            
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        
        stack: self.Stack = self.Stack()
        for a in asteroids:
            stack.collide_add(a)
        
        return stack.flush()
            
        