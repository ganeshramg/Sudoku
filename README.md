# Sudoku
The sudoku game
## Right now only the generator is uploaded. SudokuGenerator.py generates random Sudoku

## SudokuGenerator.py

The Sudoku grid consists of 9 boxes and each box consists of 9 boxes. Sudoku contains 81 small boxes in total, and can be filled with numbers from 1 to 9 such that, no number gets repeated inside a box, in the row and in the column. So, to generate a random sudoku everytime, I considered the below arrangement. __The red rectangle__ is the row0 of the three outer rows and __the green vertical rectangle__ is the col0 of the three outer columns. __The small red rectangle__ is the row0 of the three inner rows and __the green square__ is the col0 if the inner columns. So every element in the sudoku can be represented of the form **sudoku\[ROW][COL]\[row][col]**  

![](sudokugrid.png)
