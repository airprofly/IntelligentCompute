<div align="center">

# 🧠 智能计算课程实验
### Intelligent Computing Course Experiments

[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/airprofly/IntelligentCompute) [![Star](https://img.shields.io/github/stars/airprofly/IntelligentCompute?style=social)](https://github.com/airprofly/IntelligentCompute/stargazers) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/) [![NumPy](https://img.shields.io/badge/NumPy-1.19+-orange.svg)](https://numpy.org/)

深度学习基础 · 神经网络设计 · 从零实现

</div>

---

## 📖 项目简介

> 本仓库包含智能计算课程的实验代码，涵盖深度学习基础、神经网络设计与实现等内容。所有实验均使用 **NumPy 从零实现**，旨在帮助深入理解神经网络的底层原理。

---

## 📦 实验模块

本课程项目包含以下实验模块：

| 实验模块 | 简介 | 状态 | README |
|---------|------|------|--------|
| **实验 2.1** | 基于 4 层 MLP 的 MNIST 手写数字识别，准确率 98%+ | ✅ 已完成 | [查看详情](./exp_2_1_mnist_mlp/README.md) |

<details>
<summary><b>🔮 未来计划</b></summary>

- 🚧 实验 2.2：卷积神经网络（CNN）实现
- 🚧 实验 3.1：循环神经网络（RNN）与序列建模
- 🚧 实验 3.2：注意力机制与 Transformer
- 📅 更多实验持续更新中...

</details>

---

## 🛠️ 技术栈

| 技术 | 版本/说明 |
|------|----------|
| **Python** | 3.7+ |
| **NumPy** | 1.19+ - 用于数值计算和矩阵运算 |

---

## 🔧 环境要求

### 运行环境

- Python 3.7 或更高版本
- NumPy 1.19 或更高版本

### 安装依赖

```bash
# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install numpy>=1.19
```

---

## 🚀 快速开始

### 1. 克隆仓库

```bash
git clone https://github.com/airprofly/IntelligentCompute.git
cd IntelligentCompute
```

### 2. 选择实验模块

```bash
# 进入实验目录
cd exp_2_1_mnist_mlp

# 查看详细说明
cat README.md

# 运行实验
python main_exp_2_1.py
```

> 💡 **提示**：每个实验模块都有独立的 README，包含详细的实现说明、环境配置和运行方法。

---

## 📚 学习路径

本课程实验按照以下路径设计：

```text
基础篇
└── 实验 2.1：多层感知机（MLP）+ MNIST 分类
    ├── 全连接层实现
    ├── ReLU 激活函数
    ├── Softmax 损失函数
    └── 反向传播算法

进阶篇（计划中）
├── 卷积神经网络（CNN）
├── 循环神经网络（RNN）
└── 注意力机制与 Transformer
```

---

## 📝 课程目标

通过本课程实验，你将掌握：

- ✅ 神经网络的数学原理（矩阵运算、链式法则）
- ✅ 前向传播和反向传播的实现细节
- ✅ 参数梯度的计算和更新方法
- ✅ 深度学习框架（如 PyTorch、TensorFlow）背后的工作机制
- ✅ 经典数据集（MNIST、CIFAR-10 等）的处理方式

---

## 📄 许可证

本项目采用 [MIT 许可证](https://opensource.org/licenses/MIT)。

---

<div align="center">

**智能计算课程实验项目**

Made with ❤️ by [IntelligentCompute Team](https://github.com/airprofly/IntelligentCompute)

</div>
