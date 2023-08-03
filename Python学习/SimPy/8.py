import simpy


def send_1(env, event_test):
    i = 0
    while 1:
        i += 1
        yield env.timeout(15)
        event_test.succeed('im send 1 i ={0}'.format(i))
        # event_test = env.event()


# def send_2(env, event_test):
#     i = 0
#     while 1:
#         yield env.timeout(11)
#         event_test.succeed('im send 2 i ={0}'.format(i))
#         # event_test = env.event()
#         i += 1



def recv(env, event_test):
    while 1:
        value = yield event_test
        print(value)
        # event_test = env.event()

env = simpy.Environment()
event_test = env.event()
env.process( send_1(env, event_test) )
# env.process( send_2(env, event_test) )
env.process( recv(env, event_test) )
env.run()


