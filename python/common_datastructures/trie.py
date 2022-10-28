class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Trie:
    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word):
        node = self.trie
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True

    def search(self, word):
        node = self.__get_prefix_node__(word)
        return True if node and node.is_word else False
    
    def __get_prefix_node__(self, prefix):
        node = self.trie
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
    
    def is_prefix(self, prefix):
        node = self.__get_prefix_node__(prefix)
        return True if node else False


def test():
    trie = Trie()
    trie.insert('Jai-Hanuman')
    assert trie.search(
        'Jai-Hanuman') == True, '"Jai-Hanuman" should be in the trie'
    assert trie.search(
        'Jai-Hanuma') == False, '"Jai-Hanuma" should not be in the trie'
    assert trie.is_prefix(
        'Jai-Hanuma') == True, '"Jai-Hanuma" should be in the trie as prefix'


if __name__ == "__main__":
    test()
