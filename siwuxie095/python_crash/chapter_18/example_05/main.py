"""

创建其他页面


制定创建页面的流程后，可以开始扩充 “学习笔记” 项目了。下面将创建两个显示数据的页面，其中一个列出所有的主题，另一个
显示特定主题的所有条目。对于每个页面，都将指定 URL 模式、编写一个视图函数并编写一个模板。但这样做之前，需要先创建
一个父模板，项目中的其他模板都将继承它。



1、模板继承

创建网站时，一些通用元素几乎会在所有页面中出现。在这种情况下，可编写一个包含通用元素的父模板，并让每个页面都继承这个
模板，而不必在每个页面中重复定义这些通用元素。这种方法能让你专注于开发每个页面的独特方面，还能让修改项目的整体外观容
易得多。


a. 父模板

下面创建一个名为 base.html 的模板，并将其存储在 index.html 所在的目录中。这个模板包含所有页面都有的元素，而其
他模板都继承它。当前，所有页面都包含的元素只有顶端的标题。因为每个页面都包含这个模板，所以将这个标题设置为到主页的
链接：

<p>
❶    <a href="{% url 'learning_logs:index' %}">Learning Log</a>
</p>

❷ {% block content %}{% endblock content %}

这个文件的第一部分创建一个包含项目名的段落，该段落也是到主页的链接。为创建链接，使用了一个模板标签，它是用花括号和
百分号（{% %}）表示的。模板标签是一小段代码，生成要在页面中显示的信息。这里的模板标签 {% url 'learning_logs
:index' %} 生成一个 URL，该 URL 与在 learning_logs/urls.py 中定义的名为 'index' 的 URL 模式匹配（见❶）。
在本例中，learning_logs 是一个命名空间 ，而 index 是该命名空间中一个名称独特的 URL 模式。这个命名空间来自在
文件 learning_logs/urls.py 中赋给 app_name 的值。

在简单的 HTML 页面中，链接是使用锚标签 <a> 定义的：

<a href="link_url">link text</a>

通过使用模板标签来生成 URL，能很容易地确保链接是最新的：只需修改 urls.py 中的 URL 模式，Django 就会在页面下次
被请求时自动插入修改后的 URL。在本项目中，每个页面都将继承 base.html，因此从现在开始，每个页面都包含到主页的链接。

在❷处，插入了一对块标签。这个块名为 content，是一个占位符，其中包含的信息由子模板指定。

子模板并非必须定义父模板中的每个块，因此在父模板中，可使用任意多个块来预留空间，而子模板可根据需要定义相应数量的块。

注意：在 Python 代码中，几乎总是缩进四个空格。相比于 Python 文件，模板文件的缩进层级更多，因此每个层级通常只缩进
两个空格。每个层级缩进多少个空格无关紧要，只需确保一致即可。


b. 子模板

现在需要重写 index.html，使其继承 base.html。为此，向 index.html 添加如下代码：

❶ {% extends "learning_logs/base.html" %}

❷ {% block content %}
<p>Learning Log</p>
<p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>
❸ {% endblock content %}

如果将这些代码与原来的 index.html 进行比较，将发现标题 Learning Log 没有了，取而代之的是指定要继承哪个模板的代
码（见❶）。子模板的第一行必须包含标签 {% extends %} ，让 Django 知道它继承了哪个父模板。文件 base.html 位于
文件夹 learning_logs 中，因此父模板路径中包含 learning_logs。这行代码导入模板 base.html 的所有内容，让 in-
dex.html 能够指定要在 content 块预留的空间中添加的内容。

在❷处，插入了一个名为 content 的 {% block %} 标签，以定义 content 块。不是从父模板继承的内容都包含在 content
块中，在这里是一个描述项目 “学习笔记” 的段落。在❸处，使用标签 {% endblock content %} 指出了内容定义的结束位置。
在标签 {% endblock %} 中，并非必须指定块名，但如果模板包含多个块，指定块名有助于确定结束的是哪个块。

模板继承的优点开始显现出来了：在子模板中，只需包含当前页面特有的内容。这不仅简化了每个模板，还使得网站修改起来容易得
多。要修改很多页面都包含的元素，只需修改父模板即可，所做的修改将传导到继承该父模板的每个页面。在包含数十乃至数百个页
面的项目中，这种结构使得网站改进起来更容易、更快捷。

注意：在大型项目中，通常有一个用于整个网站的父模板 base.html，且网站的每个主要部分都有一个父模板。每个部分的父模板
都继承 base.html，而网站的每个页面都继承相应部分的父模板。这让你能够轻松地修改整个网站的外观、网站任何一部分的外观
以及任何一个页面的外观。这种配置提供了一种效率极高的工作方式，让你乐意不断地去改进网站。



2、显示所有主题的页面

有了高效的页面创建方法，就能专注于另外两个页面了：显示所有主题的页面和显示特定主题中条目的页面。前者显示用户创建的所
有主题，它是第一个需要使用数据的页面。


a. URL 模式

首先，定义显示所有主题的页面的 URL。通常使用一个简单的 URL 片段来指出页面显示的信息，这里使用单词 topics，因此
URL http://localhost:8000/topics/ 将返回显示所有主题的页面。下面演示了该如何修改 learning_logs/urls.py：

--snip--
urlpatterns = [
    # 主页
    path('', views.index, name='index'),
    # 显示所有的主题。
❶    path('topics/', views.topics, name='topics'),
]

这里在用于主页 URL 的字符串参数中添加了 topics/（见❶）。Django 检查请求的 URL 时，这个模式与如下 URL 匹配：
基础 URL 后面跟着 topics。可在末尾包含斜杠，也可省略，但单词 topics 后面不能有任何东西，否则就与该模式不匹配。
URL 与该模式匹配的请求都将交给 views.py 中的函数 topics() 处理。


b. 视图

函数 topics() 需要从数据库中获取一些数据，并将其交给模板。需要在 views.py 中添加的代码如下：

from django.shortcuts import render

❶ from .models import Topic

def index(request):
    --snip--

❷ def topics(request):
    \"""显示所有的主题。\"""
❸    topics = Topic.objects.order_by('date_added')
❹    context = {'topics': topics}
❺    return render(request, 'learning_logs/topics.html', context)

首先导入与所需数据相关联的模型（见❶）。函数 topics()包含一个形参：Django 从服务器那里收到的 request 对象（见❷）。
在❸处，查询数据库 —— 请求提供 Topic 对象，并根据属性 date_added 进行排序。返回的查询集被存储在 topics 中。

在❹处，定义一个将发送给模板的上下文。上下文是一个字典，其中的键是将在模板中用来访问数据的名称，而值是要发送给模板的
数据。这里只有一个键值对，包含一组将在页面中显示的主题。创建使用数据的页面时，除了对象 request 和模板的路径外，还
将变量 context 传递给 render()（见❺）。


c. 模板

显示所有主题的页面的模板接受字典 context，以便使用 topics() 提供的数据。请创建一个文件，将其命名为 topics.html，
并存储到 index.html 所在的目录中。下面演示了如何在这个模板中显示主题：

{% extends "learning_logs/base.html" %}

{% block content %}

    <p>Topics</p>

❶    <ul>
❷        {% for topic in topics %}
❸            <li>{{ topic }}</li>
❹        {% empty %}
            <li>No topics have been added yet.</li>
❺        {% endfor %}
❻    </ul>

{% endblock content %}

就像模板 index.html 中一样，首先使用标签 {% extends %} 来继承 base.html，再开始定义 content 块。这个页面
的主体是一个项目列表，其中列出了用户输入的主题。在标准 HTML 中，项目列表称为无序列表，用标签 <ul></ul> 表示。包
含所有主题的项目列表始于❶处。

在❷处，使用一个相当于 for 循环的模板标签，它遍历字典 context 中的列表 topics。模板中使用的代码与 Python 代码
存在一些重要差别：Python 使用缩进来指出哪些代码行是 for 循环的组成部分；而在模板中，每个 for 循环都必须使用 {%
endfor %} 标签来显式地指出其结束位置。因此在模板中，循环类似于下面这样：

{% for item in list %}
    do something with each item
{% endfor %}

在循环中，要将每个主题转换为项目列表中的一项。要在模板中打印变量，需要将变量名用双花括号括起。这些花括号不会出现在页
面中，只是用于告诉 Django 这里使用了一个模板变量。因此每次循环时，❸处的代码 {{ topic }} 都被替换为 topic 的
当前值。HTML 标签 <li></li> 表示一个项目列表项。在标签对 <ul></ul> 内部，位于标签 <li> 和 </li> 之间的内容
都是一个项目列表项。

在❹处，使用模板标签 {% empty %}，它告诉 Django 在列表 topics 为空时该如何办。这里是打印一条消息，告诉用户还
没有添加任何主题。最后两行分别结束 for 循环（见❺）和项目列表（见❻）。

现在需要修改父模板，使其包含到显示所有主题的页面的链接。为此，在其中添加如下代码：

<p>
❶    <a href="{% url 'learning_logs:index' %}">Learning Log</a> -
❷    <a href="{% url 'learning_logs:topics' %}">Topics</a>
</p>

{% block content %}{% endblock content %}

在到主页的链接后面添加一个连字符（见❶），再添加一个到显示所有主题的页面的链接 —— 使用的也是模板标签 {% url %}
（见❷）。这行让 Django 生成一个链接，它与 learning_logs/urls.py 中名为 'topics' 的 URL 模式匹配。

现在如果刷新浏览器中的主页，将看到链接 Topics。



3、显示特定主题的页面

接下来，需要创建一个专注于特定主题的页面，它显示该主题的名称以及所有条目。这里同样将定义一个新的 URL 模式，编写一个
视图并创建一个模板。此外，还将修改显示所有主题的页面，让每个项目列表项都变为到相应主题页面的链接。


a. URL模式

显示特定主题的页面的 URL 模式与前面的所有 URL 模式都稍有不同，因为它使用主题的 id 属性来指出请求的是哪个主题。例
如，如果用户要查看主题 Chess（其 id 为 1）的详细页面，URL 将为 http://localhost:8000/topics/1/。下面是与
这个 URL 匹配的模式，应将其放在 learning_logs/urls.py 中：

--snip--
urlpatterns = [
    --snip--
    # 特定主题的详细页面。
    path('topics/<int:topic_id>/', views.topic, name='topic'),
]

这里来详细研究这个URL模式中的字符串 'topics/<int:topic_id>/'。这个字符串的第一部分让 Django 查找在基础 URL
后包含单词 topics 的 URL，第二部分（/<int:topic_id>/）与包含在两个斜杠内的整数匹配，并将这个整数存储在一个名
为 topic_id 的实参中。

发现 URL 与这个模式匹配时，Django 将调用视图函数 topic()，并将存储在 topic_id 中的值作为实参传递给它。在这个
函数中，将使用 topic_id 的值来获取相应的主题。


b. 视图

函数 topic() 需要从数据库中获取指定的主题以及与之相关联的所有条目，如下所示：

--snip--
❶ def topic(request, topic_id):
    \"""显示单个主题及其所有的条目。\"""
❷    topic = Topic.objects.get(id=topic_id)
❸    entries = topic.entry_set.order_by('-date_added')
❹    context = {'topic': topic, 'entries': entries}
❺    return render(request, 'learning_logs/topic.html', context)

这是除 request 对象外，第一个还包含另一个形参的视图函数。这个函数接受表达式 /<int:topic_id>/ 捕获的值，并将其
存储到 topic_id 中（见❶）。在❷处，使用 get() 来获取指定的主题，就像前面在 Django shell 中所做的那样。在❸处，
获取与该主题相关联的条目，并根据 date_added 进行排序：date_added 前面的减号指定按降序排列，即先显示最近的条目。
将主题和条目都存储在字典 context 中（见❹），再将这个字典发送给模板 topic.html（见❺）。

注意：❷处和❸处的代码称为查询，因为它们向数据库查询了特定的信息。在自己的项目中编写这样的查询时，先在 Django shell
中进行尝试大有裨益。比起先编写视图和模板、再在浏览器中检查结果，在 shell 中执行代码可更快获得反馈。


c. 模板

这个模板需要显示主题的名称和条目的内容。如果当前主题不包含任何条目，还需向用户指出这一点：

{% extends "learning_logs/base.html" %}

{% block content %}

❶    <p>Topic: {{ topic }}}</p>

    <p>Entries:</p>

❷    <ul>
❸        {% for entry in entries %}
            <li>
❹                <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
❺                <p>{{ entry.text|linebreaks }}</p>
            </li>
❻        {% empty %}
            <li>There are no entries for this topic yet.</li>
        {% endfor %}
    </ul>

{% endblock content %}

像这个项目的其他页面一样，这里也继承了 base.html。接下来，显示当前的主题（见❶），它存储在模板变量 {{ topic }}
中。为什么可以使用变量 topic 呢？因为它包含在字典 context 中。接下来，定义一个显示每个条目的项目列表（见❷），
并像前面显示所有主题一样遍历条目（见❸）。

每个项目列表项都将列出两项信息：条目的时间戳和完整的文本。为列出时间戳（见❹），这里显示属性 date_added 的值。在
Django 模板中，竖线（|）表示模板过滤器，即对模板变量的值进行修改的函数。过滤器 date: 'M d, Y H:i' 以类似于
这样的格式显示时间戳：January 1, 2018 23:00。接下来的一行显示 text 的完整值，而不仅仅是前 50 字符。过滤器
 linebreaks（见❺）将包含换行符的长条目转换为浏览器能够理解的格式，以免显示为不间断的文本块。在❻处，使用模板标签
{% empty %} 打印一条消息，告诉用户当前主题还没有条目。


d. 将显示所有主题的页面中的主题设置为链接

在浏览器中查看显示特定主题的页面前，需要修改模板 topics.html，让每个主题都链接到相应的页面，如下所示：

--snip--
{% for topic in topics %}
    <li>
        <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a>
    </li>
{% empty %}
--snip--

这里使用模板标签 url 根据 learning_logs 中名为 'topic'的 URL 模式生成了合适的链接。这个 URL 模式要求提供
实参 topic_id，因此在模板标签 url 中添加了属性 topic.id。现在，主题列表中的每个主题都是链接了，链接到显示相应
主题的页面，如 http://localhost:8000/topics/1/。

如果现在刷新显示所有主题的页面，就可以单击其中的一个主题，看到对应的页面。

注意：topic.id 和 topic_id 之间存在细微而重要的差别。表达式 topic.id 检查主题并获取其 ID 值，而在代码中，
变量 topic_id 是指向该 ID 的引用。使用 ID 时如果出现错误，请确保正确地使用了这两个表达式。

"""