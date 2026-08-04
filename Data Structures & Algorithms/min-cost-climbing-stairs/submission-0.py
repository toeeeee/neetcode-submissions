class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        mincosts = list(range(len(cost)+1)) # index represents the cost to get to that floor...
        mincosts[0], mincosts[1] = 0, 0 

        for i in range(2,len(mincosts)):
            # min cost to get to current step is the 
            # minimum between the last step + min cost of getting there
            # or two steps ago + min cost of getting there
            #print(f"two choices to get to {i}th floor is{cost[i-1]}+{mincosts[i-1]},{cost[i-2]}+{mincosts[i-2]}")
            mincosts[i] = min(cost[i-1]+mincosts[i-1], cost[i-2]+mincosts[i-2])
        
        return mincosts[-1]


        