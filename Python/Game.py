from Field import Field
from Sudoku import Sudoku


class Game:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.field = Field()

    def show_sudoku(self):
        print(self.sudoku)

    def solve(self) -> bool:
        """
        Implementation of the AC -3 algorithm
        @return: true if the constraints can be satisfied, false otherwise
        """
        # TODO: implement AC-3

        grid = self.sudoku.get_board()
        var_queue = []

        for col in range(9):
            for row in range(9):
                value = grid[col][row]
                #print("field", col, ",", row, "has value:", value)

                domain = grid[col][row].get_domain()

                var_queue.append([col, row])

                neighbours = grid[col][row].get_neighbours()

                Game.revise(self, domain, neighbours, value)


        return True

    def revise(self, domain, neighbour, value):
        for n_value in neighbour:
            if n_value != 0:
                value.remove_from_domain(n_value)
                print("revised domain", domain)

        return True


    def valid_solution(self) -> bool:
        """
        Checks the validity of a sudoku solution
        @return: true if the sudoku solution is correct
        """
        # TODO: implement valid_solution function
        return False
