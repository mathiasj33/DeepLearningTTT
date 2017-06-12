import os

os.environ['GLOG_minloglevel'] = '2' 

from game import Game
import visualize
from neuralnet import net
from PIL import Image
import neuralnet.example as example

os.environ['GLOG_minloglevel'] = '0' 

def main():
    game = Game('X')
    
    nn = net.NeuralNet()
    image = Image.open('/home/mathias/mnist/train/2/00178.png')
    result = nn.get_result(image)
    print result
    
    
    #===========================================================================
    # result = example.classify(
    #         '/home/mathias/Cloned_repos/DIGITS/digits/jobs/20170610-012554-8beb/snapshot_iter_1408.caffemodel',
    #         '/home/mathias/Cloned_repos/DIGITS/digits/jobs/20170610-012554-8beb/deploy.prototxt',
    #         ['/home/mathias/mnist/train/2/00178.png'],
    #         mean_file='/home/mathias/Cloned_repos/DIGITS/digits/jobs/20170401-220250-9164/mean.binaryproto',
    #         use_gpu=False
    #     )
    # print result.argmax(1)
    # print result[0,result.argmax(1)]
    #===========================================================================
    
    #===========================================================================
    # while True:
    #     i = raw_input()
    #     game.set_figure((int(i[0]), int(i[1])))
    #     image = visualize.create_image(game)
    #     #visualize.draw(game)
    #     image = image.resize((28,28), PIL.Image.ANTIALIAS)
    #     result = nn.get_result(image)
    #     print result
    #     game.set_figure(result)
    #     #visualize.draw(game)
    #===========================================================================
        
if __name__ == '__main__':
    main()