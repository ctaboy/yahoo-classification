#!/usr/bin/env python
"""Prepares Yahoo! Answers data for Fairseq preprocessing"""

TRAIN_TXT = "train.txt"
TRAIN_INPUT = "train.input"
TRAIN_LABEL = "train.label"

VALID_TXT = "valid.txt"
VALID_INPUT = "valid.input"
VALID_LABEL = "valid.label"

TEST_TXT = "test.txt"
TEST_INPUT = "test.input"
TEST_LABEL = "test.label"

# CLASSES = "classes.txt"


# Prepare training data
with open(TRAIN_TXT, "r") as source:
    with open(TRAIN_INPUT, "w") as sink1:
        with open(TRAIN_LABEL, "w") as sink2:
            for line in source:
                line_split = line.split("\t")
                print(line_split[1].rstrip(), file=sink1)
                print(line_split[0], file=sink2)


# with open(CLASSES, "r") as classes:
#     index = 0
#     categories = {}
#     for category in classes:
#         index += 1
#         categories[index] = category.rstrip()
#     with open(TRAIN_LABEL_TXT, "r") as source:
#         for num in source:
#             with open(TRAIN_LABEL, "a") as sink:
#                 print(categories[int(num)], file=sink)


# Prepare dev data:
with open(VALID_TXT, "r") as source:
    with open(VALID_INPUT, "w") as sink1:
        with open(VALID_LABEL, "w") as sink2:
            for line in source:
                line_split = line.split("\t")
                print(line_split[1].rstrip(), file=sink1)
                print(line_split[0], file=sink2)


# with open(CLASSES, "r") as classes:
#     index = 0
#     categories = {}
#     for category in classes:
#         index += 1
#         categories[index] = category.rstrip()
#     with open(VALID_LABEL_TXT, "r") as source:
#         for num in source:
#             with open(VALID_LABEL, "a") as sink:
#                 print(categories[int(num)], file=sink)


# Prepare test data:
with open(TEST_TXT, "r") as source:
    with open(TEST_INPUT, "w") as sink1:
        with open(TEST_LABEL, "w") as sink2:
            for line in source:
                line_split = line.split("\t")
                print(line_split[1].rstrip(), file=sink1)
                print(line_split[0], file=sink2)


# with open(CLASSES, "r") as classes:
#     index = 0
#     categories = {}
#     for category in classes:
#         index += 1
#         categories[index] = category.rstrip()
#     with open(TEST_LABEL_TXT, "r") as source:
#         for num in source:
#             with open(TEST_LABEL, "a") as sink:
#                 print(categories[int(num)], file=sink)
