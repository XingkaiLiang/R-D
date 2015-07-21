# -*- coding: cp936 -*-
import os
import Queue
import threading
import urllib2
import time
"""
1.setDaemon need to start before start is called
2.user thread and daemon thread, setDaemon set the thread as background thread
3.when main thread end,user thread will terminated if daemon is set to True
4.the entire python program exits when no alive non-daemon thread are left
�ػ�����Ҳ�ɷ�����̣���û���û��߳̿ɷ���ʱ�Զ��뿪��
���ȼ����ػ��������ȼ��Ƚϵͣ�����Ϊϵͳ������������߳��ṩ����
���ã�ͨ��setDaemon��true��������Ϊ�ػ�����
"""
class DLThread(threading.Thread):
    def __init__(self,queue):
        threading.Thread.__init__(self)
        self.queue = queue
    def run(self):
        while True:
            url=self.queue.get()#delete the element in the queue and return the element
            print self.name+"begin DL "+url+"...\n"
            self.download_file(url)
            self.queue.task_done()#send signl to tell other the queue mission finish
            print self.name+"download completed!!!"
    def download_file(self,url):
        urlhandler = urllib2.urlopen(url)
        fname = os.path.basename(url)+".html"
        """print fname"""
        with open(fname,"wb") as f:
            while True:
                chunk = urlhandler.read(1024)
                if not chunk:break
                f.write(chunk)
                
if __name__ =="__main__":
    urls =["http://www.163.com",
           "http://www.baidu.com",
           "http://www.alipay.com"]
    queue = Queue.Queue()
    for i in range(5):
        t=DLThread(queue)
        t.setDaemon(True)#daemon thread(true),not daemon(false) ,before start is called
        #t.daemon = True#main thread default to daemon= false
        t.start()

    for url in urls:
        queue.put(url)
    queue.join()#block until all tasks are done
        
