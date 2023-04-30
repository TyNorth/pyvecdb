# b_plus_tree.py
from .node import InternalNode, LeafNode


class BPlusTree:
    def __init__(self, order):
        self.order = order
        self.root = LeafNode(order)

    def insert(self, key, value):
        node, index = self._search(key)
        node.keys.insert(index, key)
        node.values.insert(index, value)
        if len(node.keys) == self.order:
            self._split(node)

    def get(self, key):
        node, index = self._search(key)
        if index < len(node.keys) and node.keys[index] == key:
            return node.values[index]
        return None

    def delete(self, key):
        node, index = self._search(key)
        if index < len(node.keys) and node.keys[index] == key:
            node.keys.pop(index)
            node.values.pop(index)
            if node == self.root and not node.keys:
                self.root = LeafNode(self.order)
            elif node != self.root and len(node.keys) < self.order // 2:
                self._merge(node)

    def _search(self, key):
        node = self.root
        while isinstance(node, InternalNode):
            index = self._find_index(node.keys, key)
            node = node.children[index]
        index = self._find_index(node.keys, key)
        return node, index

    def _find_index(self, keys, key):
        for i, k in enumerate(keys):
            if key <= k:
                return i
        return len(keys)

    def _split(self, node):
        if isinstance(node, LeafNode):
            right_sibling_key, right_sibling = node.split()
            parent = self._get_parent(node)
            parent.keys.insert(self._find_index(parent.keys, right_sibling_key), right_sibling_key)
            parent.children.insert(self._find_index(parent.keys, right_sibling_key) + 1, right_sibling)
        else:
            right_sibling_key, right_sibling = node.split()
            parent = self._get_parent(node)
            parent.keys.insert(self._find_index(parent.keys, right_sibling_key), right_sibling_key)
            parent.children.insert(self._find_index(parent.keys, right_sibling_key) + 1, right_sibling)

    def _merge(self, node):
        parent = self._get_parent(node)
        index = parent.children.index(node)
        if index > 0 and len(parent.children[index - 1].keys) > self.order // 2:
            sibling = parent.children[index - 1]
            node.keys.insert(0, sibling.keys.pop())
            node.values.insert(0, sibling.values.pop())
            parent.keys[index - 1] = sibling.keys[-1]
        elif index < len(parent.children) - 1 and len(parent.children[index + 1].keys) > self.order // 2:
            sibling = parent.children[index + 1]
            node.keys.append(sibling.keys.pop(0))
            node.values.append(sibling.values.pop(0))
            parent.keys[index] = sibling.keys[0]
        else:
            if index == 0:
                sibling = parent.children[1]
                right_sibling_key = parent.keys.pop(0)
            else:
                sibling = parent.children[-2]
                right_sibling_key = parent.keys.pop()
            node.merge(sibling)
            parent.children.remove(sibling)
            if not parent.keys and parent == self.root:
                        self.root = node

    def _get_parent(self, node):
        if node == self.root:
            parent = InternalNode(self.order)
            parent.children.append(node)
            self.root = parent
            return parent
        parent = self.root
        while isinstance(parent, InternalNode):
            for i, child in enumerate(parent.children):
                if node == child:
                    return parent
                if node in child:
                    parent = child
                    break
        return None

if '__name__' == '__main__':
    tree = BPlusTree(order=4)

    # insert key-value pairs
    tree.insert(1, "one")
    tree.insert(2, "two")
    tree.insert(3, "three")
    tree.insert(4, "four")
    tree.insert(5, "five")
    tree.insert(6, "six")

    # get values by key
    assert tree.get(3) == "three"
    assert tree.get(6) == "six"

    # delete key-value pairs
    tree.delete(2)
    tree.delete(4)

    # get values by key
    assert tree.get(2) == None
    assert tree.get(4) == None