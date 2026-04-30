class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = {i: [] for i in range(n)}
        for u,v in edges:
            graph[v].append(u)
            graph[u].append(v)

        visited = set()
        count = 0

        def dfs(node,visited):
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor,visited)
            

        for node in range(n):
            if node not in visited:
                count+=1
                dfs(node,visited)

        return count