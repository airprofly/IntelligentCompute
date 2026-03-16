import sys
import numpy as np
import struct
import os
import time

def show_matrix(mat, name):
    #print(name + str(mat.shape) + ' mean %f, std %f' % (mat.mean(), mat.std()))
    pass

def show_time(time, name):
    #print(name + str(time))
    pass


class FullyConnectedLayer(object):
    def __init__(self, num_input, num_output):  # 全连接层初始化
        self.num_input=num_input
        self.num_output=num_output
        print('\tFully connected layer with input %d, output %d.' % (self.num_input, self.num_output))
    def init_param(self, std=0.01):  # 参数初始化
        # 使用标准He初始化，适合ReLU激活函数
        scale = np.sqrt(2.0 / self.num_input)
        self.weight = np.random.normal(loc=0.0, scale=scale, size=(self.num_input, self.num_output))
        self.bias=np.zeros([1, self.num_output])
        show_matrix(self.weight, 'fc weight ')
        show_matrix(self.bias, 'fc bias ')
    def forward(self, input): # 前向传播计算
        start_time = time.time()
        self.input=input
        # TODO：全连接层的前向传播，计算输出结果
        # output = input @ weight + bias
        self.output=np.dot(self.input, self.weight) + self.bias
        return self.output

    def backward(self, top_diff):   # 反向传播的计算
        # TODO：全连接层的反向传播，计算参数梯度和本层损失
        # d_weight = input.T @ top_diff
        # d_bias = sum(top_diff, axis=0)
        # bottom_diff = top_diff @ weight.T
        self.d_weight=np.dot(self.input.T, top_diff)
        self.d_bias=np.sum(top_diff, axis=0, keepdims=True)

        # 更宽松的梯度裁剪，允许更大的梯度更新
        clip_threshold = 20.0
        self.d_weight = np.clip(self.d_weight, -clip_threshold, clip_threshold)
        self.d_bias = np.clip(self.d_bias, -clip_threshold, clip_threshold)

        bottom_diff=np.dot(top_diff, self.weight.T)

        return bottom_diff
    def get_gradient(self):

        return self.d_weight,self.d_bias

    def update_param(self, lr):  # 参数更新
        # TODO：对全连接层参数利用参数进行更新
        # weight = weight - lr * d_weight
        # bias = bias - lr * d_bias
        self.weight=self.weight - lr * self.d_weight
        self.bias=self.bias - lr * self.d_bias
        
    def load_param(self, weight, bias): # 参数加载
        assert self.weight.shape == weight.shape
        assert self.bias.shape == bias.shape
        self.weight=weight
        self.bias=bias
        show_matrix(self.weight, 'fc weight ')
        show_matrix(self.bias, 'fc bias ')

    def save_param(self):    # 参数保存
        show_matrix(self.weight, 'fc weight ')
        show_matrix(self.bias, 'fc bias ')
        return self.weight, self.bias


class ReLULayer(object):
    def __init__(self):
        print('\t Relu layer')

    def forward(self, input):  # 前向传播的计算
        start_time = time.time()
        self.input=input
        # TODO：ReLU层的前向传播，计算输出结果
        # ReLU: max(0, x)
        output=np.maximum(0, self.input)
        return output
    def backward(self, top_diff):   # 反向传播的计算
        # TODO：ReLU层的反向传播，计算本层损失
        # ReLU梯度：input > 0 时为1，否则为0
        bottom_diff=top_diff * (self.input > 0)
        return bottom_diff

class SoftmaxLossLayer(object):
    def __init__(self):
        print('\tSoftmax loss layer.')
    def forward(self, input):  # 前向传播的计算
        # TODO：softmax 损失层的前向传播，计算输出结果
        input_max = np.max(input, axis=1, keepdims=True)
        input_exp = np.exp(input-input_max)
        exp_sum = np.sum(input_exp, axis=1, keepdims=True)
        self.prob = input_exp / exp_sum
        return self.prob

    def get_loss(self,label):  # 计算损失
        self.batch_size=self.prob.shape[0]
        self.label_onehot=np.zeros_like(self.prob)
        # 将label从二维数组(batch_size, 1)展平为一维数组，并转换为整数类型
        label = label.flatten().astype(int)
        self.label_onehot[np.arange(self.batch_size),label]=1.0
        # 添加小的epsilon避免log(0)
        epsilon = 1e-10
        loss=-np.sum(np.log(self.prob + epsilon)*self.label_onehot)/self.batch_size
        return loss
    def backward(self):   # 反向传播的计算
        # TODO：softmax 损失层的反向传播，计算本层损失
        # softmax梯度：prob - onehot_label
        bottom_diff=self.prob - self.label_onehot
        return bottom_diff




