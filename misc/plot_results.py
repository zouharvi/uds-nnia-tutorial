#!/usr/bin/python3

import matplotlib.pyplot as plt

# points, time
with open("misc/ass1.log", "r") as f:
    data = [
        [float(x) for x in line.replace(",", ".").split()]
        for line in f
    ]

data = sorted(data, key=lambda x: x[0])
x_ticks = list(range(len(data)))
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(0-1, len(data))

# assignment points
h1 = ax1.plot(
    x_ticks,
    [x[0] for x in data],
    marker=".", markersize=10,
    color="tab:blue",
    label="Points",
)[0]
ax1.set_ylabel("Assignment points")
hT = ax1.hlines(
    y=6, xmin=0-1, xmax=len(data),
    colors="black",
    linestyle=":",
    label="60% threshold",
)

# time
h2 = ax2.plot(
    x_ticks,
    [x[1] for x in data],
    marker=".", markersize=10,
    label="Time (hrs)",
    color="tab:red",
)[0]
ax2.set_ylabel("Time (hrs)")

ax1.set_xlabel("Students")
plt.legend(
    [h1, h2, hT],
    [h1.get_label(), h2.get_label(), hT.get_label()],
    loc="center right",
    )
plt.tight_layout()
plt.show()