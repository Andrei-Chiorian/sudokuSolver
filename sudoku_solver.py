class Board:
    def __init__(self, board):
        """
        Constructor for the Board class. The parameter 'board' should be a 9x9
        2D list of integers, each representing a cell in a Sudoku puzzle.
        The cells should be values from 0 to 9, where 0 represents a blank cell.
        """
        self.board = board

    def __str__(self):
        """
        This method is used to create a string representation of the Sudoku
        board. The representation is a 9x9 2D list of strings, where each cell
        is represented by a string. If a cell is blank (i.e. it's value is 0)
        then the string is '*', otherwise it's the string representation of the
        cell's value.
        """
        # Iterate over each row in the board
        board_str = ''
        for row in self.board:
            # Create a string of the row's elements
            # If the element is 0, the string is '*', otherwise it's the string
            # representation of the element
            row_str = [str(i) if i else '*' for i in row]
            # Join the strings for each row into a single string with ' ' as the
            # separator
            board_str += ' '.join(row_str)
            # Add a newline character at the end of each row
            board_str += '\n'
        # Return the string representation of the entire board
        return board_str

    def find_empty_cell(self):
        """
        This method iterates over each row in the Sudoku board. If a cell in the
        row is empty (i.e. its value is 0) then the method returns the position of
        that cell as a tuple of two integers. The first integer represents the row
        and the second integer represents the column. If no empty cells are found
        then the method returns None.
        """
        # Iterate over each row in the board
        for row, contents in enumerate(self.board):
            # Attempt to find the index of the first occurrence of 0 in the row
            # The index of the first occurrence of 0 is the column of the empty
            # cell
            try:
                # Find the index of the first occurrence of 0 in the row
                col = contents.index(0)
                # Return the position of the empty cell as a tuple of two
                # integers
                return row, col
            # If no empty cells are found in the row, then a ValueError is raised
            # by the index() method. This exception is caught and ignored.
            except ValueError:
                pass
        # If no empty cells are found in the entire board, then return None
        return None

    def valid_in_row(self, row, num):
        """
        This method takes a row number and a number as parameters and returns a
        boolean indicating whether the number is valid in the given row.

        The method iterates over each number in the row in the Sudoku board. If
        the given number is found in the row, then the method immediately returns
        False, indicating that the number is not valid in the given row. If the
        given number is not found in the row after iterating over all numbers in
        the row, then the method returns True, indicating that the number is valid
        in the given row.
        """
        # Iterate over each number in the given row
        for col in self.board[row]:
            # If the given number is found in the row, then immediately return
            # False
            if col == num:
                return False
        # If the given number is not found in the row, then return True
        return True

    def valid_in_col(self, col, num):
        """
        This method takes a column number and a number as parameters and returns
        a boolean indicating whether the number is valid in the given column.

        The method iterates over each row in the Sudoku board and checks the
        number in the given column of the row. If the given number is found in
        the given column, then the method immediately returns False,
        indicating that the number is not valid in the given column. If the given
        number is not found in the given column after iterating over all rows,
        then the method returns True, indicating that the number is valid in the
        given column.
        """
        # Iterate over each row in the board
        for row in range(9):
            # Check if the given number is found in the column of the row
            if self.board[row][col] == num:
                # If the given number is found in the column, then immediately
                # return False
                return False
        # If the given number is not found in the column, then return True
        return True

    def valid_in_square(self, row, col, num):
        """
        This method takes the position of a cell in the Sudoku board and a number
        as parameters and returns a boolean indicating whether the given number is
        valid in the 3x3 square that the given cell is in.

        The method calculates the starting row and column of the 3x3 square by
        dividing the given row and column by 3 and then multiplying by 3. This
        gives the top left corner of the 3x3 square.

        The method then iterates over each cell in the 3x3 square and checks if
        the given number is in the square. If the given number is found in the
        square, then the method immediately returns False, indicating that the
        number is not valid in the given square. If the given number is not found
        in the given square after iterating over all cells in the square, then
        the method returns True, indicating that the number is valid in the given
        square.
        """
        # Calculate the starting row of the 3x3 square
        row_start = (row // 3) * 3
        # Calculate the starting column of the 3x3 square
        col_start = (col // 3) * 3
        # Iterate over each cell in the 3x3 square
        for row_no in range(row_start, row_start + 3):
            for col_no in range(col_start, col_start + 3):
                # Check if the given number is found in the square
                if self.board[row_no][col_no] == num:
                    # If the given number is found in the square, then immediately
                    # return False
                    return False
        # If the given number is not found in the square, then return True
        return True

    def is_valid(self, empty, num):
        """
        This method takes a tuple representing the position of an empty cell in
        the Sudoku board and a number as parameters and returns a boolean
        indicating whether the number is valid in the given cell.

        The method uses the valid_in_row, valid_in_col, and valid_in_square
        methods to check if the given number is valid in the given cell. If the
        number is valid in the given cell, then the method returns True, otherwise
        it returns False.
        """
        row, col = empty
        # Check if the given number is valid in the row
        valid_in_row = self.valid_in_row(row, num)
        # Check if the given number is valid in the column
        valid_in_col = self.valid_in_col(col, num)
        # Check if the given number is valid in the 3x3 square
        valid_in_square = self.valid_in_square(row, col, num)
        # If the given number is valid in the row, column, and square, then
        # return True
        return all([valid_in_row, valid_in_col, valid_in_square])

    def solver(self):
        """
        This method uses a recursive backtracking algorithm to solve the Sudoku
        puzzle.

        The method starts by finding the next empty cell in the Sudoku board.
        If no empty cells are found, then the method returns True, indicating
        that the puzzle is solved.

        The method then iterates over each number from 1 to 9. For each number,
        it checks if the number is valid in the given cell by calling the
        is_valid method. If the number is valid in the given cell, then the
        method places the number in the given cell and recursively calls itself
        to continue solving the puzzle.

        If the recursive call returns True, then the method returns True.
        Otherwise, the method resets the cell to 0 and continues to the next
        number.

        If the method has tried all numbers and none of them are valid in the
        given cell, then the method returns False, indicating that the puzzle
        is unsolvable.

        :return: a boolean indicating whether the puzzle is solvable
        """
        # Find the next empty cell in the Sudoku board
        if (next_empty := self.find_empty_cell()) is None:
            # If no empty cells are found, then the puzzle is solved, so return
            # True
            return True
        # Iterate over each number from 1 to 9
        for guess in range(1, 10):
            # Check if the number is valid in the given cell
            if self.is_valid(next_empty, guess):
                # Place the number in the given cell
                row, col = next_empty
                self.board[row][col] = guess
                # Recursively call the solver method to continue solving the
                # puzzle
                if self.solver():
                    # If the recursive call returns True, then return True
                    return True
                # Reset the cell to 0
                self.board[row][col] = 0
        # If the method has tried all numbers and none of them are valid in the
        # given cell, then return False
        return False


def solve_sudoku(board):
    """
    This function takes a 2D list of integers as a parameter and attempts to
    solve the Sudoku puzzle represented by the list. The function creates an
    instance of the Board class and calls its solver method to solve the puzzle.
    If the puzzle is solvable, then the solved puzzle is printed to the console.
    If the puzzle is unsolvable, then a message is printed to the console
    indicating that the puzzle is unsolvable. The solved puzzle is returned as
    an instance of the Board class.
    """
    # Create an instance of the Board class with the given puzzle
    gameboard = Board(board)
    # Print the puzzle to be solved
    print(f'Puzzle to solve:\n{gameboard}')
    # Call the solver method on the Board instance to solve the puzzle
    if gameboard.solver():
        # If the puzzle is solvable, then print the solved puzzle
        print(f'Solved puzzle:\n{gameboard}')
    else:
        # If the puzzle is unsolvable, then print a message to the console
        print('The provided puzzle is unsolvable.')
    # Return the solved puzzle as an instance of the Board class
    return gameboard

