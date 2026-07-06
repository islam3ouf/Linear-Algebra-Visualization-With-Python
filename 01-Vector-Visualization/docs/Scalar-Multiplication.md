# 📏 Scalar Multiplication

Scalar multiplication is one of the most fundamental operations in Linear Algebra. It describes how a vector changes when multiplied by a single number called a **scalar**.

A **scalar** changes the **size** of a vector and, in some cases, its **direction**, while preserving its overall geometric nature.

---

## 📖 What is a Scalar?

A **scalar** is a single numerical value, for example:

- `2`
- `0.5`
- `-1`
- `3`
- `0`

Unlike vectors, scalars have **magnitude only** and no direction.

---

## 📖 What is Scalar Multiplication?

Given a vector

$$
\mathbf{v}=(x,y)
$$

and a scalar

$$
k
$$

their multiplication is

$$
k\mathbf{v}=(kx,ky)
$$

This means **every component of the vector is multiplied by the same scalar**.

> **Key Idea**
>
> Scalar multiplication affects the vector's **length** and sometimes its **direction**, but it does **not** change the angle unless the scalar is negative.

---

# 📐 Effect on Magnitude (Length)

The magnitude of the new vector is scaled by the absolute value of the scalar.

| Scalar | Effect on Length |
|--------:|------------------|
| `k > 1` | Longer |
| `0 < k < 1` | Shorter |
| `k = 1` | No change |
| `k = 0` | Zero vector |
| `k < 0` | Length is multiplied by `|k|` |

### Examples

| Scalar | Length Change |
|---------|---------------|
| `2` | Twice as long |
| `3` | Three times longer |
| `0.5` | Half as long |
| `0.25` | Quarter as long |

---

# 🧭 Effect on Direction

The sign of the scalar determines whether the vector keeps or reverses its direction.

## Positive Scalar (`k > 0`)

- Direction remains the same.
- Only the length changes.

Example:

```
v   --------->

2v  ---------------------->
```

---

## Negative Scalar (`k < 0`)

- Direction is reversed.
- Length changes by `|k|`.

Example:

```
v   --------->

-v  <---------
```

---

## Zero Scalar (`k = 0`)

Every component becomes zero.

$$
0\mathbf{v}=(0,0)
$$

The result is called the **zero vector**.

Properties:

- Magnitude = 0
- No direction

---

# 🧮 Worked Examples

Suppose

$$
\mathbf{v}=(2,3)
$$

---

## Example 1

Multiply by **2**

$$
2(2,3)
$$

Multiply each component:

$$
(2\times2,\;2\times3)
$$

Result

$$
(4,6)
$$

**Observation**

- Length doubles.
- Direction stays the same.

---

## Example 2

Multiply by **0.5**

$$
0.5(2,3)
$$

Result

$$
(1,1.5)
$$

**Observation**

- Length becomes half.
- Direction stays the same.

---

## Example 3

Multiply by **−1**

$$
-1(2,3)
$$

Result

$$
(-2,-3)
$$

**Observation**

- Length stays the same.
- Direction is reversed by **180°**.

---

# 📊 Summary Table

| Scalar | Result | Length | Direction |
|---------|---------|--------|-----------|
| `2` | `(4,6)` | ×2 | Same |
| `0.5` | `(1,1.5)` | ×0.5 | Same |
| `-1` | `(-2,-3)` | Same | Opposite |
| `0` | `(0,0)` | Zero | None |

---

# 💡 Key Takeaways

- Every vector component is multiplied by the scalar.
- The vector's magnitude is multiplied by the **absolute value** of the scalar.
- A **positive scalar** keeps the same direction.
- A **negative scalar** reverses the direction.
- Multiplying by **zero** produces the **zero vector**.

---

## 🎯 Intuition

Imagine holding an arrow.

- Multiply by **2** → the arrow becomes twice as long.
- Multiply by **0.5** → the arrow becomes shorter.
- Multiply by **−1** → the arrow points in the opposite direction.
- Multiply by **0** → the arrow disappears into a single point at the origin.

This simple operation is the foundation of **vector scaling**, **linear transformations**, and many concepts in computer graphics, machine learning, physics, and engineering.
