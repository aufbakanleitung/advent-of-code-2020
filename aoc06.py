# --- Day 6: Custom Customs ---
import re

with open('aoc06_input.txt') as f:
    content = f.read().split('\n\n')
    forms = [set(line) for line in content]
    [sett.discard('\n') for sett in forms]

form_sum = 0
for form in forms:
    form_sum += len(form)
print(form_sum)