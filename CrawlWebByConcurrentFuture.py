"""
Use ThreadPoolExecutor which is featured in the concurrent.futures module
A thread pool is nothing but a structure that keeps several threads,which are previous created,to be used in a certain process
It aims to reuse threads,thus avoiding unnecessary creation of thread which is costly
"""
import re,logging
import Queue,threading
import requests


def group_urls_task(urls):
    try:
        url =urls.get(True,0.05)
        result_dict [url] =None
        logger.info("[%s] putting url [%s] in dict..." % (threading.currentThread(),url))
    except Queue.Empty:
        logging.error('nothing to be done,queue is empty')
        
def crawl_task(url):
    links = []
    try:
        request_data = requests.get(url)
        logger.info()
        links = html_link_regex.findall(request_data.txt)
    except:
        logger.error(sys.exc_info()[0])
        raise
    finally:
        return (url,links)
with concurrent.futures.ThreadPoolExecutor(max_workers =3) as group_link_threads:
    
if __name__=="__main__":
    htnk_link_regex =re.compile('<a\s(":.*\s)&?href=[\'"](.*?)[\'"].*>')
    urls =Queue.Queue()
    urls.put('http://www.163.com')
    urls.put('http://www.baidu.com')
    urls.put('http://www.cnblogs.com')
    urls.put('http://www.csdn.com')
    result_dict ={}