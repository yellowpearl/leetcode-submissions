import heapq
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # Буду решать через дп, справа налево буду считать сколько значений справа больше текущего числа, буду идти до первого O(n**2) O(n)

        # Фикс - нужно идти до максимального, а не до первого
        res = 0
        dp = [0] * len(nums)
        for i in range(len(nums)-1, -1, -1):
            n = nums[i]
            r = 1
            cond = []
            for j in range(i+1, len(nums)):
                if nums[j] > nums[i]:
                    cond.append(dp[j])
            if cond:
                r += max(cond)
            res = max(res, r)
            dp[i] = r
        return res
        