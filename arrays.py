import csv
import random
array1=[]
with open("example.csv", "r+") as csvf:
	read = csv.DictReader(csvf)
	for row in read:
		array1.append((row['first'], row['last']))
for i in array1:
	itemsInarray=len(array1)-1
	print array1[random.randint(0,itemsInarray)]

