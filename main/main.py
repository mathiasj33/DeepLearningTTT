import os

os.environ['GLOG_minloglevel'] = '2' 

from game import Game
import visualize
from neuralnet import net
from PIL import Image
import scipy
import numpy as np

os.environ['GLOG_minloglevel'] = '0' 

def classify_example():
    nn = net.NeuralNet('20170607-223813-dc64', 4800, '20170607-223705-f269')
    example = Image.open('/home/mathias/example.png').convert('L').resize((28,28),Image.BILINEAR)
    print nn.get_result(example) + 1

def main():
    game = Game('X')
    pos_map_inv = {(0, 0): 1, (1, 0): 2, (2, 0): 3, (0, 1): 4, (1, 1): 5, (2, 1): 6, (0, 2): 7, (1, 2): 8, (2, 2): 9}
    pos_map = {v: k for k, v in pos_map_inv.iteritems()}
    
    nn = net.NeuralNet('20170607-223813-dc64', 4800, '20170607-223705-f269')
    
    while True:
        i = raw_input()
        game.set_figure((int(i[0]), int(i[1])))
        image = visualize.create_image(game)
        visualize.draw(game)
        image = image.resize((28,28), Image.BILINEAR)
        result = nn.get_result(image) + 1
        print result
        pos = pos_map[result]
        game.set_figure(pos)
        visualize.draw(game)
        
if __name__ == '__main__':
    main()