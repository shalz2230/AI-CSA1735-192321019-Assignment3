
# Task 5: First-Order Logic to CNF Conversion
# Skolemisation and clause representation

# Literal format:
# (True,  ("Predicate", "argument1", ...))  = Positive literal
# (False, ("Predicate", "argument1", ...)) = Negative literal

# Clause 1:
# Every employee who handled a restricted document is authorised.
#
# ~Employee(x) OR ~Document(y) OR ~Handles(x,y)
# OR ~Restricted(y) OR Authorised(x)

C1 = [
    (False, ("Employee", "?x")),
    (False, ("Document", "?y")),
    (False, ("Handles", "?x", "?y")),
    (False, ("Restricted", "?y")),
    (True, ("Authorised", "?x"))
]

# Clause 2:
# Every document containing patient data is restricted.
#
# ~Document(y) OR ~PatientData(y) OR Restricted(y)

C2 = [
    (False, ("Document", "?y")),
    (False, ("PatientData", "?y")),
    (True, ("Restricted", "?y"))
]

# Clause 3:
# There exists an employee who handled every audited document.
#
# Skolemisation:
# Existential employee is replaced by sk_employee.

C3 = [
    (True, ("Employee", "sk_employee"))
]

C4 = [
    (False, ("Document", "?y")),
    (False, ("Audited", "?y")),
    (True, ("Handles", "sk_employee", "?y"))
]

# Clause 4: Facts about report R1

C5 = [
    (True, ("Document", "R1"))
]

C6 = [
    (True, ("PatientData", "R1"))
]

C7 = [
    (True, ("Audited", "R1"))
]

# Complete Knowledge Base

knowledge_base = [
    C1, C2, C3, C4, C5, C6, C7
]

def display_clause(clause):
    literals = []

    for positive, atom in clause:
        name = atom[0]
        arguments = ", ".join(atom[1:])
        literal = f"{name}({arguments})"

        if not positive:
            literal = "~" + literal

        literals.append(literal)

    return " OR ".join(literals)


def display_knowledge_base():
    print("\nTASK 5 - CNF KNOWLEDGE BASE")
    print("=" * 60)

    for index, clause in enumerate(knowledge_base, start=1):
        print(f"C{index}: {display_clause(clause)}")

    print("\nTotal CNF clauses:", len(knowledge_base))
    print("Skolem constant: sk_employee")


if __name__ == "__main__":
    display_knowledge_base()
