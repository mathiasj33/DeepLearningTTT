import os
import ai

os.environ['GLOG_minloglevel'] = '2'

from game import Game
import visualize
from neuralnet import net
from PIL import Image
import scipy
import numpy as np

os.environ['GLOG_minloglevel'] = '0'

net_id = '20170811-150037-28a7'
iteration = 2200
db_id = '20170811-145308-534f'

def classify_example():
    nn = net.NeuralNet(net_id, iteration, db_id)
    example = Image.open('/home/mathias/.tictactoe/train/7/14.png').convert('L')
    print(nn.get_result(example) + 1)


def play_against_human():
    game = Game('X')
    pos_map_inv = {(0, 0): 1, (1, 0): 2, (2, 0): 3, (0, 1): 4, (1, 1): 5, (2, 1): 6, (0, 2): 7, (1, 2): 8, (2, 2): 9}
    pos_map = {v: k for k, v in pos_map_inv.iteritems()}

    nn = net.NeuralNet(net_id, iteration, db_id)

    while True:
        i = raw_input()
        game.set_figure((int(i[0]), int(i[1])))
        visualize.draw(game)
        image = visualize.create_direct_image(game)
        #image = image.resize((28, 28), Image.BILINEAR)
        result = nn.get_result(image) + 1
        print result
        pos = pos_map[result]
        game.set_figure(pos)
        visualize.draw(game)
        visualize.save_direct(game)


def play_against_ai(num_matches):
    pos_map_inv = {(0, 0): 1, (1, 0): 2, (2, 0): 3, (0, 1): 4, (1, 1): 5, (2, 1): 6, (0, 2): 7, (1, 2): 8, (2, 2): 9}
    pos_map = {v: k for k, v in pos_map_inv.iteritems()}

    nn = net.NeuralNet(net_id, iteration, db_id)

    ties = 0
    x_wins = 0
    o_wins = 0

    for i in range(num_matches):
        game = Game('X')
        x_player = ai.AI('X')
        while game.get_winner() == 'NoWinner':
            game.set_figure(x_player.find_best_move(game))
            if game.get_winner() == 'X':
                x_wins += 1
                break
            elif game.get_winner() == 'O':
                o_wins += 1
                break
            elif game.get_winner() == 'Tie':
                ties += 1
                break
            result = nn.get_result(visualize.create_direct_image(game)) + 1
            try:
                game.set_figure(pos_map[result])
            except ValueError:
                print('Field already used. Skipping.')
                visualize.draw(game)
                visualize.create_direct_image(game).show()
                print(pos_map[result])
                return

            if game.get_winner() == 'X':
                x_wins += 1
                break
            elif game.get_winner() == 'O':
                o_wins += 1
                break
            elif game.get_winner() == 'Tie':
                ties += 1
                break

    print('Net: {}, AI: {}, Ties: {}'.format(o_wins, x_wins, ties))

if __name__ == '__main__':
    #play_against_human()
    play_against_ai(10)
