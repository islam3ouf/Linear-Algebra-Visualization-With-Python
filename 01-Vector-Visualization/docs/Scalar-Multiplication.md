# Scalar Multiplication

## Introduction

Scalar multiplication is one of the most fundamental operations in linear algebra.

A **scalar** is a single numerical value (such as `2`, `0.5`, or `-1`), while a **vector** has both **magnitude** and **direction**.

When we multiply a vector by a scalar, every component of the vector is multiplied by that same number.

Mathematically,

\[
k \mathbf{v} = k(x, y) = (kx,\; ky)
\]

where:

- **k** → Scalar
- **v** → Vector

---

# What Happens During Scalar Multiplication?

Scalar multiplication changes the vector in predictable ways.

## 1. Magnitude (Length)

The magnitude is multiplied by the **absolute value** of the scalar.

If

\[
|\mathbf{v}| = L
\]

then

\[
|k\mathbf{v}| = |k|L
\]

This means:

| Scalar | Effect on Length |
|---------|------------------|
| `2` | Doubles the length |
| `3` | Triples the length |
| `0.5` | Half the length |
| `1` | No change |
| `0` | Becomes the zero vector |

---

## 2. Direction

The direction depends on the sign of the scalar.

### Positive Scalar (`k > 0`)

The vector keeps **exactly the same direction**.

```
v  ─────────►

2v ─────────────────────►
```

---

### Negative Scalar (`k < 0`)

The vector reverses its direction by **180°**.

```
v    ─────────►

-v   ◄─────────
```

---

### Zero Scalar (`k = 0`)

Every component becomes zero.

```
0v = (0,0)
```

The resulting vector has:

- Zero magnitude
- No specific direction

---

# Examples

Suppose

\[
\mathbf{v}=(2,3)
\]

---

## Example 1

Multiply by **2**

\[
2(2,3)
\]

Multiply every component:

\[
(2\times2,\;2\times3)
\]

Result:

\[
(4,6)
\]

**Effect**

- Length → Doubled
- Direction → Unchanged

---

## Example 2

Multiply by **0.5**

\[
0.5(2,3)
\]

Result

\[
(1,\;1.5)
\]

**Effect**

- Length → Half the original
- Direction → Unchanged

---

## Example 3

Multiply by **−1**

\[
-1(2,3)
\]

Result

\[
(-2,-3)
\]

**Effect**

- Length → Same as the original
- Direction → Reversed (180°)

---

# Visual Summary

| Scalar | New Vector | Length | Direction |
|---------|------------|---------|-----------|
| `2` | `(4,6)` | ×2 | Same |
| `0.5` | `(1,1.5)` | ×0.5 | Same |
| `-1` | `(-2,-3)` | Same | Opposite |
| `0` | `(0,0)` | Zero | None |

---

# Key Takeaways

- A scalar multiplies **every component** of a vector.
- The vector's **length scales by the absolute value** of the scalar.
- **Positive scalars** preserve direction.
- **Negative scalars** reverse direction.
- Multiplying by **zero** produces the **zero vector**.

---

> **Intuition:**  
> Think of a vector as an arrow. Scalar multiplication simply stretches, shrinks, or flips the arrow without changing its overall line of action.
