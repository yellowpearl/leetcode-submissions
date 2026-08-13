class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sets = []
        curr = []
        def s(i):
            if i == len(nums):
                sets.append(curr.copy())
                return
            curr.append(nums[i])
            s(i+1)
            curr.pop()
            s(i+1)
        s(0)
        return sets
        