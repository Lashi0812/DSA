"""
Generate the permutation of the array
"""
permutation = []


def generate_permutation(cur_state, end_state, array):
    if cur_state == end_state:
        permutation.append(array.copy())
        return
        # swap the current and fixed state
    for i in range(cur_state, end_state):
        array[cur_state], array[i] = array[i], array[cur_state]
        generate_permutation(cur_state + 1, end_state, array)
        array[i], array[cur_state] = array[cur_state], array[i]


if __name__ == '__main__':
    array = [4, 7, 8]
    generate_permutation(0, len(array), array)
    print(permutation)
