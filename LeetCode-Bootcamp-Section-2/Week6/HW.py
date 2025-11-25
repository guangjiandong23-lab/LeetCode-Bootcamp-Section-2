# Binary Tree Right Side View
class Solution:
    def rightSideView(self, root: TreeNode) -> list[int]:
        res = []
        def dfs(node, depth):
            if not node:
                return
            if depth == len(res):
                res.append(node.val)

            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        dfs(root, 0)
        return res
    
# Rotting oranges
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh = 0
        queue = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    queue.append((i, j))
    
        if fresh == 0:
            return 0
        
        time = 0
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while queue:
            level_size = len(queue)
            for _ in range(level_size):
                x, y = queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1:
                        grid[nx][ny] = 2 
                        fresh -= 1
                        queue.append((nx, ny))

            time += 1
        

        return time - 1 if fresh == 0 else -1
# Course Schedule II 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Build adjacency list and in-degree array
        adj = defaultdict(list)
        in_degree = [0] * numCourses
        
        for course, prereq in prerequisites:
            adj[prereq].append(course) 
            in_degree[course] += 1      
        
        #Initialize queue with courses having no prerequisites (in-degree = 0)
        queue = deque()
        for course in range(numCourses):
            if in_degree[course] == 0:
                queue.append(course)
        
        #Process nodes to get topological order
        topo_order = []
        while queue:
            current = queue.popleft()
            topo_order.append(current)
            
            for neighbor in adj[current]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        #
        # Check if all courses are included (no cycles)
        return topo_order if len(topo_order) == numCourses else []