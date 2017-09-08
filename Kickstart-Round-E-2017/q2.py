from collections import Counter
import math

def nCr(n,r):
	f = math.factorial
	return f(n) // f(r) // f(n-r)

def solve(lengths):
	count = Counter(lengths)
	sortedLengths = sorted(list(count.keys()))
	lengthsTwo = [length for length in sortedLengths if count[length] >= 2]
	lengthsThree = [length for length in sortedLengths if count[length] >= 3]
	prefixSum = {}
	currentSum = 0
	for length in sortedLengths:
		currentSum += count[length]
		prefixSum[length] = currentSum
	for i in range(len(sortedLengths)):
		length1 = sortedLengths[i]
		numberIndex = 0
		for j in range(len(sortedLengths)):
			length2 = sortedLengths[j]
			key = length1 * 2 + length2
			if key in prefixSum: continue
			length2 = sortedLengths[j]
			while numberIndex < len(sortedLengths)-1 and key > sortedLengths[numberIndex]:
				numberIndex += 1
			prefixSum[key] = prefixSum[sortedLengths[numberIndex]]
	result = 0
	for length in lengthsThree:
		result += nCr(count[length], 3) * (prefixSum[3*length] - count[length])
	for length in lengthsTwo:
		for otherLength in sortedLengths:
			if otherLength == length: continue
			key = 2*length+otherLength
			longestSides = prefixSum[key] - count[key] - prefixSum[otherLength]
			if length > otherLength:
				longestSides -= count[length]
			result += nCr(count[length], 2) * count[otherLength] * longestSides
	return result

with open('q2.in', 'r') as inputFile:
	lines = inputFile.readlines()[2::2]
	inputs = [list(map(int, line.split(' '))) for line in lines]
	results = [None]*len(inputs)
	for i, lengths in enumerate(inputs):
		results[i] = "Case #" + str(i+1) + ": " + str(solve(lengths)) + "\n"
	with open('q2.out', 'w') as outputFile:
		outputFile.writelines(results)