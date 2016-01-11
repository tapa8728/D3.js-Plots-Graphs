import json
""" Operations on the personality data to convert it to a JSON file of format

	Required JSON Format- 
	{
		"NV": {"extraversion": "0", "neuroticism": "0", "agreeableness": "0", "conscientiousness": "0", "gfgid": "1001", "openness": "38"}, 
		"CA": {"extraversion": "0", "neuroticism": "0", "agreeableness": "0", "conscientiousness": "0", "gfgid": "2001", "openness": 56}, 
		"TX": {"extraversion": "0", "neuroticism": "0", "agreeableness": "0", "conscientiousness": "0", "gfgid": "3001", "openness": 366}
	}
	Converted data stored in data_1.json file in same folder
	"""
#Transform Matrix

# Function to format the data in required format
def dump(a):
    result =  '"'+a[1]+'" : {"id": '+ str(a[0])+', "openness" : '+ str(a[7])+', "conscientiousness" : '+str(a[8])+', "extraversion": '+str(a[9])+', "agreeableness" : '+str(a[10])+', "neuroticism" : '+str(a[11])+'}'
    return result

# Raw data in comma-separated format
f = open("data.txt","r") 	#opens file with name of "data.txt"
fo = open("data_1.json", "w") #'w' mode will create a new file in the directory

lines = f.readlines()
mylist= []

mystring = "{"

# Step 1: Clean up data by removing spaces between each value
for l in lines:
	
	value=l.replace(" ","").replace("\n","").split(",")
	for i in range(2, 7):
		try:
			value[i] = int(value[i])	#Replace corrupt data of non-integer type to 0
		except:
			value[i] = 0;

	# Value 1 : GFGid
	# Value 2 : Location(State)
	# Values available for computation: 2,3,4,5,6
	# Step 2: Apply formula for Openness 7th position		
	tmp2=int(value[2])+int(value[3])+int(value[4])
	value[7] = tmp2
	# Step 3: Apply formula for conscientiousness 8th position
	tmp3 = 2*int(value[2]) + int(value[3])
	value[8] = tmp3
	# Step 4: Apply formula for extraversion 9th position	
	tmp4 = int(value[4])+int(value[5])+int(value[6])
	value[9] = tmp4
	# Step 5: Apply formula for agreeableness 10th position	
	tmp5 = int(value[2])+int(value[4])+int(value[6])
	value[10] = tmp5
	# Step 6: Apply formula for neuroticism	11th position
	tmp6 = 3*int(value[2])	
	value[11] = tmp6
	# Step 7: Apply formula for Normalization	

	json_str = dump(value)	# Information string
	mylist.append(json_str) # Add it to a list

mystring = str(mylist)	# Convert the list of information to a string
blah = mystring.replace("'", "").replace("[","{").replace("]","}")	# Clean up string to suit the format for Datamaps
print "Cleaned up list ----> ", blah
fo.write(blah) # Final formatted string stored in data_1.json

