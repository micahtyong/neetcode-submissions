# ord('a') - ord('a') = 0
FIRST_LETTER_ORD = ord('a')

# Idea: trie
# - children is a list of pointers to next trie node

# Edge cases
# an, and
# - can have multiple cases where it's the last letter!
# - still can have children
# and, gidder
# - create new trie node for each level? 
# - i think we have to... because "gid" is not a word
# - technically could use a dict in addition

class TrieNode:
    def __init__(self, char: str = '', is_last_letter: bool = False):
        self.char = char
        self.children = [None] * 26
        self.is_last_letter = is_last_letter
    
    def __str__(self) -> str:
        print(self.char, self.is_last_letter)
        valid_children = []
        for child in self.children:
            if child != None:
                valid_children.append(child.__str__())

        return f"char={self.char}, is_last_letter={self.is_last_letter}, children={valid_children}"

class PrefixTree:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        pointer = self.trie
        for i, c in enumerate(word):
            index = ord(c) - FIRST_LETTER_ORD
            # print("index for", c, "is", index)
            if pointer.children[index] == None:
                pointer.children[index] = TrieNode(c)

            is_last_letter = i == len(word) - 1
            if is_last_letter:
                pointer.children[index].is_last_letter = True

            pointer = pointer.children[index]
        # print(word, self.trie)
        
    def search(self, word: str) -> bool:
        pointer = self.trie
        for i, c in enumerate(word):
            index = ord(c) - FIRST_LETTER_ORD
            # print("index for", c, "is", index)
            if pointer.children[index] == None:
                # print("Couldn't finish word", word, "got to i,c", i, c)
                return False
            
            is_last_letter = i == len(word) - 1
            if is_last_letter and pointer.children[index].is_last_letter:
                # print("Reached the end of the word", word)
                return True
            
            pointer = pointer.children[index]
        return False

    def startsWith(self, prefix: str) -> bool:
        pointer = self.trie
        for i, c in enumerate(prefix):
            index = ord(c) - FIRST_LETTER_ORD
            if pointer.children[index] == None:
                return False
            pointer = pointer.children[index]
        return True
        
        