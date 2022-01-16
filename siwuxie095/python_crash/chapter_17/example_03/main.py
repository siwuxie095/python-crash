"""

使用 Plotly 可视化仓库


有了一些有趣的数据后，下面来进行可视化，呈现 GitHub 上 Python 项目的受欢迎程度。这里将创建一个交互式条形图：条形
的高度表示项目获得了多少颗星。单击条形将带你进入项目在 GitHub 上的主页。代码如下：

import requests
❶ from plotly.graph_objs import Bar
from plotly import offline

❷ # 执行API调用并存储响应。
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 处理结果。
response_dict = r.json()
repo_dicts = response_dict['items']
❸ repo_names, stars = [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化。
❹ data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
}]
❺ my_layout = {
    'title': 'GitHub上最受欢迎的Python项目',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'},
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

在❶处，导入 Plotly 中的 Bar 类和模块 offline。像之前的绘制直方图项目中定义列表 data 那样，这里也使用字典来定
义布局，因此不需要导入 Layout 类。这里也打印 API 响应的状态，以便知道是否出现了问题（见❷）。现在不是探索阶段，早
已确定了所需的数据是存在的，因此删除部分处理 API 响应的代码。

接下来，创建两个空列表，用于存储要在图表中呈现的数据（见❸）。这里需要每个项目的名称，用于给条形添加标签，还需要知道
项目获得了多少个星，用于指定条形的高度。在循环中，将每个项目的名称和星级分别附加到这两个列表末尾。

然后，定义列表data（见❹）。它像之前的列表 data 一样包含一个字典，指定了图表的类型，并提供了 x 值和 y 值：x 值为
项目名称，y 值为项目获得了多少个星。

从生成的图表中可知，前几个项目的受欢迎程度比其他项目高得多，但所有这些项目在 Python 生态系统中都很重要。



1、改进 Plotly 图表

下面来改进这个图表的样式。之前介绍过，可在 data 和 my_layout 中以键值对的形式指定各种样式。

通过修改 data，可定制条形。下面是修改后的 data，给条形指定了颜色和边框：

--snip--
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
--snip--

marker 设置影响条形设计。这里给条形指定了一种自定义的蓝色，加上了宽 1.5 像素的深灰色轮廓，还将条形的不透明度设置
为 0.6，以免图表过于惹眼。

下面来修改 my_layout：

--snip--
my_layout = {
    'title': 'GitHub上最受欢迎的Python项目',
❶    'titlefont': {'size': 28},
❷    'xaxis': {
        'title': 'Repository',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
❸    'yaxis': {
        'title': 'Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
--snip--

使用键 'titlefont' 指定图表名称的字号（见❶）。在字 'xaxis' 中，添加指定 x 轴标签字号的设置（'titlefont'）
和刻度标签字号的设置（'tickfont'）（见❷）。由于这些设置嵌套在字典中，还可以使用相应的键指定坐标轴标签和刻度标签
的颜色和字体。在❸处，给 y 轴指定类似的设置。



2、添加自定义工具提示

在 Plotly 中，将鼠标指向条形将显示其表示的信息。这通常称为工具提示 。在本例中，当前显示的是项目获得了多少个星。
下面来创建自定义工具提示，以显示项目的描述和所有者。

为生成这样的工具提示，需要再提取一些信息并修改对象 data：

--snip--
# 处理结果。
response_dict = r.json()
repo_dicts = response_dict['items']
❶ repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

❷    owner = repo_dict['owner']['login']
    description = repo_dict['description']
❸    label = f"{owner}<br />{description}";
    labels.append(label)

# 可视化。
data = [{
    'type': 'bar',
    'x': repo_names,
    'y': stars,
❹    'hovertext': labels,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
--snip--

首先新建一个空列表 labels，用于存储要给各个项目显示的文本（见❶）。在处理数据的循环中，提取每个项目的所有者和描述
（见❷）。Plotly 允许在文本元素中使用 HTML 代码，因此在创建由项目所有者和描述组成的字符串时，能够在这两部分之间
添加换行符（<br />）（见❸）。然后，将这个字符串附加到列表 labels 末尾。

在列表 data 包含的字典中，添加了键 'hovertext'，并将与之关联的值指定为刚创建的列表（见❹）。Plotly 创建每个
条形时，将提取这个列表中的文本，并在观察者将鼠标指向条形时显示。



3、在图表中添加可单击的链接

Plotly 允许在文本元素中使用 HTML，让你能够轻松地在图表中添加链接。下面将 x 轴标签作为链接，让观察者能够访问项目
在 GitHub 上的主页。为此，需要提取 URL 并用其生成 x 轴标签：

--snip--
# 处理结果。
response_dict = r.json()
repo_dicts = response_dict['items']
❶ repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
❷    repo_url = repo_dict['html_url']
❸    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])
    --snip--

# 可视化。
data = [{
    'type': 'bar',
❹    'x': repo_links,
    'y': stars,
    --snip--
}]
--snip--

这里修改了列表的名称（从 repo_names 改为 repo_links），更准确地指出了要组合的信息（见❶）。接下来，从 repo-
_dict 中提取项目的 URL，并将其赋给临时变量 repo_url（见❷）。在❸处，创建一个指向项目的链接，为此使用了 HTML
标记 <a>，其格式为 <a href='URL'>link text</a>。然后，将这个链接附加到列表 repo_links 末尾。

在❹处，将这个列表用作图表的 x 值。生成的图表与前面相同，但观察者可单击图表底端的项目名，以访问项目在 GitHub 上
的主页。 至此，对 API 获取的数据生成了可视化图表 —— 它是交互性的，包含丰富的信息！



4、深入了解 Plotly 和 GitHub API

要深入地了解如何生成 Plotly 图表，有两个不错的地方可以查看。第一个是 Plotly User Guide in Python。通过研究
该资源，可更深入地了解 Plotly 是如何使用数据来生成可视化图表的，以及它采取这种做法的原因。

第二个不错的资源是 Plotly 网站中的 Python Figure Reference，其中列出了可用来配置 Plotly 可视化的所有设置。
这里还列出了所有的图表类型，以及在各个配置选项中可设置的属性。

要更深入地了解 GitHub API，可参阅其文档。通过阅读文档，你可以知道如何从 GitHub 提取各种信息。如果有 GitHub
账户，除了向公众提供的有关仓库的信息外，你还可以提取有关自己的信息。

"""