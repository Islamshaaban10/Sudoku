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

        domain = self.field.get_domain()
        # print("domain:", domain)
        neighbours = self.field.get_neighbours()    # this returns an empty list, it should not do that
        print("neighbours:", neighbours)

        for nc in range(9):
            col = nc
            for nr in range(9):
                row = nr

                for var in domain:
                    # print("variable in domain:", d_variable)
                    if var in neighbours:
                        self.field.remove_from_domain(var)

                    #print("for position", col, ",", row)
                    #print("the updated domain is:", domain)

        return True

    def valid_solution(self) -> bool:
        """
        Checks the validity of a sudoku solution
        @return: true if the sudoku solution is correct
        """
        # TODO: implement valid_solution function
        return False
