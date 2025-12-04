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

        neighbours = self.field.get_neighbours()    # this returns an empty list, it should not do that
        domain = self.field.get_domain()

        var_queue = [(val_col, val_row) for val_col in range(9) for val_row in range(9)]



        val_queue = [d_val for d_val in domain]
        neighbour_queue = [n_val for n_val in neighbours]

        print("var_queue:", var_queue)
        print("val_queue", val_queue)
        print("neighbour_queue", neighbour_queue)

        return True

    def revise(self, var, neighbour):
        return True



    def valid_solution(self) -> bool:
        """
        Checks the validity of a sudoku solution
        @return: true if the sudoku solution is correct
        """
        # TODO: implement valid_solution function
        return False
