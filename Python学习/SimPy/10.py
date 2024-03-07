import time
from random import randint
import simpy
import numba

# 使用Numba优化函数
@numba.jit
def test(num):
    pp = []
    for x in range(num):
        pass
        pp.append(randint(1, 100) * randint(100, 200))
    return

def attendee(env, name, event):
    for x in range(256):
        rts = randint(1, 100) * randint(100, 200)
        yield env.timeout(rts)
        # cc = test(name)
        # print(f'Attendee {name} currentime is {env.now}')
    event.succeed(f"{name} finish")



def timming(env, fe, events):
    yield simpy.AllOf(env, events)
    fe.succeed('Finish')

env = simpy.Environment()
finish_event = env.event()

e_ds = []
for i in range(30):
    e_d = env.event()
    env.process(attendee(env, i, e_d))
    e_ds.append(e_d)

env.process(timming(env, finish_event, e_ds))
st = time.time()
env.run(until=finish_event)
print(f'Finished in {time.time()-st}')