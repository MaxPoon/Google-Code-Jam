from collections import defaultdict
def solve(s):
	length = len(s)
	dp = [[None]*(length//2+1) for _ in range(length)]
	# dp[i][j] means the minimum number the of operations to get s[:i+1]
	# while the last j characters are from clipboard
	dp[0][0] = 1
	dpMin = [1]*length
	# dpMin[i] is the min value of dp[i]
	occurence = defaultdict(list)
	for i in range(1, length):
		dp[i][0] = dpMin[i-1] + 1
		for j in range(2, i+2):
			copied = s[i-j+1:i+1]
			if j <= (i+1)//2:
				lastOccurenceIndex = None
				for index in reversed(occurence[copied]):
					if index <= i-j:
						lastOccurenceIndex = index
						break
				if lastOccurenceIndex:
					dp[i][j] = dpMin[i-j] + 2 #copy and paste
					if dp[lastOccurenceIndex][j] != None:
						dp[i][j] = min(dp[i][j], dp[lastOccurenceIndex][j]+(i-j-lastOccurenceIndex)+1)
			occurence[copied].append(i)
		dpMin[i] = min([n for n in dp[i] if n != None])
	return dpMin[-1]

with open('q1.in', 'r') as inputFile:
	lines = inputFile.readlines()

n = int(lines[0])
results = [None]*n
for i, s in enumerate(lines[1:]):
	results[i] = "Case #" + str(i+1) + ": " + str(solve(s[:-1])) + "\n"

with open('q1.out', 'w') as outputFile:
	outputFile.writelines(results)
