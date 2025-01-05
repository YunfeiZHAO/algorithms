""" Trie implementation """

class Trie:
    """https://leetcode.com/problems/implement-trie-prefix-tree/description/"""
    def __init__(self):
        self._trie = {}

    def insert(self, word: str) -> None:
        """ insert a word in trie """
        cur = self._trie
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['word'] = True

    def search(self, word: str) -> bool:
        """ check if a word in trie """
        cur = self._trie
        for w in word:
            if w not in cur:
                return False
            cur = cur[w]
        # Check if 'word' flag is set at the end of the word
        return 'word' in cur and cur['word'] is True

    def startsWith(self, prefix: str) -> bool:
        """ 
        check if there is a previously inserted 
        string word that has the prefix
        """
        cur = self._trie
        for w in prefix:
            if w not in cur:
                return False
            cur = cur[w]
        return True
