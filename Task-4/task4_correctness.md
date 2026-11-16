# Task 4 – Correctness and Engineering Explanation

## 1. Why is lifted inference sound?

Lifted Modus Ponens applies a universally quantified rule using a substitution obtained through unification.

For example:

- Rule: Human(x) → Mortal(x)
- Fact: Human(Socrates)

Unification gives the substitution:

x = Socrates

Applying this substitution to the conclusion produces:

Mortal(Socrates)

The inference is sound because the substitution makes the rule premise identical to the known fact. Since the rule is universally quantified, it applies to Socrates as well.

## 2. Why can lifted inference avoid generating ground instances?

A universally quantified rule represents a general relationship. Lifted inference uses variables and unification to work with only the relevant terms.

For example:

Human(x) → Mortal(x)

Instead of generating a separate rule for every person, the inference engine can unify the rule with a relevant fact or query.

This can reduce unnecessary grounding when the domain contains many constants.

## 3. Why can propositionalisation still be useful?

Propositionalisation converts quantified rules into ground instances. It can be useful when:

- The domain is small and finite.
- The constants are already known.
- The same ground rules are queried repeatedly.
- Direct lookup is cheaper than repeated unification.
- The ground knowledge base fits within available memory.

## 4. Engineering decision

Lifted inference is useful when the domain is large and only a small part of the knowledge base is relevant to a query.

Propositionalisation can be preferable for a small, fixed domain where grounding is affordable and repeated queries can reuse the generated instances.

The final choice should be based on measured inference operations, grounding cost, memory usage and query frequency rather than expressiveness alone.