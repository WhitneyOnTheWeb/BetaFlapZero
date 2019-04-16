import sys

sys.path.append('../')
sys.path.append('./game')

import gc
import numpy as np
import pprint as pp
import tensorflow as tf
import keras.backend as K
from flappy_util import Utility
from flappy_inputs import Inputs
from flappy_beta import BetaFlapDQN
from tensorflow import ConfigProto, Session, InteractiveSession, Graph
from rl.memory import SequentialMemory, RingBuffer, Memory
import os
#os.environ['TF_CPP_MIN_LOG_LEVEL']='2'


inputs = Inputs()
inputs = inputs.params
util = Utility()
gpu = '/job:localhost/replica:0/task:0/device:GPU:0'

buffer = SequentialMemory(                       # initialize buffer outside of agent
    limit=inputs['memory']['limit'], 
    window_length=inputs['memory']['state_size'],
)
util.display_status(
    'Built Replay Buffer Limited to {} States'.format(inputs['memory']['limit'])
)

with tf.device(gpu):
    graph = tf.get_default_graph()
    config = util.config_session()
    sess = InteractiveSession(config=config)
agent = BetaFlapDQN(inputs, buffer, sess)

'''Fit and Train model with BetaFlap Workflow'''
# this is a very memory intensive task, so its
# broken down into smaller increments
iters = 20
for i in range(1, iters):
    K.set_session(sess)
    '''---Session Parameters---'''
    print(        
    'Training Iterations [{}:{}]------------------------------------------------------'.\
            format(i, i + iters-1)
    )
    with sess.as_default():
        with tf.device(gpu):
            done = agent.fit(i, i + iters - 1)
        #buffer = agent.memory   # pass memory back to save interval over interval
        gc.collect()
        if done:
            break