import numpy as np
import matplotlib.pyplot as plt

# =========================
# VECTORS
# =========================
v1 = np.array([2, 3])
v2 = np.array([3, 1])

sum_vector = v1 + v2
scaled_vector = 2 * v1

# =========================
# MAGNITUDES
# =========================
mag_v1 = np.linalg.norm(v1)
mag_v2 = np.linalg.norm(v2)
mag_sum = np.linalg.norm(sum_vector)
mag_scaled = np.linalg.norm(scaled_vector)

# =========================
# FIGURE SETUP
# =========================
plt.style.use("dark_background")

fig, ax = plt.subplots(figsize=(10, 10))
ax.set_facecolor("#111827")

# =========================
# DRAW AXES
# =========================
ax.axhline(0, color="white", linewidth=1.5)
ax.axvline(0, color="white", linewidth=1.5)

# =========================
# DRAW VECTORS
# =========================
vectors = [
    (v1, "#00E5FF", "v1"),
    (v2, "#FFD54F", "v2"),
    (sum_vector, "#00FF95", "v1 + v2"),
    (scaled_vector, "#FF4D6D", "2 × v1")
]

for vec, color, label in vectors:

    ax.quiver(
        0, 0,
        vec[0], vec[1],
        angles='xy',
        scale_units='xy',
        scale=1,
        color=color,
        width=0.008
    )

    ax.scatter(
        vec[0], vec[1],
        color=color,
        s=120,
        edgecolors="white",
        zorder=5
    )

    ax.text(
        vec[0] + 0.2,
        vec[1] + 0.2,
        f"{label}\n({vec[0]}, {vec[1]})",
        color=color,
        fontsize=11,
        weight='bold'
    )

# =========================
# PARALLELOGRAM FOR ADDITION
# =========================
ax.plot(
    [v1[0], sum_vector[0]],
    [v1[1], sum_vector[1]],
    '--',
    color='gray',
    alpha=0.6
)

ax.plot(
    [v2[0], sum_vector[0]],
    [v2[1], sum_vector[1]],
    '--',
    color='gray',
    alpha=0.6
)

# =========================
# GRID
# =========================
ax.grid(
    color='gray',
    linestyle=':',
    linewidth=0.7,
    alpha=0.5
)

# =========================
# LIMITS
# =========================
ax.set_xlim(-1, 11)
ax.set_ylim(-1, 11)

# =========================
# LABELS
# =========================
ax.set_xlabel("X-axis", fontsize=12)
ax.set_ylabel("Y-axis", fontsize=12)

ax.set_title(
    "Vector Operations Visualization",
    fontsize=18,
    weight='bold',
    pad=20
)

# =========================
# LEGEND
# =========================
from matplotlib.lines import Line2D

legend_elements = [
    Line2D([0], [0], color="#00E5FF", lw=4, label='v1'),
    Line2D([0], [0], color="#FFD54F", lw=4, label='v2'),
    Line2D([0], [0], color="#00FF95", lw=4, label='v1 + v2'),
    Line2D([0], [0], color="#FF4D6D", lw=4, label='2 × v1')
]

ax.legend(
    handles=legend_elements,
    loc='lower right',
    fontsize=10
)

plt.tight_layout()
plt.show()
