import time

sudoku = open("sudoku.txt", "r")
sudoku_final = []
sudokulist = sudoku.readlines()
for array in sudokulist:
	sudoku_final.append(array.rstrip())

location0 = {}
location1 = {"1":"0,0","2":"0,0","3":"0,0","4":"0,0","5":"0,0","6":"0,0","7":"0,0","8":"0,0","9":"0,0"}
location2 = {"1":"0,0","2":"0,0","3":"0,0","4":"0,0","5":"0,0","6":"0,0","7":"0,0","8":"0,0","9":"0,0"}
location3 = {"1":"0,0","2":"0,0","3":"0,0","4":"0,0","5":"0,0","6":"0,0","7":"0,0","8":"0,0","9":"0,0"}
location4 = {"1":"0,0","2":"0,0","3":"0,0","4":"0,0","5":"0,0","6":"0,0","7":"0,0","8":"0,0","9":"0,0"}
location5 = {"1":"0,0","2":"0,0","3":"0,0","4":"0,0","5":"0,0","6":"0,0","7":"0,0","8":"0,0","9":"0,0"}
location6 = {"1":"0,0","2":"0,0","3":"0,0","4":"0,0","5":"0,0","6":"0,0","7":"0,0","8":"0,0","9":"0,0"}
location7 = {"1":"0,0","2":"0,0","3":"0,0","4":"0,0","5":"0,0","6":"0,0","7":"0,0","8":"0,0","9":"0,0"}
location8 = {"1":"0,0","2":"0,0","3":"0,0","4":"0,0","5":"0,0","6":"0,0","7":"0,0","8":"0,0","9":"0,0"}
location9 = {"1":"0,0","2":"0,0","3":"0,0","4":"0,0","5":"0,0","6":"0,0","7":"0,0","8":"0,0","9":"0,0"}

location_dict = {
	"0": location0,
	"1": location1,
	"2": location2,
	"3": location3,
	"4": location4,
	"5": location5,
	"6": location6,
	"7": location7,
	"8": location8,
	"9": location9
}

count_x = 1
count_y = 1
for array in sudoku_final:
	for number in array:
		if count_y < 4 and count_x < 4:
			if number != "0":
				location_dict.get(number)["1"] = "" + str(count_x) + "," + str(count_y)
			else:
				location_dict.get(number)["" + str(count_x) + "," + str(count_y)] = "1"
		elif count_y < 4 and count_x < 7:
			if number != "0":
				location_dict.get(number)["2"] = "" + str(count_x) + "," + str(count_y)
			else:
				location_dict.get(number)["" + str(count_x) + "," + str(count_y)] = "2"
		elif count_y < 4 and count_x > 6:
			if number != "0":
				location_dict.get(number)["3"] = "" + str(count_x) + "," + str(count_y)
			else:
				location_dict.get(number)["" + str(count_x) + "," + str(count_y)] = "3"
		elif count_y < 7 and count_x < 4:
			if number != "0":
				location_dict.get(number)["4"] = "" + str(count_x) + "," + str(count_y)
			else:
				location_dict.get(number)["" + str(count_x) + "," + str(count_y)] = "4"
		elif count_y < 7 and count_x < 7:
			if number != "0":
				location_dict.get(number)["5"] = "" + str(count_x) + "," + str(count_y)
			else:
				location_dict.get(number)["" + str(count_x) + "," + str(count_y)] = "5"
		elif count_y < 7 and count_x > 6:
			if number != "0":
				location_dict.get(number)["6"] = "" + str(count_x) + "," + str(count_y)
			else:
				location_dict.get(number)["" + str(count_x) + "," + str(count_y)] = "6"
		elif count_y > 6 and count_x < 4:
			if number != "0":
				location_dict.get(number)["7"] = "" + str(count_x) + "," + str(count_y)
			else:
				location_dict.get(number)["" + str(count_x) + "," + str(count_y)] = "7"
		elif count_y > 6 and count_x < 7:
			if number != "0":
				location_dict.get(number)["8"] = "" + str(count_x) + "," + str(count_y)
			else:
				location_dict.get(number)["" + str(count_x) + "," + str(count_y)] = "8"
		elif count_y > 6 and count_x > 6:
			if number != "0":
				location_dict.get(number)["9"] = "" + str(count_x) + "," + str(count_y)
			else:
				location_dict.get(number)["" + str(count_x) + "," + str(count_y)] = "9"

		count_x = count_x + 1

	count_y = count_y + 1
	count_x = 1

blanks_exist = 1

while blanks_exist:
	delete = []
	for coord in location_dict.get("0"):
		possible = []
		target_x, target_y = coord.split(",")
		for z in range(1,10):
			fail = 0
			for index in location_dict.get(str(z)):
				set_x, set_y = location_dict.get(str(z)).get(index).split(",")
				#print ("%s, %s : %s, %s" % (set_x, set_y, target_x, target_y))  ################################################
				
				if set_x == target_x or set_y == target_y:
					fail = 1
					#print ("value has equal x or y")
					break

				#print ("%s, %s" % (location_dict.get("0").get(coord), index))  #################################################

				if location_dict.get("0").get(coord) == index and set_x != "0" and set_y != "0":
					fail = 1
					#print ("value in same grid")
					#time.sleep(2)
					break

			if fail != 1:
				#print (z)
				#time.sleep(1)
				possible.append(z)
		#print("enter possible here")
		if len(possible) == 1:
			#print ("correct!")
			#time.sleep(2)
			location_dict.get(str(possible[0]))[location_dict.get("0").get(coord)] = coord
			delete.append(coord)

	for item in delete:
		del location_dict.get("0")[item]

	if len(location_dict.get("0")) == 0:
		blanks_exist = 0


output1 = [0,0,0,0,0,0,0,0,0]
output2 = [0,0,0,0,0,0,0,0,0]
output3 = [0,0,0,0,0,0,0,0,0]
output4 = [0,0,0,0,0,0,0,0,0]
output5 = [0,0,0,0,0,0,0,0,0]
output6 = [0,0,0,0,0,0,0,0,0]
output7 = [0,0,0,0,0,0,0,0,0]
output8 = [0,0,0,0,0,0,0,0,0]
output9 = [0,0,0,0,0,0,0,0,0]

output_dict = {
	"1": output1,
	"2": output2,
	"3": output3,
	"4": output4,
	"5": output5,
	"6": output6,
	"7": output7,
	"8": output8,
	"9": output9
}

for a in range(1,10):
	for b in range(1,10):
		x, y = location_dict.get(str(a)).get(str(b)).split(",")
		output_dict.get(y)[int(x) - 1] = a

for out in output_dict:
	print (output_dict.get(out))
