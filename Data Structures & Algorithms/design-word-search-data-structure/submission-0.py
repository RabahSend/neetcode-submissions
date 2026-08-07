class WordDictionary:

    class Node:
        def __init__(self):
            self.children = [None] * 26
            self.endOfWord = False

    def __init__(self):
        self.root = self.Node()

    def addWord(self, word: str) -> None:
        current = self.root

        for i in range(len(word)):
            index = ord(word[i]) - ord('a')

            if not current.children[index]:
                current.children[index] = self.Node()

            current = current.children[index]

        current.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(pos, node):
            if pos == len(word):
                return node.endOfWord

            if word[pos] != '.':
                index = ord(word[pos]) - ord('a')
                if not node.children[index]:
                    return False
                else:
                    return dfs(pos+1, node.children[index])
            else:
                for i in range(26):
                        if node.children[i] and dfs(pos+1, node.children[i]):
                            return True

            return False

        return dfs(0, self.root)

