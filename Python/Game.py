
import copy
import queue

from sympy import false, true


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
        queue = []

        # create arcs queue
        for row in range(9):
            for col in range(9):
                field = grid[row][col]

                 #if not field.is_finalized():
                    #neighbours_values =set()
                    #domain = field.get_domain()
                    #print(" Domain of ",row,col,domain)
                for n in field.get_neighbours():
                    queue.append((field, n))     # List of all arcs

        # revise function
        def revise(Xm, Xn):
            #print("xm:", Xm, "Xn:", Xn)

            if Xm.is_finalized():
                return False
            
            revised = False
            if Xn.is_finalized():
                Xn_domain = [Xn.get_value()]
            else:
                Xn_domain = Xn.get_domain()

            Xm_domain = Xm.get_domain()
            copy_Xm_domain = Xm_domain.copy()

            for md in copy_Xm_domain:
                if not any(md != nd for nd in Xn_domain):
                    Xm.remove_from_domain(md)
                    revised = True
            return revised           
            
        counter = 0
        while queue:
            counter = counter + 1
            #print("counter", counter)
            #print(self.sudoku)
            f, n = queue.pop()

            if revise(f, n):
               # if f.get_domain_size()==0 and not f.is_finalized():
                    # return false
                
                for xk in f.get_other_neighbours(n):
                    queue.append((xk, f))

        print(self.sudoku)
        return True
    



    """
            for row in range(9):
                for col in range(9):
                if Grid[row][col].get_domain_size()==0 :
                        continue
                neighbours= Grid[row][col].get_neighbours()
                domain   = Grid[row][col].get_domain()
                #print ("neighbours of ",row, col,neighbours)
                print("domin of",row,col,Grid[row][col].get_domain()) 
                                
                for n in domain:
                        if n in neighbours:
                            #print("n of ",row,col,n)
                            Grid[row][col].remove_from_domain(n)
                print(" New domin of ",row,col, Grid[row][col].get_domain())
                    

            neighbours = self.field.get_neighbours()    # this returns an empty list, it should not do that
            domain = self.field.get_domain()

            var_queue = [(val_col, val_row) for val_col in range(9) for val_row in range(9)]
            #print("var_queue:", var_queue)

            for var in var_queue:
                val_queue = [d_val for d_val in domain]
                neighbour_queue = [n_val for n_val in neighbours]

                #print("val_queue", val_queue)
                #print("neighbour_queue", neighbour_queue)
    

            grid = self.sudoku.get_board()
            var_queue = []

            for col in range(9):
                for row in range(9):
                    value = grid[col][row]
                    domain = grid[col][row].get_domain()
                    neighbours = grid[col][row].get_neighbours()

                    if value.is_finalized() is False:   # check if the field is empty
                        Game.revise(self, domain, neighbours, value)
                        # print("for field", col, ",", row, "the revised domain is", domain)
                        var_queue.append([col, row])    # add the fields to the queue

                        if value.get_domain_size() == 1:
                            value.set_value(domain[0])  # if the domain has one value left, set the field to that value
                            # print("for field", col, ",", row, "the new value is:", value)
                            var_queue.remove([col, row])    # remove the field from the queue

            # print(var_queue)
        

        def revise(self, domain, neighbour, value):
            for n_value in neighbour:
                if n_value != 0 and n_value in domain:
                    value.remove_from_domain(n_value)   # remove all neighbouring values from the domain
    """

    def valid_solution(self) -> bool:
        """
        Checks the validity of a sudoku solution
        @return: true if the sudoku solution is correct
        """

        domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        grid = self.sudoku.get_board()

        for r in range(9):
            for c in range(9):
                field = grid[r][c]
                if field.is_finalized() is False:
                    return False
                else:
                    for row in range(9):
                        for col in range(9):
                            domain_c = domain.copy()
                            domain_r = domain.copy()
                            domain_s = domain.copy()

                            for nc in range(9):
                                value = grid[row][nc].get_value()
                                if value in domain_c:
                                    domain_c.remove(value)

                            for nr in range(9):
                                value = grid[nr][col].get_value()
                                if value in domain_r:
                                    domain_r.remove(value)

                            subgrid_row = row // 3
                            subgrid_col = col // 3
                            subgrid_row_start = subgrid_row * 3
                            subgrid_col_start = subgrid_col * 3

                            for sr in range(subgrid_row_start, subgrid_row_start + 3):
                                for sc in range(subgrid_col_start, subgrid_col_start + 3):
                                    value = grid[sr][sc].get_value()
                                    if value in domain_s:
                                        domain_s.remove(value)

                            if not domain_c and not domain_r and not domain_s:
                                return True
