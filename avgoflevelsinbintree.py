# 637. Average of Levels in Binary Tree

import Queue;
class Solution(object):
    def averageOfLevels(self, root):
        q = Queue.Queue()
        q.put((root,0))
        preLevel = 0 
        curLst = []
        lst = []
        while q.qsize()>0:
            curNode,curLevel = q.get()
            if curLevel == preLevel:
                curLst.append(curNode.val)
            else:
                lst.append(curLst)
                curLst = [curNode.val]
                preLevel = curLevel
            if curNode.left:
                q.put((curNode.left,curLevel+1))
            if curNode.right:
                q.put((curNode.right,curLevel+1))
        lst.append(curLst)

        rst = []
        for subLst in lst:
            rst.append((sum(subLst)+0.0)/len(subLst))
        return rst
