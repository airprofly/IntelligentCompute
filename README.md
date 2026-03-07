<div align="center">

# 🧠 智能计算课程实验

### Intelligent Computing Course Experiments

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![NumPy](https://img.shields.io/badge/NumPy-1.19+-orange.svg)](https://numpy.org/)

深度学习基础 · 神经网络设计 · 从零实现

</div>

---

## 📖 项目简介

> 本仓库包含智能计算课程的实验代码，涵盖深度学习基础、神经网络设计与实现等内容。所有实验均使用 **NumPy 从零实现**，旨在帮助深入理解神经网络的底层原理。

---



## 📚 实验目录

<details>
<summary><b>🔢 实验 2.1：基于多层感知机的 MNIST 手写数字识别</b></summary>

#### 📌 实验概览

| 项目 | 内容 |
|------|------|
| **实验目标** | 从零实现四层多层感知机（MLP），完成 MNIST 手写数字分类 |
| **网络结构** | 784 → 256 → 128 → 64 → 10 |
| **训练轮数** | 20 Epochs |
| **准确率** | **98%+** |
| **技术栈** | NumPy | Python |

#### 🛠️ 实验内容

- ✅ 实现 `FullyConnectedLayer`（全连接层）
- ✅ 实现 `ReLULayer`（ReLU 激活层）
- ✅ 实现 `SoftmaxLossLayer`（Softmax 损失层）
- ✅ 前向传播计算
- ✅ 反向传播梯度计算
- ✅ 参数更新优化

#### 📁 目录结构

```
exp_2_1_mnist_mlp/
├── main_exp_2_1.py          # 🔧 主程序入口
├── stu_upload/              # 📝 学生需完成的代码
│   ├── layers_1.py          # 🔲 网络层实现
│   ├── mnist_mlp_cpu.py     # 🔲 MLP 模型实现
│   └── __init__.py
├── mnist_data/              # 📊 MNIST 数据集
├── logs/                    # 📄 训练日志
└── *.npz                    # 💾 训练好的模型参数
```

#### 🚀 运行方式

```bash
# 进入实验目录
cd exp_2_1_mnist_mlp

# 运行实验
python main_exp_2_1.py
```

#### 📊 实验结果

```
四层网络结构 (256-128-64)
├─ 训练集准确率: 99.5%
├─ 测试集准确率: 98.2%
└─ 训练时长: ~15 分钟 (CPU)
```

#### 🔧 环境要求

| 依赖 | 最低版本 |
|------|----------|
| Python | 3.7+ |
| NumPy | 1.19+ |

```bash
# 创建虚拟环境（推荐）
python -m venv venv
source venv/bin/activate  # Linux/Mac
# 或
venv\Scripts\activate     # Windows

# 安装依赖
pip install numpy
```

</details>

---

## 📄 许可证

本项目采用 [MIT 许可证](https://opensource.org/licenses/MIT)。

