import csv
array1=[]
with open("example.csv", "r+") as csvf:
	read = csv.DictReader(csvf)
	for row in read:
		array1.append((row['first'], row['last']))
print array1[1]
print array1[2]
print array1[0]

