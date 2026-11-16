
"""
Task 3 - Performance Comparison
Propositional Logic vs First-Order Logic
"""

import csv
import time
import os

MIN_ATTENDANCE = 75

# -------------------------------------------------
# PROPOSITIONAL LOGIC SIMULATION
# -------------------------------------------------

def propositional_inference(students, courses):

    operations = 0

    for student in range(students):
        for course in range(courses):

            attendance = 80
            prerequisite = True
            fees_paid = True
            disciplinary_block = False

            operations += 4

            eligible = (
                attendance >= MIN_ATTENDANCE
                and prerequisite
                and fees_paid
                and not disciplinary_block
            )

            operations += 4

    return operations


def propositional_kb_size(students, courses):
    # Four conditions and one eligibility rule per pair
    return students * courses * 5


# -------------------------------------------------
# FIRST-ORDER LOGIC SIMULATION
# -------------------------------------------------

def fol_inference(students, courses):

    operations = 0

    for student in range(students):
        for course in range(courses):

            attendance = 80
            prerequisite = True
            fees_paid = True
            disciplinary_block = False

            operations += 4

            eligible = (
                attendance >= MIN_ATTENDANCE
                and prerequisite
                and fees_paid
                and not disciplinary_block
            )

            operations += 4

    return operations


def fol_kb_size(students, courses):
    # Fixed general axioms + individual facts
    general_axioms = 12
    individual_facts = students * courses * 4
    return general_axioms + individual_facts


# -------------------------------------------------
# PERFORMANCE MEASUREMENT
# -------------------------------------------------

def measure_performance():

    test_sizes = [
        (5, 3),
        (10, 5),
        (20, 10),
        (50, 20),
        (100, 30)
    ]

    results = []

    print("\n--- PERFORMANCE COMPARISON ---")

    for students, courses in test_sizes:

        start = time.perf_counter()
        prop_ops = propositional_inference(students, courses)
        prop_time = time.perf_counter() - start

        start = time.perf_counter()
        fol_ops = fol_inference(students, courses)
        fol_time = time.perf_counter() - start

        prop_size = propositional_kb_size(students, courses)
        fol_size = fol_kb_size(students, courses)

        row = {
            "Students": students,
            "Courses": courses,
            "Propositional_KB_Size": prop_size,
            "FOL_KB_Size": fol_size,
            "Propositional_Operations": prop_ops,
            "FOL_Operations": fol_ops,
            "Propositional_Time": prop_time,
            "FOL_Time": fol_time
        }

        results.append(row)

        print(
            f"Students={students}, Courses={courses}, "
            f"Prop KB={prop_size}, FOL KB={fol_size}, "
            f"Prop Ops={prop_ops}, FOL Ops={fol_ops}"
        )

    # Save results in CSV
    output_path = os.path.join(
        os.path.dirname(__file__), "results.csv"
    )

    with open(output_path, "w", newline="") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )
        writer.writeheader()
        writer.writerows(results)

    print("\nResults saved to Task-3/results.csv")


if __name__ == "__main__":
    measure_performance()
