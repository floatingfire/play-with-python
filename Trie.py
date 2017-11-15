class TrieNode:
    def __init__(self):
        self.isAcceptable=False
        self.nextState={}
class Trie:
    def __init__(self):
        self.root=TrieNode()
    def insert(self,word):
        '''
        :type word: str
        '''
        cur=self.root
        for w in word:
            if w not in cur.nextState:
                cur.nextState[w]=TrieNode()
            cur=cur.nextState[w]
        cur.isAcceptable=True
    def query(self,word):
        '''
        :type word: str
        :rtype: bool
        '''
        cur=self.root
        for w in word:
            if w not in cur.nextState:
                return False
            cur=cur.nextState[w]
        return cur.isAcceptable
