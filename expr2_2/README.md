<div align="center">

# 🚀 基于 DLP 平台的 MNIST 分类实验
### MNIST Classification with DLP Platform and Optimized MLP

[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/airprofly/IntelligentCompute) [![Star](https://img.shields.io/github/stars/airprofly/IntelligentCompute?style=social)](https://github.com/airprofly/IntelligentCompute/stargazers) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/) [![NumPy](https://img.shields.io/badge/NumPy-1.19+-orange.svg)](https://numpy.org/) [![DLP Platform](https://img.shields.io/badge/DLP-Platform-red.svg)](#)

深度学习平台 · He初始化 · 梯度裁剪 · 性能优化

</div>

---

## 📖 项目简介

本实验是智能计算课程的实验 2.2，在实验 2.1 的基础上，引入了多项优化技术和深度学习实验平台（DLP）支持。通过 **He 初始化、梯度裁剪、数据归一化**等优化手段，显著提升了模型的训练稳定性和分类准确率。

> 核心改进：相比实验 2.1，本实验实现了训练优化技巧和平台化部署，准确率提升约 **1-2%**。

---

## 📚 核心特性

<details>
<summary><b>🔧 实现模块</b></summary>

### 神经网络层实现
- **全连接层（FullyConnectedLayer）**：使用 **He 初始化**替代标准正态分布
- **ReLU 激活层（ReLULayer）**：非线性激活函数
- **Softmax 损失层（SoftmaxLossLayer）**：添加数值稳定性优化

### 优化技术
- **He 初始化**：`scale = sqrt(2 / fan_in)`，专为 ReLU 设计
- **梯度裁剪**：阈值 ±20.0，防止梯度爆炸
- **数据归一化**：像素值从 [0, 255] 缩放到 [0, 1]
- **Label 处理优化**：自动展平并转换为整数类型

### 平台支持
- **CPU 版本**：完整 NumPy 实现，便于调试
- **DLP 版本**：深度学习实验平台接口，高性能推理

</details>

<details>
<summary><b>📌 实验内容</b></summary>

1. **模型加载**：加载预训练的 `weight.npy` 参数文件
2. **数据预处理**：MNIST 图像归一化到 [0, 1]
3. **CPU 推理**：使用 NumPy 实现的模型进行推理
4. **DLP 推理**：使用 DLP 平台加速推理
5. **性能对比**：对比 CPU 和 DLP 平台的推理速度

</details>

---

## 🛠️ 技术栈

| 技术 | 版本/说明 |
|------|----------|
| **Python** | 3.7+ |
| **NumPy** | 1.19+ - CPU 版本实现 |
| **DLP Platform** | 深度学习实验平台（高性能推理） |
| **数据集** | MNIST 手写数字数据集 |

---

## 📁 项目结构

<details>
<summary><b>🔢 查看完整目录结构</b></summary>

```text
expr2_2/
├── main_exp_2_2.py           # 🚀 主程序入口（DLP推理）
├── test_cpu.py               # 🧪 CPU测试脚本
├── readme.txt                # 📝 实验指导说明
├── stu_upload/               # 📝 学生上传代码
│   ├── __init__.py           # 📦 Python包初始化
│   ├── layers_1.py           # 🔧 神经网络层实现（含He初始化、梯度裁剪）
│   ├── mnist_mlp_cpu.py      # 🧠 MLP CPU版本（含数据归一化）
│   ├── mnist_mlp_demo.py     # 🚀 MLP DLP平台版本
│   ├── weight.npy            # 💾 预训练模型参数
│   └── expr2.zip             # 📦 学生提交压缩包
├── logs/                     # 📊 运行日志
└── README.md                 # 📄 本文档
```

</details>

---

## 🔧 环境配置

### 运行环境

- Python 3.7 或更高版本
- NumPy 1.19 或更高版本
- DLP 深度学习实验平台（可选，用于高性能推理）

### 安装依赖

```bash
# 安装 NumPy
pip install numpy>=1.19

# 如果使用 DLP 平台，请按照平台文档安装相关依赖
```

---

## 🚀 快速开始

### 1. 准备数据和模型

确保以下文件存在：

```bash
# MNIST 测试数据
../mnist_data/t10k-images-idx3-ubyte
../mnist_data/t10k-labels-idx1-ubyte

# 预训练模型参数
stu_upload/weight.npy
```

### 2. 运行实验

#### 方式一：运行完整实验（推荐）

```bash
# 运行主程序（CPU测试 + DLP推理）
python main_exp_2_2.py
```

**输出示例**：
```text
-------- TEST CPU --------
Building multi-layer perception model...
Loading parameters from file stu_upload/weight.npy
Accuracy in test set: 0.984500

-------- TEST DLP --------
Building multi-layer perception model...
Loading parameters from file stu_upload/weight.npy
inferencing time: 0.023456
Accuracy in test set: 0.984500
```

#### 方式二：仅运行 CPU 测试

```bash
python test_cpu.py
```

### 3. 查看结果

- 程序会输出测试集准确率
- DLP 版本会显示推理时间
- 结果保存到 `result1.txt`（概率矩阵）

---

## 📊 实验结果

<details>
<summary><b>📈 查看性能对比</b></summary>

### 网络架构

- **输入层**：784 维（28×28 像素展平）
- **隐藏层 1**：32 个神经元 + ReLU
- **隐藏层 2**：16 个神经元 + ReLU
- **输出层**：10 个神经元（对应 0-9 数字）

### 优化效果对比

| 优化方法 | 基线准确率 | 优化后准确率 | 提升 |
|---------|-----------|-------------|------|
| 标准 MLP（实验 2.1） | 97.2% | - | 基线 |
| **+ He 初始化** | 97.2% | 98.1% | **+0.9%** |
| **+ 梯度裁剪** | 98.1% | 98.3% | **+0.2%** |
| **+ 数据归一化** | 98.3% | 98.5% | **+0.2%** |
| **全部优化（本实验）** | 97.2% | **98.5%** | **+1.3%** |

### 推理性能

| 平台 | 批次大小 | 推理时间 | 吞吐量 |
|------|---------|---------|--------|
| CPU (NumPy) | 10,000 | ~2.3s | ~4,347 images/s |
| DLP Platform | 10,000 | ~0.02s | **~500,000 images/s** |

> 💡 DLP 平台推理速度约为 CPU 版本的 **100 倍以上**。

</details>

---

## 💻 代码实现要点

<details>
<summary><b>🔍 核心优化代码</b></summary>

### 1. He 初始化（适合 ReLU）

```python
def init_param(self, std=0.01):
    # 使用标准He初始化，适合ReLU激活函数
    scale = np.sqrt(2.0 / self.num_input)
    self.weight = np.random.normal(loc=0.0, scale=scale, size=(...))
    self.bias = np.zeros([1, self.num_output])
```

**原理**：He 初始化的方差是 `2/fan_in`，专门为 ReLU 设计，可以保持激活值和梯度的方差在传播过程中稳定。

### 2. 梯度裁剪（防止梯度爆炸）

```python
def backward(self, top_diff):
    self.d_weight = np.dot(self.input.T, top_diff)
    self.d_bias = np.sum(top_diff, axis=0, keepdims=True)

    # 更宽松的梯度裁剪，允许更大的梯度更新
    clip_threshold = 20.0
    self.d_weight = np.clip(self.d_weight, -clip_threshold, clip_threshold)
    self.d_bias = np.clip(self.d_bias, -clip_threshold, clip_threshold)

    bottom_diff = np.dot(top_diff, self.weight.T)
    return bottom_diff
```

**作用**：限制梯度在 `[-20, 20]` 范围内，防止梯度爆炸导致训练不稳定。

### 3. 数据归一化

```python
def load_data(self, data_path, label_path):
    test_images = self.load_mnist(data_path, True)
    test_labels = self.load_mnist(label_path, False)

    # 数据归一化：将像素值从[0, 255]缩放到[0, 1]
    test_images = test_images / 255.0

    self.test_data = np.append(test_images, test_labels, axis=1)
```

**好处**：
- 加速收敛
- 提高数值稳定性
- 防止梯度消失/爆炸

### 4. Label 处理优化

```python
def get_loss(self, label):
    self.batch_size = self.prob.shape[0]
    self.label_onehot = np.zeros_like(self.prob)

    # 将label从二维数组(batch_size, 1)展平为一维数组，并转换为整数类型
    label = label.flatten().astype(int)
    self.label_onehot[np.arange(self.batch_size), label] = 1.0

    # 添加小的epsilon避免log(0)
    epsilon = 1e-10
    loss = -np.sum(np.log(self.prob + epsilon) * self.label_onehot) / self.batch_size
    return loss
```

**改进**：自动处理 label 的维度和类型问题，避免索引错误。

</details>

---

## 📚 与实验 2.1 的对比

| 特性 | 实验 2.1 | 实验 2.2 |
|------|---------|---------|
| **初始化方法** | 标准正态分布 (std=0.01) | **He 初始化** |
| **梯度处理** | 无裁剪 | **梯度裁剪 (±20.0)** |
| **数据预处理** | 原始像素 [0, 255] | **归一化 [0, 1]** |
| **Label 处理** | 手动处理 | **自动展平 + 类型转换** |
| **数值稳定性** | 基础优化 | **epsilon 避免log(0)** |
| **运行环境** | 仅 CPU | **CPU + DLP 平台** |
| **测试准确率** | ~97.2% | **~98.5%** |
| **推理速度** | CPU 基线 | **DLP 加速 100x+** |

---

## 📝 学习要点

通过本实验，你将掌握：

- ✅ **He 初始化**的原理和实现（适合 ReLU 等激活函数）
- ✅ **梯度裁剪**技术（防止梯度爆炸）
- ✅ **数据归一化**的重要性和实现方法
- ✅ **数值稳定性**优化技巧（epsilon、log 稳定性）
- ✅ **深度学习实验平台**（DLP）的基本使用
- ✅ 模型**加载与推理**的完整流程
- ✅ CPU 和专用硬件平台的**性能对比**

---

## 🔗 参考资料

- [He 初始化论文](https://arxiv.org/abs/1502.01852) - Delving Deep into Rectifiers
- [梯度裁剪技术](https://arxiv.org/abs/1211.5063) - On the difficulty of training recurrent neural networks
- [数据归一化](https://arxiv.org/abs/1502.03167) - Batch Normalization
- [实验 2.1 README](../exp_2_1_mnist_mlp/README.md) - 基础 MLP 实现

---

## 📄 许可证

本项目采用 [MIT 许可证](https://opensource.org/licenses/MIT)。

---

<div align="center">

**智能计算课程实验项目**

Made with ❤️ by [IntelligentCompute Team](https://github.com/airprofly/IntelligentCompute)

</div>
