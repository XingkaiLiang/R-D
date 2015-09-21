from sys import argv
from os.path import exists
from multiprocessing import Pool
from time import sleep
import os
import multiprocessing
import threading
import time
import logging

"""refer link:
http://www.cnblogs.com/rollenholt/archive/2012/04/23/2466179.html
http://www.cnblogs.com/vamei/archive/2012/10/12/2721484.html
http://www.oschina.net/translate/reliable-file-updates-with-python
"""
def getFileList(directryName):
    if os.path.isdir(directryName):
        listFile=os.listdir(directryName)
        return listFile
    
def threadTest(str,lock):
    lock.acquire()
    print str
    lock.release()
    
#Multi_thread--------------------------------------------
def multiThread():
    record = []
    lock = threading.Lock()
    for i in range(5):
        thread = threading.Thread(target = threadTest,args =(i,lock))
        thread.start()
        record.append(thread)
    for thread in record:
        thread.join()
        
      
      
def dupicateWithSingleThread():
    start = time.clock()
    record = []
    fileCnt =0
    totoltime =0
    #directory = raw_input("Enter directory name\n")
    directory="C:\\Users\\xlian7164584\\Downloads\\rawdata (22)\\6400"
    outputfile="C:\\Users\\xlian7164584\\Downloads\\rawdata (22)\\6400\\test.csv"
    with open(outputfile,'w') as f:
        for (path,dirs,files) in os.walk(directory):
            for fileName in  files:
                filetemp=files[fileCnt]
                queue_cond=threading.Condition()
                if os.path.splitext(fileName)[1] == '.txt': 
                    fileCnt +=1
                    fileName = path+'\\'+fileName
                    bs1time,bs2time=DuplicateChecWithSingleThread(fileName,f)
                    totoltime =bs1time+bs2time
            elapsed = (time.clock() - start)
            print ("ave time =%s,Muliti thread Time used:",totoltime/(2*fileCnt),elapsed)
    
def multiThreadForDuplicateCheck():
    start = time.clock()
    record = []
    #fileList= []
    fileCnt =0
    #directory = raw_input("Enter directory name\n")
    directory="C:\\Users\\xlian7164584\\Downloads\\rawdata (10)\\6600"
    for (path,dirs,files) in os.walk(directory):
        #fileList = getFileList(path)
        for fileName in  files:
            if os.path.splitext(fileName)[1] == '.txt':
                fileName = path+'\\'+fileName
                #fileList[fileCnt] = fileName
                fileCnt +=1
                thread = threading.Thread(target = DuplicateCheck,args =(fileName,))
                #threads =[threading.Thread(target=DuplicateCheck,args=(fileName,queue_cond,)) for i in range(2)]
                logger.debug("[%s] thread starting  [%d] file name is [%s]......" % (threading.current_thread().name,fileCnt,fileName[-11:]))
                thread.start()
                thread.join()
                record.append(thread)
                    #fileCnt =0
                #[thread.start() for thread in threads]
                #[thread.join() for thread in threads]
        elapsed = (time.clock() - start)
        print ("Muliti thread Time used:",elapsed)
        
#Multi_process -------------------------------------------------
def multiProcessForDuplicateCheck():
    start = time.clock()
    record = []
    directory = raw_input("Enter directory name\n")
    for (path,dirs,files) in os.walk(directory):
        #fileList = getFileList(path)
        for fileName in  files:
            #print os.path.splitext(fileName)[1]
            if os.path.splitext(fileName)[1] == '.txt':
                fileName = path+'\\'+fileName
                process = multiprocessing.Process(target = DuplicateCheck,args=(fileName,))
                logger.debug("[%s] thread starting......" % (threading.current_thread().name))
                process.start()
                record.append(process)
    for process in record:
        process.join()
    elapsed = (time.clock() - start)
    print ("Muliti process Time used:",elapsed)
    
#duplicate check function   --------------------------
def DuplicateCheck(fileName):   
    firstLine = 0
    asatWriteDone = 0
    asatWriteGLogCnt = 0
    asatWriteCylList = []
    asatReadDone = 0
    asatReadGLogCnt =0
    asatReadCylList = []
    #fileName = 'C:/Users/xlian/Downloads/rawdata (20)/EZ08D1XM.txt'
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
            if firstLine == 0:
                SN = eachLine[7:16].strip()
                firstLine = 1
            #print eachLine
            #splitStr = eachLine.split('  ')
            if "F:47" in eachLine:
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
    logger.debug("[%s] thread check done at file [%s] " % (threading.current_thread().name,fileName[-11:]))
       
def DuplicateChecWithSingleThread(fileName,outputfile):   
    firstLine = 0   
    with open(fileName,'r') as f:
        bs1Flag =0
        bs2Flag =0
        bs1Time =0
        bs2Time =0
        bs1StartTime =0
        bs1EndTime =0
        bs2StartTime =0
        bs2EndTime =0        
        for eachLine in f:
            if firstLine == 0:
                SN = eachLine[7:16].strip()
                firstLine = 1
            if 'from Test Start' in eachLine:
                if bs1Flag ==1 and bs2Flag ==0:
                    bs1EndTime = int(eachLine.split('[')[0].split(':')[1].strip())
                    bs1Time = bs1EndTime - bs1StartTime
                    bs1Flag =2  # 0 not start,1 get done,2 calc done
                elif bs2Flag ==1:
                    bs2EndTime = int(eachLine.split('[')[0].split(':')[1].strip())
                    bs2Time = bs2EndTime - bs2StartTime 
                    bs2Flag =2
                    break            
            if "MSG->* BS Download (Option 2)" in eachLine:
                if bs1Flag ==0:
                    bs1StartTime = int(eachLine.split('[')[0].split(':')[1].strip())
                    bs1Flag =1
                elif bs1Flag ==2:
                    bs2StartTime = int(eachLine.split('[')[0].split(':')[1].strip())
                    bs2Flag =1                    
            
                                    
    outputfile.write("%s,BS time ave =%ss,bs1StartTime=%s,bs1EndTime=%s,bs2StartTime=%s,bs2EndTime=%s\n" % (SN,(bs1Time+bs2Time)/2,bs1StartTime,bs1EndTime,bs2StartTime,bs2EndTime))
    print '%s,BS time ave =%ss,bs1StartTime=%s,bs1EndTime=%s,bs2StartTime=%s,bs2EndTime=%s\n'%(SN,(bs1Time+bs2Time)/2,bs1StartTime,bs1EndTime,bs2StartTime,bs2EndTime)
    #logger.debug("[%s] thread check done" % (threading.current_thread().name))
    return bs1Time,bs2Time
if __name__=="__main__":
    """
    i = 0
    pool = Pool(processes = 4)
    directory = raw_input("Enter directory name\n")
    fileList = getFileList(directory)
    print fileList[0]
    while i< len(fileList):
        result = pool.apply_async(DuplicateCheck,(fileList[i],))
        i+=1
    pool.close()
    pool.join()
    if result.successful():
        print "check successfull"
    """
    logger =logging.getLogger()
    logger.setLevel(logging.DEBUG) 
    formatter =logging.Formatter('%(asctime)s =%(message)s')
    ch=logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)    
    HDDCnt =0
    #multiThread()                 # test for thread operation
    #multiThreadForDuplicateCheck() #multi thread operation,lower than mutiprocess
    dupicateWithSingleThread()
    #multiProcessForDuplicateCheck() #multi process operation