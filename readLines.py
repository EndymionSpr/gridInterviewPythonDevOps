file1 = open('myFile.txt', 'r')
Lines = file1.readlines()

for line in Lines:
    temp = line.split()
		if int(temp[0]) > 200:
			print(temp[0],temp[1], temp[3])
