def searchMatrix( matrix, target) :
    m = len(matrix)
    n = len(matrix[0])
    for i in range(m):
        if target>= matrix[i][0] and target <= matrix[i][n - 1]:
            l = 0
            r = n - 1
            while l < r:
                mid = (l+r) // 2
                if matrix[i][mid] == target:
                    return True
                elif matrix[i][mid] > target:
                    r = mid - 1
                else:
                    l = mid + 1
    return False
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
new=searchMatrix(matrix,target)
print(new)
