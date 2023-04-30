class BPlusTreeNode:
    def __init__(self, order):
        self.order = order
        self.keys = []
        self.values = []

    def split(self):
        raise NotImplementedError

    def merge(self, sibling):
        raise NotImplementedError

    def search(self, key):
        raise NotImplementedError


class InternalNode(BPlusTreeNode):
    def __init__(self, order):
        super().__init__(order)
        self.children = []

    def split(self):
        mid = len(self.keys) // 2
        right_sibling = InternalNode(self.order)
        right_sibling.keys = self.keys[mid + 1:]
        right_sibling.children = self.children[mid + 1:]
        self.keys = self.keys[:mid]
        self.children = self.children[:mid + 1]
        return self.keys[-1], right_sibling

    def merge(self, sibling):
        self.keys.append(sibling.keys[0])
        self.keys.extend(sibling.keys[1:])
        self.children.extend(sibling.children)
        return self

    def search(self, key):
        for i, k in enumerate(self.keys):
            if key < k:
                return self.children[i].search(key)
        return self.children[-1].search(key)


class LeafNode(BPlusTreeNode):
    def __init__(self, order):
        super().__init__(order)
        self.next = None
        self.prev = None

    def split(self):
        mid = len(self.keys) // 2
        right_sibling = LeafNode(self.order)
        right_sibling.keys = self.keys[mid:]
        right_sibling.values = self.values[mid:]
        self.keys = self.keys[:mid]
        self.values = self.values[:mid]
        right_sibling.prev = self
        right_sibling.next = self.next
        if self.next:
            self.next.prev = right_sibling
        self.next = right_sibling
        return right_sibling.keys[0], right_sibling

    def merge(self, sibling):
        self.keys.extend(sibling.keys)
        self.values.extend(sibling.values)
        self.next = sibling.next
        if sibling.next:
            sibling.next.prev = self
        return self

    def search(self, key):
        for i, k in enumerate(self.keys):
            if key == k:
                return self.values[i]
            if key < k:
                return None
        return None

