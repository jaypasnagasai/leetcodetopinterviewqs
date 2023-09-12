# 427. Construct Quad Tree

class Solution(object):
    def makeTree(self, grid, x, y, n):
        self.startVal = grid[x][y]
        newNode = Node(self.startVal, True, None, None, None, None)
        for i in range(x, x+n):
            for j in range(y, y+n):
                if grid[i][j] != self.startVal:
                    newNode.isLeaf = False
                    newNode.topLeft = self.makeTree(grid, x, y, n/2)
                    newNode.topRight = self.makeTree(grid, x, y+n/2, n/2)
                    newNode.bottomLeft = self.makeTree(grid, x+n/2, y, n/2)
                    newNode.bottomRight = self.makeTree(grid, x+n/2, y+n/2, n/2)
                    return newNode
        return newNode

    def construct(self, grid):
        n = len(grid)
