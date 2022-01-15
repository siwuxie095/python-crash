"""

CSV 文件格式


要在文本文件中存储数据，一个简单方式是将数据作为一系列以逗号分隔的值（comma-separated values）写入文件。这样的
文件称为 CSV 文件。例如，下面是一行 CSV 格式的天气数据：

"USW00025333","SITKA AIRPORT, AK US","2018-01-01","0.45",,"48","38"

这是阿拉斯加州锡特卡 2018 年 1 月 1 日的天气数据，其中包含当天的最高温度和最低温度，还有众多其他的数据。CSV 文件
对人来说阅读起来比较麻烦，但程序可轻松提取并处理其中的值，有助于加快数据分析过程。

这里将首先处理少量 CSV 格式的锡特卡天气数据。请将文件 sitka_weather_07-2018_simple.csv 复制到当前的文件夹中。

注意：该项目使用的天气数据来自美国国家海洋与大气管理局（National Oceanic and Atmospheric Administration，
NOAA）。



1、分析 CSV 文件头

csv 模块包含在 Python 标准库中，可用于分析 CSV 文件中的数据行，使得能够快速提取感兴趣的值。先来查看这个文件的第
一行，其中的一系列文件头指出了后续各行包含的是什么样的信息：

import csv

filename = 'data/sitka_weather_07-2018_simple.csv'
❶ with open(filename) as f:
❷    reader = csv.reader(f)
❸    header_row = next(reader)
    print(header_row)

导入模块 csv 后，将要使用的文件的名称赋给 filename。接下来，打开这个文件，并将返回的文件对象赋给 f（见❶）。然后，
调用 csv.reader() 并将前面存储的文件对象作为实参传递给它，从而创建一个与该文件相关联的阅读器对象（见❷）。这个阅
读器对象被赋给了 reader。

模块 csv 包含函数 next()，调用它并传入阅读器对象时，它将返回文件中的下一行。在上述代码中，只调用了 next() 一次，
因此得到的是文件的第一行，其中包含文件头（见❸）。将返回的数据存储到 header_row 中。如你所见，header_row 包含
与天气相关的文件头，指出了每行都包含哪些数据：

['STATION', 'NAME', 'DATE', 'PRCP', 'TAVG', 'TMAX', 'TMIN']

reader 处理文件中以逗号分隔的第一行数据，并将每项数据都作为一个元素存储在列表中。文件头 STATION 表示记录数据的
气象站的编码。这个文件头的位置表明，每行的第一个值都是气象站编码。文件头 NAME 指出每行的第二个值都是记录数据的气
象站的名称。其他文件头则指出记录了哪些信息。当前，最关心的是日期（DATE）、最高温度（TMAX）和最低温度（TMIN）。
这是一个简单的数据集，只包含降水量以及与温度相关的数据。你自己下载天气数据时，可选择涵盖众多测量值，如风速、风向以
及详细的降水量数据。



2、打印文件头及其位置

为了让文件头数据更容易理解，将列表中的每个文件头及其位置打印出来：

--snip--
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

❶ for index, column_header in enumerate(header_row):
    print(index, column_header)

在循环中，对列表调用了 enumerate()（见❶）来获取每个元素的索引及其值。

注意：这里删除了代码行 print(header_row) ，转而显示这个更详细的版本。

输出如下，指出了每个文件头的索引：

0 STATION
1 NAME
2 DATE
3 PRCP
4 TAVG
5 TMAX
6 TMIN

从中可知，日期和最高温度分别存储在第三列和第六列。为研究这些数据，下面将处理 sitka_weather_07-2018_simple.
csv 中的每行数据，并提取其中索引为 2 和 5 的值。



3、提取并读取数据

知道需要哪些列中的数据后，来读取一些数据。首先，读取每天的最高温度：

--snip--
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取最高温度。
❶    highs = []
❷    for row in reader:
❸        high = int(row[5])
        highs.append(high)

print(highs)

创建一个名为 highs 的空列表（见❶），再遍历文件中余下的各行（见❷）。阅读器对象从其停留的地方继续往下读取 CSV 文件，
每次都自动返回当前所处位置的下一行。由于已经读取了文件头行，这个循环将从第二行开始 —— 从这行开始包含的是实际数据。
每次执行循环时，都将索引 5 处（TMAX 列）的数据附加到 highs 末尾（见❸）。在文件中，这项数据是以字符串格式存储的，
因此在附加到 highs 末尾前，使用函数 int() 将其转换为数值格式，以便使用。

highs 现在存储的数据如下：

[62, 58, 70, 70, 67, 59, 58, 62, 66, 59, 56, 63, 65, 58, 56, 59, 64, 60, 60, 61, 65, 65, 63,
59, 64, 65, 68, 66, 64, 67, 65]

提取每天的最高温度并将其存储到列表中之后，就可以可视化这些数据了。



4、绘制温度图表

为可视化这些温度数据，首先使用 Matplotlib 创建一个显示每日最高温度的简单图形，如下所示：

import csv

import matplotlib.pyplot as plt

filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取最高温度。
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)

# 根据最高温度绘制图形。
plt.style.use('seaborn')
fig, ax = plt.subplots()
❶ ax.plot(highs, c='red')

# 设置图形的格式。
❷ ax.set_title("2018年7月每日最高温度", fontsize=24)
❸ ax.set_xlabel('', fontsize=16)
ax.set_ylabel("温度 (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

将最高温度列表传给 plot()（见❶），并传递 c='red' 以便将数据点绘制为红色。（这里使用红色显示最高温度，用蓝色显示
最低温度。）接下来，设置了一些其他的格式，如名称和字号（见❷）。鉴于还没有添加日期，因此没有给 x 轴添加标签，但 ax.
set_xlabel() 确实修改了字号，让默认标签更容易看清❸。运行代码，会显示绘制的图表：一个简单的折线图，显示了阿拉斯加
州锡特卡 2018 年 7 月的每日最高温度。



5、模块 datetime

下面在图表中添加日期，使其更有用。在天气数据文件中，第一个日期在第二行：

"USW00025333","SITKA AIRPORT, AK US","2018-07-01","0.25",,"62","50"

读取该数据时，获得的是一个字符串，因此需要想办法将字符串 "2018-7-1" 转换为一个表示相应日期的对象。为创建一个表示
2018 年 7 月 1 日的对象，可使用模块 datetime 中的方法 strptime()。下面在终端会话中看看 strptime() 的工作
原理：

>>> from datetime import datetime
>>> first_date = datetime.strptime('2018-07-01', '%Y-%m-%d')
>>> print(first_date)
2018-07-01 00:00:00

首先导入模块 datetime 中的 datetime 类，再调用方法 strptime()，并将包含所需日期的字符串作为第一个实参。第二
个实参告诉 Python 如何设置日期的格式。在这里，'%Y-' 让 Python 将字符串中第一个连字符前面的部分视为四位的年份，
'%m-' 让 Python 将第二个连字符前面的部分视为表示月份的数，'%d' 让 Python 将字符串的最后一部分视为月份中的一天
（1～31）。

方法 strptime() 可接受各种实参，并根据它们来决定如何解读日期。下表列出了这样的一些实参。

PS：模块 datetime 中设置日期和时间格式的实参。

（1）实参：%A，含义：星期几，如 Monday
（2）实参：%B，含义：月份名，如 January
（3）实参：%m，含义：用数表示的月份（01～12）
（4）实参：%d，含义：用数表示的月份中的一天（01～31）
（5）实参：%Y，含义：四位的年份，如 2019
（6）实参：%y，含义：两位的年份，如 19
（7）实参：%H，含义：24 小时制的小时数（00～23）
（8）实参：%I，含义：12 小时制的小时数（01～12）
（9）实参：%p，含义：am 或 pm
（10）实参：%M，含义：分钟数（00～59）
（11）实参：%S，含义：秒数（00～61）



6、在图表中添加日期

现在，可以通过提取日期和最高温度并将其传递给 plot()，对温度图形进行改进，如下所示：

import csv
from datetime import datetime

import matplotlib.pyplot as plt


filename = 'data/sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取日期和最高温度。
❶    dates, highs = [], []
    for row in reader:
❷        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        dates.append(current_date)
        highs.append(high)

# 根据最高温度绘制图形。
plt.style.use('seaborn')
fig, ax = plt.subplots()
❸ ax.plot(dates, highs, c='red')

# 设置图形的格式。
ax.set_title("2018年7月每日最高温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
❹ fig.autofmt_xdate()
ax.set_ylabel("温度 (F)", fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()

这里创建了两个空列表，用于存储从文件中提取的日期和最高温度（见❶）。然后，将包含日期信息的数据（row[2]）转换为 date-
time 对象（见❷），并将其附加到列表 dates 末尾。在❸处，将日期和最高温度值传递给 plot()。在❹处，调用 fig.autofmt-
_xdate() 来绘制倾斜的日期标签，以免其彼此重叠。



7、涵盖更长的时间

设置好图表后，下面来添加更多的数据，生成一幅更复杂的锡特卡天气图。请将文件 sitka_weather_2018_simple.csv 复制
到当前的文件夹，该文件包含整年的锡特卡天气数据。

现在可创建覆盖整年的天气图了：

--snip--
❶ filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
--snip--
# 设置图形的格式。
❷ ax.set_title("2018年每日最高温度", fontsize=24)
ax.set_xlabel('', fontsize=16)
--snip--

这里修改了文件名，以使用数据文件 sitka_weather_2018_simple.csv（见❶），还修改了图表的标题，以反映其内容的变化
（见❷）。



8、再绘制一个数据系列

虽然改进后的图表已经显示了丰富的数据，但是还能再添加最低温度数据，使其更有用。为此，需要从数据文件中提取最低温度，并
将它们添加到图表中，如下所示：

--snip--
filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取日期、最高温度和最低温度。
❶    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
❷        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

# 根据最高温度和最低温度绘制图形。
plt.style.use('seaborn')
plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
plt.rcParams['axes.unicode_minus']=False
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red')
❸ ax.plot(dates, lows, c='blue')

# 设置图形的格式。
❹ ax.set_title("2018年每日最高温度和最低温度", fontsize=24)
--snip--

在❶处，添加空列表 lows，用于存储最低温度。接下来，从每行的第七列（row[6]）提取最低温度并存储（见❷）。在❸处，添加
调用 plot() 的代码，以使用蓝色绘制最低温度。最后，修改标题（见❹）。



9、给图表区域着色

添加两个数据系列后，就可以知道每天的温度范围了。下面来给这个图表做最后的修饰，通过着色来呈现每天的温度范围。为此，将
使用方法 fill_between()。它接受一个 x 值系列和两个 y 值系列，并填充两个 y 值系列之间的空间：

# 根据最高温度和最低温度绘制图形。
plt.style.use('seaborn')
fig, ax = plt.subplots()
❶ ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
❷ ax.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
--snip--

❶处的实参 alpha 指定颜色的透明度。alpha 值为 0 表示完全透明，为1（默认设置）表示完全不透明。通过将 alpha 设置
为 0.5，可让红色和蓝色折线的颜色看起来更浅。

在❷处，向 fill_between() 传递一个 x 值系列（列表dates），以及两个 y 值系列（highs 和 lows）。实参 facecolor
指定填充区域的颜色，还将 alpha 设置成了较小的值 0.1，让填充区域将两个数据系列连接起来的同时不分散观察者的注意力。

着色让两个数据集之间的区域变得更显眼了。



10、错误检查

现在应该能够使用任何地方的天气数据来运行 sitka_highs_lows.py 中的代码，但有些气象站收集的数据种类不同，有些气象
站会偶尔出现故障，未能收集部分或全部应收集的数据。缺失数据可能引发异常，如果不妥善处理，可能导致程序崩溃。

例如，来看看生成加利福尼亚州死亡谷的温度图时出现的情况。请将文件 death_valley_2018_simple.csv 复制到当前的文件
夹中。

首先通过编写代码来查看这个数据文件包含的文件头：

import csv

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, column_header in enumerate(header_row):
        print(index, column_header)

输出如下：

0 STATION
1 NAME
2 DATE
3 PRCP
4 TMAX
5 TMIN
6 TOBS

与前面一样，日期也在索引 2 处，但最高温度和最低温度分别在索引 4 和索引 5 处，因此需要修改代码中的索引，以反映这一点。
另外，这个气象站没有记录平均温度，而记录了 TOBS，即特定时点的温度。

为演示缺失数据时将出现的状况，故意从这个文件中删除了一项温度数据。下面来修改 sitka_highs_lows.py，使用前面所说的
索引来生成死亡谷的天气图，看看将出现什么状况：

--snip--
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 从文件中获取日期、最高温度和最低温度。
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
❶        high = int(row[4])
        low = int(row[5])
        dates.append(current_date)
--snip--

在❶处，修改索引，使其对应于这个文件中 TMAX 和 TMIN 的位置。

运行这个程序时出现了错误，如下述输出的最后一行所示：

Traceback (most recent call last):
  File "death_valley_highs_lows.py", line 15, in <module>
    high = int(row[4])
ValueError: invalid literal for int() with base 10: ''

该 traceback 指出，Python 无法处理其中一天的最高温度，因为无法将空字符串（''）转换为整数。只要看一下文件 death-
_valley_2018_simple.csv，就知道缺失了哪项数据，但这里不这样做，而是直接对缺失数据的情形进行处理。

为此，在从 CSV 文件中读取值时执行错误检查代码，对可能出现的异常进行处理，如下所示：

--snip--
filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    --snip--
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
❶        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
❷            print(f"Missing data for {current_date}")
❸        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

# 根据最高温度和最低温度绘制图形。
--snip--

# 设置图形的格式。
❹ title = "2018年每日最高温度最和低温度\n美国加利福尼亚州死亡谷"
ax.set_title(title, fontsize=20)
ax.set_xlabel('', fontsize=16)
--snip--

对于每一行，都尝试从中提取日期、最高温度和最低温度（见❶）。只要缺失其中一项数据，Python 就会引发 ValueError 异常，
并这样进行处理：打印一条错误消息，指出缺失数据的日期（见❷）。打印错误消息后，循环将接着处理下一行。如果获取特定日期的
所有数据时没有发生错误，就运行 else 代码块，将数据附加到相应列表的末尾（见❸）。这里绘图时使用的是有关另一个地方的信息，
因此修改标题以指出这个地方。因为标题更长，所以缩小了字号（见❹）。

如果现在运行 death_valley_highs_lows.py，将发现缺失数据的日期只有一个：

Missing data for 2018-02-18 00:00:00

妥善地处理错误后，代码能够生成图形并忽略缺失数据的那天。

将这个图表与锡特卡的图表进行比较可知，总体而言，死亡谷比阿拉斯加东南部暖和，这符合预期。同时，死亡谷沙漠中每天的温差也
更大 —— 从着色区域的高度可以看出这一点。

你使用的很多数据集都可能缺失数据、格式不正确或数据本身不正确。对于这样的情形，可采用对应的工具来处理。在这里，使用了一
个 try-except-else 代码块来处理数据缺失的问题。在有些情况下，需要使用 continue 来跳过一些数据，或者使用 remove()
或 del 将已提取的数据删除。只要能进行精确而有意义的可视化，采用任何管用的方法都是可以的。



11、自己动手下载数据

如果你想自己下载天气数据，可采取如下步骤。

(1) 访问网站 NOAA Climate Data Online。在 Discover Data By 部分， 单击 Search Tool。在下拉列表 Select
a Dataset 中，选择 Daily Summaries。

(2) 选择一个日期范围，在 Search For 下拉列表中 ZIP Codes，输入你感兴趣地区的邮政编码，再单击 Search 按钮。

(3) 在下一个页面中，你将看到指定地区的地图和相关信息。单击地区名下方的 View Full Details 或单击地图再单击 Full
Details。

(4) 向下滚动并单击 Station List，以显示该地区的气象站，再选择一个气象站并单击 Add to Cart。虽然这个网站使用了
购物车图标，但提供的数据是免费的。单击右上角的购物车。


(5) 在 Select the Output 中选择 Custom GHCN-Daily CSV。确认日期范围无误后单击 Continue。

(6) 在下一个页面中，可选择要下载的数据类型。可以只下载一种数据（如气温），也可以下载该气象站提供的所有数据。做出选择
后单击 Continue。

(7) 在最后一个页面，你将看到订单小结。请输入你的电子邮箱地址，再单击 Submit Order。你将收到一封确认邮件，指出收到
了你的订单。几分钟后，你将收到另一封邮件，其中包含用于下载数据的链接。

你下载的数据与这里处理的数据有类似的结构，但包含的文件头可能不同。然而，只要按步骤做，就能对你感兴趣的数据进行可视化。

"""