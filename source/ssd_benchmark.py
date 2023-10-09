# %%
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import time
# from tqdm import tqdm

# %%
TARGET_PATH = r"EDIT_PATH"
MAX_SIZE_GB = 1000

# if not target path exists, make directory
if not os.path.exists(TARGET_PATH):
    os.makedirs(TARGET_PATH)

# if exist, clear up the directory
else:
    for file in os.listdir(TARGET_PATH):
        os.remove(os.path.join(TARGET_PATH, file))

time.sleep(3)

# %%
# create a dummy data with np.float64
array_to_save = np.random.rand(1440, 1440).astype(np.float16)
UNIT_SIZE = array_to_save.nbytes

iteration = MAX_SIZE_GB * 1024 * 1024 * 1024 // UNIT_SIZE
print("UNIT_SIZE(MB): ", UNIT_SIZE / 1024 / 1024)
print("iteration: ", iteration)

# %%
# save the data
print("Start saving data")
start_time = time.time()
time_list = []

# for i in tqdm(range(iteration)):
for i in range(iteration):
    np.save(os.path.join(TARGET_PATH, f"{i}.npy"), array_to_save)
    time_list.append(time.time() - start_time)

# %%
# calculate the speed
speed_list = []
for i in range(1, len(time_list)):
    speed_list.append(UNIT_SIZE / (time_list[i] - time_list[i - 1]) / 1024 / 1024)

# calculate the total volume
total_volume_list = []
for i in range(len(time_list)):
    total_volume_list.append(UNIT_SIZE * i / 1024 / 1024 / 1024)

# %%
# plot the speed
plt.scatter(total_volume_list[1:], speed_list)
plt.xlabel("Data (GB)")
plt.ylabel("speed (MB/s)")
plt.title("SSD Benchmark")
plt.savefig(os.path.join("ssd_benchmark_hoge.png"))
