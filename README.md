# Sudoku
The sudoku game
## Right now only the generator is uploaded. SudokuGenerator.py generates random Sudoku

## SudokuGenerator.py

![](sudokugrid.png)

The Sudoku grid consists of 9 outer boxes and each outer box consists of 9 inner boxes. Sudoku contains 81 inner boxes in total, and can be filled with numbers from 1 to 9 such that, no number gets repeated inside an outer box, in the row and in the column. So, to generate a random sudoku everytime, I considered the above arrangement. __The red rectangle__ is the row0 of the three outer rows and __the green vertical rectangle__ is the col0 of the three outer columns. __The small red rectangle__ is the row0 of the three inner rows and __the green square__ is the col0 if the inner columns. So every element in the sudoku can be represented of the form **sudoku\[ROW][COL]\[row][col]**  This is a 3x3x3x3 matrix.

## Initialization, Randomization, Reshaping, Rotation and Arrangement

### Initialization

A 3x3x3x3 matrix is initialized with all elements as 'None' by the command [\[\[\[None for _ in range(3)] for _ in range(3)]
                                                                            for _ in range(3)] for _ in range(3)]
                                                                          
Now we can access and assign value of each index.

### Randomization

The possible numbers are from 1 to 9.
So, we use random.shuffle(numbers) to shuffle the numbers

### Reshaping

I reshaped this 1x9 list to a 3x3 list for making arrangement easier

### Rotation

Now we have a 3x3 matrix. I defined two functions - **Inner Rotate** and **Outer Rotate** to rotate the elements in the list.

For example:
If the list is **\[\[5,6,4],\[8,9,7],\[2,3,1]]**
**after inner rotation** the list becomes : 
**\[\[4,5,6],\[7,8,9],\[1,2,3]]**
**after outer rotation** the list becomes : 
**\[\[1,2,3],\[4,5,6],\[7,8,9]]**. The last element becomes the first element by rotating.

### Arrangement
We fill the elements horizontally, i.e, first ROW0,COL0,row0,col0 gets filled and so on till col2 in first iteration, then the second outer column, i.e, COL1 is filled and so on till COL2,row0,col2 is filled. Now comes the second row, i.e, row2. In  this way all the 81 elements will arranged horizontally.

But during assignment, whenever there is a change in the outer row, the numbers list is **InnerRotated** once and whenver there is change in inner row, the numbers list is **OuterRotated** once. In this way, no element will get repeated both inside the box and also in the row or column.

By this method, the numbers list that we created in the first step alone needs to be shuffled, and then the same is reshaped, rotated and arranged horizontally.

### Function return
This package returns a 9x9 matrix from 3x3x3x3 matricx after reshaping for us to easily access it using \[m]\[n] indexing.

# Thank You
