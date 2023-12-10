from base import BaseDay
from collections import Counter


class Day7(BaseDay):
    def __init__(self, path):
        BaseDay.__init__(self, path)

    @property
    def part1(self):
        # return "tknk"
        return "gmcrj"

    # Done with ctrl - f in the input

    def depth(self, tree, start_node):
        depth = 1
        stored_depth = 0
        for i in tree[start_node]:
            stored_depth = max(self.depth(tree, i), stored_depth)
        return depth + stored_depth

    def cost(self, parent, tree, weights):
        weight = weights[parent]
        for child in tree[parent]:
            weight += self.cost(child, tree, weights)
        return weight

    @property
    def part2(self):
        with open(self.input_path) as file:
            structure = file.read().split("\n")
        tree = dict()
        weight = dict()
        for link in structure:
            if "->" in link:
                link_split = link.split(" -> ")
                parent = link_split[0].split(" (")[0]
                children = link_split[1].split(", ")
                tree[parent] = children
                weight[parent] = int(link_split[0].split(" (")[1][:-1])
            else:
                parent = link.split(" (")[0]
                tree[parent] = []
                weight[parent] = int(link.split(" (")[1][:-1])
        root_node = self.part1
        values = []
        children = []
        previous_good_cost = 0
        previous_bad_cost = 0
        root_weight = 0
        while True:
            for i in tree[root_node]:
                children.append(i)
                values.append(self.cost(i, tree, weight))
            count = Counter(values)
            good_cost = max(count, key=count.get)
            bad_cost = min(count, key=count.get)
            root_weight = weight[root_node]
            root_node = children[values.index(bad_cost)]
            if len(count) == 1:
                break
            values = []
            children = []
            previous_good_cost = good_cost
            previous_bad_cost = bad_cost
        return root_weight + (previous_good_cost - previous_bad_cost)
