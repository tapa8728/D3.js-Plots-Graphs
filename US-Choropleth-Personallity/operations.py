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
	
	tmp1=l.replace(" ","").replace("\n","").split(",")
	for i in range(2, 6):
		try:
			tmp1[i] = int(tmp1[i])	#Replace corrupt data of non-integer type to 0
		except:
			tmp1[i] = 0;

	# Step 2: Apply formula for Openness		
	tmp2=int(tmp1[2])+int(tmp1[3])+int(tmp1[4])
	tmp1[7] = tmp2
	# Step 3: Apply formula for conscientiousness		
	# Step 2: Apply formula for extraversion		
	# Step 2: Apply formula for agreeableness	
	# Step 2: Apply formula for neuroticism		
	# Step 2: Apply formula for Normalization		
	json_str = dump(tmp1)	# Information string
	mylist.append(json_str) # Add it to a list

mystring = str(mylist)	# Convert the list of information to a string
blah = mystring.replace("'", "").replace("[","{").replace("]","}")	# Clean up string to suit the format for Datamaps
print "Cleaned up list ----> ", blah
fo.write(blah) # Final formatted string stored in data_1.json

