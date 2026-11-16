class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price=prices[0]
        max_profit=0

        for count in range(0,len(prices)):
            
            if prices[count]<min_price:
                min_price=prices[count]
            
            if max_profit<prices[count]-min_price:
                max_profit=prices[count]-min_price
            
        return max_profit
