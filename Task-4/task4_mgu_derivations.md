# Task 4 – Most General Unifier (MGU) Derivations

## 1. Simple variable substitution

**Term 1:** P(?x, Ravi)  
**Term 2:** P(Anu, Ravi)

Unification equations:

- ?x = Anu
- Ravi = Ravi

**MGU:** {?x / Anu}

Both terms become P(Anu, Ravi).

## 2. Multiple variable substitutions

**Term 1:** Likes(?x, ?y)  
**Term 2:** Likes(Ravi, Mango)

Unification equations:

- ?x = Ravi
- ?y = Mango

**MGU:** {?x / Ravi, ?y / Mango}

Both terms become Likes(Ravi, Mango).

## 3. Nested function terms

**Term 1:** Parent(?x, Father(?y))  
**Term 2:** Parent(Anu, Father(Ravi))

Unification equations:

- ?x = Anu
- Father(?y) = Father(Ravi)
- ?y = Ravi

**MGU:** {?x / Anu, ?y / Ravi}

Both terms become Parent(Anu, Father(Ravi)).

## 4. Occurs check

**Term 1:** ?x  
**Term 2:** Father(?x)

The equation requires:

?x = Father(?x)

The variable ?x occurs inside the term Father(?x). Binding it would create an infinite recursive term.

**Result:** Unification fails (None).

The occurs check prevents this invalid substitution.

## 5. Standardising apart

Consider two clauses:

- Clause 1: Parent(?x, ?y)
- Clause 2: Parent(?y, ?z)

Before combining clauses, rename the variables in Clause 2:

- Clause 1: Parent(?x, ?y)
- Clause 2: Parent(?y_2, ?z_2)

Now unify the arguments:

- ?x = ?y_2
- ?y = ?z_2

**MGU:** {?x / ?y_2, ?y / ?z_2}

Standardising apart prevents variables from different clauses from being treated as the same variable accidentally.

## Conclusion

The most general unifier finds the least restrictive substitution that makes two expressions identical. The occurs check prevents infinite terms, while standardising apart protects the independence of variables belonging to different clauses.