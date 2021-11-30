import sys

file_circle = sys.argv[1]
file_point = sys.argv[2]

with open(file_circle, 'r') as file_c:
    data_circle = [line for line in file_c]

with open(file_point, 'r') as file_p:
    data_point = [line for line in file_p]

try:
    center_x, center_y = data_circle[0].split(sep = ' ')
    center_x = float(center_x)
    center_y = float(center_y)
    radius = float(data_circle[1])
except IndexError:
    print('Нет координат центра окружности')

for i in range(0, len(data_point)):
    x, y = data_point[i].split(sep = ' ')
    x = float(x)
    y = float(y)
    position = (x - center_x) ** 2 + (y - center_y) ** 2
    if position < radius ** 2:
        print(1)
    elif position == radius ** 2:
        print(0)
    else:   
        print(2)
    



