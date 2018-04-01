import ray
import pprint
import sys

redis_address = sys.argv[1]
output_file_name = sys.argv[2]
worker_utilization_file_name = sys.argv[3]

num_tasks = 10000000
if len(sys.argv) >= 4:
    num_tasks = sys.argv[3]


ray.init(redis_address=redis_address)

task_profiles = ray.global_state.task_profiles(num_tasks)

task_durations = []

worker_utilization = {}

for task_profile in task_profiles.items():
    worker_id = task_profile[1]["worker_id"]
    worker_ip_address = ray.global_state.workers()[worker_id]["node_ip_address"]
    if worker_ip_address not in worker_utilization:
        worker_utilization[worker_ip_address] = 0
    else:
        worker_utilization[worker_ip_address] += 1

    task_durations.append(task_profile[1]["store_outputs_end"] -
                          task_profile[1]['get_arguments_start'])

with open(output_file_name, "w+") as file_handle:
    file_handle.write("\n".join(map(str, task_durations)))


with open(worker_utilization_file_name, "w+") as file_handle:
    file_handle.write(pprint.pformat(worker_utilization))
