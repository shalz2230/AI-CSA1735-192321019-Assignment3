
import csv
import matplotlib.pyplot as plt

lengths = []
mc_times = []
resolution_times = []
mc_models = []
resolution_attempts = []

with open("Task-2/results.csv", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        lengths.append(int(row["Chain_Length"]))

        mc_times.append(
            float(row["MC_Time"])
            if row["MC_Result"] != "SKIPPED" else None
        )

        resolution_times.append(float(row["Resolution_Time"]))
        mc_models.append(int(row["MC_Models"]))
        resolution_attempts.append(int(row["Resolution_Attempts"]))

# Graph 1: Execution time
plt.figure()
plt.plot(
    [x for x, y in zip(lengths, mc_times) if y is not None],
    [y for y in mc_times if y is not None],
    marker="o",
    label="Model Checking"
)
plt.plot(
    lengths,
    resolution_times,
    marker="o",
    label="Resolution"
)
plt.yscale("log")
plt.xlabel("Implication Chain Length")
plt.ylabel("Execution Time (seconds, log scale)")
plt.title("Model Checking vs Resolution - Execution Time")
plt.legend()
plt.grid(True)
plt.savefig("Task-2/performance_time.png", dpi=300)
plt.show()

# Graph 2: Operation counts
plt.figure()
plt.plot(
    [x for x, y in zip(lengths, mc_models) if y > 0],
    [y for y in mc_models if y > 0],
    marker="o",
    label="Models Enumerated"
)
plt.plot(
    lengths,
    resolution_attempts,
    marker="o",
    label="Resolution Attempts"
)
plt.yscale("log")
plt.xlabel("Implication Chain Length")
plt.ylabel("Operation Count (log scale)")
plt.title("Operation Count Comparison")
plt.legend()
plt.grid(True)
plt.savefig("Task-2/performance_operations.png", dpi=300)
plt.show()

print("Graphs saved in Task-2/")
