class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        arithmetic = ['+', '-', '*', '/']
        for token in tokens:
            if token not in arithmetic:
                stack.append(int(token))
            else:
                n2 = stack.pop()
                n1 = stack.pop()
                if token == '+':
                    new = n1+n2
                    stack.append(new)
                elif token == '-':
                    new = n1-n2
                    stack.append(new)
                elif token == '*':
                    new = n1*n2
                    stack.append(new)
                else:
                    new = int(n1/n2)
                    stack.append(new)
        return stack[-1]

                
        