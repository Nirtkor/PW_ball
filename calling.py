from main import Ball

condition = 1
while condition != 'q':
    try:
        radius = float(input('\nДобро пожаловать в программу, которая позволит Вам узнать, \
                            \nна какой угол сместилась точка, на которой стоял мяч  за время качения t\
                            \nВведите Радиус мяча: '))
        if radius < 0:
            print('Радиус не может быть отрицательным')
            break

        time = float(input('\nВведите время, которое мяч будет находится в движении: '))
        if time < 0:
            print('Нео, время не может идти в обратную сторону')
            break
        
        choose = float(input('\nЕсли мяч движется равномерно, введите 0. \
                        \nЕсли мяч движется равноускоренно, введите 1. \
                        \n'))
        if choose == 0:
            speed = float(input('\nВведите скорость мяча, если движение равномерное:'))
            ex_1 = Ball(radius)
            print('Точка сместилась на угол равный:', ex_1.uniform_motion(speed, time), '°')
        elif choose == 1:
            acceleration = float(input('\nВведите ускорение мяча: '))
            ex_2 = Ball(radius)
            print('Точка сместилась на угол равный:', ex_2.uniformly_accelerated_motion(acceleration, time), '°')
        else:
            print('У вас был выбор, но вы не последовали правилам...')
        break
    except:
        condition = input('\nДанные должны иметь числовой вид записи, попробуйте снова.\
                   \nЧтобы выйти, введите q. Если желаете продолжить, введите любой символ.')
