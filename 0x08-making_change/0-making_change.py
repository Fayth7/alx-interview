#!/usr/bin/python3
"""Change making module.
"""


def makeChange(coins, total):
    def helper(target, memo):
        if target < 0:
            return float('inf')
        if target == 0:
            return 0
        if target in memo:
            return memo[target]

        min_coins = float('inf')
        for coin in coins:
            min_coins = min(min_coins, 1 + helper(target - coin, memo))

        memo[target] = min_coins
        return min_coins

    if total <= 0:
        return 0

    result = helper(total, {})
    return result if result != float('inf') else -1


# Test cases
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1
