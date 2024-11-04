# Practical 4 : Write a program to solve a 0-1 Knapsack problem using branch and bound strategy

class ItemValue:
	def __init__(self, wt, val, ind):
		self.wt = wt
		self.val = val
		self.ind = ind
		self.cost = val / wt 

	def __lt__(self, other):
		return self.cost < other.cost

def knapSack_BB(wt, val, capacity):
	iVal = []
	for i in range(len(wt)):
		iVal.append(ItemValue(wt[i], val[i], i))
	iVal.sort(reverse=True)

	totalValue = 0
	for i in iVal:
		curWt = int(i.wt)
		curVal = int(i.val)
		if capacity - curWt >= 0:
			capacity -= curWt
			totalValue += curVal
		else:
			fraction = capacity / curWt
			totalValue += curVal * fraction
			capacity = int(capacity - (curWt * fraction))
			break

	return totalValue

val = [60, 100, 120]
wt = [10, 20, 30]
capacity = 50
print(knapSack_BB(wt, val, capacity))
