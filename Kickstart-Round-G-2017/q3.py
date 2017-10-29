def getMinOfSubmatrix(matrix):
	minOfSubmatrix = {}
	n = len(matrix)
	m = len(matrix[0])
	for top in range(n):
		for left in range(m):
			min_of_first_col = matrix[top][left]
			for bottom in range(top, n):
				min_of_first_col = min(min_of_first_col, matrix[bottom][left])
				current_min = min_of_first_col
				for right in range(left, m):
					current_min = min(current_min, min([matrix[row][right] for row in range(top, bottom+1)]))
					minOfSubmatrix[(top, bottom, left, right)] = current_min
	return minOfSubmatrix

def maxCoinOfSubmatrix(matrix, top, bottom, left, right, minOfSubmatrix, memo):
	if top == bottom and left == right:
		return 0
	if (top, bottom, left, right) in memo:
		return memo[(top, bottom, left, right)]
	current_max = 0
	for row in range(top, bottom):
		current_max = max(current_max, maxCoinOfSubmatrix(matrix, top, row, left, right, minOfSubmatrix, memo) + maxCoinOfSubmatrix(matrix, row+1, bottom, left, right, minOfSubmatrix, memo))
	for col in range(left, right):
		current_max = max(current_max, maxCoinOfSubmatrix(matrix, top, bottom, left, col, minOfSubmatrix, memo)+ maxCoinOfSubmatrix(matrix, top, bottom, col+1, right, minOfSubmatrix, memo))
	current_max += minOfSubmatrix[(top, bottom, left, right)]
	memo[(top, bottom, left, right)] = current_max
	return current_max

def maxCoin(matrix):
	n = len(matrix)
	m = len(matrix[0])
	minOfSubmatrix = getMinOfSubmatrix(matrix)
	memo = {}
	return maxCoinOfSubmatrix(matrix, 0, n-1, 0, m-1, minOfSubmatrix, memo)

with open('q3.in', 'r') as inputFile:
	lines = inputFile.readlines()

N = int(lines[0])
results = [None]*N
case = 1
startLine = 1
while case <= N:
	print(case)
	n, m = tuple(map(int, lines[startLine].split(' ')))
	matrix = [None]*n
	for i in range(n):
		matrix[i] = list(map(int, lines[startLine+i+1].split(' ')))
	results[case-1] = "Case #" + str(case) + ": " + str(maxCoin(matrix)) + "\n"
	case += 1
	startLine += n+1

with open('q3.out', 'w') as outputFile:
	outputFile.writelines(results)