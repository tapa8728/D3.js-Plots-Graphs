#operations on the personality data

# Raw data in comma-separated format
f = open("data.txt","r") 	#opens file with name of "data.txt"
lines = f.readlines()

# Step 1: Clean up data by removing spaces between each value
print "lets clean up the data"
for l in lines:
	print l
	new_line = str.replace(str(l),' ','')
	print new_line

print "File after replacing spaces"

	

#Step 2: Apply formula for O and dump the data in a new file "data_1.txt"
