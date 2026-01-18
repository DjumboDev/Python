columns = 7
rows = 6
circle_empty_char = chr(0x25CB)
circle_full_char = chr(0x25CF)
grid = [[circle_empty_char for _ in range(columns)] for _ in range(rows)]

grid[0][1] = circle_full_char

def insert_token(token_x):
    token_y = 0
    for token_y in range(0, rows - 1):
        token_y_next = token_y + 1
        token_y_next_state = grid[token_x][token_y_next]
        if token_y_next_state == circle_full_char:
            break
    grid[token_x][token_y_next] = circle_full_char

def show_grid():
    for y in range(columns):
        for x in range(rows):
            print(grid[x][y], end="")
        print()

while True:
    token_x = None
    while token_x is None:
        try:
            token_x = int(input("Entrer une position pour insérer le jeton ? "))
            if token_x == "":
                token_x = None
        except ValueError:
            token_x = None

    insert_token(token_x)
    show_grid()

# 0
# 1
# 1 
# 1