from Field import Field


class Sudoku:

    def __init__(self, filename):
        self.board = self.read_sudoku(filename)   
          
    def __str__(self):
        output = "╔═══════╦═══════╦═══════╗\n"
        # iterate through rows
        for i in range(9):
            if i == 3 or i == 6:
                output += "╠═══════╬═══════╬═══════╣\n"
            output += "║ "
            # iterate through columns
            for j in range(9):
                if j == 3 or j == 6:
                    output += "║ "
                output += str(self.board[i][j]) + " "
            output += "║\n"
        output += "╚═══════╩═══════╩═══════╝\n"
        return output

    @staticmethod
    def read_sudoku(filename):
        """
        Read in a sudoku file
        @param filename: Sudoku filename
        @return: A 9x9 grid of Fields where each field is initialized with all its neighbor fields
        """
        assert filename is not None and filename != "", "Invalid filename"
        # Setup 9x9 grid
        grid = [[Field for _ in range(9)] for _ in range(9)]
        
        try:
            with open(filename, "r") as file:
                for row, line in enumerate(file):
                    for col_index, char in enumerate(line):
                        if char == '\n':
                            continue
                        if int(char) == 0:
                            grid[row][col_index] = Field()
                        else:
                            grid[row][col_index] = Field(int(char))
               
        except FileNotFoundError:
            print("Error opening file: " + filename)

        Sudoku.add_neighbours(grid)
        return grid

    @staticmethod
    def add_neighbours(grid):
        """
        Adds a list of neighbors to each field
        @param grid: 9x9 list of Fields
        """
 
    # TODO: for each field, add its neighbors

        for row in range(9):
            for col in range(9):        # iterate over the fields in the grid
                field = grid[row][col]
                neighbours = []

                for nc in range(9):     # find the neighbours in the colum
                    if nc == col:
                        continue
                    #neighbours.append(grid[row][nc].get_value())
                    neighbours.append(grid[row][nc].set_neighbours(col))

                for nr in range(9):       # find the neighbours in the row
                    if nr == row:
                        continue
                    #neighbours.append(grid[nr][col].get_value())
                    neighbours.append(grid[nr][col].set_neighbours(row))

                subgrid_row = row//3            # find the neighbours in the subgrid
                subgrid_col = col//3
                #subgrid_n   = subgrid_row *3 + subgrid_col+1
                subgrid_row_start = subgrid_row * 3
                subgrid_col_start = subgrid_col * 3

                for sr in range(subgrid_row_start,subgrid_row_start + 3):
                    for sc in range (subgrid_col_start,subgrid_col_start + 3):
                        if sr == row or sc == col:
                            continue
                        #neighbours.append(grid[sr][sc].get_value())
                        #neighbours.append(grid[sr][sc].set_neighbours())

                field.set_neighbours(neighbours)
                print("position", row, ",", col, "has neighbours", neighbours)


    def board_to_string(self):
        output = ""
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                output += str (self.board[row][col].get_value()) #convert to string 
            output += "\n"
        return output

    def get_board(self):
        return self.board
