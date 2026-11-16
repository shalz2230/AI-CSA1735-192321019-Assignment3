
# Task 5: First-Order Logic Resolution
# Strategy: Set of Support
# Reuses the UNIFY implementation from Task 4.

import sys
from pathlib import Path

TASK4_PATH = Path(__file__).resolve().parent.parent / "Task-4"
sys.path.insert(0, str(TASK4_PATH))

from task4_unify import unify, apply_substitution

from task5_cnf import knowledge_base


def rename_term(term, suffix):
    """Rename variables to standardise clauses apart."""
    if isinstance(term, tuple):
        return tuple(rename_term(item, suffix) for item in term)

    if isinstance(term, str) and term.startswith("?"):
        return term + "_" + str(suffix)

    return term


def rename_clause(clause, suffix):
    return [
        (positive, rename_term(atom, suffix))
        for positive, atom in clause
    ]


def apply_to_clause(clause, substitution):
    return [
        (positive, apply_substitution(atom, substitution))
        for positive, atom in clause
    ]


def is_tautology(clause):
    """Check whether a clause contains complementary identical literals."""
    for i, (sign1, atom1) in enumerate(clause):
        for sign2, atom2 in clause[i + 1:]:
            if sign1 != sign2 and atom1 == atom2:
                return True
    return False


def canonical_key(clause):
    """Create a key independent of variable names."""
    variable_map = {}

    def normalise(term):
        if isinstance(term, tuple):
            return tuple(normalise(item) for item in term)

        if isinstance(term, str) and term.startswith("?"):
            if term not in variable_map:
                variable_map[term] = f"?v{len(variable_map)}"
            return variable_map[term]

        return term

    normalised = [
        (sign, normalise(atom))
        for sign, atom in clause
    ]

    return tuple(sorted(normalised, key=repr))


def resolve_pair(clause1, clause2, suffix):
    """Resolve two clauses using the Task 4 unifier."""

    first = rename_clause(clause1, suffix)
    second = rename_clause(clause2, suffix + 1)

    resolvents = []
    unification_count = 0

    for i, (sign1, atom1) in enumerate(first):
        for j, (sign2, atom2) in enumerate(second):

            # Only complementary literals can be resolved.
            if sign1 == sign2:
                continue

            if atom1[0] != atom2[0] or len(atom1) != len(atom2):
                continue

            substitution = unify(atom1, atom2)
            unification_count += 1

            if substitution is None:
                continue

            remaining = (
                first[:i] + first[i + 1:] +
                second[:j] + second[j + 1:]
            )

            resolvent = apply_to_clause(remaining, substitution)

            # Remove duplicate literals.
            resolvent = list(dict.fromkeys(resolvent))

            if is_tautology(resolvent):
                continue

            resolvents.append(resolvent)

    return resolvents, unification_count


def display_clause(clause):
    if not clause:
        return "{}"

    parts = []

    for positive, atom in clause:
        name = atom[0]
        args = ", ".join(atom[1:])
        text = f"{name}({args})"

        if not positive:
            text = "~" + text

        parts.append(text)

    return " OR ".join(parts)


def resolution_with_set_of_support(
    kb,
    query_clause,
    max_steps=5000
):
    """
    Set of Support:
    At least one parent of each resolution must belong
    to the support set.
    """

    support = [query_clause]
    all_clauses = list(kb)

    seen = {
        canonical_key(clause)
        for clause in all_clauses + support
    }

    generated = 0
    resolution_steps = 0
    unifications = 0
    proof_length = 0
    suffix = 1

    print("\nFIRST-ORDER RESOLUTION")
    print("=" * 60)
    print("Strategy: Set of Support")
    print("Initial negated query:", display_clause(query_clause))

    while support and resolution_steps < max_steps:

        # Unit clauses are considered first.
        support.sort(key=len)
        current = support.pop(0)

        candidates = sorted(
            all_clauses + support,
            key=len
        )

        for other in candidates:

            if canonical_key(current) == canonical_key(other):
                continue

            resolvents, used_unifications = resolve_pair(
                current, other, suffix
            )
            suffix += 2

            unifications += used_unifications

            if used_unifications:
                resolution_steps += used_unifications

            for resolvent in resolvents:

                key = canonical_key(resolvent)

                if key in seen:
                    continue

                seen.add(key)
                generated += 1
                proof_length += 1

                print(
                    f"Derived clause {generated}:",
                    display_clause(resolvent)
                )

                if not resolvent:
                    print("\nSUCCESS: Empty clause derived.")
                    print("The query is proved by refutation.")

                    return {
                        "proved": True,
                        "generated_clauses": generated,
                        "resolution_steps": resolution_steps,
                        "unifications": unifications,
                        "proof_length": proof_length
                    }

                support.append(resolvent)

        if resolution_steps >= max_steps:
            break

    print("\nNo empty clause derived within the step limit.")

    return {
        "proved": False,
        "generated_clauses": generated,
        "resolution_steps": resolution_steps,
        "unifications": unifications,
        "proof_length": proof_length
    }


if __name__ == "__main__":

    # Original query:
    # EXISTS x Authorised(x)

    # Negated query for resolution refutation:
    # FOR ALL x NOT Authorised(x)

    negated_query = [
        (False, ("Authorised", "?query"))
    ]

    result = resolution_with_set_of_support(
        knowledge_base,
        negated_query
    )

    print("\nPERFORMANCE METRICS")
    print("-" * 40)

    for metric, value in result.items():
        print(f"{metric}: {value}")
