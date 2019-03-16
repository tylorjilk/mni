# Better MNISQL Program
# Written by T. Jilk 3-16-2019

"""
Log file format:
bone type (0=femur, 1=tibia, 2=pelvis), side (0=left, 1=right, 2=both)

"""

print("Better MNISQL!")

while(1):
	case = input("Enter 0 to calculate MNIs, 1 to show data, and 2 to enter new data (-1 to end):  ")
	
	if case == -1:
		break;
	
	if case == 0:
		femur_left = 0
		femur_right = 0
		tibia_left = 0
		tibia_right = 0
		pelvis_left = 0
		pelvis_right = 0
		
		# Read each line to get the data from the log file
		datafile = open("mnisql_data.log", "r")
		for line in datafile:
			splitline = line.strip("\n")
			splitline = splitline.split(",")
			# first for femurs
			if int(splitline[0])==0:
				if int(splitline[1])==0:
					femur_left += 1
				else:
					femur_right += 1
			# second are tibias
			if int(splitline[0])==1:
				if int(splitline[1])==0:
					tibia_left += 1
				else:
					tibia_right += 1
			# third is the pelvis
			if int(splitline[0])==2:
				if int(splitline[1])==0:
					pelvis_left += 1
				elif int(splitline[1])==1:
					pelvis_right += 1
				else:
					pelvis_left += 1
					pelvis_right += 1
		datafile.close()
		
		# Next calculate the MNIs
		femur_mni = max(femur_left, femur_right)
		tibia_mni = max(tibia_left, tibia_right)
		pelvis_mni = max(pelvis_left, pelvis_right)
		
		# Write this to a log file
		f = open("mnisql_mni.txt", "w")
		f.write("MNI Data:\n")
		print("\nMNI Data:")
		f.write("Femurs: " + str(femur_mni) + " individuals\n")
		print("Femurs: " + str(femur_mni) + " individuals")
		f.write("Tibias: " + str(tibia_mni) + " individuals\n")
		print("Tibias: " + str(tibia_mni) + " individuals")
		f.write("Pelvis: " + str(pelvis_mni) + " individuals\n")
		print("Pelvis: " + str(pelvis_mni) + " individuals\n")
		f.close()

	if case == 1:
		datafile = open("mnisql_data.log", "r")
		print ""
		for line in datafile:
		
			line = line.strip("\n")
			linesplit = line.split(",")
			bone = int(linesplit[0])
			side = int(linesplit[1])
			boneString = ""
			sideString = ""
			if bone == 0:
				boneString += " Femur"
			elif bone == 1:
				boneString += " Tibia"
			else:
				boneString += " Pelvis"
			
			if side == 0:
				sideString += "Left"
			elif side == 1:
				sideString += "Right"
			else:
				sideString += "Both"
			
			print(sideString + boneString)
		print("")
		datafile.close()

	if case == 2:
		bone = input("What bone? 0 = femur, 1 = tibia, 2 = pelvis:  ")
		side = input("What side? 0 = left, 1 = right, 2 = both:  ")
		newlogentry = str(bone) + "," + str(side) + "\n"
		datafile = open("mnisql_data.log", "a")
		datafile.write(newlogentry)
		datafile.close()
		print("New bone added!\n")
