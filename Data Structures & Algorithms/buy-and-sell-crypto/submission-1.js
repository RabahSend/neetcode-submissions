class Solution {
    /**
     * @param {number[]} prices
     * @return {number}
     */
    maxProfit(prices) {
        let profit = 0
        let left = 0
        let right = 0

        while(right < prices.length) {

            if(prices[right] < prices[left]) {
                left = right
            }

            profit = Math.max(profit, prices[right] - prices[left])
            right++
        }

        return profit
    }
}
