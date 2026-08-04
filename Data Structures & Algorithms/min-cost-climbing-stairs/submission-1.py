class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n =len(cost)
        mincosts = [0]*(n+1) # index represents the cost to get to that floor...

        for i in range(2,n+1):
            # min cost to get to current step is the 
            # minimum between the last step + min cost of getting there
            # or two steps ago + min cost of getting there
            #print(f"two choices to get to {i}th floor is{cost[i-1]}+{mincosts[i-1]},{cost[i-2]}+{mincosts[i-2]}")
            mincosts[i] = min(cost[i-1]+mincosts[i-1], cost[i-2]+mincosts[i-2])
        
        return mincosts[n]


        