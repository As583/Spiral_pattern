import turtle
import Calculate as triangle_solve
import Save_file

# TODO: Ограничение количество строк
# TODO: Сделать ручной ввод, возможно бегунками

type, n, ro, teta, b_side = 'whirpool', 5, 20.0, 40.0, 150.0

beta_ = 360/n
alpha_ = (180-beta_)/2

# проверка входных параметров
if ro < 0 or ro > beta_/2:
    print('ro must be in range between 0 and', beta_/2)
if teta <= 0 or ro > alpha_:
    print('teta must be in range between 0 and', alpha_)

# Выставление указателя на край экрана
screen = turtle.Screen()

turtle.penup()
turtle.goto(10 - screen.window_width() / 2, 10 - screen.window_height() / 2)
turtle.pendown()

turtle.hideturtle()
turtle.speed(0)


# Расчет углов
alpha = teta
epsilon = ro / 2
beta = epsilon + 180 / n
gamma = 180 - (alpha + beta)

count = 1
row = []

for i in range(n):  # Добавить 1, если делаем lampshade
    # row.append(turtle.clone())
    turtle.forward(b_side)
    row.append(turtle.clone())
    turtle.left(ro)

# Создать копию массива row, чтобы отрисовать нижние треугольники, если делаем lampshade

while count < 10:
    # Посчитали треугольник
    if ro != 0 or count == 1:
        a_side, c_side = triangle_solve.solve_triangle(alpha, beta, gamma, b_side)

        print('Треугольник', count, [alpha, beta, gamma, a_side, b_side, c_side])

        # считаем угол противоположного треугольника
        # TODO: считать угол один раз и вообще сделать отдельный класс Triangle
        angle = triangle_solve.get_angle(a_side, c_side, 180 - gamma - alpha - ro)
        # print(angle)

    for dot in row:
        # чертим треугольник
        # dot.forward(b_side)

        dot.left(180 - gamma)
        dot.forward(a_side)

        pos_b = dot.position()  # точка B

        dot.color('red')
        dot.left(180 - beta)
        dot.forward(c_side)
        dot.color('black')
        dot.right(gamma + alpha + ro)
        dot.forward(a_side)

        pos_a = dot.position()  # точка A

        dot.right(180 - angle)

    # посчитали базу второго треугольника
    b_side = triangle_solve.get_side(pos_a, pos_b)
    # print (b_side)

    for dot in row:
        dot.forward(b_side)
    count += 1

# Чертим пику, понадобится для типа lampshade
'''
if ro > 0:
    fin_angle = (180 - ro) / 2
    a_side, c_side = triangle_solve.solve_triangle(fin_angle, ro, fin_angle, b_side)
    print('Треугольник 0', [alpha, beta, gamma, a_side, b_side, c_side])
    for dot in row:
        dot.left(180 - fin_angle)
        dot.forward(a_side)
        dot.left(180 - ro)
        dot.forward(c_side)
'''

Save_file.SaveEps()

print('Fin!')

turtle.done()
