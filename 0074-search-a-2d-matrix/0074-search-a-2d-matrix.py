class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Поиск строки потом поиск внутри строки
        # если t больше mid - l = mid если t меньше mid то r = mid - 1
        # mid = (l+m+1) // 2

        l = 0
        r = len(matrix) - 1


        while l < r:
            mid = (l+r+1) // 2

            if target < matrix[mid][0]:
                r = mid - 1
            else:
                l = mid
        
        row = r
        l = 0
        r = len(matrix[row]) - 1

        while l <= r:
            mid = (l+r) // 2

            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        return False