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
                if bt(start+1, nr, nc):
                    return True
                visit.remove((nr, nc))
            return False
        
        ans = []
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == word[0]:
                    visit.add((r,c))
                    if bt(1, r, c):
                        return True
                    visit.remove((r,c))
        return False