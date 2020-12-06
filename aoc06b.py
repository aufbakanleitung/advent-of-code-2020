# For each group, count the number of questions to which everyone answered "yes".
# What is the sum of those counts?
import re

with open('aoc06_input.txt') as f:
    content = f.read().split('\n\n')
    deforms = [re.split('[\n]', line) for line in content]
    sorted_forms = [[''.join(sorted(line)) for line in form] for form in deforms]


def test_every_question(group):
    test = group[0]
    for answer in group[0]:
        for person in group:
            if answer not in person:
                test = test.replace(answer, '')
    return test


count = 0
for group in sorted_forms:
    print("everyone answered:", test_every_question(group))
    count += len(test_every_question(group))
print(count)
