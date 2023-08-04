

starttime = time.time()
print('开始')


for x in range(10):
    time.sleep(1)

endtime = time.time()
print('结束')
print(endtime-starttime)