class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        result = [0] * len(grid[0])
        
        for col in range(len(grid[0])):
            current_col = col
            for row in range(len(grid)):
                next_col = current_col + grid[row][current_col]
                if next_col < 0 or next_col >= len(grid[0]) or grid[row][next_col] != grid[row][current_col]:
                    result[col] = -1
                    break
                result[col] = next_col
                current_col = next_col
        return result
            
    
    
    
    
    #     result = []
    #     number_of_balls = len(grid[0])
    #     for i in range(number_of_balls):
    #         result.append(self.ball_can_fall(0,i,grid))
    #     return result
    # def ball_can_fall(self, row, col, grid):
    #     # We have exited the grid
    #     if row == len(grid):
    #         return col
    #     # We have hit a wall
    #     if col < 0 or col >= len(grid[0]):
    #         return -1
    #     # The ball will not roll out of bounds and can continue
    #     if grid[row][col] == 1 and col+1 < len(grid[0]) and grid[row][col+1] == 1:
    #         return self.ball_can_fall(row+1, col+1, grid)
    #     elif grid[row][col] == -1 and col-1 >= 0 and grid[row][col-1] == -1:
    #         return self.ball_can_fall(row+1, col-1, grid)
    #     return -1