#
# Sorting script for Data Structures & Algorithms
# Carson Forter
#

class MarblesBoard:
    '''
    Class representing an array of sequential numbers to be sorted.
    Methods for switching the first two numbers in array and
    for rotating the first number to back of array.
    '''
    
    def __init__(self, board):
        self.board = board
        
    def get_board(self):
        return self.board

    def switch(self):
        board = self.get_board()[:] #makes a copy of board and returns it because of weird reference behavior
        first = board[0] #could do this in less steps, but more readable this way
        second = board[1]
        board[0] = second
        board[1] = first
        return MarblesBoard(board)

    def rotate(self):
        board = self.get_board()[:]
        first = board[0]
        adjusted_board = []
        for i in range(1,len(board)):
            adjusted_board.append(board[i])
        board = adjusted_board
        board.append(first)
        return MarblesBoard(board)

    def is_solved(self):
        for i in range(0,len(self.board) - 1):
            if self.board[i] > self.board[i + 1]:
                return False
            elif i == len(self.board) - 2:
                return True
        
    def __repr__(self):
        return str(self.board)


class Solver:
    '''
    Calls rotate() and swtich() methods on a
    MarblesBoard object until it is solved
    '''
    
    def __init__(self, marbles_board): 
        self.marbles_board = marbles_board

    def solve(self): 
        print str(self.marbles_board)
        steps = 0
        while self.marbles_board.is_solved() == False:
            steps += 1

            if self.marbles_board.get_board()[1] < self.marbles_board.get_board()[0] and self.marbles_board.get_board()[0] != 0 and self.marbles_board.get_board()[1] != 0:
                self.marbles_board = self.marbles_board.switch()
                print str(self.marbles_board)
            else:
                self.marbles_board = self.marbles_board.rotate()
                print str(self.marbles_board)

        print "Total steps = %s" % steps
     
       
            
# main

my_board = MarblesBoard([1,3,0,2])
player = Solver(my_board)
player.solve()

#my_board = MarblesBoard([2, 10, 0, 9, 7, 11, 8, 12, 5, 4, 6, 14, 3, 1,13])
#player = Solver(my_board)
#player.solve()



