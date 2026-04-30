class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = {i: [] for i in range(numCourses)} 
        for u, v in prerequisites:
            graph[v].append(u)
        
        order =[]
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
            order.append(course)

            for neighbor in graph[course]:
                indegrees[neighbor] -=1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)

        return order if len(order) == numCourses else []

