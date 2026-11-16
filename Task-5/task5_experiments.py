
# Task 5: Non-entailed query and step-cap experiment

from task5_cnf import knowledge_base
from task5_resolution import resolution_with_set_of_support


def run_experiments():

    print("\nEXPERIMENT 1: ENTAILED QUERY")
    print("=" * 55)

    # Query: Does an authorised employee exist?
    # Negated query: NOT Authorised(?x)

    entailed_query = [
        (False, ("Authorised", "?query"))
    ]

    result1 = resolution_with_set_of_support(
        knowledge_base,
        entailed_query,
        max_steps=5000
    )

    print("\nEntailed query result:", result1["proved"])

    print("\nEXPERIMENT 2: NON-ENTAILED QUERY")
    print("=" * 55)

    # Query: Is UnknownEmployee authorised?
    # Negated query: NOT Authorised(UnknownEmployee)

    non_entailed_query = [
        (False, ("Authorised", "UnknownEmployee"))
    ]

    result2 = resolution_with_set_of_support(
        knowledge_base,
        non_entailed_query,
        max_steps=50
    )

    print("\nNon-entailed query result:", result2["proved"])

    print("\nEXPERIMENT SUMMARY")
    print("=" * 55)

    print("Entailed query:")
    print("  Proved:", result1["proved"])
    print("  Resolution steps:", result1["resolution_steps"])
    print("  Unifications:", result1["unifications"])

    print("\nNon-entailed query:")
    print("  Proved:", result2["proved"])
    print("  Resolution steps:", result2["resolution_steps"])
    print("  Unifications:", result2["unifications"])
    print("  Step limit:", 50)


if __name__ == "__main__":
    run_experiments()
