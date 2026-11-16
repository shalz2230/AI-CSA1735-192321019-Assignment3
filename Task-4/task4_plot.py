import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results.csv")

# Graph 1: Ground clause growth
plt.figure()
plt.plot(df["constants"], df["ground_clauses"], marker="o")
plt.xlabel("Number of Constants")
plt.ylabel("Number of Ground Clauses")
plt.title("Ground Clause Growth")
plt.grid(True)
plt.savefig("task4_ground_clause_growth.png")
plt.close()

# Graph 2: Inference time comparison
plt.figure()
plt.plot(
    df["constants"],
    df["lifted_inference_time_ms"],
    marker="o",
    label="Lifted Inference"
)
plt.plot(
    df["constants"],
    df["propositional_inference_time_ms"],
    marker="s",
    label="Propositional Inference"
)
plt.xlabel("Number of Constants")
plt.ylabel("Average Inference Time (ms)")
plt.title("Lifted vs Propositional Inference")
plt.legend()
plt.grid(True)
plt.savefig("task4_inference_comparison.png")
plt.close()

# Graph 3: Propositional KB construction time
plt.figure()
plt.plot(
    df["constants"],
    df["propositional_build_time_ms"],
    marker="o"
)
plt.xlabel("Number of Constants")
plt.ylabel("Construction Time (ms)")
plt.title("Propositional KB Construction Cost")
plt.grid(True)
plt.savefig("task4_build_time.png")
plt.close()

print("All Task 4 graphs generated successfully!")