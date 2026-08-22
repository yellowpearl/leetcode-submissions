class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        res = []
        il = newInterval[0]
        ir = newInterval[1]
        inserted = False
        for l, r in intervals:
            
            if r < il:
                res.append([l,r])
            else:
                if l <= ir and r >= il:
                    il = min(il, l)
                    ir = max(ir, r)
                else:
                    if not inserted:
                        res.append([il, ir])
                        inserted = True
                    res.append([l,r])
        if not inserted:
            res.append([il, ir])
        return res