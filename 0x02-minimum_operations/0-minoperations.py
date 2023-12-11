#!/usr/bin/python3


''' 
    A module that returns the minimum Operations it takes to
    get to n characters.
'''


def minOperations(n):
    if n <= 1:
        return 0

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(2, i + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
    
    return dp[n] if dp[n] != float('inf') else 0

# Example usage
if __name__ == "__main__":
    n1 = 4
    print(f"Min number of operations to reach {n1} characters: {minOperations(n1)}")

    n2 = 12
    print(f"Min number of operations to reach {n2} characters: {minOperations(n2)}")
