class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [int(tokens[0])]
        for i in tokens[1:]:
            if i in '+-*/':
                val1, val2 = stack.pop(), stack.pop()
                if i == '+':
                    stack.append(val1 + val2)
                elif i == '-':
                    stack.append(val2 - val1)
                elif i == '*':
                    stack.append(val1 * val2)
                elif i == '/':
                    stack.append(int(val2 / val1))
            else:
                stack.append(int(i))
        return stack[0]