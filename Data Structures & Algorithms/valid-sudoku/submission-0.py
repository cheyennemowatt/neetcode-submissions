class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # 3 lists of sets: rows, cols, squares -> this how we will keep track of duplicates, 
        #nested loop: for r in range(len(9)), for c in range(len(9)), the sets are keeping track of all the rows, while this lets us access each indivual row
        # value = board[r][c] -> this is how we get the value to know if it has appeared somewhere else
        # check if value == ".",, so continue
        # determine square location -> square_index = (r//3 *3) + c//3 
        #check the 3 conditions now if value in row[r]... return false
        #append
        #return true

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        squares = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                val = board[r][c]

                if val == ".":
                    continue
                
                squares_index = ((r // 3) * 3) + (c // 3)
                if val in rows[r] or val in cols[c] or val in squares[squares_index]:\
                    return False
                rows[r].add(val)
                cols[c].add(val)
                squares[squares_index].add(val)
        return True
    

