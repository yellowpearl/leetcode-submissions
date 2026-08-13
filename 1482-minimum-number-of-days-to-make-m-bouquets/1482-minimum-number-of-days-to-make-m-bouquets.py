class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        l = 1
        r = max(bloomDay)

        while l < r:
            mid = (l+r) // 2

            curr = 0
            bouq = 0
            for i in bloomDay:
                if i <= mid:
                    curr += 1
                    if curr == k:
                        bouq += 1
                        curr = 0
                else:
                    curr = 0
            
            if bouq < m:
                l = mid + 1
            else:
                r = mid
        
        curr = 0
        bouq = 0
        for i in bloomDay:
            if i <= l:
                curr += 1
                if curr == k:
                    bouq += 1
                    curr = 0
            else:
                curr = 0
            
        if bouq < m:
            return -1
        else:
            return l
        
