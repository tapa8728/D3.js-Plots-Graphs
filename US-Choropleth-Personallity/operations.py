#operations on the personality data

# Raw data in comma-separated format
f = open("data.txt","r") 	#opens file with name of "data.txt"
lines = f.readlines()

# Step 1: Clean up data by removing spaces between each value
for l in lines:

	tmp1=l.replace(" ","").replace("\n","").split(",")
	try:
		tmp2=int(tmp1[2])+int(tmp1[3])+int(tmp1[4])
	except:
		print "Cnnot be converted into integer"
	tmp1.extend([tmp2])
	print tmp1

#1001, NV, 002, 36,45,81, 52	

#Step 2: Apply formula for O and dump the data in a new file "data_1.txt"
