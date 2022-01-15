"""

使用 Plotly 模拟掷骰子


这里将使用 Python 包 Plotly 来生成交互式图表。需要创建在浏览器中显示的图表时，Plotly 很有用，因为它生成
的图表将自动缩放以适合观看者的屏幕。Plotly 生成的图表还是交互式的：用户将鼠标指向特定元素时，将突出显示有关
该元素的信息。

在这个项目中，将对掷骰子的结果进行分析。抛掷一个 6 面的常规骰子时，可能出现的结果为 1～6 点，且出现每种结果
的可能性相同。然而，如果同时掷两个骰子，某些点数出现的可能性将比其他点数大。为确定哪些点数出现的可能性最大，
将生成一个表示掷骰子结果的数据集，并根据结果绘制一个图形。

在数学领域，掷骰子常被用来解释各种数据分析类型，而它在赌场和其他博弈场景中也有实际应用，在游戏《大富翁》以及
众多角色扮演游戏中亦如此。



1、安装 Plotly

要安装 Plotly，可像之前安装 Matplotlib 那样使用 pip：

python -m pip install --user plotly

在之前安装 Matplotlib 时，如果使用了 python3 之类的命令，这里也要使用同样的命令：

python3 -m pip install --user plotly

要了解使用 Plotly 可创建什么样的图表，请在其官方网站查看图表类型画廊。每个示例都包含源代码，让你知道这些图表
是如何生成的。



2、创建 Die 类

为模拟掷一个骰子的情况，创建下面的类：

from random import randint

class Die:
    \"""表示一个骰子的类。\"""

❶    def __init__(self, num_sides=6):
        \"""骰子默认为6面。\"""
        self.num_sides = num_sides

    def roll(self):
        \"""返回一个位于1和骰子面数之间的随机值。\"""
❷        return randint(1, self.num_sides)

方法 __init__() 接受一个可选参数。创建这个类的实例时，如果没有指定任何实参，面数默认为 6；如果指定了实参，
这个值将用于设置骰子的面数（见❶）。骰子是根据面数命名的，6 面的骰子名为 D6，8面的骰子名为 D8，依此类推。

方法 roll() 使用函数 randint() 来返回一个 1 和面数之间的随机数（见❷）。这个函数可能返回起始值 1、终止
值 num_sides 或这两个值之间的任何整数。



3、掷骰子

使用这个类来创建图表前，先来掷 D6，将结果打印出来，并确认结果是合理的：

from die import Die

# 创建一个D6。
❶ die = Die()

# 掷几次骰子并将结果存储在一个列表中。
results = []
❷ for roll_num in range(100):
    result = die.roll()
    results.append(result)

print(results)

在❶处，创建一个 Die 实例，其面数为默认值 6。在❷处，掷骰子 100 次，并将每次的结果都存储在列表 results
中。下面是一个示例结果集：

[4, 6, 5, 6, 1, 5, 6, 3, 5, 3, 5, 3, 2, 2, 1, 3, 1, 5, 3, 6, 3, 6, 5,
 1, 1, 4, 2, 3, 6, 4, 2, 6, 4, 1, 3, 2, 5, 6, 3, 6, 2, 1, 1, 3, 4, 1,
 3, 5, 1, 4, 5, 5, 2, 3, 3, 1, 2, 3, 5, 6, 2, 5, 6, 1, 3, 2, 1, 1, 1,
 5, 5, 2, 2, 6, 4, 1, 4, 5, 1, 1, 1, 4, 5, 3, 3, 1, 3, 5, 4, 5, 6, 5,
 1, 5, 1, 2]

通过快速浏览这些结果可知，Die 类似乎没有问题。见到了值 1 和 6，表明返回了最大和最小的可能值；没有见到 0
或 7，表明结果都在正确的范围内；还看到了 1～6 的所有数字，表明所有可能的结果都出现了。下面来确定各个点数
都出现了多少次。



4、分析结果

为分析掷一个 D6 的结果，计算每个点数出现的次数：

from die import Die

# 创建一个D6。
die = Die()

# 掷几次骰子并将结果存储在一个列表中。
results = []
❶ for roll_num in range(1000):
    result = die.roll()
    results.append(result)

# 分析结果。
frequencies = []
❷ for value in range(1, die.num_sides+1):
❸    frequency = results.count(value)
❹    frequencies.append(frequency)

print(frequencies)

由于将使用 Plotly 来分析，而不是将结果打印出来，因此可将模拟掷骰子的次数增加到 1000（见❶）。为分析结果，
这里创建空列表 frequencies，用于存储每种点数出现的次数。在❷处，遍历可能的点数（这里为 1～6），计算每种
点数在 results 中出现了多少次（见❸），并将这个值附加到列表 frequencies 的末尾（见 ❹）。接下来，在可
视化之前将这个列表打印出来：

[155, 167, 168, 170, 159, 181]

结果看起来是合理的：有 6 个值，对应掷 D6 时可能出现的每个点数；另外，没有任何点数出现的频率比其他点数高很
多。下面来可视化这些结果。



5、绘制直方图

有了频率列表，就可以绘制一个表示结果的直方图了。直方图是一种条形图，指出了各种结果出现的频率。创建这种直方
图的代码如下：

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die
--snip--

# 分析结果。
frequencies = []
for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化。
❶ x_values = list(range(1, die.num_sides+1))
❷ data = [Bar(x=x_values, y=frequencies)]

❸ x_axis_config = {'title': '结果'}
y_axis_config = {'title': '结果的频率'}
❹ my_layout = Layout(title='掷一个D6 1000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
❺ offline.plot({'data': data, 'layout': my_layout}, filename='d6.html')

为创建直方图，需要为每个可能出现的点数生成一个条形。这里将可能出现的点数（1 到骰子的面数）存储在一个名为
x_values 的列表中（见❶）。Plotly 不能直接接受函数 range() 的结果，因此需要使用函数 list() 将其转换
为列表。Plotly 类 Bar() 表示用于绘制条形图的数据集（见❷），需要一个存储 x 值的列表和一个存储 y 值的列
表。这个类必须放在方括号内，因为数据集可能包含多个元素。

每个坐标轴都能以不同的方式进行配置，而每个配置选项都是一个字典元素。这里只设置了坐标轴标签（见❸）。类 Lay-
out() 返回一个指定图表布局和配置的对象（见❹）。这里设置了图表名称，并传入了 x 轴和 y 轴的配置字典。

为生成图表，这里调用了函数 offline.plot()（见❺）。这个函数需要一个包含数据和布局对象的字典，还接受一个
文件名，指定要将图表保存到哪里。这里将输出存储到文件 d6.html。

运行程序时，可能打开浏览器并显示文件 d6.html。如果没有自动显示 d6.html，可在任意 Web 浏览器中新建一个
标签页， 再在其中打开文件 d6.html（它位于 die_visual.py 所在的文件夹中）。

注意，Plotly 让这个图表具有交互性：如果将鼠标指向其中的任意条形，就能看到与之相关联的数据。在同一个图表中
绘制多个数据集时，这项功能特别有用。另外，注意到右上角有一些图标，让你能够平移和缩放图表以及将其保存为图像。



6、同时掷两个骰子

同时掷两个骰子时，得到的点数更多，结果分布情况也不同。下面来修改前面的代码，创建两个 D6 以模拟同时掷两个
骰子的情况。每次掷两个骰子时，都将两个骰子的点数相加，并将结果存储在 results 中。请复制 die_visual
.py 并将其保存为 dice_visual.py，再做如下修改：

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建两个D6。
die_1 = Die()
die_2 = Die()

# 掷几次骰子并将结果存储在一个列表中。
results = []
for roll_num in range(1000):
❶    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果。
frequencies = []
❷ max_result = die_1.num_sides + die_2.num_sides
❸ for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

# 对结果进行可视化。
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

❹ x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
my_layout = Layout(title='掷两个D6 1000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')

创建两个 Die 实例后，掷骰子多次，并计算每次的总点数（见❶）。可能出现的最大点数为两个骰子的最大可能点数之
和（12），这个值存储在 max_result 中（见❷）。可能出现的最小总点数为两个骰子的最小可能点数之和（2）。
分析结果时，计算 2 到 max_result 的各种点数出现的次数（见❸）。（这里原本可以使用 range(2, 13)，但
这只适用于两个 D6。模拟现实世界的情形时，最好编写可轻松模拟各种情形的代码。前面的代码能够模拟掷任意两个
骰子的情形，不管这些骰子有多少面。）

创建图表时，在字典 x_axis_config 中使用了 dtick 键（见❹）。这项设置指定了 x 轴显示的刻度间距。这里
绘制的直方图包含的条形更多，Plotly 默认只显示某些刻度值，而设置 'dtick': 1 让 Plotly 显示每个刻度值。
另外，这里还修改了图表名称及输出文件名。

运行这些代码后，你将看到生成的图表。这个图表显示了掷两个 D6 时得到的大致结果。如你所见，总点数为 2 或 12
的可能性最小，而总点数为 7 的可能性最大。这是因为在下面 6 种情况下得到的总点数都为 7：1 和 6、2 和 5、
3 和 4、4 和 3、5 和 2 以及 6 和 1。



7、同时掷两个面数不同的骰子

下面来创建一个 6 面骰子和一个 10 面骰子，看看同时掷这两个骰子 50 000 次的结果如何：

from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

# 创建一个D6和一个D10。
die_1 = Die()
❶ die_2 = Die(10)

# 掷几次骰子并将结果存储在一个列表中。
results = []
for roll_num in range(50_000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

# 分析结果。
--snip--

# 对结果进行可视化。
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': '结果', 'dtick': 1}
y_axis_config = {'title': '结果的频率'}
❷ my_layout = Layout(title='掷一个D6和一个D10 50000次的结果',
                   xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')

为创建 D10，在创建第二个 Die 实例时传递了实参 10（见❶）；修改了第一个循环，以模拟掷骰子 50 000 而不是
1000 次；还修改了图表名称和输出文件名（见❷）。

最终的图表显示，可能性最大的点数不止一个，而是有 5 个。这是因为导致出现最小点数和最大点数的组合都只有一种
（1 和 1 以及 6 和 10），但面数较小的骰子限制了得到中间点数的组合数：得到总点数 7、8、9、10 和 11 的
组合数都是 6 种。因此，这些总点数是最常见的结果，它们出现的可能性相同。

通过使用 Plotly 模拟掷骰子的结果，能够非常自由地探索这种现象。只需几分钟，就可模拟掷各种骰子很多次。

"""