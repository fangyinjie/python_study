from multiprocessing.pool import ThreadPool


def getSource(url):
    print(f"i am {url}!")
    return url


with ThreadPool(processes=4) as tpool:
    ret_list = tpool.map(getSource, [x for x in range(10)])
