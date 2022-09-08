#!/usr/bin/env python
'''Computes the baseline accuracy of the RNN model'''

from collections import Counter

LABEL_FILE = open('answers-bin/test.input-label.label', 'r')
label_list = LABEL_FILE.readlines()
label_counts = Counter(label_list)

# Find most frequent label and its value
max_key = max(label_counts, key=label_counts.get)
max_value = max(label_counts.values())

# Find sum of all label counts in test set
sum_test = sum(label_counts.values())
print(f'Most frequent label: {max_key} ({max_value})')
print(sum_test)

# Compute baseline accuracy
print(f'Baseline accuracy: {(max_value / sum_test)*100}')

