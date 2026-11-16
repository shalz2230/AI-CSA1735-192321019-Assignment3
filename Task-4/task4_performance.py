# Task 4: Performance Analysis
# Ground-clause growth, predicate arity, function terms,
# and lifted versus propositional inference.

import csv
import time
from itertools import product
from task4_unify import unify, apply_substitution

RESULT_FILE = "results.csv"


def ground_clause_count(k, arity):
    """Number of ground instances for one arity-r universal rule."""
    return k ** arity


def function_term_count(k, max_depth):
    """
    One unary function f and k constants.
    Count all terms with depth from 0 to max_depth.
    """
    return k * (max_depth + 1)


def build_facts(constants):
    """Create P(a) facts for every constant."""
    return {("P", constant) for constant in constants}


def lifted_query(constants, target,facts):
    """
    Backward lifted inference for:
        P(x) -> Q(x)
    Query:
        Q(target)

    The rule conclusion is unified with the query.
    """
    rule_conclusion = ("Q", "?x")
    query = ("Q", target)

    unification_count = 1
    theta = unify(rule_conclusion, query)

    if theta is None:
        return False, unification_count, 0

    required_fact = apply_substitution(("P", "?x"), theta)
    fact_lookups = 1

    return required_fact in facts, unification_count, fact_lookups


def build_propositional_kb(constants):
    """
    Ground all instances of:
        P(x) -> Q(x)

    Store each ground rule in a dictionary for direct lookup.
    """
    ground_rules = {}

    for constant in constants:
        ground_rules[("Q", constant)] = ("P", constant)

    return ground_rules


def propositional_query(ground_rules, facts, target):
    """Check the corresponding ground rule for the query."""
    query = ("Q", target)
    lookup_count = 1

    if query not in ground_rules:
        return False, lookup_count

    required_fact = ground_rules[query]
    return required_fact in facts, lookup_count


def measure_comparison(k, repetitions=1000):
    constants = [f"C{i}" for i in range(k)]
    target = constants[-1]

    # Measure propositional KB construction separately.
    start = time.perf_counter()
    ground_rules = build_propositional_kb(constants)
    build_time = time.perf_counter() - start

    facts = build_facts(constants)

    # Measure lifted inference.
    start = time.perf_counter()
    lifted_result = False

    for _ in range(repetitions):
        lifted_result, unifications, lifted_lookups = lifted_query(
    constants, target, facts
)
        

    lifted_time = (time.perf_counter() - start) / repetitions

    # Measure propositional inference.
    start = time.perf_counter()
    prop_result = False

    for _ in range(repetitions):
        prop_result, prop_lookups = propositional_query(
            ground_rules, facts, target
        )

    prop_time = (time.perf_counter() - start) / repetitions

    return {
        "constants": k,
        "ground_clauses": len(ground_rules),
        "lifted_unifications": unifications,
        "lifted_fact_lookups": lifted_lookups,
        "propositional_lookups": prop_lookups,
        "lifted_inference_time_ms": lifted_time * 1000,
        "propositional_build_time_ms": build_time * 1000,
        "propositional_inference_time_ms": prop_time * 1000,
        "lifted_result": lifted_result,
        "propositional_result": prop_result
    }


def save_results(rows):
    with open(RESULT_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=rows[0].keys())
        writer.writeheader()
        writer.writerows(rows)


def main():
    print("TASK 4 PERFORMANCE EXPERIMENT")
    print("=" * 65)

    # Experiment 1: Ground clauses as constants increase.
    sizes = [3, 5, 10, 15, 20, 25, 30]
    rows = []

    print("\n1. Ground clause growth and inference comparison")

    for k in sizes:
        result = measure_comparison(k)
        rows.append(result)

        print(
            f"k={k:2d} | "
            f"Ground clauses={result['ground_clauses']:4d} | "
            f"Lifted={result['lifted_inference_time_ms']:.6f} ms | "
            f"Propositional={result['propositional_inference_time_ms']:.6f} ms"
        )

    # Experiment 2: Predicate arity growth.
    print("\n2. Ground clause growth by predicate arity")

    fixed_k = 10

    for arity in [1, 2, 3, 4]:
        count = ground_clause_count(fixed_k, arity)
        print(
            f"Constants={fixed_k}, Arity={arity}, "
            f"Ground clauses={count}"
        )

    # Experiment 3: Function-symbol term-depth growth.
    print("\n3. Function symbol term-depth growth")

    fixed_k = 5

    for depth in range(0, 6):
        count = function_term_count(fixed_k, depth)
        print(
            f"Constants={fixed_k}, Maximum depth={depth}, "
            f"Ground terms={count}"
        )

    save_results(rows)

    print("\nCSV saved successfully:", RESULT_FILE)
    print("All experiments completed.")


if __name__ == "__main__":
    main()