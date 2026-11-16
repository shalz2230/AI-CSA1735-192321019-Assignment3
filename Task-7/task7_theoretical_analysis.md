
# TASK 7 – THEORETICAL VALIDATION
## Student A Responsibility

### 1. Soundness of the Inference Method

The proposed system uses First-Order Logic with definite Horn clauses and backward chaining.

The inference method is sound when every conclusion produced by the system follows logically from the knowledge base.

For example:

Fact:
HasAllergy(P101, DrugA)

Fact:
Prescribed(P101, DrugA)

Rule R1:
HasAllergy(p,d) AND Prescribed(p,d) -> Unsafe(p,d)

Conclusion:
Unsafe(P101, DrugA)

The conclusion is logically supported by the facts and rule. Therefore, the system does not produce an unsafe conclusion without a valid derivation.

### 2. Completeness of the Inference Method

SLD-resolution, which is the basis of backward chaining for definite logic programs, is complete for definite-clause programs under suitable conditions.

For ground atomic queries, if a logical proof exists, a fair search strategy can find that proof.

However, a practical depth-first implementation may fail to find a proof if recursion or search-depth restrictions are not handled carefully.

Therefore, the implementation uses indexing, loop detection and controlled search.

### 3. Query Complexity

Let:

- R = total number of rules.
- F = total number of facts.
- B = average number of relevant rules for a goal.
- D = maximum inference depth.

A naive implementation may scan all rules and facts repeatedly.

Its cost can grow significantly with the size of the knowledge base.

The proposed indexed implementation retrieves only rules matching the goal predicate and facts belonging to the requested patient.

Its practical performance depends mainly on the relevant rules and facts rather than the entire database.

A simplified search estimate is O(B^D) in the worst case for branching backward chaining.

This is not a guaranteed complexity bound for every implementation. General logical inference can be computationally expensive.

Indexing reduces unnecessary searches but does not remove worst-case complexity.

### 4. Effect of Restricting the Knowledge Base to Definite Clauses

Definite clauses contain exactly one positive conclusion and zero or more conditions.

Advantages:

1. They support forward and backward chaining.
2. They provide a straightforward rule execution mechanism.
3. SLD-resolution is suitable for proving queries.
4. They simplify explanation generation.
5. They support efficient indexing by conclusion predicate.

Limitations:

1. They cannot directly express arbitrary disjunction in rule conclusions.
2. Negation requires additional assumptions or an extended representation.
3. Uncertain medical knowledge cannot be fully represented using ordinary definite clauses.
4. Complex numerical conditions may require built-in predicates.

### 5. Conclusion

First-Order Logic with definite Horn clauses and indexed backward chaining is suitable for the proposed educational medication-safety advisor.

The approach provides traceable conclusions and avoids scanning unrelated rules for every prescription query.

However, soundness depends on correct rules and facts, while completeness depends on the inference strategy and search conditions.

The system is a demonstration and must not be used for actual clinical prescribing decisions.
