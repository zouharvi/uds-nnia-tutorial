#!/usr/bin/env python3

"""
TODO: documentation

Based on a version for SNLP https://github.com/zouharvi/uds-snlp-tutorial/blob/main/misc/find_timeslot.py
"""

import sys
import csv
from collections import defaultdict, Counter
import re
import itertools

slot_mapping = defaultdict(lambda: set())
student_slots = defaultdict(lambda: set())
student_names = set()
data_loss = defaultdict(lambda: [])
header_times = {}


def extract_names(header):
    header = header.split(",")[1:]
    header = [re.search(r"(.+)\s*\((.+)\)", x) for x in header]
    header_names = [x.group(2) for x in header]
    header_times_raw = [x.group(1).strip() for x in header]

    for i, name in enumerate(header_names):
        slot_mapping[name].add(i)

    for i, date in enumerate(header_times_raw):
        header_times[i] = date


# Input: cleaned exported csv file without the header (and without Vilém's vote which can't be removed)
with open(sys.argv[1], 'r', newline='') as f:
    extract_names(next(f))
    reader = csv.reader(f, quotechar='"')
    for line in reader:

        name = line[0]
        slots = ["OK" in x for x in line[1:]]
        # if sum(slots) < 3:
        #     print("Disregarding")
        #     continue
        for slot_i, slot in enumerate(slots):
            if slot:
                student_slots[slot_i].add(name)
        student_names.add(name)

# duplicates seem to be self-resolved
# duplicates = [item for item, count in Counter(header_times.values()).items() if count > 1]
# for duplicate in duplicates:
#     duplicate_ids = [k for k,v in header_times.items() if v == duplicate]
#     print(duplicate_ids)

# flatten slot mapping
slot_mapping = [
    {(k, x) for x in v}
    for k, v in slot_mapping.items()
]

# simply try all the combinations
for slot_ids in itertools.product(*slot_mapping):
    covered_students = set()
    for slot_name, slot_id in slot_ids:
        covered_students = covered_students.union(student_slots[slot_id])

    loss = len(student_names) - len(covered_students)
    data_loss[loss].append({k: v for k, v in slot_ids})

print("Total students:", len(student_names), "\n")

# print all configurations with minimal loss (number of student not covered)
for loss_i, loss in enumerate(sorted(list(data_loss.keys()))[:2]):
    print("Option", chr(loss_i + ord("A")))
    print("Students without a tutorial:", loss)
    for config in data_loss[loss]:
        print("-")
        for name, slot_id in config.items():
            print(f"{name+f' ({len(student_slots[slot_id])})'+':':>14}", header_times[slot_id].replace(" -", "-").replace("- ", "-"))
    print()
