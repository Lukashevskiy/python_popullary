def generate_field(n):
    field = list()
    for i in range(n):
        line = list()
        for j in range(n):
            line.append(' ')
        field.append(line)
    return field

def print_field(field, n):
    for i, line in enumerate(field):
        print(*line,sep='|')
        if i < n - 1:
            print('-' * (n * 2 -1))
    
def get_player_step(current_player):
    print("Сейчас ходит - ", current_player)
    x, y = map(int,input('Введите координаты: ').split())
    return x, y

def update_player(current_player):
    if current_player == 'X':
        return '0'
    else:
        return 'X'

def is_field_filled(field):
    for line in field:
        for el in line:
            if el == " ":
                return False
    return True

def is_cell_valid(field, n, x, y):
    if 0 > x or x >= n:
        return False

    if 0 > y or y >= n:
        return False
        
    if field[y][x] != ' ':
        return False

    return True    

def check_row(field, n, y, current_player):
    for x in range(0, n):
        if field[y][x] != current_player:
            return False

    return True    

def check_column(field, n, x, current_player):
    return True

def check_diag(field, n, diag_i, current_player):
    return True

def is_win(field, n, current_player):
    for y in range(0, n):
        if check_row(field, n, y, current_player):
            return True

    return False

n = 3
field = generate_field(n)
current_player = 'X'
step_player = []



while True:
    print('///'*10)
    print_field(field, n)
    step_player = get_player_step(current_player)
    y, x = step_player[0], step_player[1]

    if is_cell_valid(field, n, y, x):
        field[y][x] = current_player
    else:
        print("Invalid cell")
        continue
   
    if is_win(field, n, current_player):
        print("Win -", current_player)
        break 

    if is_field_filled(field):
        print('Конец игры.')
        break

    current_player = update_player(current_player)

    print('///'*10)

print('///'*10)
print_field(field, n)
