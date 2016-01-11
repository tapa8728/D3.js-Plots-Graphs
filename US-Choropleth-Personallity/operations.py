import json
""" Operations on the personality data to convert it to a JSON file of format

	Required JSON Format- 
	{
		"NV": {"extraversion": "0", "neuroticism": "0", "agreeableness": "0", "fillKey": "REP", "conscientiousness": "0", "gfgid": "1001", "openness": "38"}, 
		"CA": {"extraversion": "0", "neuroticism": "0", "agreeableness": "0", "conscientiousness": "0", "gfgid": "2001", "openness": 56}, 
		"TX": {"extraversion": "0", "fillKey": "REP", "neuroticism": "0", "fillKey": "REP", "agreeableness": "0", "fillKey": "REP", "conscientiousness": "0", "fillKey": "REP"}
	}
	Converted data stored in data_1.json file in same folder
	"""
# Print Matrix
def display(m):
	print "Matrix is ------"
	for i in range(0,50):
		print statelist[i]," : ",m[i][0],",",m[i][1],",",m[i][2],",",m[i][3],",",m[i][4]

# Normalize the Matrix
def transform(m):
	o = [row[0] for row in m]
	o_norm = [float(i)*10/sum(o) for i in o]
	for i in range(0, 50):
		m[i][0] = o_norm[i]

	c = [row[1] for row in m]
	c_norm = [float(i)*10/sum(c) for i in c]
	for i in range(0, 50):
		m[i][1] = c_norm[i]

	e = [row[2] for row in m]
	e_norm = [float(i)*10/sum(e) for i in e]
	for i in range(0, 50):
		m[i][2] = e_norm[i]

	a = [row[3] for row in m]
	a_norm = [float(i)*10/sum(a) for i in a]
	for i in range(0, 50):
		m[i][3] = a_norm[i]

	n = [row[4] for row in m]
	n_norm = [float(i)*10/sum(n) for i in n]
	for i in range(0, 50):
		m[i][4] = n_norm[i]

# Function for getting Color
def color(v):
	if 0 <= v < 0.2:
		return 'LOW'
	elif 0.2 <= v < 0.4:
		return 'LOWMED'
	elif 0.4 <= v < 0.6:
		return 'MED'
	elif 0.6 <= v < 0.8:
		return 'HIGHMED'
	else:
		return 'HIGH'


# Function to format the data in required format
def dump(idk, loc, a):
	result = '"'+loc+'" : {"id": '+ str(idk) +', "openness" : '+ str(a[0])+',"fillKey" : "'+color(a[0])+'","conscientiousness" : '+str(a[1])+',"fillKey" : "'+color(a[1])+'","extraversion": '+str(a[2])+',"fillKey" : "'+color(a[2])+'","agreeableness" : '+str(a[3])+',"fillKey" : "'+color(a[3])+'","neuroticism" : '+str(a[4])+',"fillKey" : "'+color(a[4])+'"}'
	return result

# Raw data in comma-separated format
f = open("data.txt","r") 	#opens file with name of "data.txt"
fo = open("data_1.json", "w") #'w' mode will create a new file in the directory

lines = f.readlines()
mylist= []
statelist = [] # list of states in the same order
ocean_matrix =[[0 for x in range(5)] for x in range(50)] 
mystring = "{"
count = 0 # to count the number of lines read from the file
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
	tmp1=int(value[2])+int(value[3])+int(value[4])
	value[7] = tmp1
	ocean_matrix[count][0] = tmp1
	# Step 3: Apply formula for conscientiousness 8th position
	tmp2 = 2*int(value[2]) + int(value[3])
	value[8] = tmp2
	ocean_matrix[count][1] = tmp2
	# Step 4: Apply formula for extraversion 9th position	
	tmp3 = int(value[4])+int(value[5])+int(value[6])
	value[9] = tmp3
	ocean_matrix[count][2] = tmp3
	# Step 5: Apply formula for agreeableness 10th position	
	tmp4 = int(value[2])+int(value[4])+int(value[6])
	value[10] = tmp4
	ocean_matrix[count][3] = tmp4
	# Step 6: Apply formula for neuroticism	11th position
	tmp5 = 3*int(value[2]) + int(value[4])	
	value[11] = tmp5
	ocean_matrix[count][4] = tmp5
	# Step 7: Add to list of states	
	statelist.append(value[1])
	# Step 8: Increment the counter to add the next set of values to matrix
	count+=1 

	

print "StateList is-", statelist
display(ocean_matrix)

# Step 9: Normalize the values in range of 0 to 1
transform(ocean_matrix)

display(ocean_matrix)

# Step 10: Convert matrix to JSON and dump
counter = 0 # to access the state list
for row in ocean_matrix:
	state = statelist[counter]
	json_str = dump(counter+1, state, row)	# Information string
	mylist.append(json_str) # Add it to a list
	counter+=1

mystring = str(mylist)	# Convert the list of information to a string
blah = mystring.replace("'", "").replace("[","{").replace("]","}")	# Clean up string to suit the format for Datamaps
print "Cleaned up list ----> ", blah
fo.write(blah) # Final formatted string stored in data_1.json

