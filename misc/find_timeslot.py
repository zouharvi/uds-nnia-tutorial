#!/usr/bin/env python3

"""
TODO: documentation

Based on a version for SNLP
https://github.com/zouharvi/uds-snlp-tutorial/blob/main/misc/find_timeslot.py
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

slot_mapping = defaultdict(set)
student_slots = defaultdict(set)
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
    data_loss[loss].append(dict(slot_ids))

print("Total students:", len(student_names), "\n")

# print all configurations with minimal loss (number of student not covered)
for loss_i, loss in enumerate(sorted(list(data_loss.keys()))[:2]):
    print("Option", chr(loss_i + ord("A")))
    print("Students without a tutorial:", loss)
    for config_i, config in enumerate(data_loss[loss]):
        print(f"{config_i} -")
        for name, slot_id in config.items():
            print(f"{name+f' ({len(student_slots[slot_id])})'+':':>14}",
                  header_times[slot_id].replace(" -", "-").replace("- ", "-"))
    print()

if not args.balance:
    sys.exit()

# TODO: Fix non-deterministic nature of balancing
# Automatically balance repeated students for selected option
# WARNING: A bit of spaghetti code ahead as to not modify
#          the original script too much
selected = input("Select option to balance in LetterNumber format, e.g. (A2): ")

if len(selected) != 2 or not selected[0].isalpha() or not selected[1].isnumeric():
    sys.exit("Bad selection")

# Since we're not displaying them in the order we fill it out we need
# some processing of the selection
selected_loss = ord(selected[0]) - ord('A')
selected_loss = sorted(list(data_loss.keys()))[selected_loss]
selected_config = data_loss[selected_loss][int(selected[1])]

# Create a new dictionary with final slots
final_slots = defaultdict(list)

# Create auxiliar data structures for balancing
config_slots = list(selected_config.values())

# Iterate over names, when repeated names are found:
# Assign each to the slot with the least amount of students
# while only taking into account possible slots for the student
for student_name in student_names:
    student_possible_slots = [x for x in config_slots
                              if student_name in student_slots[x]]

    # Ignore students we couldn't accommodate :(
    if len(student_possible_slots) < 1:
        continue

    min_length = len(final_slots[student_possible_slots[0]])
    selected_slot = student_possible_slots[0]
    for temp_slot_id, name_list in final_slots.items():
        # Ignore slots that aren't suitable
        if temp_slot_id not in student_possible_slots:
            continue

        if len(name_list) < min_length:
            min_length = len(name_list)
            selected_slot = temp_slot_id

    # Add name to final slots for final display
    final_slots[selected_slot].append(student_name)

# Print final slots with student names in 3 columns
for name, slot_id in selected_config.items():
    print()
    print(f"{name+f' ({len(final_slots[slot_id])})'+':'}",
          header_times[slot_id].replace(" -", "-").replace("- ", "-"))
    for i in range(0, len(final_slots[slot_id]), args.cols):
        print(' '.join(f"-- {s:25}" for s in final_slots[slot_id][i:i+args.cols]))
