class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_idx = 0
        max_idx = 0

        best_val = 0
        for i in range(len(prices)):
            if prices[i] > prices[max_idx]:
                max_idx = i
                continue

            if prices[i] < prices[min_idx]:
                best_val = max(best_val, prices[max_idx] - prices[min_idx])
                min_idx = i
                max_idx = i
                continue

        best_val = max(best_val, prices[max_idx] - prices[min_idx])

        return best_val