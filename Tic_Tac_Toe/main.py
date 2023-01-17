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

n = 3
field = generate_field(n)
current_player = 'X'
step_player = []


while True:
    print('///'*10)
    print_field(field, n)
    step_player = get_player_step(current_player)
    y, x = step_player[0], step_player[1]
    if field[y][x] == ' ':
        field[y][x] = current_player
        current_player = update_player(current_player)
    else:
        print("Ячейка уже занята!")

    # filled_cells = 0
    # for line in field:
    #     for el in line:
    #         if el != ' ':
    #             filled_cells += 1

    if is_field_filled(field):
        print('Конец игры.')
        break

    print('///'*10)

print('///'*10)
print_field(field)