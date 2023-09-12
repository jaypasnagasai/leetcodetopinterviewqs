# 909. Snakes and Ladders

class Solution(object):
    def snakesAndLadders(self, board):
        def convert_to_list(board):
            list_board = [0]
            reversed = False
            for i in range(len(board)-1, -1, -1):
                row = board[i]
                if (reversed):
                    row.reverse()
                for num in row:
                    list_board.append(num)
                reversed = not reversed
            return list_board

        list_board = convert_to_list(board)

        queue = [[1,0]] 
        visited = set()

        while (len(queue) > 0):
            index, rounds = queue.pop(0)

            if (index == len(list_board)-1):
                return rounds
            
            for next_index in range(index + 1, min(index + 7, len(list_board))):
                

                if list_board[next_index] != -1:
                    next_index = list_board[next_index]
                
                if next_index not in visited:
                    visited.add(next_index)
                    queue.append([next_index, rounds + 1])

        return -1
