
def read_word(file_name):
    myFile = open(file_name, 'r')
    words = []
    for word in myFile:
        words.append(word.strip().lower())
    myFile.close()
    return words

def read_grid(grid_file):
    myFile = open(grid_file, 'r')
    grid = []
    for line in myFile:
        grid.append(line.split())
    return grid

def search_horizontal(word_list, grid):
    found_words = []
    for row in grid:
        for i in range(len(row)):

            for index in range(3, len(row) - i + 1):
                pattern = row[i:i + index]
                if ''.join(pattern).lower() in word_list:
                    found_words.append(''.join(pattern))

    for row in grid:
        reverse = row[::-1]
        for i in range(len(reverse)):
            for index in range(3, len(reverse) - i + 1):
                pattern = reverse[i:i + index]
                if ''.join(pattern).lower() in word_list:
                    found_words.append(''.join(pattern))

    return found_words

def search_vertical(word_list, grid):
    found = []

    for col in range(len(grid)):
        for i in range(len(grid[col][0])):
            column = [row[col] for row in grid]
            for i in range(len(column)):
                for length in range(3, len(column) - i + 1):
                    pattern = column[i:i + length]
                    if ''.join(pattern).lower() in word_list: 
                        found.append(''.join(pattern))

    for col in range(len(grid)):
        for i in range(len(grid[col][0])):
            reverse = [row[col] for row in grid][::-1]
            for i in range(len(reverse)):
                for length in range(3, len(reverse) - i + 1):
                    pattern = reverse[i:i + length]
                    if ''.join(pattern).lower() in word_list:
                        found.append(''.join(pattern))

    return found

def search_diagonal(word_list, grid):
    found_words = []

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for length in range(3, min(len(grid) - i, len(grid[0]) - j) + 1):
                pattern = [grid[i + z][j + z] for z in range(length)]
                if ''.join(pattern).lower() in word_list:
                    found_words.append(''.join(pattern))

    return found_words

def print_words(words):
    for w in words:
        print(w)

def main():

    words_file = input().strip()
    grid_file = input().strip()
    
    word_list = read_word(words_file)
    grid = read_grid(grid_file)
    words_combine = []

    horizontal = search_horizontal(word_list, grid)
    vertical = search_vertical(word_list, grid)
    diagonal = search_diagonal(word_list, grid)

    words_combine.extend(horizontal)
    words_combine.extend(vertical)
    words_combine.extend(diagonal)

    words_combine.sort()
    print_words(words_combine)

main()