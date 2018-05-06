import ray
import sys

redis_address = sys.argv[1]
# task_runtime_file = sys.argv[2]
# worker_num_tasks_run_file = sys.argv[3]

num_tasks = 10000000
ray.init(redis_address=redis_address)

task_profiles = ray.global_state.task_profiles(num_tasks)

task_durations = []
worker_num_tasks_run = {}
overall_worker_task_runtime = {}

for task_profile in task_profiles.items():
    worker_id = task_profile[1]["worker_id"]
    worker_ip_address = (ray.global_state.workers()
                         [worker_id]["node_ip_address"])
    task_runtime = task_profile[1]["store_outputs_end"] - task_profile[1]['get_arguments_start']
    if worker_ip_address not in worker_num_tasks_run:
        worker_num_tasks_run[worker_ip_address] = 0
        overall_worker_task_runtime[worker_ip_address] = 0
    else:
        worker_num_tasks_run[worker_ip_address] += 1
        overall_worker_task_runtime[worker_ip_address] += task_runtime

    task_durations.append(task_profile[1]["store_outputs_end"] -
                          task_profile[1]['get_arguments_start'])

with open("overall_worker_task_runtime.txt", "w+") as file_handle:
    file_handle.write("\n".join(map(str, list(overall_worker_task_runtime.values()))))

with open("task_runtime_output.txt", "w+") as file_handle:
    file_handle.write("\n".join(map(str, task_durations)))


with open("worker_task_allocation_output.txt", "w+") as file_handle:
    file_handle.write("\n".join(map(str, list(worker_num_tasks_run.values()))))
