
"""
Task 3 - Competency Query Suite
5 Success + 5 Failure + 5 Binding Queries
"""

from task3_fol import (
    STUDENTS,
    COURSES,
    STUDENT_FACTS,
    check_eligibility
)


# -------------------------------------------------
# 1. SUCCESS QUERIES
# -------------------------------------------------

def success_queries():
    print("\n--- 5 SUCCESS QUERIES ---")

    queries = [
        ("S1", "AI"),
        ("S1", "ML"),
        ("S1", "DBMS"),
        ("S5", "AI"),
        ("S5", "ML")
    ]

    for student, course in queries:
        result = check_eligibility(student, course)
        print(
            f"Query: Eligible({student},{course}) "
            f"=> {result['eligible']}"
        )


# -------------------------------------------------
# 2. FAILURE QUERIES
# -------------------------------------------------

def failure_queries():
    print("\n--- 5 FAILURE QUERIES ---")

    queries = [
        ("S2", "AI"),
        ("S2", "ML"),
        ("S3", "AI"),
        ("S4", "AI"),
        ("S4", "DBMS")
    ]

    for student, course in queries:
        result = check_eligibility(student, course)
        print(
            f"Query: Eligible({student},{course}) "
            f"=> {result['eligible']}"
        )


# -------------------------------------------------
# 3. BINDING QUERIES
# -------------------------------------------------

def binding_queries():
    print("\n--- 5 BINDING QUERIES ---")

    eligible_bindings = []

    for student in STUDENTS:
        for course in COURSES:
            result = check_eligibility(student, course)

            if result["eligible"]:
                eligible_bindings.append(
                    (student, course)
                )

    print("Query: Eligible(x,c)")
    print("Returned bindings:")

    for student, course in eligible_bindings:
        print(f"x = {student}, c = {course}")

    print("\nQuery: Student(x)")
    for student in STUDENTS:
        print(f"x = {student}")

    print("\nQuery: Course(c)")
    for course in COURSES:
        print(f"c = {course}")

    print("\nQuery: FeesPaid(x,c)")
    for student in STUDENTS:
        if STUDENT_FACTS[student]["fees_paid"]:
            for course in COURSES:
                print(f"x = {student}, c = {course}")

    print("\nQuery: ApprovedLeave(x,c)")
    for student in STUDENTS:
        if STUDENT_FACTS[student]["approved_leave"]:
            for course in COURSES:
                print(f"x = {student}, c = {course}")


# -------------------------------------------------
# MAIN
# -------------------------------------------------

if __name__ == "__main__":
    success_queries()
    failure_queries()
    binding_queries()

    print("\nTotal Competency Queries: 15")
    print("Query execution completed!")
