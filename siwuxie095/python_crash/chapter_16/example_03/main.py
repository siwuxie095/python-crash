"""

制作全球地震散点图：JSON 格式


在这里，你将下载一个数据集，其中记录了一个月内全球发生的所有地震，再制作一幅散点图来展示这些地震的位置和震级。这些
数据是以 JSON 格式存储的，因此要使用模块 json 来处理。

Plotly 提供了根据位置数据绘制地图的工具，适合初学者使用。你将使用它来进行可视化并指出全球的地震分布情况。



1、地震数据

请将文件 eq_data_1_day_m1.json 复制到当前的文件夹中。地震是以里氏震级度量的，而该文件记录了最近 24 小时内全
球发生的所有不低于 1 级的地震。



2、查看 JSON 数据

如果打开文件 eq_data_1_day_m1.json，你将发现其内容密密麻麻，难以阅读：

{"type":"FeatureCollection","metadata":{"generated":1550361461000,...
{"type":"Feature","properties":{"mag":1.2,"place":"11km NNE of Nor...
{"type":"Feature","properties":{"mag":4.3,"place":"69km NNW of Ayn...
{"type":"Feature","properties":{"mag":3.6,"place":"126km SSE of Co...
{"type":"Feature","properties":{"mag":2.1,"place":"21km NNW of Teh...
{"type":"Feature","properties":{"mag":4,"place":"57km SSW of Kakto...
--snip--

这些数据适合机器而不是人来读取。不过可以看到，这个文件包含一些字典，还有一些让人感兴趣的信息，如震级和位置。

模块 json 提供了各种探索和处理 JSON 数据的工具，其中一些有助于重新设置这个文件的格式，使得能够更清楚地查看原始
数据，继而决定如何以编程的方式来处理。

这里先加载这些数据并将其以易于阅读的方式显示出来。这个数据文件很长，因此不打印出来，而是将数据写入另一个文件，再
打开该文件并轻松地在数据中导航：

import json

# 探索数据的结构。
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
❶    all_eq_data = json.load(f)

❷ readable_file = 'data/readable_eq_data.json'
with open(readable_file, 'w') as f:
❸    json.dump(all_eq_data, f, indent=4)

首先导入模块 json，以便恰当地加载文件中的数据，并将其存储到 all_eq_data 中（见❶）。函数 json.load() 将数据
转换为 Python 能够处理的格式，这里是一个庞大的字典。在❷处，创建一个文件，以便将这些数据以易于阅读的方式写入其中。
函数 json.dump() 接受一个 JSON 数据对象和一个文件对象，并将数据写入这个文件中（见❸）。参数 indent=4 让 dump()
使用与数据结构匹配的缩进量来设置数据的格式。

如果你现在查看目录 data 并打开其中的文件 readable_eq_data.json，将发现其开头部分像下面这样：

{
    "type": "FeatureCollection",
❶    "metadata": {
        "generated": 1550361461000,
        "url": "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_day.geojson",
        "title": "USGS Magnitude 1.0+ Earthquakes, Past Day",
        "status": 200,
        "api": "1.7.0",
        "count": 158
    },
❷    "features": [
     --snip--

这个文件的开头是一个键为 "metadata" 的片段（见❶），指出了这个数据文件是什么时候生成的，以及能够在网上的什么地方
找到。它还包含适合人类阅读的标题以及文件中记录了多少次地震：在过去的 24 小时内，发生了 158 次地震。

这个 geoJSON 文件的结构适合存储基于位置的数据。数据存储在一个与键 "features" 相关联的列表中（见❷）。这个文件
包含的是地震数据，因此列表的每个元素都对应一次地震。这种结构可能有点令人迷惑，但很有用，让地质学家能够将有关每次地
震的任意数量信息存储在一个字典中，再将这些字典放在一个大型列表中。

下面来看看表示特定地震的字典：


--snip--
        {
            "type": "Feature",
❶            "properties": {
                "mag": 0.96,
                --snip--
❷                "title": "M 1.0 - 8km NE of Aguanga, CA"
            },
❸            "geometry": {
                "type": "Point",
                "coordinates": [
❹                    -116.7941667,
❺                    33.4863333,
                    3.22
                ]
            },
            "id": "ci37532978"
        },

键 "properties" 关联到了与特定地震相关的大量信息（见❶）。

这里关心的主要是与键 "mag" 相关联的地震震级以及地震的标题，因为后者很好地概述了地震的震级和位置（见❷）。

键 "geometry" 指出了地震发生在什么地方（见❸），需要根据这项信息将地震在散点图上标出来。在与键 "coordinates"
相关联的列表中，可找到地震发生位置的经度（见❹）和纬度（见❺）。

这个文件的嵌套层级比之前编写的代码多。如果这让你感到迷惑，也不用担心，Python 将替你处理大部分复杂的工作。这里每次
只会处理一两个嵌套层级，首先将提取过去 24 小时内发生的每次地震对应的字典。

注意：说到位置时，通常先说纬度、再说经度，这种习惯形成的原因可能是人类先发现了纬度，很久后才有经度的概念。然而，很
多地质学框架都先列出经度、后列出纬度，因为这与数学约定一致。geoJSON 格式遵循(经度, 纬度)的约定，但在使用其他框架
时，获悉其遵循的约定很重要。



3、创建地震列表

首先，创建一个列表，其中包含所有地震的各种信息：

import json

# 探索数据的结构。
filename = 'data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)

all_eq_dicts = all_eq_data['features']
print(len(all_eq_dicts))

这里提取与键 'features' 相关联的数据，并将其存储到 all_eq_dicts 中。已经知道，这个文件记录了 158 次地震。
下面的输出表明，提取了这个文件记录的所有地震：

158

注意：这里编写的代码很短。格式良好的文件 readable_eq_data.json 包含超过 6000 行内容，但只需几行代码，就可
读取所有的数据并将其存储到一个 Python 列表中。下面将提取所有地震的震级。



4、提取震级

有了包含所有地震数据的列表后，就可遍历这个列表，从中提取所需的数据。下面来提取每次地震的震级：

--snip--
all_eq_dicts = all_eq_data['features']

❶ mags = []
for eq_dict in all_eq_dicts:
❷    mag = eq_dict['properties']['mag']
    mags.append(mag)

print(mags[:10])

这里创建了一个空列表，用于存储地震震级，再遍历列表 all_eq_dicts（见❶）。每次地震的震级都存储在相应字典的
'properties' 部分的 'mag' 键下（见❷）。依次将地震震级赋给变量 mag，再将这个变量附加到列表 mags 末尾。

为确定提取的数据是否正确，打印前 10 次地震的震级：

[0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]

接下来，将提取每次地震的位置信息，然后就可以绘制地震散点图了。



5、提取位置数据

位置数据存储在 "geometry" 键下。在 "geometry" 键关联的字典中，有一个 "coordinates" 键，它关联到一个列表，
而列表中的前两个值为经度和纬度。下面演示了如何提取位置数据：

--snip--
all_eq_dicts = all_eq_data['features']

mags, titles, lons, lats = [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
❶    title = eq_dict['properties']['title']
❷    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    titles.append(title)
    lons.append(lon)
    lats.append(lat)

print(mags[:10])
print(titles[:2])
print(lons[:5])
print(lats[:5])

这里创建了用于存储位置标题的列表 titles，来提取字典 'properties' 里 'title' 键对应的值（见❶），以及用于存
储经度和纬度的列表。代码 eq_dict['geometry'] 访问与 "geometry" 键相关联的字典（见❷）。第二个键（'coor-
dinates'）提取与 "coordinates" 相关联的列表，而索引 0 提取该列表中的第一个值，即地震发生位置的经度。

打印前 5 个经度和纬度时，输出表明提取的数据是正确的：

[0.96, 1.2, 4.3, 3.6, 2.1, 4, 1.06, 2.3, 4.9, 1.8]
['M 1.0 - 8km NE of Aguanga, CA', 'M 1.2 - 11km NNE of North Nenana, Alaska']
[-116.7941667, -148.9865, -74.2343, -161.6801, -118.5316667]
[33.4863333, 64.6673, -12.1025, 54.2232, 35.3098333]

有了这些数据，就可以绘制地震散点图了。



6、绘制震级散点图

有了前面提取的数据，就可以绘制可视化图了。首先要实现一个简单的震级散点图，在确保显示的信息正确无误之后，再将注意
力转向样式和外观方面。绘制初始散点图的代码如下：

❶ import plotly.express as px

fig = px.scatter(
    x=[-116.7941667],
    y=[33.4863333],
    labels={"x": "经度", "y": "纬度"},
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
❷ )

❸ fig.write_html("global_earthquakes.html")
❹ fig.show()

首先，导入 plotly.express，用别名 px 表示。Plotly Express 是 Plotly 的高级接口，简单易用，语法与 Mat-
plotlib类似（见❶）。然后，调用 px.scatter 函数配置参数创建一个 fig 实例，分别设置 x 轴为经度［范围是[-200,
200]（扩大空间，以便完整显示东西经 180° 附近的地震散点）］、 y 轴为纬度［范围是[-90, 90]］， 设置散点图显示
的宽度和高度均为 800 像素，并设置标题为 “全球地震散点图”（见❷）。

只用 14 行代码，简单的散点图就配置完成了，这返回了一个 fig 对象。fig.write_html 方法可以将可视化图保存为
html 文件。在文件夹中找到 global_earthquakes.html 文件，用浏览器打开即可（见❸）。另外，如果使用 Jupyter
Notebook，可以直接使用 fig.show 方法直接在 notebook 单元格显示散点图（见❹）。

可对这幅散点图做大量修改，使其更有意义、更好懂。下面就来做些这样的修改。



7、另一种指定图表数据的方式

配置这个图表前，先来看看另一种稍微不同的指定 Plotly 图表数据的方式。当前，经纬度数据是手动配置的：

--snip--
    x=lons,
    y=lats,
    labels={"x": "经度", "y": "纬度"},
--snip--

这是在 Plotly Express 中给图表定义数据的最简单方式之一，但在数据处理中并不是最佳的。下面是另一种给图表定义
数据的等效方式，需要使用 pandas 数据分析工具。首先创建一个 DataFrame ，将需要的数据封装起来：

import pandas as pd

data = pd.DataFrame(
 data=zip(lons, lats, titles, mags), columns=["经度", "纬度", "位置", "震级"] )

data.head()

然后，参数配置方式可以变更为：

--snip--
    data,
    x="经度",
    y="纬度",
--snip--

在这种方式中，所有有关数据的信息都以键值对的形式放在一个字典中。如果在 eq_world_map.py 中使用这些代码，生成
的图表是一样的。相比于前一种格式，这种格式能够无缝衔接数据分析，并且更轻松地进行定制。



8、定制标记的尺寸

确定如何改进散点图的样式时，应着重于让要传达的信息更清晰。当前的散点图显示了每次地震的位置，但没有指出震级。要让
观察者迅速获悉最严重的地震发生在什么地方。

为此，根据地震的震级设置其标记的尺寸：

fig = px.scatter(
    data,
    x="经度",
    y="纬度",
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
❶    size="震级",
❷    size_max=10,
)

fig.write_html("global_earthquakes.html")
fig.show()

Plotly Express 支持对数据系列进行定制，这些定制都以参数表示。这里使用了 size 参数来指定散点图中每个标记的尺
寸，这里只需要将前面 data 中的 "震级" 字段提供给 size 参数即可（见❶）。 另外，标记尺寸默认为 20 像素，还可
以通过 size_max=10 将最大显示尺寸缩放到 10（见❷）。

如果运行这些代码，将看到类似于之前的散点图。这比前面的散点图好多了，但还有很大的改进空间。



9、定制标记的颜色

还可以定制标记的颜色，以呈现地震的严重程度。执行这些修改前，将文件 eq_data_30_day_m1.json 复制到你的数据目
录中，它包含 30 天内的地震数据。通过使用这个更大的数据集，绘制出来的地震散点图将有趣得多。

下面演示了如何使用渐变来呈现地震震级：

❶ filename = 'data/eq_data_30_day_m1.json'
--snip--
fig = px.scatter(
    data,
    x="经度",
    y="纬度",
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
    size="震级",
    size_max=10,
❷    color="震级",
)
--snip--

首先修改文件名，以使用 30 天的数据集（见❶）。为了让标记的震级按照不同的颜色显示，只需要配置 color="震级" 即
可。默认的视觉映射图例渐变色范围是从蓝到红再到黄，数值越小则标记越蓝，而数值越大则标记越黄（见❷）。

如果现在运行这个程序，你看到的散点图将漂亮得多。渐变的颜色指出了地震的严重程度。通过在散点图上显示大量的地震，
可将板块边界大致呈现出来！



10、其他渐变

Plotly Express 有大量的渐变可供选择。要获悉有哪些渐变可供使用，请使用文件名 show_color_scales.py 保存
下面这个简短的程序：

import plotly.express as px

for key in px.colors.named_colorscales():
    print(key)

Plotly Express 将渐变存储在模块 colors 中。这些渐变是在列表 px.colors.named_colorscales() 中定义的。
下面的输出列出了可供你使用的所有渐变：

--snip--
greys
hot
inferno
jet
magenta
magma
--snip--

请尝试使用这些渐变其实映射到一个颜色列表。使用 px.colors.diverging.RdYlGn[::-1] 可以将对应颜色的配色
列表反转。

注意：Plotly 除了有 px.colors.diverging 表示连续变量的配色方案，还有 px.colors.sequential 和 px.
colors.qualitative 表示离散变量。随便挑一种配色，例如 px.colors.qualitative.Alphabet，你将看到渐变
是如何定义的。每个渐变都有起始色和终止色，有些渐变还定义了一个或多个中间色。Plotly 会在这些定义好的颜色之间插
入颜色。



11、添加鼠标指向时显示的文本

为完成这幅散点图的绘制，下面将添加一些说明性文本，在你将鼠标指向表示地震的标记时显示出来。除了默认显示的经度和
纬度外，还将显示震级以及地震的大致位置：

fig = px.scatter(
    data,
    x="经度",
    y="纬度",
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=800,
    height=800,
    title="全球地震散点图",
    size="震级",
    size_max=10,
    color="震级",
    hover_name="位置",
)

fig.write_html("global_earthquakes.html")
fig.show()

Plotly Express 的操作非常简单，只需要将 hover_name 参数配置为 data 的 "位置" 字段即可。

太令人震惊了！通过编写大约 40 行代码，就绘制了一幅漂亮的全球地震活动散点图，并通过 30 天地震数据大致展示了
地球的板块结构。Plotly Express 提供了众多定制可视化外观和行为的方式。使用它提供的众多选项，可让图表和散
点图准确地显示你所需的信息。

"""