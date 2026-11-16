
from task4_unify import unify, apply_substitution

# Rule: Human(x) -> Mortal(x)
RULE = {
    "premise": ("Human", "?x"),
    "conclusion": ("Mortal", "?x")
}

FACTS = [
    ("Human", "Socrates"),
    ("Human", "Plato"),
    ("Human", "Aristotle"),
    ("Animal", "Tiger")
]


def lifted_modus_ponens(rule, facts):
    inferred = []
    inference_steps = 0

    for fact in facts:
        inference_steps += 1
        substitution = unify(rule["premise"], fact)

        if substitution is not None:
            result = apply_substitution(
                rule["conclusion"], substitution
            )

            if result not in facts and result not in inferred:
                inferred.append(result)

    return inferred, inference_steps


if __name__ == "__main__":
    results, steps = lifted_modus_ponens(RULE, FACTS)

    print("LIFTED MODUS PONENS")
    print("=" * 40)
    print("Initial facts:", FACTS)
    print("Rule:", RULE)
    print("Inferred facts:", results)
    print("Inference steps:", steps)
