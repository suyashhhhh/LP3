# Practical 4 : Write a program to solve a 0-1 Knapsack problem using dynamic programming

# DPP
def knapSack_DP(W, wt, val, n):
	K = [[0 for w in range(W + 1)] for i in range(n + 1)]

	for i in range(n + 1):
		for w in range(W + 1):
			if i == 0 or w == 0:
				K[i][w] = 0
			elif wt[i-1] <= w:
				K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
			else:
				K[i][w] = K[i-1][w]

	return K[n][W]

val = [60, 100, 120]
wt = [10, 20, 30]
W = 50
n = len(val)
print(knapSack_DP(W, wt, val, n))


