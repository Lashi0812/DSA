"""
Find the shortest unique prefix to represent each  .

Note: Assume that no word is prefix of another .
"""
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

    def find_prefix(self, word):
        cur = self.root
        prefix = []
        for char in word:
            idx = self._char_to_index(char)
            if cur.child[idx].freq == 1:
                prefix.append(char)
                return "".join(prefix)
            prefix.append(char)
            cur = cur.child[idx]


def main():
    words = ["tri", "trap", "plate", "cat", "part", "place", "tie"]
    trie = Trie()
    for word in words:
        trie.insert(word)
    for word in words:
        print(f"unique prefix of {word:5} is {trie.find_prefix(word)}")


if __name__ == '__main__':
    main()
