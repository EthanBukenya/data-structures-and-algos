class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = ' ' * self.get_level() * 4
        prefix = spaces + '|___' if self.parent else ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("laptop")
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Lenovo"))
    laptop.add_child(TreeNode("Asus"))

    tv = TreeNode("T.V")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Hisense"))
    tv.add_child(TreeNode("Flamingo"))

    phones = TreeNode("Cell Phones")
    phones.add_child(TreeNode("Iphone"))
    phones.add_child(TreeNode("Sumsung"))
    phones.add_child(TreeNode("Nokia"))

    root.add_child(phones)
    root.add_child(tv)
    root.add_child(laptop)

    return root


if __name__ == '__main__':
    root = build_tree()
    root.print_tree()
    pass
