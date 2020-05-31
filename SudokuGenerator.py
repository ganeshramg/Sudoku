#We import shuffle to generate new Sudoku puzzle everytime
from random import shuffle

def generate():

    numbers = [9,7,8,3,1,2,6,4,5]

    shuffle(numbers) #This shuffles the numbers list



    #This returns a 3*3 List
    def reshapeNumbers(numbers):
        reshaped = [[None for _ in range(3)]for _ in range(3)]

        for i in range(3):
            for j in range(3):
                numbersIndex = (3*i) + j
                reshaped[i][j] = numbers[numbersIndex]

        return reshaped

    numbers = reshapeNumbers(numbers)



    #This rotates the first dimension of the numbers
    def rotateOuter(numbers):
        numbers.append(numbers[0])
        numbers.pop(0)
        return numbers

    #This rotates the second dimension of the numbers
    def rotateInner(numbers):
        new = []
        for number in numbers:
            new.append(rotateOuter(number))
        return new


    #Initialization of a Sudoku with 81 elements in total of the for (3x3)^2
    #So each element can be represented of the form [ROW][COL][row][col]
    RandomSudoku = [[[[None for _ in range(3)]for _ in range(3)]
                            for _ in range(3)]for _ in range(3)]

    #RandomSudoku Definition Algorithm
    for ROW in range(3):
        numbers = rotateInner(numbers) #For a change in outer row rotate inner elements once
        for row in range(3):
            numbers = rotateOuter(numbers) #For a change in inner row rotate outer elements once
            for COL in range(3):
                for col in range(3):
                    RandomSudoku[ROW][row][COL][col] = numbers[COL][col]


    #This function return a 9x9 Sudoku from 3x3x3x3 Sudoku(otherwise known as reshaping)
    def reshapeSudoku(sudoku):

        reshapedSudoku = [[None for _ in range(9)]for _ in range(9)]
        for ROW in range(3):
            for COL in range(3):
                for row in range(3):
                    for col in range(3):
                        i = ((3*ROW) + row)
                        j = ((3*COL) + col)
                        reshapedSudoku[i][j] = sudoku[ROW][COL][row][col]

        return reshapedSudoku

    # print(RandomSudoku)
    return reshapeSudoku(RandomSudoku)
