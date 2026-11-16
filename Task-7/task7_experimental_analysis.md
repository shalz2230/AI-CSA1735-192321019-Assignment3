
# TASK 7 – EXPERIMENTAL VALIDATION AND ANALYSIS
## Student B Responsibility

### 1. Objective

The experimental evaluation checks the behaviour and scalability of the Hospital Medication-Safety Advisor.

The experiments evaluate:

- Correctness using 30 synthetic test cases.
- Knowledge base sizes of 40, 400 and 2,000 rules.
- Rule retrieval operations.
- Average retrieval execution time.
- Memory usage.
- Explanation length.

### 2. Test Case Evaluation

A total of 30 synthetic test cases were prepared.

The test cases cover:

1. Drug allergies.
2. Harmful drug interactions.
3. Medical condition contraindications.
4. Minimum age restrictions.
5. Incomplete patient information.
6. Multiple simultaneous safety risks.
7. Prescriptions without matching safety warnings.

The expected outcomes are compared against the actual inference engine decisions.

The following measures are used:

Accuracy = (Correct Predictions / Total Test Cases) × 100

The actual number of passed and failed tests is obtained by running `task7_validate.py`.

### 3. Knowledge Base Sizes

Three knowledge base sizes are evaluated:

| Experiment | Number of Rules |
|---|---:|
| Small KB | 40 |
| Medium KB | 400 |
| Large KB | 2,000 |

The five original safety rules are retained. Additional synthetic rules are used as scalability placeholders and do not produce medical conclusions.

### 4. Baseline and Indexed Retrieval

Two rule retrieval approaches are compared.

**Baseline approach:**

The baseline scans every rule to find rules matching the requested conclusion predicate.

**Indexed approach:**

The indexed approach retrieves rules from a dictionary organised by conclusion predicate.

The comparison uses the same knowledge base and query predicate for both approaches.

The results are saved in `task7_comparison_results.csv`.

### 5. Performance Metrics

The following metrics are recorded:

- Rule retrieval operations.
- Average retrieval execution time in milliseconds.
- Peak memory usage in kilobytes.
- Explanation length in characters.
- Inference steps.

The measurements are stored in:

- `task7_results.csv`
- `task7_comparison_results.csv`

### 6. Graph Analysis

Three graphs are generated:

1. `task7_operations.png`
2. `task7_execution_time.png`
3. `task7_indexed_scalability.png`

The operation comparison illustrates the difference between scanning all rules and retrieving rules through an index.

The execution-time graph shows the measured retrieval time for each knowledge base size.

The indexed scalability graph illustrates the lookup-operation count under the simplified dictionary-index benchmark.

### 7. Interpretation

The baseline retrieval method examines every rule, so its rule inspection count increases with knowledge base size.

The indexed method uses a predicate-based dictionary lookup, avoiding a complete scan of unrelated rules.

However, the indexed method still needs to process all matching rules and evaluate their conditions during actual inference.

Therefore, a single dictionary lookup should not be interpreted as the total cost of proving a prescription-safety query.

The experimental results demonstrate the benefit of indexing for rule retrieval, while the full reasoning engine requires further performance testing.

### 8. Limitations

1. The medicine data and rules are synthetic.
2. The generated additional rules are placeholders.
3. The benchmark measures rule retrieval separately from full inference.
4. Execution time can vary depending on the machine and environment.
5. The memory measurement depends on the Python runtime and measurement method.
6. The implementation is not suitable for real clinical decisions.

### 9. Conclusion

The experimental evaluation provides a basic comparison of baseline scanning and indexed rule retrieval at three knowledge base sizes.

The results help assess how indexing can reduce unnecessary rule inspections.

The system also demonstrates how logical rules can produce explainable medication-safety warnings using patient-specific information.
