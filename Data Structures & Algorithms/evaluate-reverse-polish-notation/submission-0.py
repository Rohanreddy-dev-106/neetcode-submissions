class Solution:
    def givenumbers(self, stack):
        n = []
        b = stack.pop()
        a = stack.pop()
        n.append(a)
        n.append(b)
        return n

    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for element in tokens:
            if element == "+":
                x = self.givenumbers(stack)
                stack.append(sum(x))

            elif element == "-":
                y = self.givenumbers(stack)
                ans = y[0] - y[1]
                stack.append(ans)

            elif element == "*":
                z = self.givenumbers(stack)
                stack.append(z[0] * z[1])
                
            elif element == "/":
                z = self.givenumbers(stack)
                stack.append(int(z[0] / z[1])) 

            else:
                stack.append(int(element))

        return stack[-1]