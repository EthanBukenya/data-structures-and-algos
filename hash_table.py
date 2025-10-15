# Hash maps utilize hash functions in order to generate indices for elements in a list
# hash function example

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self, key, val):
        h = self.get_hash(key)
        self.arr[h] = val

    def get(self, key):
        h = self.get_hash(key)
        return self.arr[h]


ht = HashTable()
ht.add('march 7', 202)
print(ht.get("march 7"))
