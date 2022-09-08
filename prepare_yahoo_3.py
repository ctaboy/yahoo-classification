#!/usr/bin/env python
"""Prepares Yahoo! Answers data for Fairseq preprocessing"""

from typing import Dict

TRAIN_TXT = "train.txt"
TRAIN_INPUT = "answers/train.input"
TRAIN_LABEL = "answers/train.label"

VALID_TXT = "valid.txt"
VALID_INPUT = "answers/valid.input"
VALID_LABEL = "answers/valid.label"

TEST_TXT = "test.txt"
TEST_INPUT = "answers/test.input"
TEST_LABEL = "answers/test.label"

CLASSES = "yahoo_data/classes.txt"


def fetch_classes() -> Dict[int, str]:
    with open(CLASSES, "r") as classes:
        index = 0
        category_dict = {}
        for line in classes:
            index += 1
            category_dict[index] = line.rstrip().replace(" ", "_")
    return category_dict


class_dict = fetch_classes()
           

# Prepare training data
with open(TRAIN_TXT, "r") as source:
    with open(TRAIN_INPUT, "w") as sink1:
        with open(TRAIN_LABEL, "w") as sink2:
            for line in source:
                line_split = line.split("\t")
                line = " ".join(line_split[1].replace(" ", "_"))
                label = class_dict[int(line_split[0])]
                print(line.rstrip(), file=sink1)
                print(label, file=sink2)


# Prepare dev data:
with open(VALID_TXT, "r") as source:
    with open(VALID_INPUT, "w") as sink1:
        with open(VALID_LABEL, "w") as sink2:
            for line in source:
                line_split = line.split("\t")
                line = " ".join(line_split[1].replace(" ", "_"))
                label = class_dict[int(line_split[0])]
                print(line.rstrip(), file=sink1)
                print(label, file=sink2)


# Prepare test data:
with open(TEST_TXT, "r") as source:
    with open(TEST_INPUT, "w") as sink1:
        with open(TEST_LABEL, "w") as sink2:
            for line in source:
                line_split = line.split("\t")
                line = " ".join(line_split[1].replace(" ", "_"))
                label = class_dict[int(line_split[0])]
                print(line.rstrip(), file=sink1)
                print(label, file=sink2)

