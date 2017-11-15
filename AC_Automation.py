from collections import deque
class AC_State:
    def __init__(self):
        self.currentWord=None
        self.nextStates={}
        self.failState=None
class AC_Automation:
    def __init__(self):
        self.root=AC_State()
    def insert(self,word):
        '''
        :type word: str
        '''
        cur=self.root
        for w in word:
            if w not in cur.nextStates:
                cur.nextStates[w]=AC_State()
            cur=cur.nextStates[w]
        cur.currentWord=word
    def initFailState(self):
        queue=deque([self.root])
        while queue:
            cur=queue.popLeft()
            for lb,ns in cur.nextStates.items():
                temp=cur.failState
                while temp and lb not in temp.nextStates:
                    temp=temp.failState
                ns.failState=temp.nextStates[lb] if temp else root
                queue.append(ns)
    def query(self,sentence):
        '''
        :type sentence: str
        '''
        cur=self.root
        for ch in sentence:
            while ch not in cur.nextStates and cur:
                cur=cur.failState
            cur=cur.nextStates[ch] if cur else root
            if cur.currentWord:
                print cur.currentWord
