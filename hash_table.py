# Hash maps utilize hash functions in order to generate indices for elements in a list
# hash function example

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self, key, val):
        h = self.get_hash(key)

        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key, val)
                found = True
                break
        if not found:
            self.arr[h].append(key, val)

    def __getitem__(self, index):
        h = self.get_hash(index)
        return self.arr[h]

    def __delitem__(self, key):
        h = self.get_hash(key)
        self.arr[h] = None


h = HashTable()

print(h.get_hash('march 6'))
print(h.get_hash('march 17'))

h['march 6'] = 120
h['march 7'] = 108
h['march 17'] = 459
h['march 9'] = 209
h['march 8'] = 208

print(h['march 6'])
print(h['march 17'])
# del h['march 7']
# print(h.arr)
