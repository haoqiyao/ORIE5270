import numpy as np

class BlankObj:
    def __repr__(self):
        return ""

class Tree(object):
    def __init__(self, root):
        self.root = root

    def get_value_root(self):
        if self.root is not None:
            return self.root.value
        else:
            return None

    def height(self, root):
        if not root:
            return 0
        return 1 + max(self.height(root.left), self.height(root.right))

    def print_tree(self, root):
        height = self.height(root)
        width = 2 ** height - 1

        result = []
        for h in range(height):
            result.append(["|"] * width)

        track = [(root, 0, 0, width)]

        for curr in track:

            curr_node = curr[0]
            curr_level = curr[1]
            curr_l = curr[2]
            curr_r = curr[3]

            mid = int(np.floor((curr_l + curr_r)/2))

            result[curr_level][mid] = str(curr_node.value)

            if curr_node.left:
                track.append((curr_node.left, curr_level + 1, curr_l, mid))
            if curr_node.right:
                track.append((curr_node.right, curr_level + 1, mid, curr_r))

        return np.mat(result)



class Node(object):

    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right


if __name__ == '__main__':

    first = Node(1, None, None)
    second = Node(2, None, None)
    third = Node(3, None, None)
    fourth = Node(4, None, None)

    first.left = second
    first.right = third
    second.left = fourth

    tree = Tree(first)

    print (tree.print_tree(first))
