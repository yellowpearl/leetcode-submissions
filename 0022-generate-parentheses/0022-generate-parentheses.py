class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        curr = [[], 0, 0]

        def bt():
            if curr[1] + curr[2] == n * 2:
                res.append(''.join(curr[0]))
            
            if curr[1] < n:
                curr[0].append('(')
                curr[1] += 1
                bt()
                curr[0].pop()
                curr[1] -= 1
            if curr[2] < n and curr[2] < curr[1]:
                curr[0].append(')')
                curr[2] += 1
                bt()
                curr[0].pop()
                curr[2] -= 1
        bt()
        return res