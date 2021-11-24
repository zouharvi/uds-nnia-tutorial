#!/usr/bin/python3

from sys import argv
from csv import DictReader
import matplotlib.pyplot as plt

AT = argv[1]

def safe_float(x):
    if len(x) == 0:
        return None
    else:
        return float(x)

# points, time
with open("misc/grading.csv", "r") as f:
    # skip first row
    next(f)
    data = list(DictReader(f))
    data = [
        {k:line[k].replace(",", ".") for k in ["T"+AT, "A"+AT, "PERC"]}
        for line in data
    ]
    data = [
        {k:safe_float(x) for k,x in line.items()}
        for line in data
    ]

data = sorted(data, key=lambda x: x["A"+AT])
x_ticks = list(range(len(data)))
ax1 = plt.gca()
ax2 = ax1.twinx()
ax1.set_xlim(0 - 1, len(data))
ax1.set_xticks(x_ticks)
ax1.set_xticklabels(x_ticks)

# assignment points
hA = ax1.plot(
    x_ticks,
    [x["A"+AT] for x in data],
    marker=".", markersize=10,
    color="tab:red",
    label="Points",
    alpha=0.5,
)[0]

# overall percentage
hP = ax1.plot(
    x_ticks,
    [x["PERC"]*10 for x in data],
    marker=".", markersize=10,
    color="indigo",
    label="Avg. Points",
    alpha=0.5,
)[0]
ax1.set_ylabel("Points")
hH = ax1.hlines(
    y=6, xmin=0 - 1, xmax=len(data),
    colors="black",
    linestyle=":",
    label="60% threshold",
)

# time
hT = ax2.plot(
    [x_tick for x_tick, x in zip(x_ticks, data) if x["T"+AT] is not None],
    [x["T"+AT] for x in data if x["T"+AT] is not None],
    marker=".", markersize=10,
    label="Time",
    color="tab:green",
    alpha=0.5,
)[0]
ax2.set_ylabel("Time (hrs)")

ax1.set_xlabel("Students")
plt.legend(
    [hA, hT, hH, hP],
    [hA.get_label(), hT.get_label(), hH.get_label(), hP.get_label()],
    loc="center",
    ncol=4,
    bbox_to_anchor=(0, 0.55, 1, 1,),
)
plt.tight_layout()
plt.show()
