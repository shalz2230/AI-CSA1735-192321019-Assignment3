
import itertools
import time
import csv


def create_chain(length):
    """Create X0 and the implication chain X0 -> X1 -> ... -> Xn."""
    symbols = [f"X{i}" for i in range(length + 1)]

    # X0 is a known fact
    clauses = [{ "X0" }]

    # Xi -> Xi+1 is equivalent to ~Xi OR Xi+1
    for i in range(length):
        clauses.append({f"~X{i}", f"X{i+1}"})

    return symbols, clauses


def evaluate_clause(clause, model):
    for literal in clause:
        if literal.startswith("~"):
            if not model[literal[1:]]:
                return True
        elif model[literal]:
            return True

    return False


def model_check(symbols, clauses, query, max_models=2500000):
    total_models = 2 ** len(symbols)

    if total_models > max_models:
        return {
            "status": "SKIPPED",
            "models": 0,
            "evaluations": 0,
            "time": 0
        }

    start = time.perf_counter()
    models = 0
    evaluations = 0
    query_true = False
    query_false = False

    for values in itertools.product([False, True], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        models += 1
        valid = True

        for clause in clauses:
            evaluations += 1

            if not evaluate_clause(clause, model):
                valid = False
                break

        if valid:
            if model[query]:
                query_true = True
            else:
                query_false = True

    elapsed = time.perf_counter() - start

    if query_true and not query_false:
        result = "ENTAILED"
    elif query_false and not query_true:
        result = "NEGATION ENTAILED"
    else:
        result = "NEITHER"

    return {
        "status": result,
        "models": models,
        "evaluations": evaluations,
        "time": elapsed
    }


def negate(literal):
    return literal[1:] if literal.startswith("~") else "~" + literal


def unit_resolution(kb, query):
    """Resolution refutation using unit-clause preference."""
    start = time.perf_counter()

    clauses = set(frozenset(c) for c in kb)
    clauses.add(frozenset({negate(query)}))

    queue = [
        next(iter(c)) for c in clauses if len(c) == 1
    ]

    processed_units = set()
    attempts = 0
    generated = 0
    tautologies = 0
    subsumed = 0

    while queue:
        unit = queue.pop(0)

        if unit in processed_units:
            continue

        processed_units.add(unit)
        opposite = negate(unit)

        snapshot = list(clauses)

        for clause in snapshot:
            if opposite not in clause:
                continue

            attempts += 1
            new_clause = frozenset(clause - {opposite})
            generated += 1

            if any(negate(lit) in new_clause for lit in new_clause):
                tautologies += 1
                continue

            if not new_clause:
                return {
                    "status": "ENTAILED",
                    "clauses": len(clauses),
                    "generated": generated,
                    "attempts": attempts,
                    "tautologies": tautologies,
                    "subsumed": subsumed,
                    "time": time.perf_counter() - start
                }

            if new_clause in clauses:
                subsumed += 1
                continue

            if any(old.issubset(new_clause) for old in clauses):
                subsumed += 1
                continue

            supersets = {
                old for old in clauses
                if new_clause.issubset(old)
            }

            if supersets:
                clauses.difference_update(supersets)
                subsumed += len(supersets)

            clauses.add(new_clause)

            if len(new_clause) == 1:
                queue.append(next(iter(new_clause)))

    return {
        "status": "NOT ENTAILED",
        "clauses": len(clauses),
        "generated": generated,
        "attempts": attempts,
        "tautologies": tautologies,
        "subsumed": subsumed,
        "time": time.perf_counter() - start
    }


if __name__ == "__main__":
    rows = []

    print("TASK 2 - PERFORMANCE COMPARISON")
    print("=" * 65)

    for length in [10, 20, 40, 80]:
        symbols, kb = create_chain(length)
        query = f"X{length}"

        print(f"\nIMPLICATION CHAIN LENGTH: {length}")
        print("Proposition symbols:", len(symbols))
        print("Initial KB clauses:", len(kb))

        mc = model_check(symbols, kb, query)

        print("\nMODEL CHECKING")
        print("Result:", mc["status"])
        print("Models:", mc["models"])
        print("KB evaluations:", mc["evaluations"])
        print("Time:", round(mc["time"], 6))

        res = unit_resolution(kb, query)

        print("\nRESOLUTION")
        print("Result:", res["status"])
        print("Clauses stored:", res["clauses"])
        print("Clauses generated:", res["generated"])
        print("Resolution attempts:", res["attempts"])
        print("Tautologies:", res["tautologies"])
        print("Subsumed:", res["subsumed"])
        print("Time:", round(res["time"], 6))

        rows.append([
            length, len(symbols), len(kb),
            mc["status"], mc["models"], mc["evaluations"], mc["time"],
            res["status"], res["clauses"], res["generated"],
            res["attempts"], res["tautologies"], res["subsumed"],
            res["time"]
        ])

    # Additional non-entailed query
    symbols, kb = create_chain(10)
    non_query = "Y"

    non_result = unit_resolution(kb, non_query)

    print("\nNON-ENTAILED QUERY TEST")
    print("Query:", non_query)
    print("Resolution result:", non_result["status"])
    print("Resolution attempts:", non_result["attempts"])
    print("Execution time:", round(non_result["time"], 6))

    with open("Task-2/results.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            "Chain_Length", "Symbols", "Initial_Clauses",
            "MC_Result", "MC_Models", "MC_Evaluations", "MC_Time",
            "Resolution_Result", "Clauses_Stored", "Clauses_Generated",
            "Resolution_Attempts", "Tautologies", "Subsumed",
            "Resolution_Time"
        ])
        writer.writerows(rows)

    print("\nResults saved to Task-2/results.csv")
