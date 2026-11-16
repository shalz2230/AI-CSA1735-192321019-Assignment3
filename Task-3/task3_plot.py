
"""
Task 3 - Performance Graphs
"""

import csv
import matplotlib.pyplot as plt
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE = os.path.join(BASE_DIR, "results.csv")

with open(CSV_FILE, "r") as file:
    rows = list(csv.DictReader(file))

students = [int(row["Students"]) for row in rows]

# Graph 1: Knowledge Base Size
plt.figure(figsize=(9, 5))

plt.plot(
    students,
    [int(row["Propositional_KB_Size"]) for row in rows],
    marker="o",
    label="Propositional Logic"
)

plt.plot(
    students,
    [int(row["FOL_KB_Size"]) for row in rows],
    marker="s",
    label="First-Order Logic"
)

plt.xlabel("Number of Students")
plt.ylabel("Knowledge Base Size")
plt.title("Knowledge Base Size Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(BASE_DIR, "performance_kb_size.png")
)
plt.close()


# Graph 2: Inference Operations
plt.figure(figsize=(9, 5))

plt.plot(
    students,
    [int(row["Propositional_Operations"]) for row in rows],
    marker="o",
    label="Propositional Logic"
)

plt.plot(
    students,
    [int(row["FOL_Operations"]) for row in rows],
    marker="s",
    label="First-Order Logic"
)

plt.xlabel("Number of Students")
plt.ylabel("Inference Operations")
plt.title("Inference Operation Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(BASE_DIR, "performance_operations.png")
)
plt.close()


# Graph 3: Execution Time
plt.figure(figsize=(9, 5))

plt.plot(
    students,
    [float(row["Propositional_Time"]) for row in rows],
    marker="o",
    label="Propositional Logic"
)

plt.plot(
    students,
    [float(row["FOL_Time"]) for row in rows],
    marker="s",
    label="First-Order Logic"
)

plt.xlabel("Number of Students")
plt.ylabel("Execution Time (seconds)")
plt.title("Inference Execution Time Comparison")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    os.path.join(BASE_DIR, "performance_time.png")
)
plt.close()

print("All three performance graphs generated successfully!")
print("1. performance_kb_size.png")
print("2. performance_operations.png")
print("3. performance_time.png")
