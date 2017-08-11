import numpy as np
from caffe.proto import caffe_pb2
import caffe.io


class NeuralNet:
    def __init__(self, job_id, iteration, dataset_job_id):
        caffe.set_mode_cpu()
        path = '/home/mathias/Cloned_repos/DIGITS/digits/jobs/{}/'.format(job_id)
        self.net = caffe.Net(path + 'deploy.prototxt', path + 'snapshot_iter_{}.caffemodel'.format(iteration),
                             caffe.TEST)

        self.load_mean(dataset_job_id)

    def load_mean(self, dataset_job_id):
        with open('/home/mathias/Cloned_repos/DIGITS/digits/jobs/{}/mean.binaryproto'.format(dataset_job_id),
                  'rb') as infile:
            blob = caffe_pb2.BlobProto()
            blob.MergeFromString(infile.read())
            mean_arr = caffe.io.blobproto_to_array(blob)
            self.mean = mean_arr

    def get_result(self, image):
        probs = self.forward(image)[0].tolist()
        prob = max(probs)
        # print 'Probability: {}'.format(prob)
        # return self.pos_map[probs.index(prob) + 1]
        return probs.index(prob)

    def forward(self, image):
        image = np.array(image)
        image = np.subtract(image, self.mean)

        self.net.blobs['data'].data[...] = image
        output = self.net.forward()
        probs = output['softmax']
        print probs
        return probs
