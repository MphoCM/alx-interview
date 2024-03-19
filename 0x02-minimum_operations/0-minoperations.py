#!/usr/bin/python3

def minOperations(n):
    if n <= 1:
        return 0

    # Initialize a list to store the minimum operations required for each number
    dp = [0] * (n + 1)

    for i in range(2, n + 1):
        dp[i] = i  # Start with the maximum possible operations, which is i

        # Find the factors of i and update dp[i] with the minimum operations
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                dp[i] = min(dp[i], dp[j] + i // j)
                dp[i] = min(dp[i], dp[i // j] + j)

    return dp[n]

# Example usage:
if __name__ == "__main__":
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

