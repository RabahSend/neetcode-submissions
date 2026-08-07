class PrefixTree:

    class Node:
        def __init__(self):
            self.childrens = [None] * 26
            self.endOfWord = False

    def __init__(self):
        self.root = self.Node()

    def insert(self, word: str) -> None:
        current = self.root

        for i in range(len(word)):
            if not current.childrens[ord(word[i]) - ord('a')]:
                current.childrens[ord(word[i]) - ord('a')] = self.Node()

            current = current.childrens[ord(word[i]) - ord('a')]

        
        current.endOfWord = True      

    def search(self, word: str) -> bool:
        current = self.root

        for i in range(len(word)):
            complement = ord(word[i]) - ord('a')

            if not current.childrens[complement]:
                return False

            current = current.childrens[complement]

        return current.endOfWord
        

    def startsWith(self, prefix: str) -> bool:
        current = self.root

        for i in range(len(prefix)):
            complement = ord(prefix[i]) - ord('a')

            if not current.childrens[complement]:
                return False

            current = current.childrens[complement]

        return True
        
        