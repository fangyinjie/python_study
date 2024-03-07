
# from multiprocessing.dummy import Pool as ThreadPool
from multiprocessing.pool import ThreadPool
def getSource(url):
    print(f"i am {url}!")
    return url



pool = ThreadPool(4)
pool.map(getSource, [x for x in range(10)])
pool.close()
pool.join()
