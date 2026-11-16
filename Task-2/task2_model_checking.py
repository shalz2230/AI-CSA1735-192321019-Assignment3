
import itertools
import time
import csv

# Smart-building access-control propositions
SYMBOLS = [
    "BadgeValid",
    "DuringHours",
    "Employee",
    "Visitor",
    "HostApproval",
    "Escort",
    "Emergency",
    "AccessGranted",
    "DoorOpen",
    "Alarm",
    "RestrictedArea"
]

# Each clause is a disjunction of literals.
# A positive literal means True; "~" means False.
KB = [
    # Facts for the test scenario
    ("BadgeValid",),
    ("DuringHours",),
    ("Employee",),

    # Policy rules
    ("~BadgeValid", "~DuringHours", "~Employee", "AccessGranted"),
    ("~Visitor", "~HostApproval", "~Escort", "AccessGranted"),
    ("Emergency", "AccessGranted"),
    ("~AccessGranted", "DoorOpen"),
    ("~DoorOpen", "AccessGranted"),

    # Visitor must have host approval OR an emergency
    ("~Visitor", "HostApproval", "Emergency"),

    # Additional building policies
    ("~RestrictedArea", "Employee"),
    ("~Alarm", "Emergency"),
]

def literal_value(literal, model):
    if literal.startswith("~"):
        return not model[literal[1:]]
    return model[literal]

def evaluate_kb(model, clauses):
    evaluations = 0

    for clause in clauses:
        evaluations += 1

        if not any(literal_value(lit, model) for lit in clause):
            return False, evaluations

    return True, evaluations

def model_check(symbols, clauses, query):
    start = time.perf_counter()

    models = 0
    evaluations = 0
    query_true = False
    query_false = False

    for values in itertools.product([False, True], repeat=len(symbols)):
        model = dict(zip(symbols, values))
        models += 1

        valid, count = evaluate_kb(model, clauses)
        evaluations += count

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
    elif not query_true and not query_false:
        result = "INCONSISTENT KB"
    else:
        result = "NEITHER"

    return result, models, evaluations, elapsed


if __name__ == "__main__":
    print("SMART BUILDING - TRUTH TABLE MODEL CHECKING")
    print("=" * 55)
    print("Proposition symbols:", len(SYMBOLS))
    print("KB clauses:", len(KB))
    print("Possible models:", 2 ** len(SYMBOLS))

    queries = ["AccessGranted", "DoorOpen", "Alarm"]

    for query in queries:
        result, models, evaluations, elapsed = model_check(
            SYMBOLS, KB, query
        )

        print("\nQuery:", query)
        print("Result:", result)
        print("Models enumerated:", models)
        print("KB evaluations:", evaluations)
        print("Execution time:", round(elapsed, 6), "seconds")
