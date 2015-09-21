#coding:utf-8"
import logging,threading,time
import Queue
import os
import time

def fibo_task(cond):
    with cond:
        while shared_queue.empty():
            logger.info("[%s]- waiting for element in queue......" % threading.current_thread().name)
            cond.wait()
        else:
            value =shared_queue.get()
            DuplicateCheck(value)
        shared_queue.task_done()
        #time.sleep(2)
        logger.debug("[%s] fibo of key[%s] " % (threading.current_thread().name,value))
                     
def queue_task(cond):
    logging.debug('starting  list data to queue......')
    with cond:
        for data in impit_list:
            logger.debug("[%s] Queue data [%s] ongoing......" % (threading.current_thread().name,data))
            shared_queue.put(data)
        #[shared_queue.put(data) for data in  impit_list]
        cond.notifyAll()
    logger.debug("[%s] Queue data done" % (threading.current_thread().name))

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

if __name__ == "__main__":
    start = time.clock()
    logger =logging.getLogger()
    logger.setLevel(logging.DEBUG)
    formatter =logging.Formatter('%(asctime)s =%(message)s')
    fileCnt =0
    ch=logging.StreamHandler()
    ch.setLevel(logging.DEBUG)
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    fibo_dict={}
    impit_list = []
    shared_queue =Queue.Queue()
    directory="C:\\Users\\xlian7164584\\Downloads\\rawdata (10)\\6600"
    for (path,dirs,files) in os.walk(directory):
        #fileList = getFileList(path)
        for fileName in  files:
            if os.path.splitext(fileName)[1] == '.txt': 
                fileName = path+'\\'+fileName
                impit_list.append(fileName)
                fileCnt+=1
    while fileCnt:
        for i in range(4):
            if ".txt" in impit_list.pop():
                print "test"
        threads =[threading.Thread(target=DuplicateCheck,args=(impit_list.pop(),)) for i in range(4)]
        [thread.start() for thread in threads]
        [thread.join() for thread in threads]
        #threading.Thread(target=DuplicateCheck,args=(impit_list.pop(),))
    #impit_list =[3,10,5,7,]
    """
    queue_cond=threading.Condition()
    print "main thread starting......"
    threads =[threading.Thread(target=fibo_task,args=(queue_cond,)) for i in range(4)]
    for thread in threads:
        thread.setDaemon(False)
        #print 'daemon is %d' % thread.isDaemon()
    
    [thread.start() for thread in threads]
    
    prod = threading.Thread(name='queue_task_thread',target=queue_task,args=(queue_cond,))
    prod.setDaemon(False)
    prod.start()
   
    [thread.join() for thread in threads]  """  
    elapsed = (time.clock() - start)
    print ("Muliti thread Time used:",elapsed)    
    print "main thread done"