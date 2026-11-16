
# TASK 6: Organisation Hierarchy Knowledge Base
# 10 Definite-Clause Rules
# Shared by Forward and Backward Chaining

# Atom format: (Predicate, argument1, argument2, ...)

# Rule format: (Head, Body)
# Example:
# (("Manager", "?x"), [("Employee", "?x")])

RULES = [

    # Rule 1: An employee reporting to someone is a direct report.
    (
        ("DirectReport", "?x", "?y"),
        [("Employee", "?x"), ("ReportsTo", "?x", "?y")]
    ),

    # Rule 2: A manager supervises their direct reports.
    (
        ("Supervises", "?y", "?x"),
        [("DirectReport", "?x", "?y")]
    ),

    # Rule 3: Two-level reporting relationship.
    (
        ("ReportsToIndirect", "?x", "?z"),
        [("ReportsTo", "?x", "?y"),
         ("ReportsTo", "?y", "?z")]
    ),

    # Rule 4: Extend the indirect reporting hierarchy.
    (
        ("ReportsToIndirect", "?x", "?z"),
        [("ReportsToIndirect", "?x", "?y"),
         ("ReportsTo", "?y", "?z")]
    ),

    # Rule 5: Employee reports to a manager.
    (
        ("UnderManager", "?x", "?y"),
        [("ReportsTo", "?x", "?y"),
         ("Manager", "?y")]
    ),

    # Rule 6: An employee is eligible when their manager can approve.
    (
        ("EligibleForApproval", "?x", "?r"),
        [("UnderManager", "?x", "?m"),
         ("CanApprove", "?m", "?r")]
    ),

    # Rule 7: Eligible employee's request is approved.
    (
        ("Approved", "?x", "?r"),
        [("Requests", "?x", "?r"),
         ("EligibleForApproval", "?x", "?r")]
    ),

    # Rule 8: A manager with approval authority is an approver.
    (
        ("Approver", "?x", "?r"),
        [("Manager", "?x"),
         ("CanApprove", "?x", "?r")]
    ),

    # Rule 9: Direct manager can approve an employee's request.
    (
        ("Approved", "?x", "?r"),
        [("ReportsTo", "?x", "?m"),
         ("Approver", "?m", "?r"),
         ("Requests", "?x", "?r")]
    ),

    # Rule 10: Higher-level manager can approve a request.
    (
        ("Approved", "?x", "?r"),
        [("ReportsToIndirect", "?x", "?m"),
         ("Approver", "?m", "?r"),
         ("Requests", "?x", "?r")]
    )
]


def generate_facts(number_of_employees):

    facts = []

    # Create an organisation hierarchy.
    for i in range(number_of_employees):

        employee = f"E{i}"
        manager = f"E{i-1}" if i > 0 else "CEO"

        facts.append(("Employee", employee))
        facts.append(("ReportsTo", employee, manager))

        facts.append(("Requests", employee, "Leave"))

    # CEO and selected employees are managers.
    facts.append(("Manager", "CEO"))
    facts.append(("CanApprove", "CEO", "Leave"))

    for i in range(0, number_of_employees, 10):
        facts.append(("Manager", f"E{i}"))
        facts.append(("CanApprove", f"E{i}", "Leave"))

    return facts


def display_knowledge_base():

    print("TASK 6 - ORGANISATION KNOWLEDGE BASE")
    print("=" * 55)

    print("\nTotal definite-clause rules:", len(RULES))

    print("\nRULE LIST")
    for i, (head, body) in enumerate(RULES, start=1):
        body_text = " AND ".join(map(str, body))
        print(f"R{i}: {head} <- {body_text}")

    print("\nSAMPLE FACTS")
    sample_facts = generate_facts(5)

    for fact in sample_facts[:12]:
        print(fact)

    print("\nSample base fact count:", len(sample_facts))


if __name__ == "__main__":
    display_knowledge_base()
