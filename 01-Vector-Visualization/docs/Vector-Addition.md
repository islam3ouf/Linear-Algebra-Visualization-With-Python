# ➕ Vector Addition

Vector addition is one of the most fundamental operations in Linear Algebra.  
It allows us to combine two or more vectors into a single vector that represents their overall effect.

Think of a vector as a movement:
- Move according to the first vector.
- Then move according to the second vector.
- The final position is represented by the **resultant vector**.

---

# 📖 Geometric Interpretation

A vector represents both **magnitude** (length) and **direction**.

Adding vectors does **not** mean adding their lengths.

Instead, we combine their directions and displacements to obtain a new vector.

If

\[
\mathbf{u}=\begin{bmatrix}x_1\\y_1\end{bmatrix},
\qquad
\mathbf{v}=\begin{bmatrix}x_2\\y_2\end{bmatrix}
\]

their sum is another vector that starts at the origin and ends at the combined displacement.

Visually, vector addition answers the question:

> **"Where do I end up after performing both movements?"**

---

# 📍 Tail-to-Head Rule

The **Tail-to-Head Rule** is the most intuitive way to add vectors.

### Step 1

Draw the first vector from the origin.

```
O ─────► u
```

### Step 2

Move the second vector so that **its tail starts exactly where the first vector ends**.

```
O ─────► u
          ─────► v
```

### Step 3

Draw a new vector from the origin to the final endpoint.

This new vector is

\[
\boxed{\mathbf{u}+\mathbf{v}}
\]

It represents the total displacement after both movements.

---

# ▱ Parallelogram Rule

Another geometric interpretation is the **Parallelogram Rule**.

1. Draw both vectors from the same starting point.
2. Copy each vector to form a parallelogram.
3. Draw the diagonal beginning at the origin.

The diagonal is the vector sum.

```
        ●
       /|
      / |
     /  |
    ●---●
```

Although the construction is different, the result is **exactly the same** as the Tail-to-Head Rule.

---

# 🧮 Formula

Vector addition is performed **component by component**.

\[
\boxed{
(x_1,y_1)+(x_2,y_2)
=
(x_1+x_2,\;y_1+y_2)
}
\]

Each coordinate is added independently.

- x-components are added together.
- y-components are added together.

---

# ✅ Example

Let

\[
\mathbf{u}=(2,3)
\]

and

\[
\mathbf{v}=(3,1)
\]

Add the corresponding components.

\[
(2,3)+(3,1)
\]

\[
=(2+3,\;3+1)
\]

\[
=\boxed{(5,4)}
\]

So the resultant vector is

\[
\boxed{(5,4)}
\]

---

# ❓ Why Is the Result the Diagonal?

This is one of the most beautiful geometric properties of vectors.

When two vectors start from the same point, they create two adjacent sides of a parallelogram.

The diagonal connects:

- the **starting point**, and
- the **combined endpoint** reached by following both vectors.

Following vector **u** and then vector **v** leads to exactly the same destination as following the diagonal.

The diagonal therefore represents the **total displacement**, which is precisely the definition of vector addition.

In other words,

- First movement → **u**
- Second movement → **v**
- Combined movement → **u + v**

The diagonal is not just a convenient drawing—it is the unique vector that represents both movements together.

---

# 💡 Key Takeaways

- Vector addition combines **displacements**, not lengths.
- Components are added independently.
- The **Tail-to-Head Rule** provides an intuitive construction.
- The **Parallelogram Rule** gives the same result geometrically.
- The resultant vector always represents the overall movement.
- For

\[
(2,3)+(3,1)
\]

the answer is

\[
\boxed{(5,4)}
\]

because each coordinate is added separately and the resulting vector points directly to the final position.
