# %%
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = self.right = None

    def __repr__(self):
        return str(self.data)


def count_node_kth_distance(node, k):
    if node is None:
        return 0
    if k == 0:
        return 1
    return count_node_kth_distance(node.left, k - 1) + count_node_kth_distance(node.right, k - 1)


def path(node, ele, paths=None):
    if paths is None:
        paths = list()
    if node is None:
        return paths
    if node.data == ele:
        paths.append(node)
        return paths
    if path(node.left, ele, paths) or path(node.right, ele, paths):
        paths.append(node)
        return paths
    return paths


def count_node_at_distance_k_from_any_node(node, target, k):
    path_list = path(node, target)
    ans = count_node_kth_distance(path_list[0], k)
    k = k - 1
    for i in range(1, len(path_list)):
        if k == 0:
            ans += 1
            break
        if path_list[i].left == path_list[i - 1]:
            ans += count_node_kth_distance(path_list[i].right, k - 1)
        else:
            ans += count_node_kth_distance(path_list[i].left, k - 1)
