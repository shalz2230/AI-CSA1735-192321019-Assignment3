
"""
Task 3 - University Exam Eligibility Advisor
First-Order Logic (FOL) Knowledge Base

12 quantified axioms, including an existential statement.
"""

# -------------------------------------------------
# 1. CONFIGURATION
# -------------------------------------------------

MIN_ATTENDANCE = 75


# -------------------------------------------------
# 2. FOL VOCABULARY
# -------------------------------------------------

VOCABULARY = {
    "Student(x)": "x is a student",
    "Course(c)": "c is a course",
    "Enrolled(x,c)": "Student x is enrolled in course c",
    "Attendance(x,c,p)": "Attendance percentage of x in c is p",
    "PrerequisiteCleared(x,c)": "Prerequisites are cleared",
    "FeesPaid(x,c)": "Course fees are paid",
    "DisciplinaryBlock(x,c)": "Student has a disciplinary restriction",
    "ApprovedLeave(x,c)": "Student has approved leave",
    "AttendanceWaiver(x,c)": "Attendance waiver is officially granted",
    "AttendanceSatisfied(x,c)": "Attendance condition is satisfied",
    "PrerequisiteSatisfied(x,c)": "Prerequisite condition is satisfied",
    "FeeConditionSatisfied(x,c)": "Fee condition is satisfied",
    "DisciplineConditionSatisfied(x,c)": "Disciplinary condition is satisfied",
    "Eligible(x,c)": "Student is eligible for examination",
    "NotEligible(x,c)": "Student is not eligible for examination"
}

# -------------------------------------------------
# STUDENT AND COURSE DATA
# -------------------------------------------------

STUDENTS = ["S1", "S2", "S3", "S4", "S5"]

COURSES = ["AI", "ML", "DBMS"]

STUDENT_FACTS = {
    "S1": {
        "attendance": 85,
        "prerequisite": True,
        "fees_paid": True,
        "disciplinary_block": False,
        "approved_leave": False,
        "attendance_waiver": False
    },
    "S2": {
        "attendance": 60,
        "prerequisite": True,
        "fees_paid": True,
        "disciplinary_block": False,
        "approved_leave": False,
        "attendance_waiver": False
    },
    "S3": {
        "attendance": 90,
        "prerequisite": False,
        "fees_paid": True,
        "disciplinary_block": False,
        "approved_leave": False,
        "attendance_waiver": False
    },
    "S4": {
        "attendance": 80,
        "prerequisite": True,
        "fees_paid": False,
        "disciplinary_block": False,
        "approved_leave": False,
        "attendance_waiver": False
    },
    "S5": {
        "attendance": 65,
        "prerequisite": True,
        "fees_paid": True,
        "disciplinary_block": False,
        "approved_leave": True,
        "attendance_waiver": True
    }
}


# -------------------------------------------------
# 3. FIRST-ORDER LOGIC AXIOMS
# -------------------------------------------------

AXIOMS = [

    # Axiom 1: Attendance requirement
    "A1: ∀x∀c∀p [(Student(x) ∧ Course(c) ∧ Enrolled(x,c) "
    "∧ Attendance(x,c,p) ∧ p >= 75) → AttendanceSatisfied(x,c)]",

    # Axiom 2: Approved leave with official waiver
    "A2: ∀x∀c [(Student(x) ∧ Course(c) ∧ Enrolled(x,c) "
    "∧ ApprovedLeave(x,c) ∧ AttendanceWaiver(x,c)) "
    "→ AttendanceSatisfied(x,c)]",

    # Axiom 3: Prerequisite condition
    "A3: ∀x∀c [(Student(x) ∧ Course(c) ∧ Enrolled(x,c) "
    "∧ PrerequisiteCleared(x,c)) → PrerequisiteSatisfied(x,c)]",

    # Axiom 4: Fee condition
    "A4: ∀x∀c [(Student(x) ∧ Course(c) ∧ FeesPaid(x,c)) "
    "→ FeeConditionSatisfied(x,c)]",

    # Axiom 5: No disciplinary restriction
    "A5: ∀x∀c [(Student(x) ∧ Course(c) "
    "∧ ¬DisciplinaryBlock(x,c)) "
    "→ DisciplineConditionSatisfied(x,c)]",

    # Axiom 6: General eligibility rule
    "A6: ∀x∀c [(Enrolled(x,c) ∧ AttendanceSatisfied(x,c) "
    "∧ PrerequisiteSatisfied(x,c) "
    "∧ FeeConditionSatisfied(x,c) "
    "∧ DisciplineConditionSatisfied(x,c)) "
    "→ Eligible(x,c)]",

    # Axiom 7: Attendance failure
    "A7: ∀x∀c [(Enrolled(x,c) ∧ ¬AttendanceSatisfied(x,c)) "
    "→ NotEligible(x,c)]",

    # Axiom 8: Prerequisite failure
    "A8: ∀x∀c [(Enrolled(x,c) ∧ ¬PrerequisiteSatisfied(x,c)) "
    "→ NotEligible(x,c)]",

    # Axiom 9: Fee failure
    "A9: ∀x∀c [(Enrolled(x,c) ∧ ¬FeeConditionSatisfied(x,c)) "
    "→ NotEligible(x,c)]",

    # Axiom 10: Disciplinary restriction
    "A10: ∀x∀c [(Enrolled(x,c) ∧ DisciplinaryBlock(x,c)) "
    "→ NotEligible(x,c)]",

    # Axiom 11: Eligible students must be enrolled
    "A11: ∀x∀c [Eligible(x,c) → Enrolled(x,c)]",

    # Axiom 12: Existential statement
    "A12: ∃x Student(x)"
]


