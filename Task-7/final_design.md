
# TASK 7 – STAGE 3: JOINT FINAL DESIGN

## 1. Problem Definition

The Hospital Medication-Safety Advisor is a knowledge-based system that checks whether a newly prescribed medicine is safe for a patient.

It uses patient information such as age, allergies, current medicines and medical conditions. The system identifies dangerous prescriptions and provides explanations for its decisions.

The proposed system is designed to support approximately 2,000 medical rules and 50,000 patient records.

## 2. Knowledge Representation

First-Order Logic (FOL) is selected because the system must represent general medical rules that apply to different patients and medicines.

FOL allows variables and reusable rules, avoiding the need to create separate rules for every patient.

## 3. Vocabulary

### Patient Predicates

- Patient(p): p is a registered patient.
- Age(p,a): patient p has age a.
- HasAllergy(p,d): patient p is allergic to drug d.
- Takes(p,d): patient p currently takes drug d.
- HasCondition(p,c): patient p has medical condition c.

### Medicine Predicates

- Medicine(d): d is a medicine.
- Treats(d,c): medicine d treats condition c.
- Interacts(d1,d2): medicines d1 and d2 have a harmful interaction.
- Contraindicated(d,c): medicine d is contraindicated for condition c.
- MinimumAge(d,a): medicine d has a minimum age requirement.

### Decision Predicates

- Prescribed(p,d): medicine d is prescribed to patient p.
- Unsafe(p,d): prescription is unsafe.
- Safe(p,d): prescription passes the configured safety checks.
- Reason(p,d,r): reason r explains the prescription decision.

## 4. Example FOL Safety Rules

R1 – Allergy Rule:

For every patient and medicine, if the patient is allergic to the prescribed medicine, the prescription is unsafe.

∀p,d [HasAllergy(p,d) ∧ Prescribed(p,d) → Unsafe(p,d)]

R2 – Drug Interaction Rule:

∀p,d1,d2 [Takes(p,d1) ∧ Interacts(d1,d2) ∧ Prescribed(p,d2) → Unsafe(p,d2)]

R3 – Medical Condition Rule:

∀p,d,c [HasCondition(p,c) ∧ Contraindicated(d,c) ∧ Prescribed(p,d) → Unsafe(p,d)]

R4 – Minimum Age Rule:

∀p,d,a [Age(p,a) ∧ MinimumAge(d,m) ∧ a < m ∧ Prescribed(p,d) → Unsafe(p,d)]

R5 – Safe Decision Rule:

∀p,d [Prescribed(p,d) ∧ ¬Unsafe(p,d) ∧ ChecksComplete(p,d) → Safe(p,d)]

Note: Numerical comparisons and negation in these rules require built-in predicates or a carefully defined rule-evaluation layer.

## 5. Inference Method

Indexed backward chaining is selected as the primary inference method.

The system begins with a query such as:

Unsafe(P101, DrugA)

It searches only the rules that can derive the requested predicate and attempts to prove their conditions using patient facts.

This reduces unnecessary inference for individual prescription queries.

## 6. Indexing and Scaling Strategy

To support 2,000 rules:

1. Maintain an index based on predicate names.
2. Group rules by their conclusion predicate.
3. Retrieve only rules relevant to the current goal.
4. Use memoisation to avoid repeated subgoal evaluation.
5. Apply loop detection to prevent infinite recursion.

To support 50,000 patients:

1. Store patient facts separately using patient identifiers.
2. Index facts by patient ID and predicate.
3. Retrieve only the requested patient's medical facts.
4. Avoid scanning the complete patient database for every query.

## 7. Explanation Mechanism

Every conclusion must maintain an explanation trace.

For example:

Patient: P101
Prescribed medicine: DrugA
Decision: UNSAFE

Explanation:
- Patient P101 has an allergy to DrugA.
- Rule R1 was activated.
- The allergy condition matches the prescribed medicine.
- Therefore, the prescription is classified as unsafe.

The system stores the supporting facts and rule identifiers for every warning.

## 8. Complete Pseudocode

FUNCTION CHECK_PRESCRIPTION(patient, drug):

    goal = UNSAFE(patient, drug)

    retrieve patient-specific facts
    retrieve rules indexed by goal predicate

    result = BACKWARD_CHAIN(goal, facts, rules)

    IF result is TRUE:
        return UNSAFE with explanation trace

    ELSE:
        verify that all required safety checks
        have sufficient and complete data

        IF checks are incomplete:
            return REVIEW_REQUIRED

        ELSE:
            return SAFE with checked-rule summary


FUNCTION BACKWARD_CHAIN(goal, facts, rules):

    IF goal exists in facts:
        return TRUE with supporting fact

    IF goal is already in current recursion path:
        return FAILURE

    retrieve rules indexed by goal predicate

    FOR each matching rule:

        standardise rule variables apart
        unify rule conclusion with goal

        IF unification succeeds:

            prove each rule condition recursively

            IF all conditions succeed:
                record rule and supporting facts
                return TRUE with explanation

    return FAILURE
