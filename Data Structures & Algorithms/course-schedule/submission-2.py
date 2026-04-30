class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        graph = {i: [] for i in range(numCourses)} 
        for u, v in prerequisites:
            graph[v].append(u)
        
        count = 0
        queue = deque()
        indegrees = [0] * numCourses
        for i in range(numCourses):
            for neighbor in graph[i]:
                indegrees[neighbor] +=1

        for i in range(numCourses):
            if indegrees[i] ==0:
                queue.append(i)
        
        while queue:
            course = queue.popleft()
            count +=1

            for neighbor in graph[course]:
                indegrees[neighbor] -=1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        print(count)
        return count == numCourses



        

