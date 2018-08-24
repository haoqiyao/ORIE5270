import unittest
from tree.tree import Tree, Node


class test_tree(unittest.TestCase):
    
    def test_tree(self):
        first = Node(1, None, None)
        second = Node(2, None, None)
        third = Node(3, None, None)
        fourth = Node(4, None, None)
        fifth = Node(5, None, None)
        sixth = Node(6, None, None)
        seventh = Node(7, None, None)
        eighth = Node(8, None, None)
        ninth = Node(9, None, None)
        tenth = Node(10, None, None)
        eleventh = Node(11, None, None)
        twelve = Node(12, None, None)
        thirteenth = Node(13, None, None)
        fourteenth = Node(14, None, None)
        fifteenth = Node(15, None, None)

        first.left = second
        first.right = third
        second.left = fourth
        second.right = fifth
        third.left = sixth
        third.right = seventh
        fourth.left = eighth
        fourth.right = ninth
        fifth.left = tenth
        fifth.right = eleventh
        sixth.left = twelve
        sixth.right = thirteenth
        seventh.left = fourteenth
        seventh.right = fifteenth
        
        tree = Tree(first)

        result = [['|' '|' '|' '|' '|' '|' '|' '1' '|' '|' '|' '|' '|' '|' '|'], 
        ['|' '|' '|' '2' '|' '|' '|' '|' '|' '|' '|' '3' '|' '|' '|'], 
        ['|' '4' '|' '|' '|' '5' '|' '|' '|' '6' '|' '|' '|' '7' '|'],
        ['8' '|' '9' '|' '10' '|' '11' '|' '12' '|' '13' '|' '14' '|' '15']]

        assert self.tree.print_tree(first) == result
