import itertools
import math


def load_data(file: str) -> (str, dict, str):
    with open(file, "r") as inputfile:
        navigations, nodes_tmp = inputfile.read().split("\n\n")
        nodes = {
            x[0]: x[1].strip("()").split(", ")
            for x in [node.split(" = ") for node in nodes_tmp.split("\n")]
        }
        return navigations, nodes


def get_steps_to_zzz(navigations: str, nodes: dict) -> int:
    first_node = "AAA"
    steps = 0
    for nav in itertools.cycle([i == "R" for i in navigations]):
        if first_node == "ZZZ":
            return steps
        first_node = nodes[first_node][nav]
        steps += 1
        # print(f"steps: {steps} first_node: {first_node}")


def get_steps_to_zzz_p2(navigations: str, nodes: dict) -> int:
    first_nodes = [node for node in nodes.keys() if node.endswith("A")]
    time_to_z = []
    for first_node in first_nodes:
        steps = 0
        for nav in itertools.cycle([i == "R" for i in navigations]):
            if first_node.endswith("Z"):
                break
            first_node = nodes[first_node][nav]
            steps += 1
        time_to_z.append(int(steps))

    return math.lcm(*time_to_z)


if __name__ == "__main__":
    navigations, nodes = load_data("src\\aoc8\\input.txt")
    steps = get_steps_to_zzz(navigations, nodes)
    print(f"Steps taken to reach ZZZ: {steps}")

    steps = get_steps_to_zzz_p2(navigations, nodes)
    print(f"Steps taken to reach xxZ for all xxA nodes: {steps}")
