class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        
        rv = [0] * m
        cv = [0] * n

        for ir, ic in indices:
            rv[ir] += 1
            cv[ic] += 1
        
        res = 0
        for r in range(m):
            for c in range(n):
                if (rv[r] + cv[c]) % 2 == 1:
                    res += 1
        return res