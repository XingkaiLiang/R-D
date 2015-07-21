from sys import argv
from os.path import exists

script = argv[0]
openfile = 'D:/Programing/python code/temp.txt'

print "the first script is called",script
print "open file name is:",openfile
#input something
target =open(openfile,'w')
inputfile = open(script,'r')
#inputfile=open(filename) is ok
inputdata=inputfile.read()
target.write("input file len is:%d bytes" % len(inputdata))
print "input file len is:%d bytes" % len(inputdata)
#inputfile.readline() only 1 line
print "does file exit %r" % exists(openfile)
line = raw_input("line:\n")
line2=raw_input("line1:\n")

target.write(line+"\n")

target.write(inputdata)
#need close() 
target.close()
inputfile.close()
                 


