from collections import Counter
from random import randrange
import pprint
#-----------------collections.Counter-----------
mycounter = Counter()
for i in range(1000):
	random_num = randrange(100)
	mycounter[random_num]+=100
	
for i in range(100):
	print (i,mycounter[i])
#---------------------dictionary--------------------	
my_phrase = ["No","one","expect","the","china","rich man"]
my_dict = {key:value for value,key in enumerate(my_phrase)}
print(my_dict)

reverse_dict = {value:key for key,value in my_dict.items()}
print(reverse_dict)

#---------------subproccess to execute shell command
import subprocess
output = subprocess.check_output('dir',shell=True)
print (output)