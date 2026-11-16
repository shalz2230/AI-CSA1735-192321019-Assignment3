# Task 3 - Knowledge Base Defect Log

## Defect 1: Missing Student Facts

Problem:
The inference function raised a NameError because
STUDENTS, COURSES and STUDENT_FACTS were not defined.

Fix:
Defined student identifiers, course identifiers and
student eligibility facts in the knowledge base.

Verification:
The FOL program executed and displayed eligibility results.

## Defect 2: Approved Leave Handling

Problem:
Approved leave alone should not automatically satisfy
the attendance requirement.

Fix:
Attendance exemption is considered only when both
ApprovedLeave and AttendanceWaiver are true.

Verification:
Student S5 with approved leave and official waiver
satisfies the attendance condition.

## Defect 3: Missing Eligibility Conditions

Problem:
A student could be incorrectly treated as eligible if
prerequisite, fee or disciplinary conditions were ignored.

Fix:
The eligibility evaluation checks attendance,
prerequisite completion, fee payment and disciplinary
status separately.

Verification:
Students S2, S3 and S4 fail eligibility because
they do not satisfy all required conditions.

## Conclusion

Three knowledge base defects were identified,
corrected and verified through program execution.
