
# TASK 7 – STAGE 2: DESIGN COMPARISON

## 1. Comparison of Initial Proposals

| Design Aspect | Student A | Student B |
|---|---|---|
| Knowledge Representation | First-Order Logic (FOL) | First-Order Logic (FOL) |
| Vocabulary | Patient, Drug, Allergy, Medicine, Condition, Prescription | Patient, Drug, Allergy, Medicine, Interaction, Safe, Unsafe |
| Inference Method | Backward Chaining | Forward Chaining |
| Explanation Method | Trace the rules used to prove an unsafe prescription | Record every rule that fires and its conclusion |

## 2. Areas of Agreement

Both students agree that:

1. First-Order Logic is suitable because general medical safety rules can be represented using variables and quantifiers.
2. Patient information should be stored as facts.
3. Medication allergies and drug interactions must be checked before approving a prescription.
4. The system must provide explanations for unsafe prescriptions.
5. The system should support future growth in medical rules and patient records.

## 3. Areas of Difference

Student A proposes backward chaining because it checks only rules relevant to the patient's prescription.

Student B initially proposes forward chaining because it can derive all possible safety warnings from patient facts.

Backward chaining may reduce unnecessary inference when only a few queries are requested. However, forward chaining can be useful when the hospital needs to generate alerts for many patients continuously.

## 4. Strengths and Weaknesses

### Student A – Backward Chaining

Strengths:
- Focuses on the requested safety query.
- Avoids processing many unrelated rules.
- Can produce a trace of the rules supporting a conclusion.

Weaknesses:
- Repeated subgoals can increase inference cost.
- Requires loop detection and efficient indexing.

### Student B – Forward Chaining

Strengths:
- Automatically derives warnings from available patient facts.
- Useful for generating multiple alerts.
- Can reuse derived conclusions.

Weaknesses:
- May generate conclusions unrelated to the current query.
- Can perform unnecessary work when the knowledge base is large.

## 5. Ideas Retained for the Joint Design

The final design retains:

1. First-Order Logic representation.
2. Backward chaining for query-focused medication safety checks.
3. Predicate indexing to locate relevant rules efficiently.
4. Substitution tracking during inference.
5. Explanation traces containing the fired rules and supporting facts.
6. A rule validation mechanism to prevent contradictory or incomplete safety decisions.

## 6. Final Decision

The group selects First-Order Logic with indexed backward chaining as the primary reasoning approach.

This design is suitable because the hospital expects a large knowledge base and individual prescription queries. The system can focus on relevant medication-safety rules instead of evaluating every rule for every query.
