import networkx as nx

def solve(r, b):
	n = len(r)
	G = nx.Graph()
	for i in range(n-1):
		for j in range(i+1, n):
			length = min(r[i]^b[j], r[j]^b[i])
			G.add_edge(i, j, weight=length)
	mst = nx.minimum_spanning_tree(G)
	return sum([x[2]['weight'] for x in mst.edges(data=True)])

with open('q2.in', 'r') as inputFile:
	lines = inputFile.readlines()

n = int(lines[0])
results = [None]*n
case = 1
for i in range(1, len(lines), 3):
	r = list(map(int, lines[i+1].split(' ')))
	b = list(map(int, lines[i+2].split(' ')))
	results[case-1] = "Case #" + str(case) + ": " + str(solve(r, b)) + "\n"
	case += 1

with open('q2.out', 'w') as outputFile:
	outputFile.writelines(results)