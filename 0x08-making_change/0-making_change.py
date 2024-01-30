#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
     """Determines the fewest number of coins needed to meet a given
    amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0

    # Initialize an array to store the minimum number of coins for each value from 0 to total
    dp = [float('inf')] * (total + 1)

    # There are 0 coins needed to make change for 0
    dp[0] = 0

    # Iterate through each coin and update the dp array
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    # If the value at dp[total] is still infinity, it means it's not possible to make change
    return dp[total] if dp[total] != float('inf') else -1

# Test cases
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
