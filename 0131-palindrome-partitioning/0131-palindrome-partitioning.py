class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        res = []
        curr = []

        def bt(start):
            if start >= len(s):
                res.append(curr.copy())
            
            for i in range(start+1, len(s)+1):
                if s[start:i] == s[start:i][::-1]:
                    curr.append(s[start:i])
                    bt(i)
                    curr.pop()
        bt(0)
        return res

                