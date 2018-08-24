import numpy as np


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
            # if empty tree, return 0
            return 0
        # if not, recursively go to the left and right part, add 1 to the height
        return 1 + max(self.height(root.left), self.height(root.right))

    def print_tree(self, root):
        # get the height of the tree
        height = self.height(root)

        # width of the array follows this structure
        width = 2 ** height - 1

        result = []

        # first initialize all the result as "|"
        for h in range(height):
            result.append(["|"] * width)

        # using bfs and update the corresponding values using array, start from root
        track = [(root, 0, 0, width)]

        for curr in track:

            # current node is root
            curr_node = curr[0]
            # current level is 0
            curr_level = curr[1]
            # current left is 0
            curr_l = curr[2]
            # current right is width
            curr_r = curr[3]

            # get the middle index value
            mid = int(np.floor((curr_l + curr_r) / 2))

            # replace the result matrix with the node
            result[curr_level][mid] = str(curr_node.value)

            # if has left node, do left part again using bfs
            if curr_node.left:
                # current node becomes left, level goes down by 1,
                # current left stays the same, current right becomes middle
                track.append((curr_node.left, curr_level + 1, curr_l, mid))
            # same for right part
            if curr_node.right:
                # current node becomes right, level goes down by 1,
                # current left becomes middle, current right stays the same
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

    print(tree.print_tree(first))
