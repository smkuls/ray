import sys
import time
import ray

address = sys.argv[1]

ray.init(redis_address=address)

@ray.remote
def f():
    time.sleep(0.01)
    return ray.services.get_node_ip_address()

# Get a list of the IP addresses of the nodes that have joined the cluster.
nodes = set(ray.get([f.remote() for _ in range(1000)]))
for node in nodes:
    print node
print len(nodes)
