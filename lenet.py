'''
  Author       : Bao Jiarong
  Creation Date: 2020-06-14
  email        : bao.salirong@gmail.com
  Task         : LeNet Implementation
  Dataset      : MNIST Digits (0,1,...,9)
'''

import tensorflow as tf

class Block(tf.keras.models.Sequential):
    def __init__(self,n):
        super().__init__()
        self.add(tf.keras.layers.Conv2D(filters = n, kernel_size=(5,5),strides=(1,1),padding = 'valid',activation = "tanh"))
        self.add(tf.keras.layers.AveragePooling2D(pool_size = (2, 2)))

class Block1(tf.keras.models.Sequential):
    def __init__(self,n):
        super().__init__()
        self.add(tf.keras.layers.Conv2D(filters = n, kernel_size=(5,5),strides=(1,1),padding = 'valid',activation = "relu"))
        self.add(tf.keras.layers.MaxPool2D(pool_size = (2, 2)))

class LeNet_5(tf.keras.models.Sequential):
    def __init__(self, input_shape, classes):
        super().__init__()
        self.add(tf.keras.layers.InputLayer(input_shape = input_shape))

        # Backbone
        self.add(Block(n = 6))
        self.add(Block(n = 16))
        self.add(tf.keras.layers.Conv2D(filters = 120, kernel_size=(5,5),strides=(1,1),padding = 'valid',activation = "tanh"))
        # top
        self.add(tf.keras.layers.Flatten())
        self.add(tf.keras.layers.Dense(units = 84, activation = "tanh"))
        self.add(tf.keras.layers.Dense(units = classes,activation = "softmax"))


class LeNet(tf.keras.models.Sequential):
    def __init__(self, input_shape, classes):
        super().__init__()
        self.add(tf.keras.layers.InputLayer(input_shape = input_shape))

        # Backbone
        self.add(Block1(n = 6))
        self.add(Block1(n = 16))
        self.add(tf.keras.layers.Conv2D(filters = 120, kernel_size=(5,5),strides=(1,1),padding = 'valid',activation = "relu"))

        #top
        self.add(tf.keras.layers.Flatten())
        self.add(tf.keras.layers.Dense(units = 84, activation = "relu"))
        self.add(tf.keras.layers.Dense(units = classes, activation = "softmax"))
