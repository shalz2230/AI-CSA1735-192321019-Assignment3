
"""
Task 7: Hospital Medication-Safety Advisor
Student B - Experimental Test Cases

Synthetic educational test data only.
Not intended for real medical decisions.
"""

TEST_CASES = [
    # Allergy cases
    {"id": 1, "allergies": ["DrugA"], "medicines": [], "conditions": [], "age": 30, "drug": "DrugA", "complete": True, "expected": "UNSAFE"},
    {"id": 2, "allergies": ["DrugB"], "medicines": [], "conditions": [], "age": 25, "drug": "DrugA", "complete": True, "expected": "SAFE"},
    {"id": 3, "allergies": ["DrugC"], "medicines": [], "conditions": [], "age": 40, "drug": "DrugC", "complete": True, "expected": "UNSAFE"},
    {"id": 4, "allergies": ["DrugA", "DrugB"], "medicines": [], "conditions": [], "age": 35, "drug": "DrugB", "complete": True, "expected": "UNSAFE"},
    {"id": 5, "allergies": [], "medicines": [], "conditions": [], "age": 28, "drug": "DrugA", "complete": True, "expected": "SAFE"},

    # Drug interaction cases
    {"id": 6, "allergies": [], "medicines": ["DrugX"], "conditions": [], "age": 45, "drug": "DrugY", "complete": True, "expected": "UNSAFE"},
    {"id": 7, "allergies": [], "medicines": ["DrugB"], "conditions": [], "age": 50, "drug": "DrugA", "complete": True, "expected": "SAFE"},
    {"id": 8, "allergies": [], "medicines": ["DrugM"], "conditions": [], "age": 60, "drug": "DrugN", "complete": True, "expected": "UNSAFE"},
    {"id": 9, "allergies": [], "medicines": ["DrugP"], "conditions": [], "age": 55, "drug": "DrugQ", "complete": True, "expected": "SAFE"},
    {"id": 10, "allergies": [], "medicines": ["DrugX", "DrugZ"], "conditions": [], "age": 42, "drug": "DrugY", "complete": True, "expected": "UNSAFE"},

    # Medical condition cases
    {"id": 11, "allergies": [], "medicines": [], "conditions": ["ConditionA"], "age": 40, "drug": "DrugC", "complete": True, "expected": "UNSAFE"},
    {"id": 12, "allergies": [], "medicines": [], "conditions": ["ConditionB"], "age": 32, "drug": "DrugA", "complete": True, "expected": "SAFE"},
    {"id": 13, "allergies": [], "medicines": [], "conditions": ["ConditionC"], "age": 65, "drug": "DrugD", "complete": True, "expected": "UNSAFE"},
    {"id": 14, "allergies": [], "medicines": [], "conditions": ["ConditionD"], "age": 48, "drug": "DrugB", "complete": True, "expected": "SAFE"},
    {"id": 15, "allergies": [], "medicines": [], "conditions": ["ConditionA", "ConditionC"], "age": 52, "drug": "DrugC", "complete": True, "expected": "UNSAFE"},

    # Age restriction cases
    {"id": 16, "allergies": [], "medicines": [], "conditions": [], "age": 10, "drug": "DrugE", "complete": True, "expected": "UNSAFE"},
    {"id": 17, "allergies": [], "medicines": [], "conditions": [], "age": 25, "drug": "DrugE", "complete": True, "expected": "SAFE"},
    {"id": 18, "allergies": [], "medicines": [], "conditions": [], "age": 15, "drug": "DrugF", "complete": True, "expected": "UNSAFE"},
    {"id": 19, "allergies": [], "medicines": [], "conditions": [], "age": 40, "drug": "DrugF", "complete": True, "expected": "SAFE"},
    {"id": 20, "allergies": [], "medicines": [], "conditions": [], "age": 8, "drug": "DrugA", "complete": True, "expected": "SAFE"},

    # Missing or incomplete information
    {"id": 21, "allergies": [], "medicines": [], "conditions": [], "age": None, "drug": "DrugA", "complete": False, "expected": "REVIEW_REQUIRED"},
    {"id": 22, "allergies": None, "medicines": [], "conditions": [], "age": 30, "drug": "DrugB", "complete": False, "expected": "REVIEW_REQUIRED"},
    {"id": 23, "allergies": [], "medicines": None, "conditions": [], "age": 45, "drug": "DrugC", "complete": False, "expected": "REVIEW_REQUIRED"},
    {"id": 24, "allergies": [], "medicines": [], "conditions": None, "age": 50, "drug": "DrugD", "complete": False, "expected": "REVIEW_REQUIRED"},
    {"id": 25, "allergies": [], "medicines": [], "conditions": [], "age": 35, "drug": "UnknownDrug", "complete": False, "expected": "REVIEW_REQUIRED"},

    # Multiple-risk and additional cases
    {"id": 26, "allergies": ["DrugA"], "medicines": ["DrugX"], "conditions": ["ConditionA"], "age": 12, "drug": "DrugA", "complete": True, "expected": "UNSAFE"},
    {"id": 27, "allergies": [], "medicines": ["DrugM"], "conditions": ["ConditionC"], "age": 70, "drug": "DrugN", "complete": True, "expected": "UNSAFE"},
    {"id": 28, "allergies": [], "medicines": [], "conditions": [], "age": 55, "drug": "DrugB", "complete": True, "expected": "SAFE"},
    {"id": 29, "allergies": ["DrugD"], "medicines": ["DrugP"], "conditions": [], "age": 22, "drug": "DrugD", "complete": True, "expected": "UNSAFE"},
    {"id": 30, "allergies": [], "medicines": ["DrugX"], "conditions": ["ConditionA"], "age": 60, "drug": "DrugY", "complete": True, "expected": "UNSAFE"},
]

if __name__ == "__main__":
    print("Total test cases:", len(TEST_CASES))
    for case in TEST_CASES:
        print(
            f"Test {case['id']:02d}: "
            f"Drug={case['drug']}, "
            f"Expected={case['expected']}"
        )
