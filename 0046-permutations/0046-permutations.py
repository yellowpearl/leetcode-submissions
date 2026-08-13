class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []
        used = [False] * len(nums)
        
        def s():
            if len(path) == len(nums):
                res.append(path.copy())
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                
                used[i] = True
                path.append(nums[i])
                s()
                used[i] = False
                path.pop()
        s()
        return res

            

        