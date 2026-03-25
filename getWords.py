"""
This file contains the "getWords" helper function for the Lingo assignment

Author: Spencer Caplan
Date Last Modified: Oct 9, 2024
"""

def getWords():
    """
    get a list of 5 letter English dictionary words that are
    not proper nouns
    """

    def isLatinOne(word):
        """
        be sure every letter in the word is between 'a' and 'z'.
        """
        for letter in word:
            if not ('a' <= letter <= 'z'):
                return False
        return True

    ans = []
    with open("wordsclean.txt") as f:
        for line in f:
            word = line.strip()
            if word.islower() and word.isalpha() and len(word)==5:
                ans.append(word)
    return [a for a in ans if isLatinOne(a)]