def grouping(groupSizes):
    groups = {}
    result = []

    for i, size in enumerate(groupSizes):
        if size not in groups:
            groups[size] = []
        groups[size].append(i)

        if len(groups[size]) == size:
            result.append(groups[size])
            groups[size] = []

    return result


print(grouping([3, 3, 3, 3, 3, 1, 3]))
