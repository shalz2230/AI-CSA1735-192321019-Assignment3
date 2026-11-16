
# TASK 6: Forward vs Backward Chaining Performance
# Tests 100, 1000 and 10000 base facts.

import csv
import time

from task6_knowledge_base import generate_facts
from task6_forward import forward_chaining
from task6_backward import run_backward_query



def generate_scaled_facts(target_size):
    """
    Generate exactly target_size facts.
    Keep CEO approval facts at the beginning so
    they are never removed by truncation.
    """

    facts = [
        ("Manager", "CEO"),
        ("CanApprove", "CEO", "Leave")
    ]

    number_of_employees = (target_size - 2) // 3

    for i in range(number_of_employees):
        employee = f"E{i}"

        facts.append(("Employee", employee))
        facts.append(("ReportsTo", employee, "CEO"))
        facts.append(("Requests", employee, "Leave"))

    # Pad remaining slots with irrelevant facts.
    counter = 0

    while len(facts) < target_size:
        facts.append(("Unrelated", f"U{counter}"))
        counter += 1

    return facts[:target_size]



def run_benchmark():

    sizes = [100, 1000, 10000]
    results = []

    print("\nTASK 6 PERFORMANCE COMPARISON")
    print("=" * 65)

    for size in sizes:

        print(f"\nTesting with {size} base facts...")

        facts = generate_scaled_facts(size)

        # Query uses an employee whose facts are present.
        query = ("Approved", "E0", "Leave")

        # Forward chaining
        start = time.perf_counter()

        forward_metrics = forward_chaining(
            facts,
            query
        )

        forward_time = time.perf_counter() - start

        # Backward chaining
        start = time.perf_counter()

        answers, backward_metrics = run_backward_query(
            facts,
            query,
            max_depth=100
        )

        backward_time = time.perf_counter() - start

        row = {
            "base_facts": len(facts),

            "forward_time_seconds": round(forward_time, 6),
            "forward_inferred_facts":
                forward_metrics["inferred_facts"],
            "forward_rule_firings":
                forward_metrics["rule_firings"],
            "forward_iterations":
                forward_metrics["iterations"],
            "forward_query_found":
                forward_metrics["query_found"],

            "backward_time_seconds": round(backward_time, 6),
            "backward_goals_expanded":
                backward_metrics["goals_expanded"],
            "backward_unifications":
                backward_metrics["unifications"],
            "backward_maximum_depth":
                backward_metrics["maximum_depth"],
            "backward_repeated_subgoals":
                backward_metrics["repeated_subgoals"],
            "backward_query_found": bool(answers)
        }

        results.append(row)

        print("Base facts:", len(facts))
        print("Forward query found:", row["forward_query_found"])
        print("Backward query found:", row["backward_query_found"])
        print("Forward time:", forward_time)
        print("Backward time:", backward_time)

    # Save raw results.
    with open("results.csv", "w", newline="") as file:

        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)

    print("\nRESULTS SAVED TO results.csv")
    print("=" * 65)

    for row in results:
        print(row)


if __name__ == "__main__":
    run_benchmark()
