class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l,r = 0, len(matrix)-1
        row = []
        while l <= r:
            if r - l == 0:
                row = matrix[r]
                break
            mid = (l + r) // 2
            
            if target >= matrix[mid][0] and target <= matrix[mid][len(matrix[mid])-1]:
                row = matrix[mid]
                break
            
            if target < matrix[mid][0]:
                # in upper part of matrix
                r = mid-1
            else:
                # in lower part of matrix
                l = mid+1
                
        l, r = 0, len(row)-1
        
        while l <= r:
            mid = (l + r) // 2
            
            if row[mid] == target:
                return True
            
            if target < row[mid]:
                r = mid-1
            else:
                l = mid + 1
                
        return False