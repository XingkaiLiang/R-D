import Queue
import threading
import random
from os.path import exists
import os
import time

#writelock =threading.Lock()
class Producer(threading.Thread):
    def __init__(self,q,con,filename):
        super(Producer,self).__init__()
        self.q = q
        self.con = con
        self.filename = filename
        print "produce " +self.filename+" started"
    def run(self):
        #global writelock      
        for (path,dirs,files) in os.walk(directory):
            #fileList = getFileList(path)
            for fileName in  files:
                if os.path.splitext(fileName)[1] == '.txt':
                    fileName = path+'\\'+fileName             
                    self.con.acquire()#acquire the lock   
                    if self.q.full():
                        #if queue is full with writelock:#output info
                        print "queue is full,please producer wait"
                        queueFull = True
                        #wait for resource
                        self.con.wait()
                    else:                       
                        #value = random.randint(0,10)
                        #with writelock:
                        #print self.filename+" put value "+" : "+str(value)+" into queue"
                        #self.q.put((self.filename+":"+str(value)))#put to queue
                        self.q.put(fileName)
                        self.con.notify()#inform consumer
                    self.con.release()#release the lock
        
class Consumer(threading.Thread):
    def __init__(self,q,con,filename):
        super(Consumer,self).__init__()
        self.q = q
        self.con = con
        self.filename = filename
        print " consume " +self.name+"started\n"
    def run(self):
        while 1:
            #global writelock
            self.con.acquire()
            if self.q.empty():#if empty
                #with writelock:
                print "queue is empty,consumer wait"
                queueFull = False
                self.con.wait()#wait the resource ready
            else:
                filename = self.q.get()#get one element from queue
                #with writelock:
                DuplicateCheck(filename)
                self.con.notify()
                #inform producer
            self.con.release()#release the lock

def DuplicateCheck(fileName):   
    firstLine = 0
    asatWriteDone = 0
    asatWriteGLogCnt = 0
    asatWriteCylList = []
    asatReadDone = 0
    asatReadGLogCnt =0
    asatReadCylList = []
    start = time.clock()
    #fileName = raw_input("Enter file to decode")
    with open(fileName,'r') as f:
        #A:read all lines if file is small,if too big,change to B
        """allLines = f.readlines()
        f.close()
        for eachLine in allLines:
            print eachLine
        """
        #B:Read line by line using file iterator
        #with open(fileName) as f:
        for eachLine in f:
            #print eachLine
            if firstLine == 0:
                SN = eachLine[7:16].strip()
                firstLine = 1
            #print eachLine
            #splitStr = eachLine.split('  ')
            if "F:47" in eachLine:
                print eachLine
                asatWriteGLogCnt +=1
                #print eachLine
                #asatWriteCylList.append(eachLine[:}
                asatWriteCylList.append(eachLine[0:12].strip()+eachLine[13:15].strip()+eachLine[23:26].strip())
             
            if "0x2e" in eachLine:
                if asatWriteDone == 0:
                    asatWriteDone = 1 # asat write increase done
                elif asatWriteDone == 1:
                    asatWriteDone = 2 # asat write descrease done
                else:
                    pass
            if asatWriteDone == 2:
                if "0x2b" in eachLine:
                    asatReadDone = 1 #Asat Read log check done
                if asatReadDone == 0:
                    if eachLine[23:26].strip() == '10':
                        #if eachLine[0:12].strip() in asatWriteCylList:
                        for cylIndex in range(len(asatWriteCylList)):
                            if eachLine[0:12].strip() == asatWriteCylList[cylIndex][0:-3] and eachLine[13:15].strip() == asatWriteCylList[cylIndex][-3]:
                                asatReadGLogCnt +=1
                                del asatWriteCylList[cylIndex]
                                break
                            
    if asatWriteGLogCnt != 0:
        ratio = 100*asatReadGLogCnt/asatWriteGLogCnt
    else:
        ratio = 0
        
    #elapsed = (time.clock() - start)
    print "[%s] thread Time used[%s]:" % (threading.currentThread(), time.ctime())     
    print 'SN:%s,Write G log:%d Read G log:%d Ratio:%.4f%%\n'%(SN,asatWriteGLogCnt,asatReadGLogCnt,ratio)

if __name__ == "__main__":
    print "start to run\n"
    queueFull = False
    start = time.clock()
    print "[%s] thread Time used[%s]:" % (threading.currentThread(), time.ctime())   
    q = Queue.Queue(10)
    con = threading.Condition()
    #directory = raw_input("Enter directory name\n")
    directory="C:\\Users\\xlian7164584\\Downloads\\rawdata (10)\\6600"
       
    p1 = Producer(q,con,"p1")
    p1.start()
    c1 = Consumer(q,con,"c1 ")
    c1.start()  
    c2 = Consumer(q,con,"c2 ")
    c2.start()  
    c3 = Consumer(q,con,"c3 ")
    c3.start() 
    c4 = Consumer(q,con,"c4 ")
    c4.start()     
    
    #c1.join(4)
    #c2.join(4)
    #c3.join(4)
    elapsed = (time.clock() - start)
    print ("Muliti thread Time used:",elapsed)    
    

        

        
    
