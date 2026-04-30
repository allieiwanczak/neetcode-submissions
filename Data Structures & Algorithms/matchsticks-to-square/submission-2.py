class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # perimeter is sum so side is perimeter/4
        # need to find pair that match up to side
        if sum(matchsticks) % 4 != 0:
            return False

        side = sum(matchsticks)//4
        used= [False] * len(matchsticks)

        def backtrack(sides, start_i, side_i):
            if side_i == 4:
                return True
            
            if sides[side_i] == side:
                return backtrack(sides, 0, side_i+1)

            for i in range(start_i, len(matchsticks)):
                if sides[side_i]+matchsticks[i] <= side and used[i] == False:
                    used[i] = True
                    sides[side_i] += matchsticks[i]

                    if backtrack(sides, i+1, side_i):
                        return True
                    
                    used[i] = False
                    sides[side_i] -= matchsticks[i]
            return False
        
        return backtrack([0, 0, 0, 0],0,0)
          