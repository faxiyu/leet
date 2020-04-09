class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        r = list(zip(*matrix[::-1]))#矩阵倒置
        for i in range(n):
            for j in range(n):
                matrix[i][j] = r[i][j]