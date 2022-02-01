import random

steps = []


class Field:
    """
    Содержит игровое поле
    """
    matrix = ['\n']
    for i in range(3):
        for j in range(3):
            matrix.append(i * 3 + (j + 1))
        matrix.append('\n')


class GameLogic:
    """
    Содержит всю смысловую нагрузку игры
    """

    def check(self):
        """
        Функция проверяет выиграл человек или проиграл
        :return: если исход положительный, завершает игру, иначе продолжает
        """
        while True:
            if Field.matrix[1] == self and Field.matrix[2] == self and Field.matrix[3] == self \
                    or Field.matrix[5] == self and Field.matrix[6] == self and Field.matrix[7] == self \
                    or Field.matrix[9] == self and Field.matrix[10] == self and Field.matrix[11] == self \
                    or Field.matrix[1] == self and Field.matrix[6] == self and Field.matrix[11] == self \
                    or Field.matrix[1] == self and Field.matrix[5] == self and Field.matrix[9] == self \
                    or Field.matrix[2] == self and Field.matrix[6] == self and Field.matrix[10] == self \
                    or Field.matrix[3] == self and Field.matrix[7] == self and Field.matrix[11] == self \
                    or Field.matrix[3] == self and Field.matrix[6] == self and Field.matrix[9] == self:
                print(*Field.matrix)
                print(self, 'выиграли!')
                return exit(0)
            elif len(steps) == 9:
                print(*Field.matrix)
                print('Ничья')
                return exit(0)
            else:
                return

    def motion(self):
        """
        Функция осуществляет ход человека, в том случае если он верный то
        :return: если исход положительный, продолжает игру, иначе просит ввести другое число
        """
        while True:
            print(*Field.matrix)
            try:
                b = int(input(f'Введите число от 1 до 9, куда хотите поставить {self} '))
                if b <= 0 or b > 9:
                    print('\nНеверное значение, попробуйте еще раз!')
                    continue
                if b > 0 and b < 4:
                    b = b
                elif b > 3 and b < 7:
                    b += 1
                elif b > 6 and b < 10:
                    b += 2
                if b not in steps:
                    Field.matrix[b] = f'{self}'
                    break
                print('\nНеверное значение, попробуйте еще раз!')
            except:
                print('\nНеверное значение, попробуйте еще раз!')
        return steps.append(b)

    def computer_motion(self):
        """
        Ход компьютера осуществляется рандомно
        :return: возвращает игровое поле
        """
        while True:
            a = random.randrange(0, 12)
            if a == 0 or a == 4 or a == 8:
                continue
            if a not in steps:
                Field.matrix[a] = '0'
                return steps.append(a)


choise = input(
    """Ты хочешь сыграть с другом или с компьютером?

Если с другом, нажми '1' 
Если с компьютером, нажми '2' """
)
if choise == '1':
    while len(steps) < 9:
        GameLogic.motion('X')
        GameLogic.check('X')
        GameLogic.motion('0')
        GameLogic.check('0')
    exit(0)
elif choise == '2':
    while len(steps) < 9:
        GameLogic.motion('X')
        GameLogic.check('X')
        GameLogic.computer_motion('0')
        GameLogic.check('0')
    exit(0)
else:
    print('\nНеверное значение, попробуйте еще раз!')
