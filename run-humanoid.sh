python ~/ray/python/ray/rllib/train.py --env RoboschoolHumanoid-v1 --run ES --config '{ "l2_coeff":0.005, "noise_stdev":0.02, "episodes_per_batch":1000, "timesteps_per_batch":10000, "eval_prob":0.003, "return_proc_mode":"centered_rank", "num_workers":10, "stepsize":0.01, "observation_filter":"MeanStdFilter", "noise_size":250000 }' --redis-address $1

