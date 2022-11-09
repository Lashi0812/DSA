"""
Given the array generate the all possible subset from the array
"""
subset = []


def generate_subset(cur_state, end_state, path, array):
    if cur_state == end_state:
        subset.append(path.copy())
        return
    path.append(array[cur_state])
    generate_subset(cur_state + 1, end_state, path, array)
    path.pop()
    generate_subset(cur_state + 1, end_state, path, array)


if __name__ == '__main__':
    array = [5, -2, 9]
    generate_subset(0, len(array), [], array)
    print(subset)
