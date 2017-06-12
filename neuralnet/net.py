import caffe
import numpy as np
from PIL import Image
from caffe.proto import caffe_pb2
import caffe.io

class NeuralNet:
    
    def __init__(self):
        caffe.set_mode_cpu()
        path = '/home/mathias/Cloned_repos/DIGITS/digits/jobs/20170401-220343-caab/'
        self.net = caffe.Net(path + 'deploy.prototxt', path + 'snapshot_iter_1408.caffemodel', caffe.TEST)
        
        self.load_mean()
        
        pos_map_inv = {(0, 0): 1, (1, 0): 2, (2, 0): 3, (0, 1): 4, (1, 1): 5, (2, 1): 6, (0, 2): 7, (1, 2): 8, (2, 2): 9}
        self.pos_map = {v: k for k, v in pos_map_inv.iteritems()}
    
    def load_mean(self):
        with open('/home/mathias/Cloned_repos/DIGITS/digits/jobs/20170401-220250-9164/mean.binaryproto', 'rb') as infile:
            blob = caffe_pb2.BlobProto()
            blob.MergeFromString(infile.read())
            mean_arr = caffe.io.blobproto_to_array(blob)
            self.mean = mean_arr
    
    def get_result(self, image):
        probs = self.forward(image)[0].tolist()
        prob = max(probs)
        print 'Probability: {}'.format(prob)
        # return self.pos_map[probs.index(prob) + 1]
        return probs.index(prob)
    
    def forward(self, image):
        image = np.array(image)
        image = np.subtract(image, self.mean)

        self.net.blobs['data'].data[...] = image
        output = self.net.forward()
        probs = output['softmax']
        print 'Probs:' + str(probs)
        return probs