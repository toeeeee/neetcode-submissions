class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyI = 0
        sellI = 0
        buy = prices[buyI]
        sell = prices[sellI]
        profit = sell - buy
        print(profit)

        n = len(prices)
        for i in range(1,n):
            #print(f"i:{i}")
            cur = prices[i]

            if cur < buy:
                #print('a')
                buy = cur
                buyI = i

            

            if cur > sell:
                #print('b')
                sell = cur
                sellI = i

            #print(sell-buy)

            if sellI >= buyI:
                profit = max(profit, sell-buy)
                if profit <= 0:
                    profit = 0
            else:
                sellI = buyI 
                sell = buy
        
        return profit
        