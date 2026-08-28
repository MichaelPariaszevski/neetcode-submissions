class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: list = []

        for operation in operations: 
            if operation == "+": 
                stack.append(stack[-1] + stack[-2])
            elif operation == "D": 
                stack.append(stack[-1] * 2)
            elif operation == "C": 
                stack.pop()
            else:
                stack.append(int(operation))

        result = 0
        for value in stack: 
            result += value

        return result

        