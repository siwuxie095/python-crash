"""

随机漫步


这里将使用 Python 来生成随机漫步数据，再使用 Matplotlib 以引人瞩目的方式将这些数据呈现出来。随机漫步是这样
行走得到的路径：每次行走都是完全随机的、没有明确的方向，结果是由一系列随机决策决定的。你可以将随机漫步看作蚂蚁
在晕头转向的情况下，每次都沿随机的方向前行所经过的路径。

在自然界、物理学、生物学、化学和经济领域，随机漫步都有其实际用途。例如，漂浮在水滴上的花粉因不断受到水分子的挤压
而在水面上移动。水滴中的分子运动是随机的，因此花粉在水面上的运动路径犹如随机漫步。稍后编写的代码将模拟现实世界的
很多情形。



1、创建 RandomWalk 类

为模拟随机漫步，将创建一个名为 RandomWalk 的类，它随机地选择前进方向。这个类需要三个属性：一个是存储随机漫步
次数的变量，其他两个是列表，分别存储随机漫步经过的每个点的 x 坐标和 y 坐标。

RandomWalk 类只包含两个方法：方法 __init___() 和 fill_walk()，后者计算随机漫步经过的所有点。先来看看
__init__()，如下所示：

❶ from random import choice

class RandomWalk:
    \"""一个生成随机漫步数据的类。\"""

❷    def __init__(self, num_points=5000):
        \"""初始化随机漫步的属性。\"""
        self.num_points = num_points

        # 所有随机漫步都始于(0, 0)。
❸        self.x_values = [0]
        self.y_values = [0]

为做出随机决策，将所有可能的选择都存储在一个列表中，并在每次决策时都使用模块 random 中的 choice() 来决定使
用哪种选择（见❶）。接下来，将随机漫步包含的默认点数设置为 5000。这个数大到足以生成有趣的模式，又小到可确保能
够快速地模拟随机漫步（见❷）。然后，在❸处创建两个用于存储 x 值和 y 值的列表，并让每次漫步都从点 (0, 0) 出发。



2、选择方向

这里将使用方法 fill_walk() 来生成漫步包含的点并决定每次漫步的方向，如下所示。请将这个方法添加到 random_-
walk.py 中：

    def fill_walk(self):
        \"""计算随机漫步包含的所有点。\"""

        # 不断漫步，直到列表达到指定的长度。
❶        while len(self.x_values) < self.num_points:

            # 决定前进方向以及沿这个方向前进的距离。
❷            x_direction = choice([1, -1])

            x_distance = choice([0, 1, 2, 3, 4])
❸            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
❹            y_step = y_direction * y_distance

            # 拒绝原地踏步。
❺            if x_step == 0 and y_step == 0:
                continue

            # 计算下一个点的x值和y值。
❻            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

❶处建立了一个循环，它不断运行，直到漫步包含所需的点数。方法 fill_walk() 的主要部分告诉 Python 如何模拟四种
漫步决定：向右走还是向左走？沿指定的方向走多远？向上走还是向下走？沿选定的方向走多远？

使用 choice([1, -1]) 给 x_direction 选择一个值，结果要么是表示向右走的 1，要么是表示向左走的 -1（见❷）。
接下来，choice([0, 1, 2, 3, 4]) 随机地选择一个 0～4 的整数，告诉 Python 沿指定的方向走多远（x_distance）。
通过包含 0，不仅能够同时沿两个轴移动，还能够只沿一个轴移动。

在❸和❹处，将移动方向乘以移动距离，确定沿 x 轴和 y 轴移动的距离。如果 x_step 为正将向右移动，为负将向左移动，
为零将垂直移动；如果 y_step 为正将向上移动，为负将向下移动，为零将水平移动。如果 x_step 和 y_step 都为零，
则意味着原地踏步。这里拒绝这样的情况，接着执行下一次循环（见❺）。

为获取漫步中下一个点的 x 值，将 x_step 与 x_values 中的最后一个值相加（见❻），对 y 值也做相同的处理。获得
下一个点的 x 值和 y 值后，将它们分别附加到列表 x_values 和 y_values 的末尾。



3、绘制随机漫步图

下面的代码将随机漫步的所有点都绘制出来：

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 创建一个RandomWalk实例。
❶ rw = RandomWalk()
rw.fill_walk()

# 将所有的点都绘制出来。
plt.style.use('classic')
fig, ax = plt.subplots()
❷ ax.scatter(rw.x_values, rw.y_values, s=15)
plt.show()

首先导入模块 pyplot 和 RandomWalk 类，再创建一个 RandomWalk 实例并将其存储到 rw 中（见❶），并且调用
fill_walk()。在❷处，将随机漫步包含的 x 值和 y 值传递给 scatter()，并选择合适的点尺寸。运行后会看到包含
5000 个点的随机漫步图。



4、模拟多次随机漫步

每次随机漫步都不同，因此探索可能生成的各种模式很有趣。要在不多次运行程序的情况下使用前面的代码模拟多次随机漫步，
一种办法是将这些代码放在一个 while 循环中，如下所示：

import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步。
while True:
    # 创建一个RandomWalk实例。
    rw = RandomWalk()
    rw.fill_walk()

    # 将所有的点都绘制出来。
    plt.style.use('classic')
    fig, ax = plt.subplots()
    ax.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

这些代码模拟一次随机漫步，在 Matplotlib 查看器中显示结果，再在不关闭查看器的情况下暂停。如果关闭查看器，程
序将询问是否要再模拟一次随机漫步。如果输入 y，可模拟在起点附近进行的随机漫步、大多沿特定方向偏离起点的随机漫
步、漫步点分布不均匀的随机漫步，等等。要结束程序，请输入 n。



5、设置随机漫步图的样式

这里将定制图表，以突出每次漫步的重要特征，并让分散注意力的元素不那么显眼。为此，需要确定要突出的元素，如漫步的
起点、终点和经过的路径。接下来确定要使其不那么显眼的元素，如刻度标记和标签。最终的结果是简单的可视化表示，清楚
地指出了每次漫步经过的路径。


a. 给点着色

这里将使用颜色映射来指出漫步中各点的先后顺序，并删除每个点的黑色轮廓，让其颜色更为明显。为根据漫步中各点的先后
顺序来着色，传递参数 c，并将其设置为一个列表，其中包含各点的先后顺序。这些点是按顺序绘制的，因此给参数 c 指定
的列表只需包含数 0～4999，如下所示：

--snip--
while True:
    # 创建一个RandomWalk实例。
    rw = RandomWalk()
    rw.fill_walk()

    # 将所有的点都绘制出来。
    plt.style.use('classic')
    fig, ax = plt.subplots()
❶    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break

在❶处，使用 range() 生成了一个数字列表，其中包含的数与漫步包含的点数量相同。接下来，将这个列表存储在 point-
_numbers 中，以便后面使用它来设置每个漫步点的颜色。将参数 c 设置为 point_numbers，指定使用颜色映射 Blues，
并传递实参 edgecolors='none' 以删除每个点周围的轮廓。最终的随机漫步图从浅蓝色渐变为深蓝色。


b. 重新绘制起点和终点

除了给随机漫步的各个点着色，以指出其先后顺序外，如果还能呈现随机漫步的起点和终点就好了。为此，可在绘制随机漫步
图后重新绘制起点和终点。这里让起点和终点更大并显示为不同的颜色，以示突出，如下所示：

--snip--
while True:
    --snip--
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors='none', s=15)

    # 突出起点和终点。
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()

    --snip--

为突出起点，使用绿色绘制点 (0, 0)，并使其比其他点大（s=100）。为突出终点，在漫步包含的最后一个 x 值和 y 值
处绘制一个点，将其颜色设置为红色，并将尺寸设置为 100。 务必将这些代码放在调用 plt.show() 的代码前面，确保
在其他点之上绘制起点和终点。

如果现在运行这些代码，将能准确地知道每次随机漫步的起点和终点（如果起点和终点不明显，请调整颜色和大小，直到明显
为止）。


c. 隐藏坐标轴

下面来隐藏这个图表的坐标轴，以免分散观察者对随机漫步路径的注意力。要隐藏坐标轴，可使用如下代码：

--snip--
while True:
    --snip--
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # 隐藏坐标轴。
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()

    --snip--

为修改坐标轴，使用方法 ax.get_xaxis() 和 ax.get_yaxis()（见❶）将每条坐标轴的可见性都设置为 False。随
着对数据可视化的不断学习和实践，你会经常看到这种串接方法的方式。

如果现在运行代码，你将看到一系列图形，但看不到坐标轴。


d. 增加点数

下面来增加点数，以提供更多数据。为此，在创建 RandomWalk 实例时增大 num_points 的值，并在绘图时调整每个点
的大小，如下所示：

--snip--
while True:
    # 创建一个RandomWalk实例。
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # 将所有的点都绘制出来。
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers,
               cmap=plt.cm.Blues, edgecolors='none', s=1)
    --snip--

这个示例模拟了一次包含 50 000 个点的随机漫步（以模拟现实情况），并将每个点的大小都设置为 1。最终的随机漫步图
更稀疏，犹如云朵。如你所见，使用简单的散点图就制作出了一件艺术品！

请尝试修改上述代码，看看将漫步包含的点数增加到多少后，程序的运行速度变得极其缓慢或绘制出的图形变得很难看。


e. 调整尺寸以适合屏幕

图表适合屏幕大小时，更能有效地将数据中的规律呈现出来。为让绘图窗口更适合屏幕大小，可以像下面这样调整 Matplot-
lib 输出的尺寸：

--snip--
while True:
    # 创建一个RandomWalk实例。
    rw = RandomWalk(50_000)
    rw.fill_walk()

    # 将所有的点都绘制出来。
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    --snip--

创建图表时，可传递参数 figsize 以指定生成的图形的尺寸。需要给参数 figsize 指定一个元组，向 Matplotlib
指出绘图窗口的尺寸，单位为英寸 1。

Matplotlib 假定屏幕分辨率为 100 像素/英寸。如果上述代码指定的图表尺寸不合适，可根据需要调整数字。如果知道
当前系统的分辨率，可通过参数 dpi 向 plt.subplots() 传递该分辨率，以有效利用可用的屏幕空间，如下所示：

fig, ax = plt.subplots(figsize=(10, 6), dpi=128)

"""