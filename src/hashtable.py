# '''
# Linked List hash table key/value pair
# '''
# used for collisions
class LinkedPair:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashTable:
    '''
    A hash table that with `capacity` buckets
    that accepts string keys
    '''
    def __init__(self, capacity):
        self.capacity = capacity  # Number of buckets in the hash table
        self.storage = [None] * capacity


    def _hash(self, key):
        '''
        Hash an arbitrary key and return an integer.

        You may replace the Python hash with DJB2 as a stretch goal.
        '''
        return hash(key)


    def _hash_djb2(self, key):
        '''
        Hash an arbitrary key using DJB2 hash

        OPTIONAL STRETCH: Research and implement DJB2
        '''
        pass


    def _hash_mod(self, key):
        '''
        Take an arbitrary key and return a valid integer index
        within the storage capacity of the hash table.
        '''
        return self._hash(key) % self.capacity

    def get_node(self, key):
        node = self.storage[self._hash_mod(key)]
        while True:
            if node.key == key:
                return node
            else:
                node = node.next


    def insert(self, key, value):
        '''
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Fill this in.
        '''
        #hash the key
        index = self._hash_mod(key)
        
        # There is nothing in storage at the key's index
        if self.storage[self._hash_mod(key)] is None:
            self.storage[self._hash_mod(key)] = LinkedPair(key, value)

        # Key already exists, overwrite the value
        elif self.retrieve(key) is not None:
            node = self.get_node(key)
            node.value = value

        # Key does not exist, append it
        elif self.retrieve(key) is None:
            node = self.storage[self._hash_mod(key)]
            while True:
                if node.next is None:
                    node.next = LinkedPair(key, value)
                    return
                else:
                    node = node.next



    def remove(self, key):
        '''
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Fill this in.
        '''
        index = self._hash_mod(key)
        # There is no matching node, return None
        if self.get_node(key) is None:
            return None


        # Single node at the node's  location
        elif self.storage[index].next is None:
            self.storage[index] = None


        else:
            prev = None
            node = self.storage[index]
            while True:
                # prev = node
                if node.key == key:
                    if node.next is None:
                        prev.next = None
                    else:
                        prev.next = node.next
                    prev.next = node.next
                    break
                else:
                    prev = node
                    node = node.next 


    def retrieve(self, key):
        '''
        Retrieve the value stored with the given key.

        Returns None if the key is not found.

        Fill this in.
        '''
        if self.storage[self._hash_mod(key)] is None:
            return None
        else:
            node = self.storage[self._hash_mod(key)]
            while True:
                if node.key == key:
                    return node.value
                elif node.next is not None:
                    node = node.next
                else:
                    return None



    def resize(self):
        '''
        Doubles the capacity of the hash table and
        rehash all key/value pairs.

        Fill this in.
        '''
        old_map = self.storage
        self.capacity = self.capacity * 2
        self.storage = [None] * self.capacity

        for contents in old_map:
            if contents is None:
                continue
            elif contents.next is None:
                self.insert(contents.key, contents.value)
            else:
                node = contents
                while True:
                    self.insert(node.key, node.value)
                    if node.next is None:
                        break
                    else:
                        node = node.next



if __name__ == "__main__":
    ht = HashTable(2)

    ht.insert("line_1", "Tiny hash table")
    ht.insert("line_2", "Filled beyond capacity")
    ht.insert("line_3", "Linked list saves the day!")

    print("")

    # Test storing beyond capacity
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    # Test resizing
    old_capacity = len(ht.storage)
    ht.resize()
    new_capacity = len(ht.storage)

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    print(ht.retrieve("line_1"))
    print(ht.retrieve("line_2"))
    print(ht.retrieve("line_3"))

    print("")
