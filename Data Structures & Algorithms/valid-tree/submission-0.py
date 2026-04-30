class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        
        graph = {i:[] for i in range(n)}
        for u,v in edges:
            graph[v].append(u)
            graph[u].append(v)

        def dfs(node,visited):
            visited.add(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor,visited)
            
            return visited
        visited = dfs(0,set())
        
        return len(visited)==n