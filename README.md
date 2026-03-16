<div align="center">

# 🧠 智能计算课程实验
### Intelligent Computing Course Experiments

[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/airprofly/IntelligentCompute) [![Star](https://img.shields.io/github/stars/airprofly/IntelligentCompute?style=social)](https://github.com/airprofly/IntelligentCompute/stargazers) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/) [![NumPy](https://img.shields.io/badge/NumPy-1.19+-orange.svg)](https://numpy.org/)

深度学习基础 · 神经网络设计 · MNIST分类 · 从零实现

</div>

---

## 📖 项目简介

> 本仓库包含智能计算课程的实验代码与作业答案，涵盖深度学习基础、神经网络设计与实现等内容。所有实验均使用 **NumPy 从零实现**，旨在帮助深入理解神经网络的底层原理，同时提供完整的作业解答供学习参考。

---

## 📦 实验模块

本课程项目包含以下实验模块：

| 实验模块 | 简介 | 状态 | README |
|---------|------|------|--------|
| **实验 2.1** | 基于 4 层 MLP 的 MNIST 手写数字识别，准确率 98%+ | ✅ 已完成 | [查看详情](./exp_2_1_mnist_mlp/README.md) |
| **实验 2.2** | 基于 DLP 深度学习平台的 MNIST 分类实现，使用 He 初始化和梯度裁剪优化 | ✅ 已完成 | [查看详情](./expr2_2/) |

<details>
<summary><b>🔮 未来计划</b></summary>

- 🚧 实验 3.1：卷积神经网络（CNN）实现与图像分类
- 🚧 实验 3.2：循环神经网络（RNN）与序列建模
- 🚧 实验 4.0：注意力机制与 Transformer
- 📅 更多实验持续更新中...

</details>

---

## 📚 作业答案

本仓库包含智能计算课程第 2-7 章的作业答案详解，涵盖多层感知机、卷积神经网络、网络结构设计、计算图模式、深度学习处理器和数值表示等核心知识点。

| 主题 | 简介 | README |
|------|------|--------|
| **作业答案** | 第 2-7 章深度学习理论作业详解与推导过程 | [查看详情](./homeWork/README.md) |

---

## 📁 项目结构

<details>
<summary><b>查看目录结构</b></summary>

```text
IntelligentCompute/
├── exp_2_1_mnist_mlp/          # 🔧 实验2.1: MLP实现MNIST分类
├── expr2_2/                    # 🔧 实验2.2: DLP平台实现
├── homeWork/                   # 📚 作业答案目录
├── mnist_data/                 # 💾 MNIST数据集
├── .gitignore                  # 🚫 Git忽略文件配置
└── README.md                   # 📄 项目说明文档
```

</details>

---

## 🛠️ 技术栈

| 技术 | 版本/说明 |
|------|----------|
| **Python** | 3.7+ |
| **NumPy** | 1.19+ - 用于数值计算和矩阵运算 |
| **DLP Platform** | 深度学习实验平台（实验2.2） |

---

## 🔧 环境配置

### 前置要求

- Python 3.7 或更高版本
- NumPy 1.19 或更高版本
- （可选）DLP 深度学习实验平台

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
# 实验 2.1: MLP 实现
cd exp_2_1_mnist_mlp
python main_exp_2_1.py

# 实验 2.2: DLP 平台实现
cd expr2_2
python main_exp_2_2.py
```

> 💡 **提示**：每个实验模块都有独立的 README，包含详细的实现说明、运行方法和核心代码。请点击上方的"查看详情"链接查看完整文档。

### 3. 查看作业答案

```bash
# 查看特定章节答案
cat homeWork/chapter2.md
cat homeWork/chapter3.md
# 或在 Markdown 阅读器中打开以获得更好的阅读体验
```

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

平台应用篇
└── 实验 2.2：DLP 平台实现
    ├── He 初始化方法
    ├── 梯度裁剪技术
    ├── 数据预处理
    └── 模型加载与推理

理论巩固篇
└── 作业答案（第2-7章）
    ├── 第2章：多层感知机原理
    ├── 第3章：经典 CNN 架构
    ├── 第4章：网络结构设计
    ├── 第5章：计算图模式
    ├── 第6章：深度学习硬件
    └── 第7章：数值表示方法
```

---

## 📝 课程目标

通过本课程实验与作业，你将掌握：

- ✅ 神经网络的数学原理（矩阵运算、链式法则）
- ✅ 前向传播和反向传播的实现细节
- ✅ 参数梯度的计算和更新方法
- ✅ 深度学习框架（如 PyTorch、TensorFlow）背后的工作机制
- ✅ 经典数据集（MNIST、CIFAR-10 等）的处理方式
- ✅ 深度学习平台（DLP）的使用方法
- ✅ CNN 架构设计与参数计算
- ✅ 训练技巧与优化方法

---

## 🔗 相关资源

- [MNIST 数据集官网](http://yann.lecun.com/exdb/mnist/)
- [NumPy 官方文档](https://numpy.org/doc/)
- [深度学习课程推荐](https://www.deeplearning.ai/)

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request 来改进本项目！

---

## 📄 许可证

本项目采用 [MIT 许可证](https://opensource.org/licenses/MIT)。

---

<div align="center">

**智能计算课程实验项目**

Made with ❤️ by [IntelligentCompute Team](https://github.com/airprofly/IntelligentCompute)

</div>
