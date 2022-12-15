from random import randint


def get_answer(number):
    """Function takes player`s answer"""
    available_answers = ('to big', 'to small', 'you win')
    print(f'My guess is {number}.')
    while True:
        answer = input('Enter your answer (to big/to small/you win): ')
        if answer.lower() in available_answers:
            return answer
        else:
            print(f'That is not correct answer')


def game_loop():
    """main game loop"""
    print(f'Imagine and remember number between 0 and 1000, I will try to guess the number.')
    mx_num = 1000
    mi_num = 0
    available_tries = 10
    tries = 0
    pc_number = randint(mi_num, mx_num)
    while tries < available_tries:
        tries += 1
        p_answer = get_answer(pc_number)
        if p_answer == 'to big':
            mx_num = pc_number
            pc_number = randint(mi_num, mx_num)
        elif p_answer == 'to small':
            mi_num = pc_number
            pc_number = randint(mi_num, mx_num)
        elif p_answer == 'you win':
            return f'I have won, wohooo!'
        else:
            continue
    return f'I am out of tries ;('


if __name__ == '__main__':
    print(game_loop())



