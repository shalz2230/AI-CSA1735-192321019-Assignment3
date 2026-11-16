
"""
Task 7: Validate all 30 medication-safety test cases.
"""

from task7_test_cases import TEST_CASES
from task7_inference import check_prescription


def run_validation():
    passed = 0
    failed = 0

    print("=" * 65)
    print("HOSPITAL MEDICATION-SAFETY ADVISOR")
    print("30 TEST CASE VALIDATION")
    print("=" * 65)

    for case in TEST_CASES:
        result = check_prescription(case)

        expected = case["expected"]
        actual = result["decision"]

        if expected == actual:
            status = "PASS"
            passed += 1
        else:
            status = "FAIL"
            failed += 1

        print(
            f"Test {case['id']:02d} | "
            f"Expected: {expected:15s} | "
            f"Actual: {actual:15s} | {status}"
        )

    print("-" * 65)
    print("Total Tests :", len(TEST_CASES))
    print("Passed      :", passed)
    print("Failed      :", failed)

    accuracy = (passed / len(TEST_CASES)) * 100
    print(f"Accuracy    : {accuracy:.2f}%")

    if failed == 0:
        print("RESULT: ALL TEST CASES PASSED")
    else:
        print("RESULT: SOME TEST CASES FAILED")


if __name__ == "__main__":
    run_validation()
