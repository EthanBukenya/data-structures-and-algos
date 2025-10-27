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

        if data < self.data:
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
            elements += self.left.in_order_traversal()

        # visit base node
        elements.append(self.data)

        # visit right sub tree
        if self.right:
            elements += self.right.in_order_traversal()

        return elements

    def search(self, val):
        if val == self.data:
            return True

        if val < self.data:
            if self.left:
                return self.left.search(val)
            else:
                return False

        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root


if __name__ == '__main__':

    numbers = [9, 2, 4, 12, 10, 3, 8, 4, 12]

    numbers_tree = build_tree(numbers)
    # print(numbers_tree.in_order_traversal())

    print(numbers_tree.search(20))
