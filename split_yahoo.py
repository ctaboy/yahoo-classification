#!/usr/bin/env python
"""Randomly splits Y!A data into training, development, and test data."""

import random
import argparse

MAIN_TXT = "main.txt"
TRAIN_TXT = "train.txt"
VALID_TXT = "valid.txt"
TEST_TXT = "test.txt"


def read_data(path):
    corpus = []
    with open(path, "r") as source:
        for line in source:
            corpus.append(line)
    return corpus


def write_data(path, data):
    with open(path, "w") as sink:
        for line in data:
            print(line.rstrip(), file=sink)


def main(args: argparse.Namespace) -> None:
    random.seed(args.seed)
    corpus = read_data(MAIN_TXT)
    random.shuffle(corpus)
    ten = len(corpus) // 10
    write_data(TEST_TXT, corpus[:ten])
    write_data(VALID_TXT, corpus[ten:ten + ten])
    write_data(TRAIN_TXT, corpus[ten + ten:])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--seed", required=True, help="random seed")
    main(parser.parse_args())
