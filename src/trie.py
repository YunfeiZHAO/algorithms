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


class WordDictionary:
    """https://leetcode.com/problems/design-add-and-search-words-data-structure/"""
    def __init__(self):
        self._trie = {}

    def addWord(self, word: str) -> None:
        """ insert a word in trie """
        cur = self._trie
        for w in word:
            if w not in cur:
                cur[w] = {}
            cur = cur[w]
        cur['word'] = True

    def dfs(self, cur, postfix):
        """dfs to check the postfix"""
        if len(postfix) == 0:
            return 'word' in cur

        c = postfix[0]
        postfix = postfix[1:]
        if c == '.':
            result = False
            for key in cur:
                if key != 'word' and self.dfs(cur[key], postfix):
                    result = True
                    break
            return result
        elif not c in cur:
            return False
        else:
            return self.dfs(cur[c], postfix)

    def search(self, word: str) -> bool:
        """ check if a word in trie, 
            the word can contain '.' which is a wildcard
        """
        return self.dfs(self._trie, word)

if __name__ == "__main__":
    obj = WordDictionary()
    obj.addWord("a")
    obj.addWord("a")
    # obj.search(".")
    # obj.search("a")
    # obj.search("aa")
    # obj.search("a")
    # obj.search(".a")
    obj.search("a.")
