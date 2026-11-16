
# TASK 6: Backward Chaining Engine
# Uses Task 4 UNIFY implementation.
# Includes substitutions, loop checking and depth limit.

import sys
from pathlib import Path

TASK4_PATH = Path(__file__).resolve().parent.parent / "Task-4"
sys.path.insert(0, str(TASK4_PATH))

from task4_unify import unify, apply_substitution
from task6_knowledge_base import RULES, generate_facts


def rename_term(term, suffix):
    if isinstance(term, tuple):
        return tuple(rename_term(x, suffix) for x in term)

    if isinstance(term, str) and term.startswith("?"):
        return term + "_" + str(suffix)

    return term


def rename_rule(head, body, suffix):
    return (
        rename_term(head, suffix),
        [rename_term(atom, suffix) for atom in body]
    )


def merge_substitutions(old, new):
    """Combine substitutions and apply the newer bindings."""
    result = {
        key: apply_substitution(value, new)
        for key, value in old.items()
    }

    for key, value in new.items():
        result[key] = apply_substitution(value, new)

    return result


def goal_key(goal):
    """Canonical form for detecting repeated variant goals."""
    variable_map = {}

    def normalise(term):
        if isinstance(term, tuple):
            return tuple(normalise(x) for x in term)

        if isinstance(term, str) and term.startswith("?"):
            if term not in variable_map:
                variable_map[term] = f"?v{len(variable_map)}"
            return variable_map[term]

        return term

    return normalise(goal)


class BackwardChainer:

    def __init__(self, facts, max_depth=100):
        self.facts = list(facts)
        self.max_depth = max_depth
        self.goals_expanded = 0
        self.unifications = 0
        self.max_depth_reached = 0
        self.repeated_subgoals = 0
        self.rule_applications = 0
        self.counter = 0

    def prove(self, goal, substitution=None, path=None, depth=0):

        if substitution is None:
            substitution = {}

        if path is None:
            path = set()

        self.max_depth_reached = max(
            self.max_depth_reached, depth
        )

        if depth > self.max_depth:
            return []

        goal = apply_substitution(goal, substitution)
        key = goal_key(goal)

        # Loop checking prevents repeated variant goals.
        if key in path:
            self.repeated_subgoals += 1
            return []

        self.goals_expanded += 1
        new_path = path | {key}

        answers = []

        # First: Match the goal against existing facts.
        for fact in self.facts:

            if fact[0] != goal[0] or len(fact) != len(goal):
                continue

            self.unifications += 1
            theta = unify(goal, fact)

            if theta is not None:
                answers.append(
                    merge_substitutions(substitution, theta)
                )

        # Second: Match the goal against rule heads.
        for head, body in RULES:

            if head[0] != goal[0] or len(head) != len(goal):
                continue

            self.counter += 1
            renamed_head, renamed_body = rename_rule(
                head, body, self.counter
            )

            self.unifications += 1
            theta = unify(goal, renamed_head)

            if theta is None:
                continue

            self.rule_applications += 1

            combined = merge_substitutions(
                substitution, theta
            )

            grounded_body = [
                apply_substitution(atom, combined)
                for atom in renamed_body
            ]

            partial_answers = [combined]

            # Prove each body goal in order.
            for subgoal in grounded_body:

                next_answers = []

                for answer in partial_answers:
                    next_answers.extend(
                        self.prove(
                            subgoal,
                            answer,
                            new_path,
                            depth + 1
                        )
                    )

                partial_answers = next_answers

                if not partial_answers:
                    break

            answers.extend(partial_answers)

        return answers

    def metrics(self):
        return {
            "goals_expanded": self.goals_expanded,
            "unifications": self.unifications,
            "maximum_depth": self.max_depth_reached,
            "repeated_subgoals": self.repeated_subgoals,
            "rule_applications": self.rule_applications
        }


def run_backward_query(facts, query, max_depth=100):

    engine = BackwardChainer(
        facts,
        max_depth=max_depth
    )

    answers = engine.prove(query)

    return answers, engine.metrics()


if __name__ == "__main__":

    facts = generate_facts(5)

    print("\nBACKWARD CHAINING")
    print("=" * 55)

    # E2 reports to E1, and E1 reports to E0.
    # E0 is a manager who can approve Leave.
    query = ("Approved", "E2", "Leave")

    answers, metrics = run_backward_query(facts, query)

    print("Query:", query)
    print("Query proved:", bool(answers))
    print("Number of answers:", len(answers))

    print("\nBACKWARD CHAINING METRICS")
    print("-" * 40)

    for key, value in metrics.items():
        print(f"{key}: {value}")

    print("\nLEFT-RECURSION TEST")
    print("-" * 40)

    # Rule 4 is left-recursive:
    # ReportsToIndirect(x,z) <-
    # ReportsToIndirect(x,y), ReportsTo(y,z)

    recursive_query = (
        "ReportsToIndirect", "E4", "CEO"
    )

    answers2, metrics2 = run_backward_query(
        facts,
        recursive_query,
        max_depth=30
    )

    print("Recursive query:", recursive_query)
    print("Query proved:", bool(answers2))
    print("Repeated subgoals:", metrics2["repeated_subgoals"])
    print("Maximum depth:", metrics2["maximum_depth"])
    print("Loop checking prevented repeated expansion.")
