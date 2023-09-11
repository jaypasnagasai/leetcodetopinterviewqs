# 130. Surrounded Regions

class Solution(object):
    def solve(self, board):
        n,m=len(board),len(board[0])
        seen=set()
        def is_valid(i,j):
            return 0 <= i < n and 0<= j <m and board[i][j]=="O" and (i,j) not in seen
        def is_border(i,j):
            return i == 0 or i == n-1 or j == 0 or j == m-1
        def dfs(i,j):
            board[i][j]="y"
            seen.add((i,j))
            for dx , dy in ((0,1) ,(0,-1) ,(1,0),(-1,0)):
                new_i , new_j = dx + i , dy + j
                if is_valid(new_i , new_j):
                    dfs(new_i , new_j)
            
        for i in range(n):
            for j in range(m):
                if is_border(i,j) and board[i][j]=="O":
                    dfs(i,j) 
                    
        for i in range(n):
            for j in range(m):
                if board[i][j]=="y":
                    board[i][j]="O"
                else:
                    board[i][j]="X"
        return board
       
