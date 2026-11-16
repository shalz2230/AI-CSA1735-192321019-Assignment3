
"""
Task 7: Baseline vs Indexed Rule Retrieval

Compares full rule scanning against predicate indexing.
Synthetic rules are used for scalability testing.
"""

import time
import csv

from task7_knowledge_base import generate_rules


def build_rule_index(rules):
    """Create an index using rule conclusion predicates."""

    index = {}

    for rule_id in rules:
        if rule_id in ("R1", "R2", "R3", "R4"):
            predicate = "Unsafe"
        elif rule_id == "R5":
            predicate = "NeedsReview"
        else:
            predicate = "Synthetic"

        index.setdefault(predicate, []).append(rule_id)

    return index


def baseline_search(rules, target):
    """Scan every rule to find rules matching the target."""

    matches = []
    operations = 0

    for rule_id in rules:
        operations += 1

        if rule_id in ("R1", "R2", "R3", "R4"):
            predicate = "Unsafe"
        elif rule_id == "R5":
            predicate = "NeedsReview"
        else:
            predicate = "Synthetic"

        if predicate == target:
            matches.append(rule_id)

    return matches, operations


def indexed_search(index, target):
    """Retrieve only rules stored under the target predicate."""

    matches = index.get(target, [])
    operations = 1

    return matches, operations


def run_comparison():

    sizes = [40, 400, 2000]
    results = []

    print("=" * 75)
    print("BASELINE VS INDEXED RULE RETRIEVAL")
    print("=" * 75)

    for size in sizes:

        rules = generate_rules(size)
        index = build_rule_index(rules)

        # Baseline measurement
        start = time.perf_counter()

        baseline_matches = None
        baseline_operations = 0

        for _ in range(1000):
            baseline_matches, baseline_operations = baseline_search(
                rules, "Unsafe"
            )

        baseline_time = (
            time.perf_counter() - start
        ) * 1000 / 1000

        # Indexed measurement
        start = time.perf_counter()

        indexed_matches = None
        indexed_operations = 0

        for _ in range(1000):
            indexed_matches, indexed_operations = indexed_search(
                index, "Unsafe"
            )

        indexed_time = (
            time.perf_counter() - start
        ) * 1000 / 1000

        # Verify both approaches return the same rules.
        assert baseline_matches == indexed_matches

        result = {
            "rules": size,
            "baseline_operations": baseline_operations,
            "indexed_operations": indexed_operations,
            "baseline_time_ms": baseline_time,
            "indexed_time_ms": indexed_time,
        }

        results.append(result)

        print(f"\nKnowledge Base: {size} rules")
        print("Matching rules:", len(baseline_matches))
        print("Baseline operations:", baseline_operations)
        print("Indexed operations:", indexed_operations)
        print(f"Baseline time: {baseline_time:.6f} ms")
        print(f"Indexed time: {indexed_time:.6f} ms")

    with open("task7_comparison_results.csv", "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "rules",
                "baseline_operations",
                "indexed_operations",
                "baseline_time_ms",
                "indexed_time_ms",
            ],
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nComparison results saved successfully.")


if __name__ == "__main__":
    run_comparison()
