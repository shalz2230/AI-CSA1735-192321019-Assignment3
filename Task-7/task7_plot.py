
"""
Task 7: Performance Graph Generation
Reads task7_comparison_results.csv and generates graphs.
"""

import csv
import matplotlib.pyplot as plt


def load_results():
    with open("task7_comparison_results.csv", "r") as file:
        return list(csv.DictReader(file))


def generate_graphs():
    results = load_results()

    sizes = [int(row["rules"]) for row in results]

    baseline_ops = [
        int(row["baseline_operations"]) for row in results
    ]
    indexed_ops = [
        int(row["indexed_operations"]) for row in results
    ]

    baseline_time = [
        float(row["baseline_time_ms"]) for row in results
    ]
    indexed_time = [
        float(row["indexed_time_ms"]) for row in results
    ]

    # Graph 1: Operation comparison
    plt.figure()
    plt.plot(sizes, baseline_ops, marker="o", label="Baseline")
    plt.plot(sizes, indexed_ops, marker="s", label="Indexed")
    plt.xlabel("Knowledge Base Size (Rules)")
    plt.ylabel("Rule Retrieval Operations")
    plt.title("Baseline vs Indexed Retrieval Operations")
    plt.legend()
    plt.grid(True)
    plt.savefig("task7_operations.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Graph 2: Execution time comparison
    plt.figure()
    plt.plot(sizes, baseline_time, marker="o", label="Baseline")
    plt.plot(sizes, indexed_time, marker="s", label="Indexed")
    plt.xlabel("Knowledge Base Size (Rules)")
    plt.ylabel("Average Retrieval Time (ms)")
    plt.title("Baseline vs Indexed Retrieval Time")
    plt.legend()
    plt.grid(True)
    plt.savefig("task7_execution_time.png", dpi=300, bbox_inches="tight")
    plt.close()

    # Graph 3: Indexed retrieval operations
    plt.figure()
    plt.plot(sizes, indexed_ops, marker="o")
    plt.xlabel("Knowledge Base Size (Rules)")
    plt.ylabel("Indexed Lookup Operations")
    plt.title("Knowledge Base Size vs Indexed Lookup Operations")
    plt.grid(True)
    plt.savefig("task7_indexed_scalability.png", dpi=300, bbox_inches="tight")
    plt.close()

    print("All Task 7 graphs generated successfully!")
    print("Generated files:")
    print("- task7_operations.png")
    print("- task7_execution_time.png")
    print("- task7_indexed_scalability.png")


if __name__ == "__main__":
    generate_graphs()
