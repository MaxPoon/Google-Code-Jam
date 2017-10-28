def remainderOfPower(a, n, p):
	if n == 0:
		return 1
	half_power = remainderOfPower(a, n//2, p)
	half_power_sq = (half_power  * half_power) % p
	if n % 2 == 0:
		return half_power_sq
	else:
		return (half_power_sq * a) % p

def remainderOfPowerOfFactorial(a, n, p):
	result = a%p
	for i in range(2, n):
		result = remainderOfPower(result, i, p)
	return result

with open('q1.in', 'r') as inputFile:
	lines = inputFile.readlines()

n = int(lines[0])
results = [None]*n
for i, s in enumerate(lines[1:]):
	a, n, p = tuple(map(int, s.split(' ')))
	results[i] = "Case #" + str(i+1) + ": " + str(remainderOfPowerOfFactorial(a, n, p)) + "\n"

with open('q1.out', 'w') as outputFile:
	outputFile.writelines(results)