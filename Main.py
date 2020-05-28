import turtle
import Calculate
import Save_file

n = int(input("Enter the number of corners: ") or 4)

beta_ = 360/n
alpha_ = (180-beta_)/2

ro, sigma = -1, -1

while ro < 0 or ro > beta_/2:
    ro = float(input("Enter the angle of rotation (0 =< ro <= " +
                 str(beta_/2) + "): ") or 10)
while sigma < 0 or sigma > alpha_:
    sigma = float(input("Enter the angle of spirality (0 < sigma <= " +
                   str(alpha_) + "): ") or 10)

type, b_side = 'whirpool', 100

# Выставление указателя на край экрана
screen = turtle.Screen()

turtle.penup()
turtle.goto(100 - screen.window_width() / 2,
            10 - screen.window_height() / 2)
turtle.pendown()

turtle.hideturtle()
turtle.speed(0)


# Расчет углов
alpha = sigma
epsilon = ro / 2
beta = epsilon + 180 / n
gamma = 180 - (alpha + beta)

count = 1
row = []

a_side, c_side = Calculate.solve_triangle(alpha, beta, gamma, b_side)

print('Треугольник', count,
      [alpha, beta, gamma, a_side, b_side, c_side])

# считаем угол противоположного треугольника

angle = Calculate.get_angle(a_side, c_side, 180 - gamma - alpha - ro)

for i in range(n):  # Добавить 1, если делаем lampshade
    # row.append(turtle.clone())
    turtle.forward(b_side)
    row.append(turtle.clone())
    turtle.left(ro)

# Создать копию массива row,
# чтобы отрисовать нижние треугольники, если делаем lampshade

while count <= 15:
    # Посчитали треугольник
    if ro != 0 and count > 1:
        a_side, c_side = Calculate.solve_triangle(
            alpha, beta,
            gamma, b_side)

        print('Треугольник', count,
              [alpha, beta, gamma, a_side, b_side, c_side])

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
    b_side = Calculate.get_side(pos_a, pos_b)
    # print (b_side)

    for dot in row:
        dot.forward(b_side)
    count += 1

# Чертим пику, понадобится для типа lampshade
'''
if ro > 0:
    fin_angle = (180 - ro) / 2
    a_side, c_side = Calculate.solve_triangle(
        fin_angle, ro, 
        fin_angle, b_side)
    print('Треугольник 0', 
         [alpha, beta, gamma, a_side, b_side, c_side])
    for dot in row:
        dot.left(180 - fin_angle)
        dot.forward(a_side)
        dot.left(180 - ro)
        dot.forward(c_side)
'''

Save_file.SaveEps('Pattern')


print('Fin!')

turtle.done()
