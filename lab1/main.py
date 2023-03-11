from csv_functions import generate_csv_table, shaker_sort_csv, quick_sort_csv, merge_sort_csv
import os

size = 100
for i in range(1, 11):
  	os.makedirs("tables", exist_ok=True)
  	filename = f"tables/table{size}.csv"
  	generate_csv_table(size, filename)
  	size += (100000 - 100) // 9


file_list = []
for filename in os.listdir("tables"):
    if os.path.isfile(os.path.join("tables", filename)) and os.path.join("tables", filename) != "tables/.DS_Store":
        file_list.append(os.path.join("tables", filename))

sizes = sorted([int(fil.split('tables/table')[1].split('.csv')[0]) for fil in file_list])

shaker_times = []
for file in file_list:
    start_time = time.time()
    shaker_sort_csv(file)
    end_time = time.time()
    shaker_times.append(end_time - start_time)

quick_times = []
for file in file_list:
    start_time = time.time()
    quick_sort_csv(file)
    end_time = time.time()
    quick_times.append(end_time - start_time)

merge_times = []
for file in file_list:
    start_time = time.time()
    merge_sort_csv(file)
    end_time = time.time()
    merge_times.append(end_time - start_time)


plt.plot(sizes, merge_times, label="Merge Sort")
plt.plot(sizes, quick_times, label="Quick Sort")
plt.plot(sizes, shaker_times, label="Shaker sort")
plt.xlabel("Size of file (strings)")
plt.ylabel("Time (seconds)")
plt.legend()
plt.savefig("plot.png")