<div align="center">

# 📚 智能计算课程作业答案
### Intelligent Computing Course Homework Solutions

[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/airprofly/IntelligentCompute) [![Star](https://img.shields.io/github/stars/airprofly/IntelligentCompute?style=social)](https://github.com/airprofly/IntelligentCompute/stargazers) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

深度学习理论 · 网络架构 · 计算图 · 硬件基础

</div>

---

## 📖 简介

本目录包含智能计算课程第 2-7 章的作业答案详解，涵盖多层感知机、卷积神经网络、网络结构设计、计算图模式、深度学习处理器和数值表示等核心知识点。

> 使用说明：点击下方各章节链接查看详细答案解析，或直接查看对应的 Markdown 文件。

---

## 📦 作业答案索引

| 章节 | 主题 | 核心内容 | 文件 |
|------|------|----------|------|
| **第2章** | 多层感知机 | MLP与感知机区别、参数计算、反向传播、过拟合避免、激活函数导数 | [查看答案](./chapter2.md) |
| **第3章** | 卷积神经网络 | AlexNet/VGG/ResNet参数量、IoU与mAP、训练收敛、风格迁移 | [查看答案](./chapter3.md) |
| **第4章** | 网络结构计算 | VGG19池化层输出形状计算 | [查看答案](./chapter4.md) |
| **第5章** | 计算图模式 | 静态图与动态图模式对比分析 | [查看答案](./chapter5.md) |
| **第6章** | 深度学习处理器 | 现代处理器与80年代神经芯片的技术差异 | [查看答案](./chapter6.md) |
| **第7章** | 数值表示 | IEEE 754浮点数换算与表示 | [查看答案](./chapter7.md) |

---

## 📁 目录结构

```text
homeWork/
├── README.md      # 📄 本文件（作业答案索引）
├── chapter2.md    # 📝 第2章：多层感知机
├── chapter3.md    # 📝 第3章：卷积神经网络
├── chapter4.md    # 📝 第4章：网络结构计算
├── chapter5.md    # 📝 第5章：计算图模式
├── chapter6.md    # 📝 第6章：深度学习处理器
├── chapter7.md    # 📝 第7章：数值表示
└── test.md        # 🧪 测试答案
```

---

## 📚 章节内容概要

### 第2章：多层感知机

**核心问题**：
1. 多层感知机和感知机的区别是什么？
2. 如何计算网络的可训练参数数量？
3. 反向传播中梯度和权重如何计算更新？
4. 如何避免过拟合？
5. Sigmoid 和自定义激活函数的导数计算

**知识要点**：
- ✅ 万能逼近定理
- ✅ 链式法则与梯度计算
- ✅ 正则化、Dropout、早停法

### 第3章：卷积神经网络

**核心问题**：
1. AlexNet、VGG19、ResNet152 的参数量计算
2. IoU 与 mAP 的关系
3. 训练收敛、训练精度和测试精度的关系
4. 图像风格迁移的基本过程

**知识要点**：
- ✅ 经典 CNN 架构对比
- ✅ 目标检测评估指标
- ✅ 过拟合与泛化能力
- ✅ 神经风格迁移原理

### 第4章：网络结构计算

**核心问题**：
- VGG19 网络各池化层后的输出形状计算

**知识要点**：
- ✅ 卷积层参数计算
- ✅ 池化层尺寸变化
- ✅ 特征图维度推导

### 第5章：计算图模式

**核心问题**：
- 静态图与动态图模式的对比分析

**知识要点**：
- ✅ TensorFlow 1.x vs PyTorch
- ✅ 性能与灵活性权衡
- ✅ 现代 PyTorch 2.0 与 TensorFlow 2.x 融合趋势

### 第6章：深度学习处理器

**核心问题**：
- 深度学习处理器与 80 年代早期神经网络芯片的区别

**知识要点**：
- ✅ 工艺进步：微米 → 纳米
- ✅ 架构演进：简单前馈 → 支持任意深度网络
- ✅ 软件生态：底层操作 → 完整框架支持
- ✅ 模拟计算复兴：存内计算、光子神经网络

### 第7章：数值表示

**核心问题**：
- IEEE 754 浮点数的二进制转换

**知识要点**：
- ✅ 单精度浮点数格式
- ✅ 规格化数与非规格化数
- ✅ 指数偏移与尾数计算

---

## 🎯 学习建议

### 推荐学习顺序

```text
基础理论
├── 第2章：多层感知机（理解神经网络基础）
└── 第7章：数值表示（理解浮点运算）

网络架构
├── 第3章：卷积神经网络（经典架构）
└── 第4章：网络结构计算（参数与尺寸）

实现与优化
├── 第5章：计算图模式（框架底层原理）
└── 第6章：深度学习处理器（硬件加速）
```

### 配合实验学习

| 章节 | 配合实验 | 学习目标 |
|------|---------|---------|
| 第2章 | 实验 2.1、2.2 | 理解 MLP 原理，实现前向/反向传播 |
| 第3章 | - | 了解经典 CNN 架构，为后续实验做准备 |
| 第5章 | 实验 2.1、2.2 | 理解 NumPy 实现与 PyTorch 的区别 |

---

## 📖 使用说明

### 查看答案

```bash
# 查看特定章节答案
cat homeWork/chapter2.md

# 或在 Markdown 阅读器中打开（推荐）
# - VS Code: 右键 -> 打开预览
# - Typora: 直接打开文件
# - GitHub: 在线渲染查看
```

### 答案格式

每个章节的答案包含：
- ✅ **问题重述**：明确题目要求
- ✅ **详细推导**：关键步骤的数学推导
- ✅ **代码示例**：必要的代码说明
- ✅ **总结归纳**：核心知识点提炼

---

## 🔗 相关资源

- [实验 2.1：MLP 实现](../exp_2_1_mnist_mlp/README.md)
- [实验 2.2：DLP 平台实现](../expr2_2/README.md)
- [CS231n：卷积神经网络](http://cs231n.stanford.edu/)
- [深度学习（花书）](https://www.deeplearningbook.org/)

---

## 📄 许可证

本项目采用 [MIT 许可证](https://opensource.org/licenses/MIT)。

---

<div align="center">

**智能计算课程作业答案**

Made with ❤️ by [IntelligentCompute Team](https://github.com/airprofly/IntelligentCompute)

</div>
