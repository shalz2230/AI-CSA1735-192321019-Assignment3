# Task 3 - University Exam Eligibility Advisor

## 1. Problem Statement
The University Exam Eligibility Advisor determines whether a
student is eligible to attend an examination using logical rules.

## 2. Eligibility Conditions
1. Minimum attendance percentage is 75%.
2. Required prerequisites must be cleared.
3. Examination fees must be paid.
4. The student must not have an active disciplinary block.
5. Approved leave is considered as an attendance exemption
   in the demonstration model.

## 3. Knowledge Base Vocabulary

- Student(x): x is a student.
- Course(c): c is a course.
- Attendance(x,c,p): attendance percentage of student x.
- PrerequisiteCleared(x,c): prerequisites are cleared.
- FeesPaid(x): fees are paid.
- DisciplinaryBlock(x): disciplinary restriction exists.
- ApprovedLeave(x,c): approved leave exists.
- Eligible(x,c): student is eligible for examination.

## 4. Logical Decision Rule

Eligible(x,c) is true when:
- Attendance is at least 75% or approved leave exemption exists.
- Prerequisites are cleared.
- Fees are paid.
- No disciplinary block exists.

## 5. Implementation Approaches
1. Propositional Logic
2. First-Order Logic

## 6. Evaluation
The two approaches will be compared using:
- Knowledge Base size
- Inference operation count
- Inference execution time
- Different numbers of students and courses

### 7. Assumptions

1. The minimum attendance requirement is configurable.
2. The attendance threshold used in this implementation is
   75% as a demonstration value.
3. Approved leave is recorded separately in the knowledge base.
4. Approved leave will be considered according to the
   eligibility rule defined in the knowledge base.
5. Prerequisite completion, fee payment and disciplinary
   status are treated as separate eligibility conditions.