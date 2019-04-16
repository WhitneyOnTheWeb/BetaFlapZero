import tensorflow as tf
from learner.flappy_beta import NeuralNet
from tensorflow import Session, InteractiveSession

sess = tf.Session()
model = NeuralNet(sess)
print(model.nn.summary())
sess.close()