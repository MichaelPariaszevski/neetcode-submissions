class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: list = []
        result = 0

        for operation in operations: 
            if operation == "+": 
                add = stack[-1] + stack[-2]
                result += add
                stack.append(add)
            elif operation == "D": 
                double = stack[-1] * 2
                result += double
                stack.append(double)
            elif operation == "C": 
                result -= stack.pop()
            else:
                int_operation = int(operation)
                result += int_operation
                stack.append(int_operation)

        return result

        