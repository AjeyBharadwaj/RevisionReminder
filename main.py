import sys
import math
import pdb

#python main.py <no.days> <max.repitition>

def next_day(cur_date):
	return cur_date*2
	#return int(math.pow(2, cur_date))

if len(sys.argv) != 3:
	print("python main.py <no.days> <max.repitition>")
else:
	no_days = int(sys.argv[1])
	max_repitition = int(sys.argv[2])

	total_days = int(math.pow(2, max_repitition))

	data = {}

	for i in range(1, no_days+total_days):
		data[f"Day {i}"] = []

	for i in range(1, no_days+1):
		data[f"Day {i}"].append(f"Day {i} : 1 time")
		index = i
		for j in range(1, max_repitition):
			index = index + next_day(j)
			data[f"Day {index}"].append(f"Day {i} : {j+1} time")

	for i in data:
		if len(data[i]) != 0:
			print(f"{i} : {data[i]}")


