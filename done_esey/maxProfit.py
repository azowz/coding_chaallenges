from typing import List

def maxProfit(prices: List[int]) -> int:
    if not prices:
        return 0

    n = len(prices)
    profit_one = [0] * n  # Max profit achievable with one transaction up to each day
    profit_two = [0] * n  # Max profit achievable with the second transaction starting from each day

    # Calculate max profit with the first transaction up to each day
    min_price = prices[0]
    for i in range(1, n):
        min_price = min(min_price, prices[i])
        profit_one[i] = max(profit_one[i - 1], prices[i] - min_price)

    # Calculate max profit with the second transaction starting from each day to the end
    max_price = prices[-1]
    for i in range(n - 2, -1, -1):
        max_price = max(max_price, prices[i])
        profit_two[i] = max(profit_two[i + 1], max_price - prices[i])

    # Combine the maximum profits from both transactions
    max_profit = 0
    for i in range(n):
        max_profit = max(max_profit, profit_one[i] + profit_two[i])

    return max_profit

prices = [1, 2, 3, 4, 5]
print(maxProfit(prices))  # Expected output: 6
