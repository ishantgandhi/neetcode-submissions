class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ari = ["+","-","*","/"]
        for char in tokens:
            if char not in ari:
                stack.append(int(char))
            else:
                if char == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a+b)
                elif char == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                elif char == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(a*b)
                elif char == "/":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b/a))
        return int(stack[-1])
                    
            