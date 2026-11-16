
# Task 4: Propositionalisation
# Instantiate universal rules using all ground constants.

from itertools import product

CONSTANTS = ["Ravi", "Anu", "Priya"]

PREDICATES = {
    "Human": 1,
    "Likes": 2,
    "Knows": 2
}


def generate_ground_atoms(constants, predicates):
    ground_atoms = []

    for predicate, arity in predicates.items():
        combinations = product(constants, repeat=arity)

        for arguments in combinations:
            atom = (predicate,) + arguments
            ground_atoms.append(atom)

    return ground_atoms


if __name__ == "__main__":
    atoms = generate_ground_atoms(CONSTANTS, PREDICATES)

    print("PROPOSITIONALISATION")
    print("=" * 40)
    print("Constants:", CONSTANTS)
    print("Predicate definitions:", PREDICATES)
    print("Ground atoms:")

    for atom in atoms:
        print(atom)

    print("\nTotal ground atoms:", len(atoms))
