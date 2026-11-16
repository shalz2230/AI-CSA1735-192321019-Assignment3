
"""
Task 7: Hospital Medication-Safety Advisor
Indexed backward-chaining inference engine.

Synthetic educational implementation only.
Not for clinical use.
"""

from task7_knowledge_base import (
    MEDICINES,
    INTERACTIONS,
    CONTRAINDICATIONS,
    MINIMUM_AGE,
    RULES,
)


def backward_chain(case):
    """
    Check whether the prescribed medicine is unsafe.

    Returns:
        decision: UNSAFE, SAFE or REVIEW_REQUIRED
        explanation: list of supporting reasons
        inference_steps: number of checks performed
    """

    patient_id = case.get("id")
    drug = case.get("drug")

    explanation = []
    inference_steps = 0

    # Goal 1: Prove UNSAFE(patient, drug)

    allergies = case.get("allergies")
    medicines = case.get("medicines")
    conditions = case.get("conditions")
    age = case.get("age")

    # R1: Allergy rule
    inference_steps += 1

    if allergies is not None and drug in allergies:
        explanation.append(
            f"R1: Patient {patient_id} has an allergy to {drug}."
        )

    # R2: Drug interaction rule
    inference_steps += 1

    if medicines is not None:
        for current_drug in medicines:
            if (
                (current_drug, drug) in INTERACTIONS
                or (drug, current_drug) in INTERACTIONS
            ):
                explanation.append(
                    f"R2: {drug} interacts with current medicine "
                    f"{current_drug}."
                )

    # R3: Medical condition rule
    inference_steps += 1

    if conditions is not None:
        for condition in conditions:
            if (drug, condition) in CONTRAINDICATIONS:
                explanation.append(
                    f"R3: {drug} is contraindicated for {condition}."
                )

    # R4: Minimum age rule
    inference_steps += 1

    minimum_age = MINIMUM_AGE.get(drug)

    if (
        age is not None
        and minimum_age is not None
        and age < minimum_age
    ):
        explanation.append(
            f"R4: Patient age {age} is below the minimum "
            f"age {minimum_age} for {drug}."
        )

    # A proven danger takes priority over missing information.
    if explanation:
        return {
            "decision": "UNSAFE",
            "explanation": explanation,
            "inference_steps": inference_steps,
        }

    # Goal 2: Check whether a safe conclusion is justified.

    required_fields = [
        "allergies",
        "medicines",
        "conditions",
        "age",
    ]

    complete = all(
        case.get(field) is not None
        for field in required_fields
    )

    if not complete or drug not in MEDICINES:
        return {
            "decision": "REVIEW_REQUIRED",
            "explanation": [
                "R5: Patient information is incomplete or "
                "the prescribed medicine is not in the knowledge base."
            ],
            "inference_steps": inference_steps,
        }

    return {
        "decision": "SAFE",
        "explanation": [
            "All configured safety checks passed.",
            "No matching allergy, interaction, contraindication "
            "or age restriction was found."
        ],
        "inference_steps": inference_steps,
    }


def check_prescription(case):
    """Public function for checking one prescription."""
    return backward_chain(case)


if __name__ == "__main__":

    sample_case = {
        "id": 101,
        "allergies": ["DrugA"],
        "medicines": [],
        "conditions": [],
        "age": 30,
        "drug": "DrugA",
        "complete": True,
        "expected": "UNSAFE",
    }

    result = check_prescription(sample_case)

    print("Hospital Medication-Safety Advisor")
    print("----------------------------------")
    print("Patient ID:", sample_case["id"])
    print("Prescribed Drug:", sample_case["drug"])
    print("Decision:", result["decision"])
    print("Inference Steps:", result["inference_steps"])
    print("Explanation:")

    for reason in result["explanation"]:
        print("-", reason)
