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
        prefix = spaces + "|___" if self.parent else ""

        print(prefix + self.data)
        if self.children:
            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Macbook"))
    laptop.add_child(TreeNode("Dell"))
    laptop.add_child(TreeNode("Thinkpad"))

    Phone = TreeNode("Cell Phone")
    Phone.add_child(TreeNode("Iphone"))
    Phone.add_child(TreeNode("Samsung"))
    Phone.add_child(TreeNode("Nokia"))

    tv = TreeNode("TV")
    tv.add_child(TreeNode("Flamingo"))
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Hisense"))

    root.add_child(Phone)
    root.add_child(tv)
    root.add_child(laptop)

    return root


if __name__ == '__main__':
    root = build_tree()

    root.print_tree()
    pass
