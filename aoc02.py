# Day 2: Password Philosophy
# https://adventofcode.com/2020/day/2
import re

pass_ex = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc']
pass_list = [line.rstrip('\n') for line in open("aoc02_input.txt")]
pass_llist = [re.split('[-:\s]', line) for line in pass_list]


def pass_test(item):
    letter_range = range(int(item[0]), int(item[1])+1)
    letter = item[2]
    passw = item[4]
    if passw.count(letter) in letter_range:
        return True
    else:
        return False


def pass_test2(item):
    letter = item[2]
    passw = item[4]
    if (passw[int(item[0])-1] == letter) ^ (passw[int(item[1])-1] == letter):  # xor
        return True
    else:
        return False

pass_count = 0
for item in pass_llist:
    if pass_test2(item):
        print(item)
        pass_count += 1
print(pass_count)