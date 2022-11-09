"""
Print all the n digit number that can formed with {1,2}
"""


def print_all(cur_state, total_state, ans):
    if cur_state == total_state:
        print("".join(ans))
        return
    # start from the 1
    for i in range(1, 3):
        ans[cur_state] = str(i)
        print_all(cur_state+1, total_state, ans)


if __name__ == '__main__':
    print_all(0, 3, [None] * 3)
