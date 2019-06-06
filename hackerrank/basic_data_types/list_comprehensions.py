if __name__ == '__main__':
	X = int(raw_input())
	Y = int(raw_input())
	Z = int(raw_input())
	N = int(raw_input())

	cuboid = []
	for i in range(X+1):
		for j in range(Y+1):
			for k in range(Z+1):
				if i+j+k != N:
					cuboid.append([i, j, k])
	#cuboid.append([i, j, k] for (i, j, k) in (range(X), range(Y), range(Z))
	print(cuboid)