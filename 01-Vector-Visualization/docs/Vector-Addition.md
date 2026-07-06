➕ Vector Addition

Vector addition is one of the most fundamental operations in Linear Algebra.

It allows us to combine two or more vectors into a single vector that represents their overall effect.

Think of a vector as a movement:

- Move according to the first vector.
- Then move according to the second vector.
- The final position is represented by the resultant vector.

---

📖 Geometric Interpretation

A vector represents both magnitude (length) and direction.

Adding vectors does not mean adding their lengths.

Instead, we combine their directions and displacements to obtain a new vector.

Suppose we have two vectors

$$
\mathbf{u}=
\begin{bmatrix}
x_1\
y_1
\end{bmatrix},
\qquad
\mathbf{v}=
\begin{bmatrix}
x_2\
y_2
\end{bmatrix}
$$

Their sum is another vector that starts at the origin and ends at the combined displacement.

Visually, vector addition answers a simple question:

«"Where do I end up after performing both movements?"»

---

📍 Tail-to-Head Rule

The Tail-to-Head Rule is the most intuitive way to add vectors.

Step 1

Draw the first vector from the origin.

O ─────► u

Step 2

Move the second vector so that its tail starts exactly where the first vector ends.

O ─────► u
          ─────► v

Step 3

Draw a new vector from the origin to the final endpoint.

The resulting vector is

$$
\boxed{\mathbf{u}+\mathbf{v}}
$$

It represents the total displacement after completing both movements.

---

▱ Parallelogram Rule

Another geometric interpretation is the Parallelogram Rule.

1. Draw both vectors from the same starting point.
2. Copy each vector to create a parallelogram.
3. Draw the diagonal starting from the common origin.

        ●
       /|
      / |
     /  |
    ●---●

The diagonal is the vector sum

$$
\boxed{\mathbf{u}+\mathbf{v}}
$$

Although the construction is different, it produces exactly the same result as the Tail-to-Head Rule.

---

🧮 Formula
## 🧮 Formula

Vector addition is performed **component by component**.

<p align="center">
  <img src="assets/vector-addition-formula.svg" width="500">
</p>

---

## ✅ Example

<p align="center">
  <img src="assets/vector-addition-example.svg" width="450">
</p>

---

✅ Example

Consider the vectors

$$
\mathbf{u}=
\begin{bmatrix}
2\
3
\end{bmatrix},
\qquad
\mathbf{v}=
\begin{bmatrix}
3\
1
\end{bmatrix}
$$

Apply the vector addition rule.

$$
\mathbf{u}+\mathbf{v}

\begin{bmatrix}
2\
3
\end{bmatrix}
+
\begin{bmatrix}
3\
1
\end{bmatrix}
$$

Add the corresponding components.

$$

\begin{bmatrix}
2+3\
3+1
\end{bmatrix}
$$

Simplify.

$$

\begin{bmatrix}
5\
4
\end{bmatrix}
$$

Therefore,

$$
\boxed{
\mathbf{u}+\mathbf{v}

\begin{bmatrix}
5\
4
\end{bmatrix}
}
$$

The resultant vector points to the coordinates (5, 4).

---

❓ Why Is the Result the Diagonal?

This is one of the most beautiful geometric properties of vectors.

When two vectors start from the same point, they naturally form two adjacent sides of a parallelogram.

If you travel along u and then continue along v, you arrive at exactly the same destination reached by moving directly along the diagonal.

Mathematically,

$$
\boxed{
\text{Diagonal}

\mathbf{u}+\mathbf{v}
}
$$

The diagonal therefore represents the combined displacement of both vectors.

It is not simply a convenient line inside the parallelogram—it is the unique vector that describes the effect of applying both vectors together.

---

💡 Key Takeaways

- Vector addition combines displacements, not lengths.
- Components are added independently.
- The Tail-to-Head Rule provides an intuitive geometric construction.
- The Parallelogram Rule produces exactly the same resultant vector.
- The resultant vector always represents the overall displacement.
- In general,

$$
\boxed{
\mathbf{u}+\mathbf{v}

\begin{bmatrix}
x_1+x_2\
y_1+y_2
\end{bmatrix}
}
$$

- For this example,

$$
\boxed{
\begin{bmatrix}
2\
3
\end{bmatrix}
+
\begin{bmatrix}
3\
1
\end{bmatrix}

\begin{bmatrix}
5\
4
\end{bmatrix}
}
$$

The result is the vector that points directly from the origin to the final position after both movements.
