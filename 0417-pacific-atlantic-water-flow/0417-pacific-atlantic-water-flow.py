from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        p_s = [
            (-1, i) for i in range(len(heights[0]))
        ] + [
            (i, -1) for i in range(len(heights))
        ]

        a_s = [
            (len(heights), i) for i in range(len(heights[0]))
        ] + [
            (i, len(heights[0])) for i in range(len(heights))
        ]

        neigbours = [
            [0, 1],
            [0, -1],
            [1, 0],
            [-1, 0],
        ]
        
        def bfs(starts):
            visit = set()
            q = deque()
            for r, c in starts:
                q.append((r, c, float('-inf')))
                visit.add((r, c))
                
                while q:
                    cr, cc, cl = q.popleft()

                    for dr, dc in neigbours:
                        nr = cr + dr
                        nc = cc + dc

                        if (
                            (nr, nc) in visit
                        ) or (
                            min(nr, nc) < 0
                        ) or (
                            nr >= len(heights)
                        ) or (
                            nc >= len(heights[0])
                        ) or (
                            heights[nr][nc] < cl
                        ):
                            continue
                        
                        visit.add((nr, nc))
                        q.append((nr, nc, heights[nr][nc]))
            return visit
        
        visit_p = bfs(p_s)
        visit_a = bfs(a_s)
        return [[r, c] for r, c in visit_p if (r, c) in visit_a]