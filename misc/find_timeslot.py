#!/usr/bin/env python3

"""
TODO: documentation

Based on a version for SNLP https://github.com/zouharvi/uds-snlp-tutorial/blob/main/misc/find_timeslot.py
"""

import re
import sys
import csv
import argparse
import itertools
from collections import defaultdict


if __name__ != '__main__':
    sys.exit()

parser = argparse.ArgumentParser(
                    prog = 'Finder for balanced time slots',
                    description = ("Description: "
                                   "Goes through user responses and finds ideal times "
                                   "Input file is quite peculiar. First column must "
                                   "contain the names of the students. The rest of "
                                   "the columns must contain whether the student can "
                                   "attend the timeslot specified by the colums. "
                                   "The format of the headers for each time slot "
                                   "needs to contain the name of the tutor between "
                                   "parenthesis, e.g. 'Mondays 12:15 (Jacob)'.")
                )


parser.add_argument('filename',
                    help="CSV file with first column being names and all columns after that being time slots with values of whether they are possible for each student or not")
parser.add_argument('-y', '--yes',
                    nargs='+',
                    default=['Yes', 'May be'],
                    help="What values are considered a positive response, e.g. 'OK' or 'Yes'; more than one value is possible")
parser.add_argument('-c', '--cols',
                    type=int,
                    default=3,
                    help="How many columns to use to display names")
parser.add_argument('-b', '--balance',
                    action='store_true',
                    help="Prompts user for a selection and balances selection")

args = parser.parse_args()

slot_mapping = defaultdict(lambda: set())
student_slots = defaultdict(lambda: set())
student_names = set()
data_loss = defaultdict(lambda: [])
header_times = {}


def extract_names(header):
    """ Extract slot times and names """
    header = header.split(",")[1:]
    header = [re.search(r"(.+)\s*\((.+)\)", x) for x in header]
    header_names = [x.group(2) for x in header]
    header_times_raw = [x.group(1).strip() for x in header]

    for i, name in enumerate(header_names):
        slot_mapping[name].add(i)

    for i, date in enumerate(header_times_raw):
        header_times[i] = date


# Input: cleaned exported csv file without the header
# (and without Vilém's vote which can't be removed)
with open(args.filename, 'r', newline='') as f:
    extract_names(next(f))
    reader = csv.reader(f, quotechar='"')
    for line in reader:

        name = line[0]
        slots = [x in args.yes for x in line[1:]]
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
    for config_i, config in enumerate(data_loss[loss]):
        print(f"{config_i} -")
        for name, slot_id in config.items():
            print(f"{name+f' ({len(student_slots[slot_id])})'+':':>14}", header_times[slot_id].replace(" -", "-").replace("- ", "-"))
    print()
