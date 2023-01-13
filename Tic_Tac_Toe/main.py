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
n = 3
field = generate_field(n)
current_player = 'X'
step_player = []
while True:
    print('///'*10)
    print_field(field, n)
    step_player = get_player_step(current_player)
    field[step_player[0]][step_player[1]] = current_player
    current_player = update_player(current_player)
    print('///'*10)
    