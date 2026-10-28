import random

g=[
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
    [0,0,0,0,0],
]

used=[]

# Fill in the board
for y in range(0,5):
    for x in range(0,5):
        offset=x*15
        while (r:=random.randint(1+offset,15+offset)) in used:
            continue
        g[y][x]=r
        used.append(r)
g[2][2]-=1000

BINGO=[]

print("\033[2J\033[H")
while (wincondition:=input("Which win condition? (all/horiz/vert/angle)  ")) \
        not in ["all","horiz","vert","angle"]:
            continue

while len(BINGO)==0:
    # Clear screen
    print("\033[2J\033[H")

    # Draw board
    for row in g:
        print(*[" .." if n<0 else f"{n:>3}" for n in row],sep='')
    print()

    # Get user input
    number=int(input("What number was called?  "))

    # Set cell called by user
    for y in range(0,5):
        for x in range(0,5):
            if g[y][x]==number:
                g[y][x]-=1000

    # Check for BINGO
    wins = []
    if wincondition=="all" or wincondition=="angle":
        wins.append([[0,0],[1,1],[2,2],[3,3],[4,4]])
        wins.append([[0,4],[1,3],[2,2],[3,1],[4,0]])
    if wincondition=="all" or wincondition=="horiz":
        wins.append([[0,0],[0,1],[0,2],[0,3],[0,4]])
        wins.append([[1,0],[1,1],[1,2],[1,3],[1,4]])
        wins.append([[2,0],[2,1],[2,2],[2,3],[2,4]])
        wins.append([[3,0],[3,1],[3,2],[3,3],[3,4]])
        wins.append([[4,0],[4,1],[4,2],[4,3],[4,4]])
    if wincondition=="all" or wincondition=="vert":
        wins.append([[0,0],[1,0],[2,0],[3,0],[4,0]])
        wins.append([[0,1],[1,1],[2,1],[3,1],[4,1]])
        wins.append([[0,2],[1,2],[2,2],[3,2],[4,2]])
        wins.append([[0,3],[1,3],[2,3],[3,3],[4,3]])
        wins.append([[0,4],[1,4],[2,4],[3,4],[4,4]])

    # Append wins to BINGO
    for win in wins:
        if all(g[a][b]<0 for [a,b] in win):
            BINGO.append(win)


else:
    # Clear screen
    print("\033[2J\033[H")

    # Draw board
    for y,row in enumerate(g):
        for x,cell in enumerate(row):
            if cell<0:
                coord=[y,x]
                ch=" **"
                for win in BINGO:
                    if coord in win:
                        ch=f" \033[7m{cell+1000:>2}\033[0m"
                print(ch,end='')
            else:
                print(f"{cell:>3}",end='')
        print()

    print()
    print(BINGO)
    print("BINGOOOOO!!!!")
