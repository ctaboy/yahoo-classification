#!/usr/bin/env python
"""Combines Y!A data into one corpus"""

import re

MAIN_INPUT = "main.txt"
TRAIN_CSV = "train.csv"
TEST_CSV = "test.csv"


# Get text from `train.csv`
with open(TRAIN_CSV, "r") as source:
    with open(MAIN_INPUT, "w") as sink:
        for line in source:
            source = re.match(r"\"\d+\",\"(.+)\"\s$", line)
            source = re.sub(
                r"\\n|<br>|<br />|<+|>+|&#xd;|\",\"|\"\"", "", source[1]
            )
            index = re.match(r"\"(\d+)\"", line)
            print(f"{index[1]}\t{source}", file=sink)


# Get text from `test.csv`
with open(TEST_CSV, "r") as source:
    with open(MAIN_INPUT, "a") as sink:
        for line in source:
            source = re.match(r"\"\d+\",\"(.+)\"\s$", line)
            source = re.sub(
                r"\\n|<br>|<br />|<+|>+|&#xd;|\",\"|\"\"", "", source[1]
            )
            index = re.match(r"\"(\d+)\"", line)
            print(f"{index[1]}\t{source}", file=sink)
