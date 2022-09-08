#!/usr/bin/env python
"""Combines Y!A data into one corpus"""

import re

MAIN_OUTPUT = "main.txt"
TRAIN_CSV = "yahoo_data/train.csv"
TEST_CSV = "yahoo_data/test.csv"


# Get text from `train.csv` & `test.csv`
with open(MAIN_OUTPUT, "w") as sink:
    with open(TRAIN_CSV, "r") as source:
        for line in source:
            source = re.match(r"\"\d+\",\"(.+)\"$", line)
            sent = re.sub(
                r"\\n|<br>|<br />|<+|>+|&#xd;|\",\"|\"\"", " ", source[1]
            )
            s = re.sub("([\.,\!\?\(\)\:\-\"\/])", r" \1 ", sent)
            s = re.sub("\s{2,}", " ", s)
            index = re.match(r"\"(\d+)\"", line)
            print(f"{index[1]}\t{s.casefold()}", file=sink)
    with open(TEST_CSV, "r") as source:
        for line in source:
            source = re.match(r"\"\d+\",\"(.+)\"$", line)
            sent = re.sub(
                r"\\n|<br>|<br />|<+|>+|&#xd;|\",\"|\"\"", " ", source[1]
            )
            s = re.sub("([\.,\!\?\(\)\:\-\"\/])", r" \1 ", sent)
            s = re.sub("\s{2,}", " ", s)
            index = re.match(r"\"(\d+)\"", line)
            print(f"{index[1]}\t{s.casefold()}", file=sink)

