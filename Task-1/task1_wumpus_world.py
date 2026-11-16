
import itertools
import time
import csv
import os


# ==========================================
# TASK 1 - PART A: WUMPUS WORLD
# Knowledge Base and Model Checking
# ==========================================

def get_neighbors(x, y, n):
    """Return valid neighboring squares."""
    neighbors = []

    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nx, ny = x + dx, y + dy

        if 1 <= nx <= n and 1 <= ny <= n:
            neighbors.append((nx, ny))

    return neighbors


def create_symbols(n):
    """Create propositional symbols for an n x n world."""
    symbols = []

    for x in range(1, n + 1):
        for y in range(1, n + 1):
            symbols.extend([
                f"P_{x}_{y}",
                f"W_{x}_{y}",
                f"B_{x}_{y}",
                f"S_{x}_{y}"
            ])

    return symbols


def create_knowledge_base(n):
    """
    Create Wumpus World rules.

    B(x,y) iff a neighboring square has a pit.
    S(x,y) iff a neighboring square has a Wumpus.
    """

    rules = []

    for x in range(1, n + 1):
        for y in range(1, n + 1):

            neighbors = get_neighbors(x, y, n)

            pit_neighbors = [f"P_{a}_{b}" for a, b in neighbors]
            wumpus_neighbors = [f"W_{a}_{b}" for a, b in neighbors]

            rules.append({
                "type": "breeze",
                "percept": f"B_{x}_{y}",
                "neighbors": pit_neighbors
            })

            rules.append({
                "type": "stench",
                "percept": f"S_{x}_{y}",
                "neighbors": wumpus_neighbors
            })

    # Starting square has no pit or Wumpus.
    rules.append({
        "type": "fact",
        "symbol": "P_1_1",
        "value": False
    })

    rules.append({
        "type": "fact",
        "symbol": "W_1_1",
        "value": False
    })

    return rules


def evaluate_kb(model, rules):
    """Evaluate all knowledge-base rules under one model."""
    evaluations = 0

    for rule in rules:
        evaluations += 1

        if rule["type"] == "fact":
            if model[rule["symbol"]] != rule["value"]:
                return False, evaluations

        elif rule["type"] == "breeze":
            expected = any(model[s] for s in rule["neighbors"])

            if model[rule["percept"]] != expected:
                return False, evaluations

        elif rule["type"] == "stench":
            expected = any(model[s] for s in rule["neighbors"])

            if model[rule["percept"]] != expected:
                return False, evaluations

    return True, evaluations


def model_check(symbols, rules, query):
    """
    Check whether KB entails query or its negation.

    Returns:
    ENTAILED
    NEGATION ENTAILED
    NEITHER
    """

    start = time.perf_counter()

    models_enumerated = 0
    kb_evaluations = 0

    query_true_model = False
    query_false_model = False

    for values in itertools.product([False, True], repeat=len(symbols)):

        model = dict(zip(symbols, values))
        models_enumerated += 1

        valid, evaluations = evaluate_kb(model, rules)
        kb_evaluations += evaluations

        if valid:
            if model[query]:
                query_true_model = True
            else:
                query_false_model = True

    elapsed = time.perf_counter() - start

    if query_true_model and not query_false_model:
        result = "ENTAILED"
    elif query_false_model and not query_true_model:
        result = "NEGATION ENTAILED"
    else:
        result = "NEITHER"

    return {
        "result": result,
        "models": models_enumerated,
        "evaluations": kb_evaluations,
        "time": elapsed
    }


# ==========================================
# MAIN EXPERIMENT
# ==========================================

if __name__ == "__main__":

    import csv

    print("=" * 60)
    print("TASK 1 - PERFORMANCE EXPERIMENTS")
    print("=" * 60)

    results = []

    # Full-symbol experiments
    for n in [2, 3, 4]:

        symbols = create_symbols(n)
        rules = create_knowledge_base(n)

        rules.append({
            "type": "fact",
            "symbol": "B_1_1",
            "value": True
        })

        total_models = 2 ** len(symbols)

        print(f"\nFULL SYMBOL SET: {n} x {n}")
        print("Symbols:", len(symbols))
        print("Theoretical models:", total_models)

        # Limit exhaustive enumeration to feasible cases.
        if total_models <= 100000:

            result = model_check(symbols, rules, "P_1_2")

            print("Models enumerated:", result["models"])
            print("KB evaluations:", result["evaluations"])
            print("Time:", result["time"])

            results.append([
                n, "Full", len(symbols), total_models,
                result["models"], result["evaluations"],
                result["time"], "Executed"
            ])

        else:
            print("Status: SKIPPED - computationally infeasible")

            results.append([
                n, "Full", len(symbols), total_models,
                0, 0, 0, "Skipped"
            ])

    # Query-specific local restriction.
    # Query: P_1_2, using the breeze information at (1,1).
    print("\n" + "=" * 60)
    print("RELEVANT-SYMBOL RESTRICTION")
    print("=" * 60)

    for n in [2, 3, 4]:

        symbols = create_symbols(n)
        rules = create_knowledge_base(n)

        rules.append({
            "type": "fact",
            "symbol": "B_1_1",
            "value": True
        })

        # Only the local breeze rule and relevant starting fact.
        relevant_symbols = [
            "P_1_2", "P_2_1", "P_2_1", "B_1_1"
        ]

        relevant_rules = [
            rule for rule in rules
            if (
                rule.get("percept") == "B_1_1"
            )
        ]

        result = model_check(
            relevant_symbols,
            relevant_rules,
            "P_1_2"
        )

        print(f"\nGrid: {n} x {n}")
        print("Relevant symbols:", len(relevant_symbols))
        print("Models enumerated:", result["models"])
        print("KB evaluations:", result["evaluations"])
        print("Result:", result["result"])
        print("Time:", result["time"])

        results.append([
            n, "Relevant", len(relevant_symbols),
            2 ** len(relevant_symbols),
            result["models"], result["evaluations"],
            result["time"], "Executed"
        ])

    # Save performance data.
    with open("Task-1/results.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Grid_Size",
            "Method",
            "Symbols",
            "Theoretical_Models",
            "Models_Enumerated",
            "KB_Evaluations",
            "Execution_Time",
            "Status"
        ])

        writer.writerows(results)

    print("\nPerformance results saved to Task-1/results.csv")
