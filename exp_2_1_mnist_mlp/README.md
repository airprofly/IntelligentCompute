<div align="center">

# 🔧 MNIST 多层感知器实验
### Multi-Layer Perceptron for MNIST Classification from Scratch

[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/airprofly/IntelligentCompute) [![Star](https://img.shields.io/github/stars/airprofly/IntelligentCompute?style=social)](https://github.com/airprofly/IntelligentCompute/stargazers) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/) [![NumPy](https://img.shields.io/badge/NumPy-1.19+-orange.svg)](https://numpy.org/)

深度学习 · 神经网络 · 从零实现 · MNIST识别

</div>

---

## 📖 项目简介

本项目是智能计算课程的实验项目，旨在通过从零实现多层感知器（Multi-Layer Perceptron, MLP），深入理解神经网络的核心原理。项目使用 NumPy 实现了包括全连接层、ReLU 激活层、Softmax 损失层在内的完整神经网络，并在 MNIST 手写数字数据集上完成训练和评估。

> 学习目标：掌握神经网络的前向传播、反向传播和参数更新机制，理解深度学习框架背后的实现原理。

---

## 📚 核心特性

<details>
<summary><b>🔧 实现模块</b></summary>

### 神经网络层实现
- **全连接层（FullyConnectedLayer）**：实现线性变换和参数学习
- **ReLU 激活层（ReLULayer）**：引入非线性，提升网络表达能力
- **Softmax 损失层（SoftmaxLossLayer）**：输出概率分布并计算交叉熵损失

### 网络架构
- 支持自定义网络层数和神经元数量
- 默认架构：784 → 256 → 128 → 64 → 10
- 可灵活调整超参数（学习率、批次大小、训练轮数等）

### 训练与评估
- 完整的训练流程：前向传播 → 损失计算 → 反向传播 → 参数更新
- 测试集评估：计算分类准确率
- 模型参数保存与加载

</details>

<details>
<summary><b>📌 实验内容</b></summary>

1. **数据加载与预处理**：读取 MNIST 数据集的二进制文件
2. **网络搭建**：构建多层神经网络结构
3. **前向传播**：逐层计算网络输出
4. **反向传播**：计算各层参数梯度
5. **参数更新**：使用梯度下降更新权重和偏置
6. **模型评估**：在测试集上验证模型性能

</details>

---

## 🛠️ 技术栈

| 技术 | 版本/说明 |
|------|----------|
| **Python** | 3.7+ |
| **NumPy** | 1.19+ - 用于数值计算和矩阵运算 |
| **数据集** | MNIST 手写数字数据集 |

---

## 📁 项目结构

<details>
<summary><b>🔢 查看完整目录结构</b></summary>

```text
exp_2_1_mnist_mlp/
├── main_exp_2_1.py           # 🚀 主程序入口
├── stu_upload/               # 📝 学生需完成的代码
│   ├── layers_1.py           # 🔧 神经网络层实现（全连接、ReLU、Softmax）
│   └── mnist_mlp_cpu.py      # 🧠 MLP 网络结构和训练流程
├── mnist_data/               # 💾 MNIST 数据集文件
├── logs/                     # 📊 训练日志
├── .gitignore                # 🚫 Git 忽略文件配置
├── .vscode/                  # ⚙️ VS Code 配置
└── README.md                 # 📄 项目说明文档

生成的模型文件：
├── mlp-256-128-64-20epoch.npz    # 训练好的模型参数
└── mlp-32-16-10epoch.npz         # 小规模模型参数
```

</details>

---

## 🔧 环境配置

### 运行环境

- Python 3.7 或更高版本
- NumPy 1.19 或更高版本

### 安装依赖

```bash
# 安装 NumPy
pip install numpy>=1.19

# 或使用 requirements.txt（如果提供）
pip install -r requirements.txt
```

---

## 🚀 快速开始

### 1. 准备数据集

确保 MNIST 数据集文件位于 `mnist_data/` 目录下：

```bash
mnist_data/
├── train-images-idx3-ubyte
├── train-labels-idx1-ubyte
├── t10k-images-idx3-ubyte
└── t10k-labels-idx1-ubyte
```

> 如需下载 MNIST 数据集，可访问 [MNIST 官网](http://yann.lecun.com/exdb/mnist/)

### 2. 运行实验

完成 `stu_upload/` 目录下的代码后，运行主程序：

```bash
# 运行完整实验（训练 + 评估）
python main_exp_2_1.py

# 或直接运行 MLP 模块
python stu_upload/mnist_mlp_cpu.py
```

### 3. 查看结果

- 训练过程会在终端输出损失值
- 训练完成后自动保存模型参数
- 程序会在测试集上评估并输出准确率

---

## 📊 实验结果

<details>
<summary><b>📈 查看预期结果</b></summary>

### 网络架构

- **输入层**：784 维（28×28 像素展平）
- **隐藏层 1**：256 个神经元 + ReLU
- **隐藏层 2**：128 个神经元 + ReLU
- **隐藏层 3**：64 个神经元 + ReLU
- **输出层**：10 个神经元（对应 0-9 数字）

### 训练配置

- **批次大小**：100
- **学习率**：0.01
- **训练轮数**：20 epochs
- **优化器**：随机梯度下降（SGD）

### 预期性能

在测试集上的分类准确率约为 **96% - 98%**（具体取决于实现细节和随机初始化）。

</details>

---

## 💻 代码实现要点

<details>
<summary><b>🔍 核心代码说明</b></summary>

### 全连接层

**前向传播**：
```python
self.output = np.dot(self.input, self.weight) + self.bias
```

**反向传播**：
```python
self.d_weight = np.dot(self.input.T, top_diff)
self.d_bias = np.dot(np.ones([1, self.input.shape[0]]), top_diff)
bottom_diff = np.dot(top_diff, self.weight.T)
```

### ReLU 激活层

**前向传播**：
```python
output = np.maximum(0, self.input)
```

**反向传播**：
```python
bottom_diff = top_diff.copy()
bottom_diff[self.input < 0] = 0
```

### Softmax 损失层

**前向传播**（带数值稳定性优化）：
```python
input_max = np.max(input, axis=1, keepdims=True)
input_exp = np.exp(input - input_max)
self.prob = input_exp / np.sum(input_exp, axis=1, keepdims=True)
```

**反向传播**：
```python
bottom_diff = (self.prob - self.label_onehot) / self.batch_size
```

</details>

---

## 📝 学习要点

通过本实验，你将掌握：

- ✅ 神经网络的数学原理（矩阵运算、链式法则）
- ✅ 前向传播和反向传播的实现细节
- ✅ 参数梯度的计算和更新方法
- ✅ 深度学习框架（如 PyTorch、TensorFlow）背后的工作机制
- ✅ MNIST 数据集的处理方式

---

## 🔗 参考资料

- [MNIST 数据集官网](http://yann.lecun.com/exdb/mnist/)
- [神经网络与深度学习](http://neuralnetworksanddeeplearning.com/)
- [CS231n: 卷积神经网络](http://cs231n.stanford.edu/)

---

## 📄 许可证

本项目采用 [MIT 许可证](https://opensource.org/licenses/MIT)。

---

<div align="center">

**智能计算课程实验项目**

Made with ❤️ by [IntelligentCompute Team](https://github.com/airprofly/IntelligentCompute)

</div>
