class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        up = 0
        down = len(matrix)-1
        right = len(matrix[0])-1
        left = 0
        while(down >= up and right >= left):
                for i in range(left, right+1):
                        # print("up")
                        result.append(matrix[up][i])
                up += 1
                
                for i in range(up, down+1):
                        # print("right")
                        result.append(matrix[i][right])
                right -= 1
                if up <= down:
                        for i in range(right, left-1, -1):
                                # print("down")
                                result.append(matrix[down][i])
                down -=1
                if left <= right:
                        for i in range(down, up-1, -1):
                                # print("left")
                                result.append(matrix[i][left])
                left += 1
        return result