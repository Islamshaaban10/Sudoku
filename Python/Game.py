
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
        
        Grid = self.sudoku.get_board()
        queue = []

        # creat arcs queue
        for row in range(9):
            for col in range(9):
                 field = Grid[row][col]   

                 #if not field.is_finalized():
                    #neighbours_values =set()
                    #domain = field.get_domain()
                    #print(" Domain of ",row,col,domain)
                 for n in field.get_neighbours():
                        queue.append((field,n))     # List of all arcs

      # revise function 
        def revise (Xm,Xn):

            if Xm.is_finalized():
                return False
            
            revised = False
            if Xn.is_finalized():
                Xn_domain =[ Xn.get_value()]
            else:
                Xn_domain = Xn.get_domain()

            Xm_domain = Xm.get_domain()
            copy_Xm_domain = Xm_domain.copy()

            for md in copy_Xm_domain:
                    if not any (md != nd  for nd in Xn_domain)  :
                      Xm.remove_from_domain(md) 
                      revised = True
            return revised           
            
        counter = 0
        while queue :
            counter =counter +1
            print ( "counter", counter)
            print(self.sudoku)
            f,n =queue.pop()

            if   revise(f,n):
               # if f.get_domain_size()==0 and not f.is_finalized():
                    #return false
                
                for xk in f.get_other_neighbours(n):
                    queue.append((xk,f))
                
                   # if n.get_value() != 0 :
                      # neighbours_values.add(n.get_value())
                       

                    # add to queue (field , neighbours)

                 # remove neighbours values from the domain  
                 #if not field.is_finalized(): 
                   # for d in domain :                         
                        #if d in neighbours_values:
                          #  field.remove_from_domain(d)
                           # print ("remove domain",d, row,col,field.get_domain())

                 #print("neighbours_values of ",row,col,neighbours_values)
                # print ("new domain of ", row,col,field.get_domain())              
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
        # TODO: implement valid_solution function
        return False
