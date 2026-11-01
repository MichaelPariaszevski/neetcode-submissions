class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result: int = 0
        for person in details:
            if int(person[11 : 13]) > 60: 
                result += 1

        return result
        