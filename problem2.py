## Problem2
"""
Given an array of numbers of length N, 
find both the minimum and maximum. 

Follow up : Can you do it using less than 2 * (N - 2) comparison
"""
## Problem3 (https://leetcode.com/problems/game-of-life/)

"""
Time Complexity: O(N^2)
Space Complexity: O(N^2)
"""

class Solution:
    def count_live_dead(self, board, nrows, ncols, i, j):
        num_live, num_dead = 0, 0
        
        loc = [ (0, -1), (1, 1), (1, 0), (0, 1), (-1, -1), (-1, 0), (1, -1), (-1, 1) ]
        
        for dx, dy in loc:
            x = dx + i
            y = dy + j
            
            if x < 0 or x >= nrows or y < 0 or y >= ncols:
                continue
            if board[x][y] == 0:
                num_dead += 1
            else:
                num_live += 1
        #print(num_live, num_dead)
        return (num_live, num_dead)
        
    
    def update_next_state(self, board, nrows, ncols, i, j):
        num_live, num_dead = self.count_live_dead(board, nrows, ncols, i, j)
        
        #print(i, j, num_live, num_dead)
        
        if board[i][j] == 1:                         #if live cell
            
            if num_live < 2:                    #if fewer than 2 live cells
                return 0
            elif num_live == 2 or num_live == 3:#if live cells equal to 2 or 3
                return 1
            elif num_live > 3:                  #if live cells more than 3
                return 0
        elif board[i][j] == 0 and num_live == 3: #dead cells becomes alive
            return 1
        else:
            return board[i][j]
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrows = len(board)
        ncols = len(board[0])
        
        next_state = []
        for i in range(nrows):
            next_state.append( [0 for j in range(ncols)] )
                    
        for i in range(nrows):
            for j in range(ncols):
                next_state[i][j] = self.update_next_state(board, nrows, ncols, i, j)
                #print(next_state[i][j])
        #print(next_state)
        
        for i in range(nrows):
            for j in range(ncols):
                board[i][j] = next_state[i][j]
        #board = next_state[::]
        print(board)
        