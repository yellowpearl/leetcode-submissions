import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Использую sliding window, буду расширять окно пока не достигну длины k, потом расширять на 1 и сокращать на 1(через while r-l+1 > k) 
        # Брутфорс - считать максимум в каждом отдельном окне - O(n**2) O(n)
        # Оптимизированный вариант - держим макс кучу, когда окно достигает размера k берем из кучи максимум и записываем в ответ, если на куче лежит индекс который не входит в окно то просто отбрасываем элемент - O(n logn) O(n)
        res = []
        h = []
        l = 0
        for r in range(len(nums)):
            heapq.heappush_max(h, (nums[r], r))

            while r-l+1 > k:
                l += 1
            
            if r-l+1 == k:
                while h:
                    val, idx = h[0]
                    if idx < l:
                        heapq.heappop_max(h)
                    else:
                        res.append(val)
                        break
        return res
