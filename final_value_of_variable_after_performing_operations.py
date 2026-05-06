class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        for op in operations:
            if op[1] == "+":
                result +=1
            else:
                result -=1
        return result