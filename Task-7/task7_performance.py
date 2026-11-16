
"""
Task 7: Performance Evaluation
Measures query latency, inference steps,
memory usage and explanation length.

Synthetic academic benchmark only.
"""

import time
import tracemalloc
import csv
from statistics import mean

from task7_knowledge_base import generate_rules
from task7_test_cases import TEST_CASES
from task7_inference import check_prescription


def measure_performance(rule_count, repetitions=100):

    # Generate the requested knowledge base size.
    rules = generate_rules(rule_count)

    sample_case = TEST_CASES[0]

    latencies = []
    inference_steps = []
    explanation_lengths = []

    tracemalloc.start()

    for _ in range(repetitions):
        start = time.perf_counter()

        result = check_prescription(sample_case)

        end = time.perf_counter()

        latencies.append((end - start) * 1000)
        inference_steps.append(result["inference_steps"])
        explanation_lengths.append(
            len(" ".join(result["explanation"]))
        )

    current_memory, peak_memory = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "rules": len(rules),
        "latency_ms": mean(latencies),
        "inference_steps": mean(inference_steps),
        "peak_memory_kb": peak_memory / 1024,
        "explanation_length": mean(explanation_lengths),
    }


def main():

    rule_sizes = [40, 400, 2000]
    results = []

    print("=" * 75)
    print("TASK 7 - PERFORMANCE EVALUATION")
    print("=" * 75)

    for size in rule_sizes:
        result = measure_performance(size)
        results.append(result)

        print(f"\nKnowledge Base: {size} rules")
        print(f"Average Query Latency: {result['latency_ms']:.6f} ms")
        print(f"Average Inference Steps: {result['inference_steps']:.2f}")
        print(f"Peak Memory: {result['peak_memory_kb']:.2f} KB")
        print(f"Explanation Length: {result['explanation_length']:.2f} characters")

    with open("task7_results.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "rules",
                "latency_ms",
                "inference_steps",
                "peak_memory_kb",
                "explanation_length",
            ],
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nResults saved to task7_results.csv")


if __name__ == "__main__":
    main()
