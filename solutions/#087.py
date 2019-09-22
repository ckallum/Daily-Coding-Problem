def correct_compass(rules, param_dict={}):
    opposite_dict = {"N": "S", "E": "W", "W": "E", "S": "N"}
    res = False
    for rule in rules:
        params = rule.split()
        node1 = params[0]
        directions = params[1]
        node2 = params[2]
        if node1 not in param_dict:
            param_dict[node1] = {"N": set(), "E": set(), "S": set(), "W": set()}
        if node2 not in param_dict:
            param_dict[node2] = {"N": set(), "E": set(), "S": set(), "W": set()}
        for direction in directions:
            if node2 in param_dict[node1][opposite_dict[direction]] or node1 in param_dict[node2][direction]:
                return False, param_dict
            for node in param_dict[node1][direction]:
                if node:
                    res, param_dict = correct_compass([node+" "+direction+" "+node2], param_dict)
        for direction in directions:
            param_dict[node1][direction].add(node2)
            param_dict[node2][opposite_dict[direction]].add(node1)
    return res and True, param_dict


def main():
    assert not correct_compass(["A N B",
                                "B NE C",
                                "C N A"])[0]

    assert correct_compass(["A NW B",
                            "A N B"])


if __name__ == '__main__':
    main()
