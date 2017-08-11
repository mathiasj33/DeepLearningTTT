from game import Game
import visualize
import ai
from os.path import expanduser, join
import os
import random

FOLDER = join(expanduser('~'), '.tictactoe')
TRAIN_FOLDER = join(FOLDER, 'train')
VAL_FOLDER = join(FOLDER, 'val')
CHOICE_TO_FOLDER_NAME = {(0, 0): 1, (1, 0): 2, (2, 0): 3, (0, 1): 4, (1, 1): 5, (2, 1): 6, (0, 2): 7, (1, 2): 8,
                         (2, 2): 9}
x_player = ai.AI('X')
o_player = ai.AI('O')


def play():
    game = Game('X')
    visualize.draw(game)

    while True:
        i = input()
        game.set_figure((int(i[0]), int(i[1])))
        game.set_figure(o_player.find_best_move(game))
        visualize.draw(game)


def generate_best_start_o():
    positions = [(i, j) for i in range(3) for j in range(3)]
    id = 1
    for i, j in positions:
        game = Game('X')

        game.set_figure((i, j))

        while game.get_winner() == 'NoWinner':
            save_image(visualize.create_image(game), join(str(get_folder(game)), str(id)))
            id += 1
            game.set_figure(o_player.find_best_move(game))

            if game.get_winner() != 'NoWinner': break
            game.set_figure(x_player.find_best_move(game))
        print('Finished')


def generate_random(num_games):
    id = 0
    for i in range(num_games):
        game = Game('X')

        while game.get_winner() == 'NoWinner':
            game.set_figure(game.get_possible_moves()[random.randint(0, len(game.get_possible_moves()) - 1)])

            if game.get_winner() != 'NoWinner': break

            save_image(visualize.create_direct_image(game), join(str(get_folder(game)), str(id)), 'train')
            id += 1
            game.set_figure(o_player.find_best_move(game))

        print('Finished game {}/{}'.format(i, num_games))

    print('Generated {} images.'.format(id))


def generate_random_x_and_o(num_train, num_val):
    simulate_games(num_train, 'train')
    simulate_games(num_val, 'val')


def simulate_games(num, type):
    id = 0
    for i in range(num):
        start_player = 'X' if random.random() <= 0.5 else 'O'
        game = Game(start_player)

        while game.get_winner() == 'NoWinner':
            save_image(visualize.create_image(game), join(str(get_folder(game)), str(id)), type)
            id += 1
            game.set_figure(game.get_possible_moves()[random.randint(0, len(game.get_possible_moves()) - 1)])

            if game.get_winner() != 'NoWinner': break

            save_image(visualize.create_image(game), join(str(get_folder(game)), str(id)), type)
            id += 1
            game.set_figure(game.get_possible_moves()[random.randint(0, len(game.get_possible_moves()) - 1)])

        print('Finished {} game {}/{}'.format(type, i, num))


def get_folder(game):
    if game.get_player() == 'X':
        return CHOICE_TO_FOLDER_NAME[x_player.find_best_move(game)]
    elif game.get_player() == 'O':
        return CHOICE_TO_FOLDER_NAME[o_player.find_best_move(game)]


def save_image(img, name, type):
    folder = TRAIN_FOLDER if type == 'train' else VAL_FOLDER
    path = join(folder, name)
    if not os.path.exists(os.path.dirname(path)): os.makedirs(os.path.dirname(path))
    img.save('{}.png'.format(path))


if __name__ == '__main__':
    generate_random(500)
