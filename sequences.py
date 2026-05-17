#Comma code
def add_commas(lst):
    for idx in range(len(lst)):
        if (idx==len(lst)-1):
            lst[idx] = "and " + lst[idx]
        else:
            lst[idx] += ", "

    returned_str = ''
    for val in lst:
        returned_str += val
    return returned_str

#Character picture grid
def char_picture_grid():
    grid = [['.', '.', '.', '.', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['.', 'O', 'O', 'O', 'O', 'O'],
            ['O', 'O', 'O', 'O', 'O', '.'],
            ['O', 'O', 'O', 'O', '.', '.'],
            ['.', 'O', 'O', '.', '.', '.'],
            ['.', '.', '.', '.', '.', '.']]

    for y in range(len(grid[0])):
        for x in range(len(grid)):
            print(grid[x][y], end='')
        print()

fruits = ['apples', 'bananas', 'pears', 'kiwis']
print("Fruits: " +  add_commas(fruits))

print("Heart:")
char_picture_grid()
