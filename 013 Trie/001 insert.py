from typing import List, Optional


class TrieNode:
    def __init__(self):
        self.freq = 0
        self.child: List[Optional[TrieNode]] = [None] * 26


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def _char_to_index(self, ch):
        return ord(ch) - ord('a')

    def insert(self, word):
        cur = self.root
        for char in word:
            idx = self._char_to_index(char)
            if cur.child[idx] is None:
                cur.child[idx] = TrieNode()
            cur = cur.child[idx]
        cur.freq += 1

    def search(self, word):
        cur = self.root
        for char in word:
            idx = self._char_to_index(char)
            if cur.child[idx] is None:
                return False
            cur = cur.child[idx]
        return True if cur.freq > 0 else False


if __name__ == '__main__':

    # Input keys (use only 'a' through 'z' and lower case)
    keys = ["the", "a", "there", "answer", "any",
            "by", "their"]
    output = ["Not present in trie",
              "Present in trie"]

    # Trie object
    t = Trie()

    # Construct trie
    for key in keys:
        t.insert(key)

    # Search for different keys
    print("{} ---- {}".format("the", output[t.search("the")]))
    print("{} ---- {}".format("these", output[t.search("these")]))
    print("{} ---- {}".format("their", output[t.search("their")]))
    print("{} ---- {}".format("thaw", output[t.search("thaw")]))
