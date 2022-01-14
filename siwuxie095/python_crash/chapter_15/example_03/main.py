"""

绘制简单的折线图


下面使用 Matplotlib 绘制一个简单的折线图，再对其进行定制，以实现信息更丰富的数据可视化效果。这里将使用平方数序列
1、4、 9、16 和 25 来绘制这个图表。

只需提供如下的数，Matplotlib 将完成其他工作：

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
❶ fig, ax = plt.subplots()
ax.plot(squares)
plt.show()




首先导入模块 pyplot，并为其指定别名 plt，以免反复输入 pyplot（在线示例大多这样做，这里也不例外）。模块 pyplot
包含很多用于生成图表的函数。

这里创建了一个名为 squares 的列表，在其中存储要用来制作图表的数据。然后，采取了另一种常见的 Matplotlib 做法 ——
调用函数 subplots()（见❶）。这个函数可在一张图片中绘制一个或多个图表。变量 fig 表示整张图片。变量 ax 表示图片
中的各个图表，大多数情况下要使用它。

接下来调用方法 plot()，它尝试根据给定的数据以有意义的方式绘制图表。函数 plt.show() 打开 Matplotlib 查看器并
显示绘制的图表。在查看器中，你可缩放和导航图形，还可单击磁盘图标将图表保存起来。



1、修改标签文字和线条粗细

上面生成的图形表明数是越来越大的，但标签文字太小、线条 太细，难以看清楚。所幸 Matplotlib 让你能够调整可视化的各个
方面。

下面通过一些定制来改善这个图表的可读性，如下所示：

import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
❶ ax.plot(squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签。
❷ ax.set_title("平方数", fontsize=24)
❸ ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小。
❹ ax.tick_params(axis='both', labelsize=14)

plt.show()

参数 linewidth（见❶）决定了 plot() 绘制的线条粗细。方法 set_title()（见❷）给图表指定标题。在上述代码中，出现
多次的参数 fontsize 指定图表中各种文字的大小。

方法 set_xlabel() 和 set_ylabel() 让你能够为每条轴设置标题（见❸）。方法 tick_params() 设置刻度的样式（见❹），
其中指定的实参将影响轴和轴上的刻度（axes='both'），并将刻度标记的字号设置为 14（labelsize=14）。

最终的图表阅读起来容易得多：标签文字更大，线条也更粗了。通常，需要尝试不同的值，才能确定什么样的设置生成的图表最合适。



2、校正图形

图形更容易看清后，发现没有正确地绘制数据：折线图的终点指出 4.0 的平方为 25！下面来修复这个问题。

向 plot() 提供一系列数时，它假设第一个数据点对应的 x 坐标值为 0，但这里第一个点对应的 x 值为 1。为改变这种默认
行为，可向 plot() 同时提供输入值和输出值：

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# 设置图表标题并给坐标轴加上标签。
--snip--

现在 plot() 将正确地绘制数据，因为同时提供了输入值和输出值，plot() 无须对输出值的生成方式做出假设。最终的图形是
正确的。

使用 plot() 时可指定各种实参，还可使用众多函数对图形进行定制。后续处理更有趣的数据集时，将继续探索这些定制函数。



3、使用内置样式

Matplotlib 提供了很多已经定义好的样式，它们使用的背景色、网格线、线条粗细、字体、字号等设置很不错，让你无须做太多
定制就可生成引人瞩目的可视化效果。要获悉在你的系统中可使用哪些样式，可在终端会话中执行如下命令：

>>> import matplotlib.pyplot as plt
>>> plt.style.available
['seaborn-dark', 'seaborn-darkgrid', 'seaborn-ticks', 'fivethirtyeight',
--snip--

要使用这些样式，可在生成图表的代码前添加如下代码行：

import matplotlib.pyplot as plt

input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
--snip--

可供使用的内置样式有很多，请尝试使用它们，找出你喜欢的。



4、使用 scatter() 绘制散点图并设置样式

有时候，绘制散点图并设置各个数据点的样式很有用。例如，你可能想以一种颜色显示较小的值，用另一种颜色显示较大的值。绘制
大型数据集时，还可对每个点都设置同样的样式，再使用不同的样式选项重新绘制某些点以示突出。

要绘制单个点，可使用方法scatter() 。向它传递一对 x 坐标和 y 坐标，它将在指定位置绘制一个点：

import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(2, 4)

plt.show()

下面来设置图表的样式，使其更有趣。这里将添加标题，给坐标轴加上标签，并且确保所有文本都大到能够看清：

import matplotlib.pyplot as plt

plt.style.use('seaborn')
fig, ax = plt.subplots()
❶ ax.scatter(2, 4, s=200)

# 设置图表标题并给坐标轴加上标签。
ax.set_title("平方数", fontsize=24)
ax.set_xlabel("值", fontsize=14)
ax.set_ylabel("值的平方", fontsize=14)

# 设置刻度标记的大小。
ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

在❶处，调用 scatter() 并使用参数 s 设置绘制图形时使用的点的尺寸。如果此时运行 scatter_squares.py，将在图表
中央看到一个点。



5、使用 scatter() 绘制一系列点

要绘制一系列的点，可向 scatter() 传递两个分别包含 x 值和 y 值的列表，如下所示：

import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)

# 设置图表标题并给坐标轴加上标签。
--snip--

列表 x_values 包含要计算平方值的数，列表 y_values 包含前述数的平方值。将这些列表传递给 scatter() 时，Mat-
plotlib 依次从每个列表中读取一个值来绘制一个点。要绘制的点的坐标分别为 (1, 1)、(2, 4)、(3, 9)、(4, 16) 和
(5, 25)。



6、自动计算数据

手工计算列表要包含的值可能效率低下，需要绘制的点很多时尤其如此。其实不必手工计算包含点坐标的列表，可以用 Python
循环来完成。

下面是绘制 1000 个点的代码：

import matplotlib.pyplot as plt

❶ x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
❷ ax.scatter(x_values, y_values, s=10)

# 设置图表标题并给坐标轴加上标签。
--snip--

# 设置每个坐标轴的取值范围。
❸ ax.axis([0, 1100, 0, 1100000])

plt.show()

首先创建了一个包含 x 值的列表，其中包含数 1～1000（见❶）。接下来，是一个生成 y 值的列表解析，它遍历值（for x
in x_values），计算其平方值（x**2），并将结果存储到列表 y_values 中。然后，将输入列表和输出列表传递给 sca-
tter()（见❷）。这个数据集较大，因此将点设置得较小。

在❸处，使用方法 axis() 指定了每个坐标轴的取值范围。方法 axis() 要求提供4个值：x 和 y 坐标轴的最小值和最大值。
这里将 x 坐标轴的取值范围设置为 0～1100，并将 y 坐标轴的取值范围设置为 0～1 100 000。



7、自定义颜色

要修改数据点的颜色，可向 scatter() 传递参数 c，并将其设置为要使用的颜色的名称（放在引号内），如下所示：

ax.scatter(x_values, y_values, c='red', s=10)

还可使用 RGB 颜色模式自定义颜色。要指定自定义颜色，可传递参数 c，并将其设置为一个元组，其中包含三个 0～1 的小数
值，分别表示红色、绿色和蓝色的分量。例如，下面的代码行创建一个由淡绿色点组成的散点图：

ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

值越接近 0，指定的颜色越深；值越接近 1，指定的颜色越浅。



8、使用颜色映射

颜色映射（colormap）是一系列颜色，从起始颜色渐变到结束颜色。在可视化中，颜色映射用于突出数据的规律。例如，你可能
用较浅的颜色来显示较小的值，并使用较深的颜色来显示较大的值。

模块 pyplot 内置了一组颜色映射。要使用这些颜色映射，需要告诉 pyplot 该如何设置数据集中每个点的颜色。下面演示了
如何根据每个点的 y 值来设置其颜色：

import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# 设置图表标题并给坐标轴加上标签。
--snip--

这里将参数 c 设置成了一个 y 值列表，并使用参数 cmap 告诉 pyplot 使用哪个颜色映射。这些代码将 y 值较小的点显示
为浅蓝色，并将 y 值较大的点显示为深蓝色。

注意：要了解 pyplot 中所有的颜色映射，请访问 Matplotlib 网站主页，单击 Examples，向下滚动到 Color，再单击
Colormaps reference。



9、自动保存图表

要让程序自动将图表保存到文件中，可将调用 plt.show() 替换为调用 plt.savefig()：

plt.savefig('squares_plot.png', bbox_inches='tight')

第一个实参指定要以什么文件名保存图表，这个文件将存储到 scatter_squares.py 所在的目录。第二个实参指定将图表多余
的空白区域裁剪掉。如果要保留图表周围多余的空白区域，只需省略这个实参即可。

注意：plt.show() 和 plt.savefig() 不能同时调用。

"""