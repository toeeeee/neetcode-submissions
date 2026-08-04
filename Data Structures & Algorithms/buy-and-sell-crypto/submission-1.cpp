class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int buy = prices[0];
        int buyI = 0;
        int sell = prices[1];
        int sellI = 1;
        profit = sell - buy;

        for (int i = 1; i < prices.size(); ++i) {
            if (prices[i] < buy) { buy = prices[i]; buyI = i; }
            if (sellI < buyI) { sell = prices[i]; sellI = i; }
            if (prices[i] > sell) { sell = prices[i]; sellI = i; }
            if (buyI <= sellI && (sell - buy > profit)) { profit = sell - buy; }
        }

        profit = (profit > 0) ? profit : 0;
        return profit; 
    }
};
