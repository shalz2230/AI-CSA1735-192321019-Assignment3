
# TASK 6: Forward Chaining Engine
# Uses the shared Task 6 knowledge base and Task 4 UNIFY.

import sys
from pathlib import Path


from task4_unify import unify, apply_substitution
from task6_knowledge_base import RULES


def build_fact_index(facts):
    """Group facts by predicate and argument count."""
    index = {}

    for fact in facts:
        key = (fact[0], len(fact))
        index.setdefault(key, []).append(fact)

    return index


def match_body(body, fact_index, substitution=None, stats=None):
    """Match rule-body atoms using indexed facts."""

    if substitution is None:
        substitution = {}

    if stats is None:
        stats = {"unifications": 0}

    if not body:
        return [substitution]

    first_atom = apply_substitution(body[0], substitution)

    key = (first_atom[0], len(first_atom))
    candidates = fact_index.get(key, [])

    results = []

    for fact in candidates:
        stats["unifications"] += 1

        new_sub = unify(first_atom, fact, substitution)

        if new_sub is not None:
            remaining = [
                apply_substitution(atom, new_sub)
                for atom in body[1:]
            ]

            results.extend(
                match_body(
                    remaining,
                    fact_index,
                    new_sub,
                    stats
                )
            )

    return results


def forward_chaining(initial_facts, query=None):

    facts = set(initial_facts)
    initial_count = len(facts)

    inferred_facts = set()

    rule_firings = 0
    redundant_derivations = 0
    iterations = 0
    unifications = 0

    while True:

        iterations += 1
        new_facts = set()

        fact_index = build_fact_index(facts)
        stats = {"unifications": 0}

        for head, body in RULES:

            substitutions = match_body(
                body,
                fact_index,
                stats=stats
            )

            for substitution in substitutions:

                rule_firings += 1

                derived = apply_substitution(head, substitution)

                # Only add fully grounded facts.
                if any(
                    isinstance(term, str) and term.startswith("?")
                    for term in derived
                ):
                    continue

                if derived not in facts and derived not in new_facts:
                    new_facts.add(derived)
                else:
                    redundant_derivations += 1

        unifications += stats["unifications"]

        print(
            f"Iteration {iterations}: "
            f"{len(new_facts)} new facts"
        )

        if not new_facts:
            break

        facts.update(new_facts)
        inferred_facts.update(new_facts)

    query_found = query in facts if query is not None else None

    relevant_count = sum(
        1 for fact in inferred_facts
        if query is not None and fact[0] == query[0]
    )

    irrelevant_count = len(inferred_facts) - relevant_count

    irrelevant_percentage = (
        (irrelevant_count / len(inferred_facts)) * 100
        if inferred_facts else 0
    )

    return {
        "base_facts": initial_count,
        "total_facts": len(facts),
        "inferred_facts": len(inferred_facts),
        "rule_firings": rule_firings,
        "redundant_derivations": redundant_derivations,
        "iterations": iterations,
        "unifications": unifications,
        "query_found": query_found,
        "irrelevant_percentage_proxy": round(
            irrelevant_percentage, 2
        )
    }


if __name__ == "__main__":
    print("Forward chaining module ready.")
