# A Binary search Treeis the internal implementation of a Set.
# It doesn't accept duplicates.
'''
country_list = ["USA", "Angola", "USA", "Mali", "Angola"]
countries_set = set(country_list)
print(countries_set)

'''


class BinarySearchTreeNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return

        if data <= self.data:
            # add to left sub tree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)

        else:
            # add to right sub tree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)


def in_order_traversal(self):
    elements = []
    # visit left tree
    if self.left:
        elements += self.right.in_order_traversal()

    # visit base node
    elements.append(self.data)

    # visit right sub tree
    if self.right:
        elements += self.right.in_order_traversal()

    return elements
