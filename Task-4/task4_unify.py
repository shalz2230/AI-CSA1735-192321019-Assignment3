
# Task 4: First-Order Logic Unification
# Supports substitutions, composition and occurs check.

def is_variable(term):
    return isinstance(term, str) and term.startswith("?")


def apply_substitution(term, substitution):
    """Apply substitutions recursively."""
    if is_variable(term):
        if term in substitution:
            return apply_substitution(substitution[term], substitution)
        return term

    if isinstance(term, tuple):
        return tuple(apply_substitution(x, substitution) for x in term)

    return term


def occurs(variable, term, substitution):
    """Check whether variable occurs inside term."""
    term = apply_substitution(term, substitution)

    if variable == term:
        return True

    if isinstance(term, tuple):
        return any(occurs(variable, x, substitution) for x in term)

    return False


def unify_variable(variable, term, substitution):
    if variable in substitution:
        return unify(
            substitution[variable], term, substitution
        )

    if is_variable(term) and term in substitution:
        return unify(
            variable, substitution[term], substitution
        )

    if occurs(variable, term, substitution):
        return None

    new_substitution = substitution.copy()
    new_substitution[variable] = term
    return new_substitution


def unify(x, y, substitution=None):
    """Return most general unifier (MGU), or None."""
    if substitution is None:
        substitution = {}

    x = apply_substitution(x, substitution)
    y = apply_substitution(y, substitution)

    if x == y:
        return substitution

    if is_variable(x):
        return unify_variable(x, y, substitution)

    if is_variable(y):
        return unify_variable(y, x, substitution)

    if isinstance(x, tuple) and isinstance(y, tuple):
        if len(x) != len(y) or x[0] != y[0]:
            return None

        current = substitution
        for a, b in zip(x[1:], y[1:]):
            current = unify(a, b, current)
            if current is None:
                return None

        return current

    return None


def compose_substitutions(theta1, theta2):
    """Compose theta1 and theta2."""
    result = {}

    for variable, term in theta1.items():
        result[variable] = apply_substitution(term, theta2)

    for variable, term in theta2.items():
        if variable not in result:
            result[variable] = apply_substitution(term, result)

    return result


def standardize_apart(expression, suffix):
    """Rename variables to make two clauses independent."""
    if is_variable(expression):
        return expression + suffix

    if isinstance(expression, tuple):
        return tuple(
            standardize_apart(x, suffix) for x in expression
        )

    return expression


def run_tests():
    tests = [
        (
            "Test 1: Simple variable substitution",
            ("Likes", "?x", "Mango"),
            ("Likes", "Ravi", "Mango")
        ),
        (
            "Test 2: Multiple substitutions",
            ("Knows", "?x", "?y"),
            ("Knows", "Anu", "Ravi")
        ),
        (
            "Test 3: Nested function terms",
            ("Parent", "?x", ("Father", "?x")),
            ("Parent", "Ravi", ("Father", "Ravi"))
        ),
        (
            "Test 4: Occurs check",
            "?x",
            ("Father", "?x")
        ),
        (
            "Test 5: Standardising apart",
            ("Parent", "?x", "?y"),
            ("Parent", "?x_2", "?y_2")
        )
    ]

    print("UNIFICATION TEST RESULTS")
    print("=" * 50)

    for name, term1, term2 in tests:
        result = unify(term1, term2)

        print("\n" + name)
        print("Term 1:", term1)
        print("Term 2:", term2)
        print("MGU:", result)

    print("\nSubstitution Composition")
    theta1 = {"?x": "?y"}
    theta2 = {"?y": "Ravi"}
    print(compose_substitutions(theta1, theta2))

    print("\nStandardising Apart Demonstration")
    clause = ("Knows", "?x", "?y")
    print("Original:", clause)
    print("Renamed:", standardize_apart(clause, "_2"))


if __name__ == "__main__":
    run_tests()