# -------------------------------------------------
# 4. DISPLAY KNOWLEDGE BASE
# -------------------------------------------------

def display_knowledge_base():

    print("=" * 65)
    print("UNIVERSITY EXAM ELIGIBILITY ADVISOR")
    print("FIRST-ORDER LOGIC KNOWLEDGE BASE")
    print("=" * 65)

    print("\nMinimum Attendance:", MIN_ATTENDANCE, "%")

    print("\n--- FOL VOCABULARY ---")

    for predicate, meaning in VOCABULARY.items():
        print(f"{predicate:35} : {meaning}")

    print("\n--- FIRST-ORDER LOGIC AXIOMS ---")

    for axiom in AXIOMS:
        print(axiom)

    print("\nTotal FOL Axioms:", len(AXIOMS))
    print("Existential Axiom Included: Yes")
    print("Universal Quantifiers Included: Yes")

    print("\nFOL Knowledge Base Loaded Successfully!")


# -------------------------------------------------
# 7. FOL INFERENCE ENGINE
# -------------------------------------------------

def check_eligibility(student, course):

    facts = STUDENT_FACTS[student]

    attendance_ok = (
        facts["attendance"] >= MIN_ATTENDANCE
        or (
            facts["approved_leave"]
            and facts["attendance_waiver"]
        )
    )

    prerequisite_ok = facts["prerequisite"]
    fees_ok = facts["fees_paid"]
    discipline_ok = not facts["disciplinary_block"]

    eligible = (
        attendance_ok
        and prerequisite_ok
        and fees_ok
        and discipline_ok
    )

    return {
        "student": student,
        "course": course,
        "attendance": attendance_ok,
        "prerequisite": prerequisite_ok,
        "fees": fees_ok,
        "discipline": discipline_ok,
        "eligible": eligible
    }


def display_eligibility_results():

    print("\n--- FOL INFERENCE RESULTS ---")

    for student in STUDENTS:
        for course in COURSES:

            result = check_eligibility(student, course)

            status = (
                "ELIGIBLE"
                if result["eligible"]
                else "NOT ELIGIBLE"
            )

            print(
                f'{student} | {course} | {status}'
            )



# -------------------------------------------------
# 5. MAIN PROGRAM
# -------------------------------------------------

if __name__ == "__main__":
    display_knowledge_base()
    display_eligibility_results()

# -------------------------------------------------
# 6. STUDENT AND COURSE FACTS
# -------------------------------------------------

# STUDENT AND COURSE DATA

STUDENTS = ["S1", "S2", "S3", "S4", "S5"]

COURSES = ["AI", "ML", "DBMS"]

STUDENT_FACTS = {
    "S1": {
        "attendance": 85,
        "prerequisite": True,
        "fees_paid": True,
        "disciplinary_block": False,
        "approved_leave": False,
        "attendance_waiver": False
    },
    "S2": {
        "attendance": 60,
        "prerequisite": True,
        "fees_paid": True,
        "disciplinary_block": False,
        "approved_leave": False,
        "attendance_waiver": False
    },
    "S3": {
        "attendance": 90,
        "prerequisite": False,
        "fees_paid": True,
        "disciplinary_block": False,
        "approved_leave": False,
        "attendance_waiver": False
    },
    "S4": {
        "attendance": 80,
        "prerequisite": True,
        "fees_paid": False,
        "disciplinary_block": False,
        "approved_leave": False,
        "attendance_waiver": False
    },
    "S5": {
        "attendance": 65,
        "prerequisite": True,
        "fees_paid": True,
        "disciplinary_block": False,
        "approved_leave": True,
        "attendance_waiver": True
    }
}
