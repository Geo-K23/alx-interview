#!/usr/bin/env python3
""" Minimum operations
"""


def minOperations(n):
    """
    Calculate the fewest number of operations needed to result
    in exactly n 'H' characters in the file.
    """
    if n == 1:
        return 0  # Already have 1 'H', no operations needed

    dp = [float('inf')] * (n + 1)
    dp[1] = 0

    for i in range(2, n + 1):
        for j in range(1, i):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)

    return dp[n] if dp[n] != float('inf') else 0