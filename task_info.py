import ray
import sys

redis_address = sys.argv[1]
output_file_name = sys.argv[2]

num_tasks = 10000000
if len(sys.argv) >= 4:
    num_tasks = sys.argv[3]


ray.init(redis_address=redis_address)

task_profiles = ray.global_state.task_profiles(num_tasks)

task_durations = []

for task_profile in task_profiles.items():
    task_durations.append(task_profile[1]['get_arguments_start'] -
                          task_profile[1]["store_outputs_end"])

with open(output_file_name, "w+") as file_handle:
    file_handle.write("\n".join(map(str, task_durations)))
