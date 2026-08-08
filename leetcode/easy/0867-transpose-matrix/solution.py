class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row=len(matrix)
        col=len(matrix[0])
        w=[]
        for i in range(col):
            t=[]
            for j in range(row):
                t.append(matrix[j][i])
            w.append(t)
        return w
        