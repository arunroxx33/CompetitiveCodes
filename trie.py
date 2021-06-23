
from collections import *
class Node:
    def __init__(self):
        self.isthere = 0
        self.l = {}
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        """
        temp = self.root
        for j in word:
            if ord(j) - ord('a') not in temp.l:
                temp.l[ord(j) - ord('a')] = Node()
            temp = temp.l[ord(j) - ord('a')]
        temp.isthere = 1

    def search(self, word):
        """
        Returns if the word is in the trie.
        """
        temp = self.root
        for j in word:
            if ord(j) - ord('a') not in temp.l:
                return False
            temp = temp.l[ord(j) - ord('a')]
        return True if temp.isthere else False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        temp = self.root
        for j in prefix:
            if ord(j) - ord('a') not in temp.l:
                return False
            temp = temp.l[ord(j) - ord('a')]
        return True

# a = Trie()
# a.insert('asdmoasd')
# print(a.search('asd'))
# print(a.startsWith('asd'))
# print(a.startsWith("fuck"))

