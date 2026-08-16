class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        neigbours = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]
        visit = set()

        def bt(start, r, c):
            if start == len(word):
                return True
            ans = []
            for dr, dc in neigbours:
                nr = r+dr
                nc = c+dc

                if (
                    min(nr, nc) < 0
                ) or (
                    nr == len(board)
                ) or (
                    nc == len(board[0])
                ) or (
                    board[nr][nc] != word[start]
                ) or (
                    (nr, nc) in visit
                ):
                    continue
                visit.add((nr, nc))
                ans.append(bt(start+1, nr, nc))
                visit.remove((nr, nc))
            return any(ans)
        
        ans = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visit.add((r,c))
                    ans.append(bt(1, r, c))
                    visit.remove((r,c))
        return any(ans)