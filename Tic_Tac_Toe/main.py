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
field = list()
for i in range(n):
    line = list()
    for j in range(n):
        line.append(' ')
    field.append(line)
current_player = 'X'
step_player = []


while True:
    print('///'*10)
    
    for i, line in enumerate(field):
        print(*line,sep='|')
        if i < n - 1:
            print('-' * (n * 2 -1))
    print("Сейчас ходит - ", current_player)
    y, x = map(int,input('Введите координаты: ').split())
    if 0 <= x < n and 0 <= y < n:
        if field[y][x] == ' ':
            field[y][x] = current_player
            if current_player == 'X':
                current_player = '0'
            else:
                current_player = 'X'
        else:
            print("Ячейка уже занята!")
    else:
        print("Не корректный ввод")
    filled_cells = 0
    for line in field:
        for el in line:
            if el != ' ':
                filled_cells += 1
    if filled_cells == n*n:
        print('Конец игры.')
        break
    print('///'*10)

print('///'*10)
# print_field(field)