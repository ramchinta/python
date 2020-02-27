'''
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.
'''


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = []

    def insert(self, word) -> None:
        """
        Inserts a word into the trie.
        """
        self.trie.append(word)

    def search(self, word) -> bool:
        """
        Returns if the word is in the trie.
        """
        if word in self.trie:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        for i in self.trie:
            if prefix == i[:len(prefix)]:
                return True
        return False

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
trie = Trie();

print(trie.insert("apple"));
print(trie.search("apple"));   #returns true
print(trie.search("app"));     # returns false
print(trie.startsWith("app"));  #returns true
print(trie.insert("app"));
print(trie.search("app"));     # returns true