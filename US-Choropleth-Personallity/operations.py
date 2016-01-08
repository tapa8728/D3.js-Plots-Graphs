#operations on the personality data
import json
def dump(a):
        return {'gfgid': a[0],'location': a[1],"personality": {'openness': a[7],
                               									'conscientiousness': a[8],
								                               'extraversion': a[9],
								                               'agreeableness': a[10],
								                               'neuroticism': a[11]}}
		     


# Raw data in comma-separated format
f = open("data.txt","r") 	#opens file with name of "data.txt"
fo = open("data_1.txt", "w") #'w' mode will create a new file in the directory

lines = f.readlines()
mylist= []

# Step 1: Clean up data by removing spaces between each value
for l in lines:
	
	tmp1=l.replace(" ","").replace("\n","").split(",")
	for i in range(2, 7):
		try:
			tmp1[i] = int(tmp1[i])	#Replace corrupt data of non-integer type to 0
		except:
			tmp1[i] = 0;

	#Step 2: Apply formula for Openness		
	tmp2=int(tmp1[2])+int(tmp1[3])+int(tmp1[4])
	tmp1[7] = tmp2
	json_str = dump(tmp1)
	print json_str
	mylist.append(json_str)
	

print mylist
fo.write(json.dumps(mylist))
print"----------------------"
print"lets read from ouput file"
# f2 = open("data_1.txt", "r")
# print f2.readlines()
