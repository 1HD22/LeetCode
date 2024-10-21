class Solution:
    def isValid(self, s: str) -> bool:
        class Stack:
            def __init__(self):
                self.l: List[int] = []

            def insert(self, elem: int) -> None:
                self.l.append(elem)

            def remove(self) -> int:
                if not self.l:
                    return -1
                return self.l.pop(-1)
        
        bracket: dict[str, int] = {'(': 0, ')': 0, '[': 1, ']': 1, '{': 2, '}': 2}
        stack: Stack = Stack()
        opening: List[str] = ['(', '{', '[']
        closing: List[str] = [')', '}', '[']
        
        for c in s:
            if c in opening:
                stack.insert(bracket[c])
            else:
                if bracket[c] != stack.remove():
                    return False
        
        if len(stack.l) != 0:
            return False
        
        return True