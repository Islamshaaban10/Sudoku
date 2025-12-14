from collections import deque
import time

class Game:
    def __init__(self, sudoku):
        self.sudoku = sudoku
        self.start_time = time.process_time()

    def show_sudoku(self):
        print(self.sudoku)

    def solve(self) -> bool:
        """
        Implementation of the AC -3 algorithm
        @return: true if the constraints can be satisfied, false otherwise
        """

        print("Enter a heuristic (0-2): ")
        heuristic = int(input())

        grid = self.sudoku.get_board()
        queue = deque()

        # create arcs queue List of all arcs
        for row in range(9):
            for col in range(9):
                field = grid[row][col]

                for n in field.get_neighbours():
                    if heuristic == 0:
                        queue.append((field, n))

                    # Heuristics priority to arcs with finalized fields
                    elif heuristic == 1:
                        if n.is_finalized():
                            queue.appendleft((field, n))
                        else:
                            queue.append((field, n))

                    elif heuristic == 2:
                        if n.get_domain_size() < 4:
                            queue.appendleft((field, n))
                        else:
                            queue.append((field, n))

        counter = 0     # for testing and performance check
        while queue:
            counter = counter + 1
            # remove the top of the queue (has most priority)
            f, n = queue.popleft()  

            if self.revise(f, n):
                if f.get_domain_size() == 0 and not f.is_finalized():
                    return False

                for xk in f.get_other_neighbours(n):
                    if xk != n:
                        if heuristic == 0:
                            queue.append((xk, f))

                        # Heuristics priority to arcs with finalized fields
                        elif heuristic == 1:
                            if f.is_finalized():
                                queue.appendleft((xk, f))
                            else:
                                queue.append((xk, f))

                        elif heuristic == 2:
                            if f.get_domain_size() < 4:
                                queue.appendleft((xk, f))
                            else:
                                queue.append((xk, f))

        print(self.sudoku)
        print("counter", counter)

        return True

# revise function
    def revise(self, Xm, Xn):
        # return False if it is finalized
        if Xm.is_finalized():
            return False

        revised = False
        # get domain of the xn (neighbour of Xm)
        if Xn.is_finalized():
            Xn_domain = [Xn.get_value()]
        else:
            Xn_domain = Xn.get_domain()

        # get domain of Xm
        Xm_domain = Xm.get_domain()
        # copy the domain preparing for the following iteration
        copy_Xm_domain = Xm_domain.copy()

        # delete from the xm domain if there is no matching value in xn domain
        for md in copy_Xm_domain:
            if not any(md != nd for nd in Xn_domain):
                Xm.remove_from_domain(md)
                revised = True
        return revised
        
    def valid_solution(self) -> bool:
        """
        Checks the validity of a sudoku solution
        @return: true if the sudoku solution is correct
        """
        grid = self.sudoku.get_board()

       # validate all the fields 
        for row in range(9):
            for col in range(9):
                field = grid[row][col]
                if not field.is_finalized() or any(field.get_value() == n.get_value() for n in field.get_neighbours()):
                    end_time = time.process_time()
                    total_time = end_time - self.start_time
                    print("process time:", total_time)
                    return False
                
        # return True if all fields are valid       
        end_time = time.process_time()
        total_time = end_time - self.start_time
        print("process time:", total_time)
        return True

        
           