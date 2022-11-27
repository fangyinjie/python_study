import simpy

def resource_user(env, resource):
    request = resource.request()  # Generate a request event
    yield request                 # Wait for access
    yield env.timeout(1)          # Do something
    resource.release(request)     # Release the resource

def resource_user(env, resource):
    with resource.request() as req:  # Generate a request event
        yield req                    # Wait for access
        yield env.timeout(1)         # Do something
    # Resource released automatically（不用再释放了）


env = simpy.Environment()
res = simpy.Resource(env, capacity=1)   # 创建资源
user = env.process(resource_user(env, res))
env.run()
