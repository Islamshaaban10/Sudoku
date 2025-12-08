
class Game:
    def __init__(self, sudoku):
        self.sudoku = sudoku

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
        domain_queue = []

        for col in range(9):
            for row in range(9):
                value = grid[col][row]
                domain = grid[col][row].get_domain()
                neighbours = grid[col][row].get_neighbours()

                if value.is_finalized() is False:   # check if the field is empty
                    Game.remove_neighbours(self, domain, neighbours, value)
                    # print("for field", col, ",", row, "the revised domain is", domain)
                    var_queue.append([col, row])    # add the fields to the queue
                    domain_queue.append(domain)

                    if value.get_domain_size() == 1:
                        value.set_value(domain[0])  # if the domain has one value left, set the field to that value
                        # print("for field", col, ",", row, "the new value is:", value)
                        var_queue.remove([col, row])    # remove the field from the queue
                        domain_queue.remove(domain)

        domain_queue_sorted = sorted(domain_queue, key=len)
        # print(domain_queue_sorted)

        return True

    def remove_neighbours(self, domain, neighbour, value):
        for n_value in neighbour:
            if n_value != 0 and n_value in domain:
                value.remove_from_domain(n_value)   # remove all neighbouring values from the domain

    def valid_solution(self) -> bool:
        """
        Checks the validity of a sudoku solution
        @return: true if the sudoku solution is correct
        """
        # TODO: implement valid_solution function
        return False
