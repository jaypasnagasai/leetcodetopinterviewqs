# 173. Binary Search Tree Iterator

class BSTIterator:
    st=[]
    def __init__(self, root):
        self.pushall(root)

    def next(self):
        temp=self.st.pop()
        self.pushall(temp.right)
        return temp.val

    def hasNext(self):
        return True if len(self.st)>0 else False

    def pushall(self,root):
        while root:
            self.st.append(root)
            root=root.left
