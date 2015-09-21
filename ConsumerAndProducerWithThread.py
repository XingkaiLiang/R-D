import Queueimport threadingimport random#writelock =threading.Lock()class Producer(threading.Thread):    def __init__(self,q,con,name):
        super(Producer,self).__init__()
        self.q = q
        self.con = con
        self.name = name
        print "produce " +self.name+" started"
    def run(self):        while 1:
            #global writelock      
            self.con.acquire()#acquire the lock   
            if self.q.full():               #if queue is full
               #with writelock:#output info
               print " queue is full, producer wait"               #wait for resource               self.con.wait()
            else:
                value = random.randint(0,10)
                #with writelock:                print self.name+" put value "+" : "+str(value)+" into queue"
                self.q.put((self.name+":"+str(value)))#put to queue
                self.con.notify()#inform consumer
                self.con.release()#release the lock
        
class Consumer(threading.Thread):
    def __init__(self,q,con,name):
        super(Consumer,self).__init__()
        self.q = q
        self.con = con
        self.name = name
        print " consume " +self.name+"started\n"
    def run(self):
        while 1:
            #global writelock
            self.con.acquire()
            if self.q.empty():#if empty
                #with writelock:
                print "queue is empty,consumer wait"
                self.con.wait()#wait the resource ready
            else:
                value = self.q.get()#get one element from queue
                #with writelock:
                print self.name +" get value "+ value+" from queue"
                self.con.notify()                #inform producer
            self.con.release()#release the lock

if __name__ == "__main__":
    print "start to run\n"
    q = Queue.Queue(10)
    con = threading.Condition()
    #p = Producer(q,con,"p1 ")
    #p.start()
    p1 = Producer(q,con,"p2 ")
    p1.start()
    c1 = Consumer(q,con,"c1 ")
    c1.start()
        
        
    
