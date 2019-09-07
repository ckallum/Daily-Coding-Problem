# https://ieftimov.com/post/when-why-least-frequently-used-cache-implementation-golang/#targetText=LFU%20is%20a%20caching%20algorithm,how%20frequently%20it%20is%20used.


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DLL(object):
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_node(self, cls, data):
        return self.insert_node(cls, data, self.tail, None)
        # cls is used as DLL can have various different node types

    def insert_node(self, cls, data, prev, next):
        new_node = cls(data)
        new_node.prev = prev
        new_node.next = next

        if prev:
            prev.next = new_node
        if next:
            next.prev = new_node

        if not self.head or next is self.head:
            self.head = new_node
        if not self.tail or prev is self.tail:
            self.tail = new_node
        self.size += 1
        return new_node

    def remove_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current == self.head:
                    self.head = current.next
                else:
                    current.prev.next = current.next
                if current == self.tail:
                    self.tail = current.prev
                else:
                    current.next.prev = current.prev
                break
            else:
                current = current.next
        self.size -= 1

    def get_all_data(self):
        current = self.head
        data = []
        while current:
            data.append(current.data)
            current = current.next
        return data


# A node in the frequency DLL that references to the prev and next items and points to the parent FreqNode
class FreqListItem(Node):
    def __init__(self, data):
        super().__init__(data)
        self.parent = None


# Frequency Node that is a apart of the LFU DLL that has a DLL of FreqListItems that have the same frequency
class FreqNode(DLL, Node):
    def __init__(self, data):
        super().__init__()
        Node.__init__(self, data)

    def add_list_item(self, data):
        node = self.add_node(FreqListItem, data)
        node.parent = self
        return node

    def insert_list_node(self, data, prev, next):
        node = self.insert_node(FreqListItem, data, prev, next)
        node.parent = self
        return node

    def remove_list_node(self, data):
        self.remove_node(data)


# Each item in the cache references to a FreqNode and all the data in that DLL
class CacheItem(object):
    def __init__(self, freq_node, data, node):
        self.freq_node_pointer = freq_node
        self.data = data
        self.node = node


class LFUCache(DLL):
    def __init__(self):
        super().__init__()
        self.hash_table = {}

    def insert_freq_node(self, data, prev, next):
        return self.insert_node(FreqNode, data, prev, next)

    def remove_freq_node(self, data):
        self.remove_node(data)

    def access(self, key):
        if key not in self.hash_table:
            raise Exception("Key not in table")
        cache_item = self.hash_table[key]
        freq_node = cache_item.freq_node_pointer
        next_freq_node = freq_node.next
        if not next_freq_node or next_freq_node.data != freq_node.data + 1:
            next_freq_node = self.insert_freq_node(freq_node.data + 1, freq_node, next_freq_node)
        temp_item = next_freq_node.add_list_item(key)
        cache_item.freq_node_pointer = next_freq_node

        freq_node.remove_list_node(key)
        if freq_node.size == 0:
            self.remove_freq_node(freq_node.data)
        cache_item.node = temp_item
        return cache_item.data

    def insert(self, key, value):
        if key in self.hash_table:
            raise Exception("Key already exists")
        freq_node = self.head
        if not freq_node or freq_node.data != 1:
            freq_node = self.insert_freq_node(1, None, freq_node)
        freq_item = freq_node.add_list_item(key)
        self.hash_table[key] = CacheItem(freq_node, value, freq_item)

    def __repr__(self):
        """Display access frequency list and items.
        Using the representation:
        freq1: [item, item, ...]
        freq2: [item, item]
        ...
        """
        s = ''
        freq_node = self.head
        while freq_node:
            s += '%s: %s\n' % (freq_node.data, freq_node.get_all_data())
            freq_node = freq_node.next
        return s


def main():
    cache = LFUCache()
    cache.insert('key1', 'value1')
    cache.insert('key2', 'value2')
    cache.insert('key3', 'value3')
    cache.insert('key4', 'value4')
    print(cache)
    assert cache.access('key2') == 'value2'
    print(cache)


if __name__ == '__main__':
    main()
