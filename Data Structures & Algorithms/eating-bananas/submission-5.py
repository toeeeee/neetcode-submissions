from math import ceil as ceil 

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def getTime(rate, piles):
            time = 0.0
            for amt in piles:
                time += ceil(amt/rate)
            return time


        # Our index represents the rate of eating
        i = 1
        j = max(piles)
        minimum = j

        while i <= j:
            m = (i+j)//2
            time = getTime(m,piles)
            if time <= h:
                minimum = m
                j = m - 1
            else:
                i = m + 1

        return minimum
