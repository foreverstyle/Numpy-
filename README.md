# Numpy_learning
练习python第三方库Numpy

# 学习网站

[莫烦Python](https://mofanpy.com/tutorials/data-manipulation/numpy/why)

# 为什么用 Numpy

1. 需要批量处理数据的时候
2. 机器学习，人工智能这些需要进行海量数据运算处理的地方
3. 写游戏里面的物体运行逻辑时，经常涉及到矩阵、向量运算
4. 机器人模拟环境，背后的环境反馈信息，全是靠批量数据算出来的
5. 任何需要做统计的时候（爬虫爬完了信息后）
6. 画图表之前，要对数据做一轮批量处理

# Numpy 基本概念

1. Numpy 是 Python 语言的一个第三方库，支持高效的矢量化数组运算，可以用来存储和处理大型数据集。
2. Numpy 是一个运行速度非常快的库，它提供了大量的数学函数库，可以用来进行线性代数、傅里叶变换、随机数生成、统计运算等。
3. Numpy 数组的维度可以是任意的，可以是 1 维、2 维、3 维甚至更高维。
4. Numpy 数组的元素类型可以是任意的，可以是整数、浮点数、复数、字符串等。
5. Numpy 数组的内存布局可以是 C 风格的 row-major 或 C 风格的 column-major。

# Numpy 和 Python List 的差别

Numpy的核心优势：运算快。用专业的语言描述的话，Numpy 喜欢用电脑内存中连续的一块物理地址存储数据，因为都是连号的嘛，找到前后的号，不用跑很远， 非常迅速。而 Python 的 List 并不是连续存储的，它的数据是分散在不同的物理空间，在批量计算的时候，连号的肯定比不连号的算起来更快。

Numpy的缺点：占用内存大。Numpy 数组的元素类型可以是任意的，可以是整数、浮点数、复数、字符串等，但占用的内存空间是固定的，这就意味着，如果数据类型比较多，比如有 100 种，那么 Numpy 数组的总内存空间就得是 100 倍于 Python List 的。
