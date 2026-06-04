# Same as trie, but every level has a wildcard node.

# TrieNode
    # char = ''
    # is_last_letter = False
    # next_char = {
    #       ".": TrieNode()
    #   }
    # Well, this ^ causes infinite recursion.
    # We'll do it lazily in addWord
    #   - Needs an equivalent path to fan out? 
    # Hmm. Or we need it lazily in search
    # Can basically check that dict is not empty
    # And go through first char

# bay, bad, bayview
# search(b...) =>
    # goes through each char 
    # for the ".", choose first letter?
    # actually, need to bfs from all the letters
    # bad doesnt have 4 chars
    # but bayview has >4 chars
    # so we do fan out 
    # can be very expensive to search whole tree

# opt: every trie node has a "." by construction
# as we add words, we add a trie node not to the 
# char's children (e.g., "a"'s children), but also 
# "."'s children 
# so "." is a superset of all the connections at that level

# then search is still O(n) instead of like, O(M)
# where n is length of word
# and M is all the characters ever seen, so M >> n

# addWord


class WordDictionary:

    def __init__(self):
        
        # Initialize your data structure here.
        self.children = [None]*26
        self.isEndOfWord = False
        

    def addWord(self, word: str) -> None:

        # Adds a word into the data structure.
        curr = self
        for c in word:
            if curr.children[ord(c) - ord('a')] == None:
                curr.children[ord(c) - ord('a')] = WordDictionary()
            curr = curr.children[ord(c) - ord('a')]
        
        curr.isEndOfWord = True;
        

    def search(self, word: str) -> bool:

        # Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        curr = self
        for i in range(len(word)):
            c = word[i]
            if c == '.':
                for ch in curr.children:
                    if ch != None and ch.search(word[i+1:]): return True
                return False
            
            if curr.children[ord(c) - ord('a')] == None: return False
            curr = curr.children[ord(c) - ord('a')]
        
        return curr != None and curr.isEndOfWord
        
