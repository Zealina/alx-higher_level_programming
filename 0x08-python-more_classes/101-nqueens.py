#!/usr/bin/python3
'''this module contains algorithm for backtracking n-queens'''

import sys

if len(sys.argv) != 2:
    print('Usage: nqueens N')
    sys.exit(1)
try:
    size = int(sys.argv[1])
except ValueError:
    print('N must be a number')
    sys.exit(1)

if size < 4:
    print('N must be at least 4')
    sys.exit(1)

class Solution:
    '''
    Example on the left: [1, 3, 0, 2]
    example on the right: [2, 0, 3, 1]
    '''
    def solveNQueens(self, n):
        '''
        The Entry Point, takes the number of queen, calls the search function
        and return the result

        Args:
            n (int): The number of queens
        Return:
            All solutions to the N-queen problem
        '''
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_valid_state(self, state, n):
        '''
        Check if a state has the right number of queens

        Args:
            n (int): number of queens
            state: state to check if valid
        Return:
            Return true if valid and false otherwise
        '''
        return len(state) == n

    def get_candidates(self, state, n):
        if not state:
            return range(n)
        position = len(state)
        candidates = set(range(n))
        for row, col in enumerate(state):
            candidates.discard(col)
            dist = position - row
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_valid_state(state, n):
            state_string = self.state_to_string(state, n)
            solutions.append(state_string)
            return
        for candidate in self.get_candidates(state, n):
            # recurse
            state.append(candidate)
            self.search(state, solutions, n)
            state.pop()

    def state_to_string(self, state, n):
        ret = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - i - 1)
            ret.append(string)
        return ret

sol = Solution()
solutions = sol.solveNQueens(size)
print(solutions)
