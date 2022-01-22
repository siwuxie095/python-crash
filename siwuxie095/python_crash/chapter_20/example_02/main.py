"""

设置项目 “学习笔记” 的样式


之前，特意一直专注于项目 “学习笔记” 的功能，没有考虑样式设置问题。这是一种不错的开发方法，因为能正确运行的应用程序
才是有用的。当然，应用程序能够正确运行后，外观就显得很重要了，因为漂亮的应用程序才能吸引用户。

下面简要介绍应用程序 django-bootstrap4，并演示如何将其集成到项目中，为部署做好准备。



1、应用程序 django-bootstrap4

这里将使用 django-bootstrap4 将 Bootstrap 集成到项目中。这个应用程序下载必要的 Bootstrap 文件，将其放到项
目的合适位置，让你能够在项目的模板中使用样式设置指令。

为安装 django-bootstrap4，在活动状态的虚拟环境中执行如下命令：

(ll_env)learning_log$ pip install django-bootstrap4
--snip--
Successfully installed django-bootstrap4-0.0.7

接下来，需要在 settings.py 的 INSTALLED_APPS 中添加如下代码，在项目中包含应用程序 django-bootstrap4：

--snip--
INSTALLED_APPS = [
    # 我的应用程序
    'learning_logs',
    'users',
    # 第三方应用程序
    'bootstrap4',
    # 默认添加的应用程序
    'django.contrib.admin',
    --snip--
]

新建一个名为 “第三方应用程序” 的片段，用于指定其他开发人员开发的应用程序，并在其中添加 'bootstrap4'。务必将这个
片段放在 “我的应用程序” 和 “默认添加的应用程序” 之间。



2、使用 Bootstrap 设置项目 “学习笔记” 的样式

Bootstrap 是一个大型样式设置工具集，还提供了大量模板，可应用于项目以创建独特的总体风格。对 Bootstrap 初学者来
说，这些模板比样式设置工具用起来容易得多。要查看 Bootstrap 提供的模板，可访问其官方网站，单击 Examples 并找到
Navbars。这里将使用模板 Navbars static，它提供了简单的顶部导航栏以及用于放置页面内容的容器。



3、修改 base.html

这里需要修改模板 base.html，以使用前述 Bootstrap 模板。下面分几部分介绍新的 base.html。


α. 定义 HTML 头部

对 base.html 所做的第一项修改是，在其中定义 HTML 头部，使得显示 “学习笔记” 的每个页面时，浏览器标题栏都显示该
网站名。此外，还要添加一些在模板中使用 Bootstrap 所需的信息。请删除 base.html 的全部代码，并输入下面的代码：

❶ {% load bootstrap4 %}

❷ <!doctype html>
❸ <html lang="en">
❹ <head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1,
    shrink-to-fit=no">
❺  <title>Learning Log</title>

❻  {% bootstrap_css %}
  {% bootstrap_javascript jquery='full' %}

❼ </head>

在❶处，加载 django-bootstrap4 中的模板标签集。接下来，将这个文件声明为使用英语（见❸）编写的 HTML 文档（见❷）。
HTML 文件分为两个主要部分：头部（head）和主体（body）。在这个文件中，头部始于❹处。HTML 文件的头部不包含任何内容，
只是向浏览器提供正确显示页面所需的信息。❺处包含一个 title 元素，在浏览器中打开网站 “学习笔记” 的页面时，浏览器的
标题栏将显示该元素的内容。

在❻处，使用 django-bootstrap4 的一个自定义模板标签，让 Django 包含所有的 Bootstrap 样式文件。接下来的标签
启用你可能在页面中使用的所有交互式行为，如可折叠的导航栏。❼处为结束标签 </head>。


β. 定义导航栏

定义页面顶部导航栏的代码很长，因为需要同时支持较窄的手机屏幕和较宽的台式计算机显示器。这里将分三部分定义导航栏。

下面是导航栏定义代码的第一部分：

--snip--
</head>
❶ <body>

❷  <nav class="navbar navbar-expand-md navbar-light bg-light mb-4 border">

❸    <a class="navbar-brand" href="{% url 'learning_logs:index'%}">
        Learning Log</a>

❹    <button class="navbar-toggler" type="button" data-toggle="collapse"
        data-target="#navbarCollapse" aria-controls="navbarCollapse"
        aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span></button>

第一个元素为起始标签 <body>（见❶）。HTML 文件的主体包含用户将在页面上看到的内容。❷处是一个 <nav> 元素，表示页
面的导航链接部分。对于这个元素内的所有内容，都将根据此处的 navbar 和 navbar-expand-md 等选择器定义的 Boot-
strap 样式规则来设置样式。选择器（selector）决定了样式规则将应用于页面上的哪些元素。选择器 navbar-light 和
bg-light 使用一种浅色主题来设置导航栏的颜色。mb-4 中的 mb 表示下边距（margin-bottom），这个选择器确保导航栏
和页面其他部分之间有一些空白区域。选择器 border 在浅色背景周围添加很细的边框，将导航栏与页面其他部分分开。

在❸处，指定在导航栏最左端显示项目名，并将其设置为到主页的链接，因为它将出现在这个项目的每个页面中。选择器 navbar
-brand 设置这个链接的样式，使其比其他链接更显眼，这是一种网站推广方式。

❹处定义了一个按钮，它将在浏览器窗口太窄、无法水平显示整个导航栏时显示出来。如果用户单击这个按钮，将出现一个下拉列表，
其中包含所有的导航元素。在用户缩小浏览器窗口或在屏幕较小的移动设备上显示网站时，collapse 会导致导航栏折叠起来。

下面是导航栏定义代码的第二部分：

      <span class="navbar-toggler-icon"></span></button>
❶    <div class="collapse navbar-collapse" id="navbarCollapse">
❷      <ul class="navbar-nav mr-auto">
❸        <li class="nav-item">
          <a class="nav-link" href="{% url 'learning_logs:topics'%}">
              Topics</a></li>
      </ul>

❶处开启了导航栏的一个新区域。div 是 division（分隔）的缩写。创建页面时，将其分隔成多个区域，并指定要应用于各个
区域的样式和行为规则。在 <div> 起始标签中定义的样式和行为规则将影响下一个结束标签 </div> 之前的所有元素。这里
指定了屏幕或窗口太窄时将折叠起来的导航栏部分的起始位置。

❷处定义了一组链接。Bootstrap 将导航元素定义为无序列表项，但使用的样式规则让它们一点也不像列表。导航栏中的每个链接
或元素都能以列表项的方式定义。这里只有一个列表项——到显示所有主题的页面的链接（见❸）。

下面是导航栏定义代码的最后一部分：

--snip--
      </ul>
❶      <ul class="navbar-nav ml-auto">
❷        {% if user.is_authenticated %}
          <li class="nav-item">
❸            <span class="navbar-text"}">Hello, {{ user.username }}.</span>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'users:logout' %}">Log out</a>
          </li>
        {% else %}
          <li class="nav-item">
            <a class="nav-link" href="{% url 'users:register' %}">Register</a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="{% url 'users:login' %}">Log in</a></li>
        {% endif %}
      </ul>
❹    </div>

  </nav>

❶处使用起始标签 <ul> 定义了另一组链接（你可根据需要在页面中包含任意数量的链接编组），这组链接与登录和注册相关，出
现在导航栏最右端。选择器 ml-auto 表示自动左边距（margin-left-automatic），它根据导航栏包含的其他元素设置左边
距，确保这组链接位于屏幕右边。

❷处的if 代码块与以前使用的条件代码块相同，它根据用户是否已登录显示相应的消息。这个代码块比以前长一些，因为它现在包
含一些样式规则。❸处是一个 <span> 元素，用于设置区域内一系列文本或元素的样式。这起初可能有些令人迷惑：为什么不嵌套
<div> 呢？毕竟有很多页面深度嵌套了 <div> 元素。这是因为 <div> 元素创建区域，而 <span> 元素不会。这里只是要设
置导航栏中信息性文本（如已登录用户的名称）的样式，旨在让其外观与链接不同，以免用户忍不住去单击，因此使用了 <span>。

❹处指出 <div> 元素（它包含将在屏幕太窄时折叠起来的导航栏部分）到此结束，然后指出整个导航栏到此结束。要在导航栏中
添加其他链接，可在既有的 <ul> 元素中添加 <li> 元素，并使用这里演示的样式设置指令。

在 base.html 中，还需添加一些代码：定义两个块，供各个页面放置其特有的内容。


γ. 定义页面的主要部分

base.html 的余下部分包含页面的主要部分：

  </nav>

❶  <main role="main" class="container">
❷    <div class="pb-2 mb-2 border-bottom">
      {% block page_header %}{% endblock page_header %}
    </div>
❸    <div>
      {% block content %}{% endblock content %}
    </div>
  </main>

</body>

</html>

❶处是一个 <main> 起始标签。<main> 元素用于定义页面主体的最重要部分。此处指定了 Bootstrap 选择器 container，
这是一种对页面元素进行编组的简单方式。这里将在这个容器中放置两个 <div> 元素。

第一个 <div> 元素（见❷）包含一个 page_header 块，这里会在大多数页面中使用它来指定标题。为突出标题，设置内边距。
内边距（padding）指的是元素内容和边框之间的距离。选择器 pb-2 是一个 Bootstrap 指令，将元素的下内边距设置为适度
的值。外边距（margin）指的是元素的边框与其他元素之间的距离。由于这里只想在标题下面添加边框，因此使用选择器 border
-bottom，它在 page_header 块的下面添加较细的边框。

❸处定义了另一个 <div> 元素，其中包含 content 块。这里没有对这个块指定样式，因此在具体的页面中，可根据需要设置内
容的样式。文件 base.html 的末尾是元素 <main> 、<body> 和 <html> 的结束标签。

如果现在在浏览器中加载 “学习笔记” 的主页，你将看到一个专业级导航栏。请尝试将窗口调整得非常窄，此时导航栏将变成一个
按钮。如果你单击这个按钮，将打开一个下拉列表，其中包含所有的导航链接。



4、使用 jumbotron 设置主页的样式

下面使用 Bootstrap 元素 jumbotron 来修改主页。jumbotron 元素是一个大框，在页面中显得鹤立鸡群。它可以包含任何
东西，通常用于在主页中呈现简要的项目描述和让用户行动起来的元素。

修改后的文件 index.html 如下所示：

{% extends "learning_logs/base.html" %}

❶ {% block page_header %}
❷  <div class="jumbotron">
❸    <h1 class="display-3">Track your learning.</h1>

❹    <p class="lead">Make your own Learning Log, and keep a list of the
        topics you're learning about. Whenever you learn something new
        about a topic, make an entry summarizing what you've learned.</p>

❺    <a class="btn btn-lg btn-primary" href="{% url 'users:register' %}"
        role="button">Register &raquo;</a>
  </div>
❻ {% endblock page_header %}

在❶处，告诉 Django 接下来要定义 page_header 块包含的内容。jumbotron 就是应用了一系列样式设置指令的 <div>
元素（见❷）。这里使用选择器 jumbotron 应用这组来自 Bootstrap 库的样式设置指令。

这个 jumbotron 包含三个元素。第一个是一条简短的消息——Track your learning，让首次访问者大致知道 “学习笔记”
是做什么用的。h1 类表示一级标题，而选择器 display-3 让这个标题显得更窄更高（见❸）。在❹处添加一条更长的消息，
让用户更详细地知道使用学习笔记可以做什么。

在❺处，通过创建一个按钮（而不是文本链接）邀请用户注册账户。它与导航栏中的链接 Register 一样链接到的注册页面，但是
按钮更显眼，并且让用户知道要使用这个项目首先需要如何做。这里的选择器让这个按钮很大，召唤用户赶快行动起来。代码 &raquo;
是一个 HTML 实体，表示两个右尖括号（>>）。在❻处，结束 page_header 块。这里不想在这个页面中添加其他内容，因此不
需要定义 content 块。



5、设置登录页面的样式

已经改进了登录页面的整体外观，但还未改进登录表单。下面来修改文件 login.html，让表单与页面的其他部分一致：

{% extends "learning_logs/base.html" %}

❶ {% load bootstrap4 %}

❷ {% block page_header %}
  <h2>Log in to your account.</h2>
{% endblock page_header %}

{% block content %}

❸  <form method="post" action="{% url 'users:login' %}" class="form">
    {% csrf_token %}
❹    {% bootstrap_form form %}
❺    {% buttons %}
      <button name="submit" class="btn btn-primary">Log in</button>
    {% endbuttons %}

    <input type="hidden" name="next"
      value="{% url 'learning_logs:index' %}" />
  </form>

{% endblock content %}

在❶处，在这个模板中加载 bootstrap4 模板标签。在❷处，定义 page_header 块，指出这个页面是做什么用的。注意，这里
从这个模板中删除了代码块 {% if form.errors %} ，因为 django-bootstrap4 会自动管理表单错误。

在❸处，添加属性 class="form"，再使用模板标签 {% bootstrap_form %} 来显示表单（见❹），它替换了之前使用的标签
{{ form.as_p }} 。模板标签 {% booststrap_form %} 将 Bootstrap 样式规则应用于各个表单元素。❺处是 boot-
strap4 起始模板标签 {% buttons %} ，它将 Bootstrap 样式应用于按钮。

这样，新渲染的登录表单页面比以前整洁得多，且风格一致、用途明确。如果你尝试使用错误的用户名或密码登录，将发现消息的样
式与整个网站一致，完美地融入了进来。



6、设置显示所有主题的页面的样式

下面来确保用于查看信息的页面也有合适的样式，首先来设置显示所有主题的页面：

{% extends "learning_logs/base.html" %}

❶ {% block page_header %}
  <h1>Topics</h1>
{% endblock page_header %}

{% block content %}
  <ul>
    {% for topic in topics %}
❷      <li><h3>
        <a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a>
      </h3></li>
    {% empty %}
      <li><h3>No topics have been added yet.</h3></li>
    {% endfor %}
  </ul>

❸  <h3><a href="{% url 'learning_logs:new_topic' %}">Add a new topic</a></h3>

{% endblock content %}

不需要标签 {% load bootstrap4 %} ，因为这个文件中没有使用任何 bootstrap4 自定义标签。这里将标题 Topics 移到
page_header 块中，并给它指定标题样式，而没有使用简单的段落标签（见❶）。将每个主题都设置为 <h3> 元素，使其在页面上
显得大一些（见❷）。对于添加新主题的链接，也做同样的处理（见❸）。



7、设置显示单个主题的页面中的条目样式

比起大部分页面，显示单个主题的页面包含更多内容，因此需要做的样式设置工作要更多一些。这里将使用 Bootstrap 的卡片组件
（card）来突出每个条目。 卡片是带灵活的预定义样式的 <div>，非常适合用于显示主题的条目：

{% extends 'learning_logs/base.html' %}

❶ {% block page_header %}
  <h3>{{ topic }}</h3>
{% endblock page_header %}

{% block content %}
  <p>
    <a href="{% url 'learning_logs:new_entry' topic.id %}">Add new entry</a>
  </p>

  <ul>
  {% for entry in entries %}
❷    <div class="card mb-3">
❸      <h4 class="card-header">
        {{ entry.date_added|date:'M d, Y H:i' }}
❹        <small><a href="{% url 'learning_logs:edit_entry' entry.id %}">
            edit entry</a></small>
      </h4>
❺      <div class="card-body">
        {{ entry.text|linebreaks }}
      </div>
    </div>
  {% empty %}
    <p>There are no entries for this topic yet.</p>
  {% endfor %}

{% endblock content %}

首先将主题放在 page_header 块中（见❶），并删除该模板中以前使用的无序列表结构。在❷处，创建一个带选择器 card 的
<div> 元素（而不是将每个条目作为一个列表项），其中包含两个嵌套的元素：一个包含条目的创建日期以及用于编辑条目的链接，
另一个包含条目的内容。

嵌套的第一个元素是个标题。它是带选择器 card-header 的 <h4> 元素（见❸），包含条目的创建日期以及用于编辑条目的链
接。用于编辑条目的链接放在标签 <small> 内，这让它看起来比时间戳小一些（见❹）。第二个嵌套的元素是一个带选择器 card
-body 的 <div> 元素（见❺），将条目的内容放在一个简单的框内。注意这里只修改了影响页面外观的元素，对在页面中包含信
息的 Django 代码未做任何修改。

这样，“学习笔记” 的功能没有任何变化，但显得更专业，对用户更有吸引力。

注意：要使用其他 Bootstrap 模板，可采用类似的流程：将要使用的模板复制到 base.html 中并修改包含实际内容的元素，
以使用该模板来显示项目的信息，然后使用 Bootstrap 的样式设置工具来设置各个页面中内容的样式。

"""