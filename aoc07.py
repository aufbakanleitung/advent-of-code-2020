# --- Day 7: Handy Haversacks ---
import re

content = [line.rstrip('\n') for line in open("input/aoc07_input.txt")]
rules = [re.split('[\s]', line) for line in content]

class Bag:
    def __init__(self, bag, nr1=None, sub_bag1=None, nr2=None, sub_bag2=None):
        self.bag = bag
        self.nr1 = nr1
        self.sub_bag1 = sub_bag1
        self.nr2 = nr2
        self.sub_bag2 = sub_bag2

    def __str__(self):
        return f"{self.bag} is empty"

    def __str__(self):
        return f"{self.bag} bags contain {str(self.nr1)} {self.sub_bag1} bags."

    # def __str__(self, bag, nr1, sub_bag1, nr2, sub_bag2):
    #     return f"{self.bag} bags contain {self.nr1} {self.sub_bag1} bags, {self.nr2} {self.sub_bag2} bags."


def sentence_to_bag(sentence):
    super_bag = sentence[0:2]
    if sentence[4] == "no":
        return super_bag
    nr1, sub_bag1 = int(sentence[4]), sentence[5:7]
    if len(sentence) < 9:
        return super_bag, nr1, sub_bag1
    else:
        nr2, sub_bag2 = int(sentence[8]), sentence[9:11]
        return super_bag, nr1, sub_bag1, nr2, sub_bag2

test = Bag("brown", 2, "yellow")
print(test)


# bag_list = []
# for sentence in rules:
#     bag_list.append(Bag(sentence_to_bag(sentence)))
#
# print(bag_list)
#
# for bag in bag_list:
#     print(bag)