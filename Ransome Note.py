'''Given an arbitrary ransom note string and another string containing letters from all the magazines,
write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true'''

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
    # For each character, c,  in the ransom note.
        for c in ransomNote:
            # If there are none of c left in the String, return False.
            if c not in magazine:
                return False
            # Find the index of the first occurrence of c in the magazine.
            location = magazine.index(c)
            # Use splicing to make a new string with the characters
            # before "location" (but not including), and the characters
            #after "location".
            magazine = magazine[:location] + magazine[location + 1:]
        # If we got this far, we can successfully build the note.
        return True

print(Solution().canConstruct('aa','aba'))
#True