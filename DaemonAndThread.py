import os
import threading
import time
import logging
import random


logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)

def work1():
    count=0
    while count<=5:
        threadname= threading.currentThread()
        wait_time=random.randrange(1,4)
        print("%s,count =%s wait for =%s s,time %s "%(threadname,count,wait_time,time.ctime()[-13:]))
        time.sleep(wait_time)
        count +=1
     
def work2():
    i=0
    while i<=5:
        threadname= threading.currentThread()
        wait_time=random.randrange(1,4)
        print("%s,i     =%s wait for =%s s,time %s "%(threadname,i,wait_time,time.ctime()[-13:]))
        time.sleep(wait_time)
        i +=1
        
class Counter(object):
    def __init__(self,start=0):
        self.lock = threading.Lock()
        self.value = start
    def incr(self):
        logging.debug('waiting for lock')
        self.lock.acquire()
        try:
            logging.debug('acquired lock')
            self.value = self.value + 1
            print 'counter is %d'% self.value
        finally:
            self.lock.release()
            
def worker(c):
    for i in xrange(1,5):
        pause = random.random()
        logging.debug('sleeping %0.02f',pause)
        time.sleep(pause)
        c.incr()
    logging.debug('done')


def daemon():
    logging.debug('daemon starting')
    print time.ctime()
    #logging.debug('daemon doing sth')
    time.sleep(3)
    logging.debug('daemon exiting')
    print time.ctime()

def nonDaemon():
    logging.debug('nonDaemon starting')
    print time.ctime()
    time.sleep(2)
    logging.debug('non daemon doing sth')
    print time.ctime()
    logging.debug('nonDaemon exiting')
    
    
    
def consumer(cond):
    logging.debug('starting sunsumer thread')
    t = threading.currentThread()
    with cond:
        cond.wait()
        logging.debug('resource is available to consumer')
def producer(cond):
    logging.debug('starting producer thread')
    with cond:
        logging.debug('making resource available')
        cond.notifyAll()
    

if __name__ =="__main__":
    #-----------------daemon thread operation---------------------------------
    
    #d = threading.Thread(name ='daemon',target = daemon)
    #d.setDaemon(True)    
    #t=threading.Thread(name='non-daemon',target =nonDaemon)
    #d.start()
    #t.start()
    #d.join()
    #t.join()    
    
    #-----------------thread join method usage---------------------------------
    
    mainthread= threading.currentThread()
    print '%s main thread is waiting for exit'% mainthread
    
    test1=threading.Thread(name='work1',target=work1)
    test2=threading.Thread(name='work2',target=work2)
    test1.start()
    test2.start()
    test1.join()#timeout set a timer
    test2.join()    
    
    #-------------lock object to update counter by sereral thread-------------
    
    counter = Counter()
    for i in range(4):
        t = threading.Thread(target=worker,args=(counter,))
        t.start()
    
    logging.debug('waiting for worker threads')
    for t in threading.enumerate():
        if t is not mainthread:
            t.join()
    logging.debug('counter:%d',counter.value)
    
    print 'main thread finish'
    
    
    #------------------comsumer and producer---------------------------------
    condition = threading.Conditon()
    c1 = threading.Thread(name ='c1',target= consumer,args =(condition,))
    c2 = threading.Thread(name ='c1',target= consumer,args =(condition,))
    p  = threading.Thread(name ='p',target = producer,args =(condition,))
    
    c1.start()
    time.sleep(2)
    c2.start()
    c2.sleep(2)
    p.start()