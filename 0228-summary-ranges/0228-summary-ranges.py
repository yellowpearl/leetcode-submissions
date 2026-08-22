class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        res = []
        i = 0
        j = 0
        while j < len(nums):
            if j:
                if nums[j] - nums[j-1] > 1:
                    if j-1-i > 0:
                        res.append(f'{nums[i]}->{nums[j-1]}')
                    else:
                        res.append(f'{nums[i]}')
                    i = j
            j += 1
        if j-1-i > 0:
            res.append(f'{nums[i]}->{nums[j-1]}')
        else:
            res.append(f'{nums[i]}')
        return res