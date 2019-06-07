with open("/home/tstone10/catkin_ws/some.txt", "r") as filestream:
	for line in filestream:
		currentline = line.rstrip('\n').split(",")
		print currentline
