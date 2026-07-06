# 📘 Mathematical Background

Before diving into vector visualization, it is helpful to understand the basic mathematical concepts behind vectors.

---

# What is a Vector?

A **vector** is a mathematical object that has **both magnitude and direction**.

Unlike a scalar (such as temperature or mass), which only has a numerical value, a vector describes **how much** and **where**.

Examples of quantities represented by vectors include:

- 📍 Position
- 🚗 Velocity
- ⚡ Force
- 🌬️ Wind

A simple two-dimensional vector can be written as:

\[
\vec{v} = (x,\;y)
\]

where:

- **x** is the horizontal component.
- **y** is the vertical component.

---

# Magnitude

The **magnitude** (or length) of a vector represents its size.

For a vector

\[
\vec{v}=(x,y)
\]

its magnitude is

\[
|\vec{v}|=\sqrt{x^2+y^2}
\]

### Example

For

\[
\vec{v}=(3,4)
\]

the magnitude is

\[
|\vec{v}|=\sqrt{3^2+4^2}
=\sqrt{25}
=5
\]

The magnitude tells us **how long** the vector is, regardless of its direction.

---

# Direction

A vector always points toward a specific direction.

The direction is commonly measured as the angle between the vector and the positive x-axis.

It can be calculated using

\[
\theta=\tan^{-1}\left(\frac{y}{x}\right)
\]

where:

- θ is the direction angle.
- x and y are the vector components.

Together, the magnitude and direction completely describe a vector.

---

# Coordinates

A vector is defined by its coordinates.

For example,

\[
(2,\;5)
\]

means:

- Move **2 units** along the x-axis.
- Move **5 units** along the y-axis.

The vector starts at the origin

\[
(0,0)
\]

and ends at

\[
(2,5)
\]

Its endpoint determines both its direction and magnitude.

---

# Cartesian Plane

Vectors are usually represented on the **Cartesian coordinate plane**.

The plane consists of:

- **x-axis** → horizontal axis
- **y-axis** → vertical axis
- **Origin (0,0)** → the starting point of most vectors

The endpoint of a vector determines its location on the plane.

Different quadrants correspond to different combinations of positive and negative coordinates.

---

# Vector Notation

Vectors can be represented in several common forms.

### Component Form

\[
(3,4)
\]

---

### Column Vector

\[
\begin{bmatrix}
3\\
4
\end{bmatrix}
\]

---

### Arrow Notation

\[
\vec{v}
\]

---

### Boldface Notation

\[
\mathbf{v}
\]

All of these notations describe the same mathematical object.

---

# Why Are Vectors Important?

Vectors are one of the fundamental building blocks of linear algebra.

They are used extensively in:

- 🤖 Artificial Intelligence
- 📊 Data Science
- 🎮 Computer Graphics
- 🛰️ Robotics
- 🎯 Physics
- 📡 Computer Vision
- 🧠 Machine Learning

Understanding vectors is the first step toward learning more advanced topics such as vector addition, linear combinations, matrices, transformations, eigenvectors, and neural networks.

---

## Key Takeaways

- A vector has **magnitude** and **direction**.
- Coordinates determine a vector's endpoint.
- Magnitude measures the vector's length.
- Direction specifies where the vector points.
- Vectors are drawn on the Cartesian plane.
- Multiple notations can represent the same vector.
- Vectors form the foundation of linear algebra and many modern technologies.
