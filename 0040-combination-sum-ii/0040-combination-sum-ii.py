class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = set()
        curr = []
        curr_s = 0

        def bt(start, curr_s):
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                curr_s += candidates[i]
                curr.append(candidates[i])
                if curr_s < target:
                    bt(i+1, curr_s)
                    curr.pop()
                    curr_s -= candidates[i]
                elif curr_s == target:
                    res.add(tuple(curr))
                    curr.pop()
                    curr_s -= candidates[i]
                    return
                else:
                    curr.pop()
                    curr_s -= candidates[i]
                    return
        bt(0, curr_s)
        return [list(l) for l in res]
            