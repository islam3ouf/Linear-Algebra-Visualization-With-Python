
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D


# COLORS

BACKGROUND_COLOR = "#111827"

VECTOR_COLORS = {
    "v1": "#00E5FF",
    "v2": "#FFD54F",
    "sum": "#00FF95",
    "scaled": "#FF4D6D",
}


# DRAWING FUNCTIONS

def draw_vector(ax, vector, color, label):
    """Draw a single vector with its endpoint and label."""

    ax.quiver(
        0,
        0,
        vector[0],
        vector[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color=color,
        width=0.008,
    )

    ax.scatter(
        vector[0],
        vector[1],
        s=120,
        color=color,
        edgecolors="white",
        zorder=5,
    )

    ax.text(
        vector[0] + 0.2,
        vector[1] + 0.2,
        f"{label}\n({vector[0]}, {vector[1]})",
        fontsize=11,
        weight="bold",
        color=color,
    )


def draw_parallelogram(ax, v1, v2, result):
    """Draw the helper lines for vector addition."""

    ax.plot(
        [v1[0], result[0]],
        [v1[1], result[1]],
        "--",
        color="gray",
        alpha=0.6,
    )

    ax.plot(
        [v2[0], result[0]],
        [v2[1], result[1]],
        "--",
        color="gray",
        alpha=0.6,
    )


def configure_axes(ax):
    """Configure axes appearance."""

    ax.set_xlim(-1, 11)
    ax.set_ylim(-1, 11)

    ax.axhline(0, color="white", linewidth=1.5)
    ax.axvline(0, color="white", linewidth=1.5)

    ax.grid(
        linestyle=":",
        linewidth=0.7,
        alpha=0.5,
    )

    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")

    ax.set_title(
        "Vector Operations Visualization",
        fontsize=18,
        weight="bold",
        pad=20,
    )


def create_legend(ax):

    handles = [
        Line2D([0], [0], color=VECTOR_COLORS["v1"], lw=4, label="v1"),
        Line2D([0], [0], color=VECTOR_COLORS["v2"], lw=4, label="v2"),
        Line2D([0], [0], color=VECTOR_COLORS["sum"], lw=4, label="v1 + v2"),
        Line2D([0], [0], color=VECTOR_COLORS["scaled"], lw=4, label="2 × v1"),
    ]

    ax.legend(handles=handles, loc="lower right")


# MAIN


def main():

    plt.style.use("dark_background")

    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor(BACKGROUND_COLOR)

    v1 = np.array([2, 3])
    v2 = np.array([3, 1])

    vectors = [
        (v1, VECTOR_COLORS["v1"], "v1"),
        (v2, VECTOR_COLORS["v2"], "v2"),
        (v1 + v2, VECTOR_COLORS["sum"], "v1 + v2"),
        (2 * v1, VECTOR_COLORS["scaled"], "2 × v1"),
    ]

    configure_axes(ax)

    for vector, color, label in vectors:
        draw_vector(ax, vector, color, label)

    draw_parallelogram(ax, v1, v2, v1 + v2)

    create_legend(ax)

    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()# =========================
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
