""" Recursion and backtracking problem
The main difference between recusion and backtracking is that
the backtracking need to handle the memorized steps and ealy stop generally.
"""


def placable(grid, word, m, n,  ver=True):
    """ check wether a work can be placed in the crossword given a work.
        we suppose the grid is square of size 10.
        Args:
            grid: the gridworld that contain the chars.
            word: the string that we need to fill in.
            m: start line.
            n: start column.
            ver: verticle feed or not.
    """
    for i, c in enumerate(word):
        x, y = (m+i, n) if ver else (m, n+i)
        if x >= 10 or y >= 10:
            return False
        if grid[x][y] != '-' and grid[x][y] != c:
            return False
    return True


def place_word(grid, word, m, n, ver=True):
    """ place the word in the grid and return orign value for backtrack"""
    origin = []
    for i, v in enumerate(word):
        x, y = (m + i, n) if ver else (m, n + i)
        origin.append(grid[x][y])
        grid[x][y] = v
    return origin


def convert_word(grid, origin, m, n, ver=True):
    """ convert the grid value back with origin value"""
    for i, v in enumerate(origin):
        x, y  = (m + i, n) if ver else (m, n + i)
        grid[x][y] = v


def crosswordPuzzle(crossword, words):
    """ crossword list of 10 of string size 10,
        words is a list of string that we need to fill
        in the crossword.    
    """
    words = words.split(";")
    n_word = len(words)
    n_grid = len(crossword)
    grid = [list(s) for s in crossword]

    def dfs(grid, index):
        """ backtracking function"""
        if index == n_word:
            return True
        word = words[index]
        for m in range(n_grid):
            for n in range(n_grid):
                for ver in [True, False]:
                    if placable(grid, word, m, n,  ver):
                        origin = place_word(grid, word, m, n, ver)
                        if dfs(grid, index + 1):
                            return True
                        convert_word(grid, origin, m, n, ver)
        return False

    dfs(grid, 0)
    crossword = ["".join(l) for l in grid]
    return crossword


if __name__ =="__main__":
    crossword = [
        "+-++++++++",
        "+-++++++++",
        "+-++++++++",
        "+-----++++",
        "+-+++-++++",
        "+-+++-++++",
        "+++++-++++",
        "++------++",
        "+++++-++++",
        "+++++-++++"
    ]
    words = "LONDON;DELHI;ICELAND;ANKARA"
    # m = 0
    # n = 1
    # print(placable(crossword, word, m, n,  ver=False))
    r = crosswordPuzzle(crossword, words)
    for i in r:
        print(i)
