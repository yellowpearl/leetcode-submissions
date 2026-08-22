class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = []

        ll = intervals[0][0]
        lr = intervals[0][1]
        for rl, rr in intervals:

            if lr >= rl and ll <= rr:
                ll = min(ll, rl)
                lr = max(lr, rr)
            else:
                res.append([ll, lr])
                ll = rl
                lr = rr
        
        res.append([ll, lr])
        return res