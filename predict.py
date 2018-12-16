import numpy as np
import pandas as pd
import tensorflow as tf
from sklearn import preprocessing

import os

CURRENT_MODEL_NAME = 'dog_model'
INCEPTION_INPUT_TENSOR = 'DecodeJpeg/contents:0'
INCEPTION_OUTPUT_TENSOR = 'pool_3:0'
OUTPUT_NODE_NAME = 'output_node'
OUTPUT_TENSOR_NAME = OUTPUT_NODE_NAME + ':0'
BREEDS = './breeds.csv'
CLASSES_COUNT = 120


def one_hot_label_encoder():
    train_Y_orig = pd.read_csv(BREEDS, dtype={'breed': np.str})
    lb = preprocessing.LabelBinarizer()
    lb.fit(train_Y_orig['breed'])

    def encode(labels):
        return np.asarray(lb.transform(labels), dtype=np.float32)

    def decode(one_hots):
        return np.asarray(lb.inverse_transform(one_hots), dtype=np.str)

    return encode, decode


def unfreeze_into_current_graph(model_path, tensor_names):
    with tf.gfile.FastGFile(name=model_path, mode='rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        tf.import_graph_def(graph_def, name='')
        g = tf.get_default_graph()

        tensors = {t: g.get_tensor_by_name(t) for t in tensor_names}

        return tensors


def infer(model_name, img_raw):
    with tf.Graph().as_default(), tf.Session().as_default() as sess:
        tensors = unfreeze_into_current_graph(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), model_name + '.pb'),
            tensor_names=[INCEPTION_INPUT_TENSOR, OUTPUT_TENSOR_NAME])

        _, one_hot_decoder = one_hot_label_encoder()

        probs = sess.run(tensors[OUTPUT_TENSOR_NAME],
                         feed_dict={tensors[INCEPTION_INPUT_TENSOR]: img_raw})

        breeds = one_hot_decoder(np.identity(CLASSES_COUNT)).reshape(-1)

        df = pd.DataFrame(data={'prob': probs.reshape(-1), 'breed': breeds})

        return df.sort_values(['prob'], ascending=False)


def classify(path):
    with open(path, 'rb') as f:
        img_raw = f.read()

    return infer(CURRENT_MODEL_NAME, img_raw)

def getPrediction(image_dir):
    path = image_dir
    probs = classify(path)
    dog_breed_table = (probs.sort_values(['prob'], ascending=False).take(range(5)))
    return (dog_breed_table)

if __name__ == '__main__':
    path = './baldman.jpeg'
    probs = classify(path)
    #getPrediction(probs)
    print(probs.sort_values(['prob'], ascending=False).take(range(5)))
