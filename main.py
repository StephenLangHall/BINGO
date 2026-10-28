import random
from colorama import Fore, Style, ansi


INVERT=Fore.GREEN
RESET=Style.RESET_ALL
CLEAR=ansi.clear_screen() + ansi.Cursor.POS(1, 1)

g=[[0 for _ in range(5)] for _ in range(5)]


# Fill in the board
used=[]

for y in range(0,5):
    for x in range(0,5):
        offset=x*15
        while (r:=random.randint(1+offset,15+offset)) in used:
            continue
        g[y][x]=r
        used.append(r)
g[2][2]-=1000

BINGO=[]

print(CLEAR)
while (wincondition:=input("Which win condition? (any/horiz/vert/angle)  ").lower()) \
        not in ["any","horiz","vert","angle"]:
            continue

while len(BINGO)==0:
    # Clear screen
    print(CLEAR)

    # Draw board
    for row in g:
        print(*[" .." if n<0 else f"{n:>3}" for n in row],sep='')
    print()

    # Get user input
    number=int(input("(Only input the number, not the letter!)\nEx. input '21' not 'B-21'.\nWhat number was called?  "))

    # Set cell called by user
    for y in range(0,5):
        for x in range(0,5):
            if g[y][x]==number:
                g[y][x]-=1000
    #g=[[cell-1000 if cell==number else cell for cell in row] for row in g]

    # Check for BINGO
    wins = []
    if wincondition=="any" or wincondition=="angle":
        wins += [[[0,0],[1,1],[2,2],[3,3],[4,4]],
                 [[0,4],[1,3],[2,2],[3,1],[4,0]]]
    if wincondition=="any" or wincondition=="horiz":
        wins += [[[0,0],[0,1],[0,2],[0,3],[0,4]],
                 [[1,0],[1,1],[1,2],[1,3],[1,4]],
                 [[2,0],[2,1],[2,2],[2,3],[2,4]],
                 [[3,0],[3,1],[3,2],[3,3],[3,4]],
                 [[4,0],[4,1],[4,2],[4,3],[4,4]]]
    if wincondition=="any" or wincondition=="vert":
        wins += [[[0,0],[1,0],[2,0],[3,0],[4,0]],
                 [[0,1],[1,1],[2,1],[3,1],[4,1]],
                 [[0,2],[1,2],[2,2],[3,2],[4,2]],
                 [[0,3],[1,3],[2,3],[3,3],[4,3]],
                 [[0,4],[1,4],[2,4],[3,4],[4,4]]]

    # Append wins to BINGO
    for win in wins:
        if all(g[a][b]<0 for [a,b] in win):
            BINGO.append(win)


else:
    # Clear screen
    print(CLEAR)

    # Draw board
    for y,row in enumerate(g):
        for x,cell in enumerate(row):
            if cell<0:
                coord=[y,x]
                ch=" **"
                for win in BINGO:
                    if coord in win:
                        ch=f" {INVERT}{cell+1000:>2}{RESET}"
                print(ch,end='')
            else:
                print(f"{cell:>3}",end='')
        print()

    print()
    for win in BINGO:
        print(win)
    print("BINGOOOOO!!!!")
