"""
IPC
http://www.cnblogs.com/BoyXiao/archive/2011/01/01/1923828.html
"""
import os,time
import threading

def child(pipeout):
    zzz = 0
    while True:
        time.sleep(zzz)                                             # make parent wait
        msg=('spam %03d \n' % zzz).encode()                         # pipes are binary bytes
        os.write(pipeout,msg)                                       # send to parent
        zzz = (zzz+1)%5
        
def parent(pipein):
    while True:
        line = os.read(pipein,32)                                   # blocks until data sent
        print('parent %d got [%s]  at [%s]'%(os.getpid(),line,time.ctime()))
    
pipein,pipeout = os.pipe()
threading.Thread(target = child,args=(pipeout,)).start()
parent(pipein)