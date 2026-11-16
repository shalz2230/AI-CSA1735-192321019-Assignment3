
import time

# Same smart-building policy as the model-checking program
KB = [
    ("BadgeValid",),
    ("DuringHours",),
    ("Employee",),
    ("~BadgeValid", "~DuringHours", "~Employee", "AccessGranted"),
    ("~Visitor", "~HostApproval", "~Escort", "AccessGranted"),
    ("Emergency", "AccessGranted"),
    ("~AccessGranted", "DoorOpen"),
    ("~DoorOpen", "AccessGranted"),
    ("~Visitor", "HostApproval", "Emergency"),
    ("~RestrictedArea", "Employee"),
    ("~Alarm", "Emergency"),
]

def negate(literal):
    if literal.startswith("~"):
        return literal[1:]
    return "~" + literal

def is_tautology(clause):
    return any(negate(lit) in clause for lit in clause)

def resolve(c1, c2):
    resolvents = []

    for literal in c1:
        opposite = negate(literal)

        if opposite in c2:
            new_clause = (c1 - {literal}) | (c2 - {opposite})

            if not is_tautology(new_clause):
                resolvents.append(frozenset(new_clause))

    return resolvents

def resolution_entails(kb, query):
    start = time.perf_counter()

    clauses = []
    attempts = 0
    tautologies = 0
    subsumed = 0

    def add_clause(new_clause):
        nonlocal subsumed

        if is_tautology(new_clause):
            return False

        # Ignore a clause if an existing clause is its subset
        for old_clause in clauses:
            if old_clause.issubset(new_clause):
                subsumed += 1
                return False

        # Remove existing clauses that are supersets
        to_remove = [
            old for old in clauses
            if new_clause.issubset(old)
        ]

        for old in to_remove:
            clauses.remove(old)
            subsumed += 1

        clauses.append(new_clause)
        return True

    for clause in kb:
        add_clause(frozenset(clause))

    initial_count = len(clauses)

    # Resolution refutation: add the negation of the query
    add_clause(frozenset([negate(query)]))

    processed_pairs = set()

    while True:
        new_clauses = []

        for i in range(len(clauses)):
            for j in range(i + 1, len(clauses)):
                pair = (i, j)

                if pair in processed_pairs:
                    continue

                processed_pairs.add(pair)
                c1, c2 = clauses[i], clauses[j]

                for literal in c1:
                    if negate(literal) in c2:
                        attempts += 1

                resolvents = resolve(c1, c2)

                for resolvent in resolvents:
                    if len(resolvent) == 0:
                        elapsed = time.perf_counter() - start
                        return {
                            "result": "ENTAILED",
                            "clauses": len(clauses),
                            "attempts": attempts,
                            "tautologies": tautologies,
                            "subsumed": subsumed,
                            "time": elapsed
                        }

                    if add_clause(resolvent):
                        new_clauses.append(resolvent)

        if not new_clauses:
            elapsed = time.perf_counter() - start
            return {
                "result": "NOT ENTAILED",
                "clauses": len(clauses),
                "attempts": attempts,
                "tautologies": tautologies,
                "subsumed": subsumed,
                "time": elapsed
            }


if __name__ == "__main__":
    print("SMART BUILDING - RESOLUTION PROVER")
    print("=" * 55)
    print("Initial KB clauses:", len(KB))

    for query in ["AccessGranted", "DoorOpen", "Alarm"]:
        result = resolution_entails(KB, query)

        print("\nQuery:", query)
        print("Result:", result["result"])
        print("Clauses stored:", result["clauses"])
        print("Resolution attempts:", result["attempts"])
        print("Tautologies discarded:", result["tautologies"])
        print("Subsumed clauses:", result["subsumed"])
        print("Execution time:", round(result["time"], 6), "seconds")
