
"""
Task 7: Hospital Medication-Safety Advisor
Knowledge Base

All rules and medicine data are synthetic examples
for academic demonstration only.
"""

# -------------------------------------------------
# 1. Known medicines
# -------------------------------------------------

MEDICINES = {
    "DrugA", "DrugB", "DrugC", "DrugD",
    "DrugE", "DrugF", "DrugX", "DrugY",
    "DrugM", "DrugN", "DrugP", "DrugQ"
}


# -------------------------------------------------
# 2. Drug interaction facts
# -------------------------------------------------

INTERACTIONS = {
    ("DrugX", "DrugY"),
    ("DrugY", "DrugX"),
    ("DrugM", "DrugN"),
    ("DrugN", "DrugM")
}


# -------------------------------------------------
# 3. Contraindication facts
# -------------------------------------------------

CONTRAINDICATIONS = {
    ("DrugC", "ConditionA"),
    ("DrugD", "ConditionC")
}


# -------------------------------------------------
# 4. Minimum age restrictions
# -------------------------------------------------

MINIMUM_AGE = {
    "DrugE": 18,
    "DrugF": 18
}


# -------------------------------------------------
# 5. Knowledge Base Rules
# -------------------------------------------------

RULES = {
    "R1": {
        "name": "Allergy Rule",
        "description": "A medicine is unsafe if the patient is allergic to it."
    },

    "R2": {
        "name": "Drug Interaction Rule",
        "description": "A medicine is unsafe if it interacts with a current medicine."
    },

    "R3": {
        "name": "Medical Condition Rule",
        "description": "A medicine is unsafe if it is contraindicated for a patient condition."
    },

    "R4": {
        "name": "Minimum Age Rule",
        "description": "A medicine is unsafe if the patient is below its minimum age."
    },

    "R5": {
        "name": "Missing Information Rule",
        "description": "Incomplete patient information requires manual review."
    }
}


# -------------------------------------------------
# 6. Rule count generator for experiments
# -------------------------------------------------

def generate_rules(target_size):
    """
    Generate a knowledge base of the requested size.

    The five original safety rules are retained.
    Additional synthetic rules are added to test scalability.
    """

    if target_size < len(RULES):
        raise ValueError("Target size must be at least 5.")

    generated = dict(RULES)

    for i in range(len(RULES) + 1, target_size + 1):
        rule_id = f"R{i:04d}"

        generated[rule_id] = {
            "name": f"Synthetic Rule {i}",
            "description": (
                "Additional synthetic rule for "
                "knowledge-base scalability testing."
            )
        }

    return generated


if __name__ == "__main__":
    print("Hospital Medication-Safety Knowledge Base")
    print("-----------------------------------------")
    print("Known medicines:", len(MEDICINES))
    print("Drug interactions:", len(INTERACTIONS))
    print("Contraindications:", len(CONTRAINDICATIONS))
    print("Age restrictions:", len(MINIMUM_AGE))
    print("Original safety rules:", len(RULES))

    for size in (40, 400, 2000):
        generated = generate_rules(size)
        print(f"Knowledge Base Size: {len(generated)} rules")
