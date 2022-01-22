"""

让用户输入数据


建立用于创建用户账户的身份验证系统之前，先来添加几个页面，让用户能够输入数据。这里将让用户添加新主题，添加新条目
以及编辑既有条目。

当前，只有超级用户能够通过管理网站输入数据。这里不想让用户与管理网站交互，因此将使用 Django 的表单创建工具来创
建让用户能够输入数据的页面。



1、添加新主题

首先来让用户能够添加新主题。创建基于表单的页面的方法几乎与前面创建页面一样：定义 URL，编写视图函数并编写一个模板。
一个主要差别是，需要导入包含表单的模块 forms.py。


a. 用于添加主题的表单

让用户输入并提交信息的页面都是表单，那怕看起来不像。用户输入信息时，需要进行验证，确认提供的信息是正确的数据类型，
而不是恶意的信息，如中断服务器的代码。然后，对这些有效信息进行处理，并将其保存到数据库的合适地方。这些工作很多都
是由 Django 自动完成的。

在 Django 中，创建表单的最简单方式是使用 ModelForm，它根据在之前定义的模型中的信息自动创建表单。请创建一个名
为 forms.py 的文件，将其存储到 models.py 所在的目录，并在其中编写你的第一个表单：

from django import forms

from .models import Topic

❶ class TopicForm(forms.ModelForm):
    class Meta:
❷        model = Topic
❸        fields = ['text']
❹        labels = {'text': ''}

首先导入模块 forms 以及要使用的模型 Topic。在❶处，定义一个名为 TopicForm 的类，它继承了 forms.ModelForm。

最简单的 ModelForm 版本只包含一个内嵌的 Meta 类，让 Django 根据哪个模型创建表单以及在表单中包含哪些字段。在
❷处，根据模型 Topic 创建表单，其中只包含字段 text（见❸）。❹处的代码让 Django 不要为字段 text 生成标签。


b. URL 模式 new_topic

新页面的 URL 应简短且具有描述性，因此当用户要添加新主题时，需要切换到 http://localhost:8000/new_topic/。
下面是页面 new_topic 的 URL 模式，请将其添加到 learning_logs/urls.py 中：

--snip--
urlpatterns = [
    --snip--
    # 用于添加新主题的页面。
    path('new_topic/', views.new_topic, name='new_topic'),
]

这个 URL 模式将请求交给视图函数 new_topic()，下面来编写这个函数。


c. 视图函数 new_topic()

函数 new_topic() 需要处理两种情形。一是刚进入 new_topic 页面（在这种情况下应显示空表单）；二是对提交的表单
数据进行处理，并将用户重定向到页面 topics：

def new_topic(request):
    \"""添加新主题。\"""
❶    if request.method != 'POST':
        # 未提交数据：创建一个新表单。
❷        form = TopicForm()
    else:
        # POST提交的数据：对数据进行处理。
❸        form = TopicForm(data=request.POST)
❹        if form.is_valid():
❺            form.save()
❻            return redirect('learning_logs:topics')

    # 显示空表单或指出表单数据无效。
❼    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

这里导入了函数 redirect，用户提交主题后将使用这个函数重定向到页面 topics。函数 redirect 将视图名作为参数，
并将用户重定向到这个视图。这里还导入了刚创建的表单 TopicForm。


d. GET 请求和 POST 请求

创建 Web 应用程序时，将用到的两种主要请求类型是 GET 请求和 POST 请求。对于只是从服务器读取数据的页面，使用
GET 请求；在用户需要通过表单提交信息时，通常使用 POST 请求。处理所有表单时，都将指定使用 POST 方法。还有一
些其他类型的请求，但本项目没有使用。

函数 new_topic() 将请求对象作为参数。用户初次请求该页面时，其浏览器将发送 GET 请求；用户填写并提交表单时，
其浏览器将发送 POST 请求。根据请求的类型，可确定用户请求的是空表单（GET 请求）还是要求对填写好的表单进行处理
（POST 请求）。

❶处的测试确定请求方法是 GET 还是 POST。如果请求方法不是 POST，请求就可能是 GET，因此需要返回一个空表单。
（即便请求是其他类型的，返回空表单也不会有任何问题。） ❷处创建一个 TopicForm 实例，将其赋给变量 form，
再通过上下文字典将这个表单发送给模板（见❼）。由于实例化 TopicForm 时没有指定任何实参，Django 将创建一个
空表单，供用户填写。

如果请求方法为 POST，将执行 else 代码块，对提交的表单数据进行处理。这里使用用户输入的数据（存储在 request
.POST 中）创建一个 TopicForm 实例（见❸），这样对象 form 将包含用户提交的信息。

要将提交的信息保存到数据库，必须先通过检查确定它们是有效的（见❹）。方法 is_valid() 核实用户填写了所有必不可少
的字段（表单字段默认都是必不可少的），且输入的数据与要求的字段类型一致（例如，字段 text 少于 200 字符，这是之
前在 models.py 中指定的）。这种自动验证避免了去做大量的工作。如果所有字段都有效，就可调用 save() （见❺），将
表单中的数据写入数据库。

保存数据后，就可离开这个页面了。为此，使用 redirect() 将用户的浏览器重定向到页面 topics（见❻）。在页面 top-
ics 中，用户将在主题列表中看到他刚输入的主题。

这里在这个视图函数的末尾定义了变量 context，并使用稍后将创建的模板 new_topic.html 来渲染页面。这些代码不在
if 代码块内，因此无论是用户刚进入 new_topic 页面还是提交的表单数据无效，这些代码都将执行。用户提交的表单数据
无效时，将显示一些默认的错误消息，帮助用户提供有效的数据。


e. 模板 new_topic

下面来创建新模板 new_topic.html，用于显示刚创建的表单：

{% extends "learning_logs/base.html" %}

{% block content %}

    <p>Add a new topic:</p>

❶    <form action="{% url 'learning_logs:new_topic' %}" method="post">
❷         {% csrf_token %}
❸        {{ form.as_p }}
❹        <button name="submit">Add topic</button>
    </form>

{% endblock content %}

这个模板继承了 base.html，因此其基本结构与项目 “学习笔记” 的其他页面相同。在❶处，定义了一个 HTML 表单。实参
action 告诉服务器将提交的表单数据发送到哪里。这里将它发回给视图函数 new_topic()。而实参 method 让浏览器以
POST 请求的方式提交数据。

Django 使用模板标签 {% csrf_token %}（见❷）来防止攻击者利用表单来获得对服务器未经授权的访问（这种攻击称为
跨站请求伪造）。❸处显示表单，从中可知 Django 使得完成显示表单等任务有多简单：只需包含模板变量{{ form.as_p }}，
就可让 Django 自动创建显示表单所需的全部字段。修饰符 as_p 让 Django 以段落格式渲染所有表单元素，这是一种整
洁地显示表单的简单方式。

Django 不会为表单创建提交按钮，因此在❹处定义了一个。


f. 链接到页面 new_topic

下面在页面 topics 中添加到页面 new_topic 的链接：

{% extends "learning_logs/base.html" %}

{% block content %}

    <p>Topics</p>

    <ul>
        --snip--
    </ul>

    <a href="{% url 'learning_logs:new_topic' %}">Add a new topic</a>

{% endblock content %}

这个链接放在既有主题列表的后面。这样，就可以添加新主题了。



2、添加新条目

可以添加新主题之后，用户还会想添加几个新条目。这里将再次定义 URL，编写视图函数和模板，并且链接到添加新条目的页面。
但在此之前，需要在 forms.py 中再添加一个类。


i. 用于添加新条目的表单

这里需要创建一个与模型 Entry 相关联的表单，但这个表单的定制程度比 TopicForm 更高一些：

from django import forms

from .models import Topic, Entry

class TopicForm(forms.ModelForm):
    --snip--

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
❶        labels = {'text': 'Entry:'}
❷        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

首先修改 import 语句，使其除导入 Topic 外，还导入 Entry。新类 EntryForm 继承了 forms.ModelForm，它包含
的 Meta 类指出了表单基于的模型以及要在表单中包含哪些字段。这里给字段 'text' 指定了标签 'Entry:'（见❶）。

在❷处，定义了属性 widgets。小部件（widget）是一个 HTML 表单元素，如单行文本框、多行文本区域或下拉列表。通过
设置属性 widgets，可覆盖 Django 选择的默认小部件。通过让 Django 使用 forms.Textarea，定制了字段 'text'
的输入小部件，将文本区域的宽度设置为 80 列，而不是默认的 40 列。这给用户提供了足够的空间来编写有意义的条目。


ii. URL 模式 new_entry

在用于添加新条目的页面的 URL 模式中，需要包含实参 topic_id，因为条目必须与特定的主题相关联。该 URL 模式如下，
请将它添加到 learning_logs/urls.py 中：

--snip--
urlpatterns = [
    --snip--
    # 用于添加新条目的页面。
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
]

这个URL模式与形如 http://localhost:8000/new_entry/id/ 的 URL 匹配，其中的 id 是一个与主题 ID 匹配的数。
代码 <int:topic_id> 捕获一个数值，并将其赋给变量 topic_id。请求的 URL 与这个模式匹配时，Django 将请求和主
题 ID 发送给函数 new_entry()。


iii. 视图函数 new_entry()

视图函数 new_entry() 与函数 new_topic() 很像，请在 views.py 中添加如下代码：

from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm, EntryForm

--snip--
def new_entry(request, topic_id):
    \"""在特定主题中添加新条目。\"""
❶    topic = Topic.objects.get(id=topic_id)
❷    if request.method != 'POST':
        # 未提交数据：创建一个空表单。
❸        form = EntryForm()
    else:
        # POST提交的数据：对数据进行处理。
❹        form = EntryForm(data=request.POST)
        if form.is_valid():
❺            new_entry = form.save(commit=False)
❻            new_entry.topic = topic
            new_entry.save()
❼            return redirect('learning_logs:topic', topic_id=topic_id)

    # 显示空表单或指出表单数据无效。
    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)

这里修改 import 语句，在其中包含刚创建的 EntryForm。new_entry() 的定义包含形参 topic_id，用于存储从 URL
中获得的值。渲染页面和处理表单数据时，都需要知道针对的是哪个主题，因此使用 topic_id 来获得正确的主题（见❶）。

在❷处，检查请求方法是 POST 还是 GET。如果是 GET 请求，就执行 if 代码块，创建一个空的 EntryForm 实例（见❸）。
如果请求方法为 POST，就对数据进行处理：创建一个 EntryForm 实例，使用 request 对象中的 POST 数据来填充它（见❹）。
然后检查表单是否有效。如果有效，就设置条目对象的属性 topic，再将条目对象保存到数据库。

调用 save() 时，传递实参 commit=False（见❺），让 Django 创建一个新的条目对象，并将其赋给 new_entry， 但
不保存到数据库中。将 new_entry 的属性 topic 设置为在这个函数开头从数据库中获取的主题（见❻），再调用 save()
且不指定任何实参。这将把条目保存到数据库，并将其与正确的主题相关联。

在❼处，调用 redirect()，它要求提供两个参数：要重定向到的视图和要给视图函数提供的参数。这里重定向到 topic()，
而这个视图函数需要参数 topic_id。视图函数 topic() 渲染新增条目所属主题的页面，其中的条目列表包含新增的条目。

在视图函数 new_entry() 的末尾，创建了一个上下文字典，并使用模板 new_entry.html 渲染页面。这些代码将在用户
刚进入页面或提交的表单数据无效时执行。


iv. 模板 new_entry

模板 new_entry 类似于模板 new_topic，如下面的代码所示：

{% extends "learning_logs/base.html" %}

{% block content %}

❶    <p><a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a></p>

    <p>Add a new entry:</p>
❷    <form action="{% url 'learning_logs:new_entry' topic.id %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">Add entry</button>
    </form>

{% endblock content %}

在页面顶端显示主题（见❶），让用户知道自己是在哪个主题中添加条目。该主题名也是一个链接，可用于返回到该主题的主页面。

表单的实参 action 包含 URL 中的 topic_id 值，让视图函数能够将新条目关联到正确的主题（见❷）。除此之外，这个模
板与模板 new_topic.html 完全相同。


v. 链接到页面 new_entry

接下来，需要在显示特定主题的页面中添加到页面 new_entry 的链接：

{% extends "learning_logs/base.html" %}

{% block content %}

    <p>Topic: {{ topic }}</p>

    <p>Entries:</p>
    <p>
        <a href="{% url 'learning_logs:new_entry' topic.id %}">Add new entry</a>
    </p>

    <ul>
        --snip--
    </ul>

{% endblock content %}

这里将这个链接放在条目列表前面，因为在这种页面中，执行的最常见的操作是添加新条目。现在用户可添加新主题，还可在每个
主题中添加任意数量的条目。请在一些主题中添加新条目，尝试使用一下页面 new_entry。



3、编辑条目

下面来创建让用户能够编辑既有条目的页面。


α. URL 模式 edit_entry

这个页面的 URL 需要传递要编辑的条目的 ID。修改后的 learning_logs/urls.py 如下：

--snip--
urlpatterns = [
    --snip--
    # 用于编辑条目的页面。
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]

在 URL（如 http://localhost:8000/edit_entry/1/）中传递的 ID 存储在形参 entry_id 中。这个 URL 模式将
与其匹配的请求发送给视图函数 edit_entry()。


β. 视图函数 edit_entry()

页面 edit_entry 收到 GET 请求时，edit_entry() 将返回一个表单，让用户能够对条目进行编辑；收到 POST 请求
（条目文本经过修订）时，则将修改后的文本保存到数据库：

from django.shortcuts import render, redirect

from .models import Topic, Entry
from .forms import TopicForm, EntryForm

--snip--
def edit_entry(request, entry_id):
    \"""编辑既有条目。\"""
❶    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != 'POST':
        # 初次请求：使用当前条目填充表单。
❷        form = EntryForm(instance=entry)
    else:
        # POST提交的数据：对数据进行处理。
❸        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
❹            form.save()
❺            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'learning_logs/edit_entry.html', context)

首先导入模型 Entry。在❶处，获取用户要修改的条目对象以及与其相关联的主题。在请求方法为 GET 时将执行的 if 代码块
中，使用实参 instance=entry 创建一个 EntryForm 实例（见❷）。这个实参让 Django 创建一个表单，并使用既有条
目对象中的信息填充它。用户将看到既有的数据，并且能够编辑。

处理 POST 请求时，传递实参 instance=entry 和 data=request.POST（见❸），让 Django 根据既有条目对象创建
一个表单实例，并根据 request.POST 中的相关数据对其进行修改。然后，检查表单是否有效。如果有效，就调用 save()
且不指定任何实参（见❹），因为条目已关联到特定的主题。然后，重定向到显示条目所属主题的页面（见❺），用户将在其中看
到其编辑的条目的新版本。

如果要显示表单让用户编辑条目或者用户提交的表单无效，就创建上下文字典并使用模板 edit_entry.html 渲染页面。


γ. 模板 edit_entry

下面来创建模板 edit_entry.html，它与模板 new_entry.html 类似：

{% extends "learning_logs/base.html" %}

{% block content %}

    <p><a href="{% url 'learning_logs:topic' topic.id %}">{{ topic }}</a></p>

    <p>Edit entry:</p>
❶    <form action="{% url 'learning_logs:edit_entry' entry.id %}" method="post">
        {% csrf_token %}
        {{ form.as_p }}
❷        <button name="submit">Save changes</button>
    </form>

{% endblock content %}

在❶处，实参 action 将表单发送给函数 edit_entry() 处理。在标签 {% url %} 中，将条目 ID 作为一个实参，让视
图函数 edit_entry() 能够修改正确的条目对象。在❷处，将提交按钮的标签设置成 Save changes，旨在提醒用户：单击
该按钮将保存所做的编辑，而不是创建一个新条目。


δ. 链接到页面 edit_entry

现在，需要在显示特定主题的页面中给每个条目添加到页面 edit_entry 的链接：

--snip--
{% for entry in entries %}
    <li>
        <p>{{ entry.date_added|date:'M d, Y H:i' }}</p>
        <p>{{ entry.text|linebreaks }}</p>
        <p>
            <a href="{% url 'learning_logs:edit_entry' entry.id %}">Edit entry</a>
        </p>
    </li>
--snip--

将编辑链接放在了每个条目的日期和文本后面。在循环中，使用模板标签 {% url %} 根据 URL 模式 edit_entry 和当前
条目的 ID 属性（entry.id）来确定 URL。链接文本为 Edit entry，它出现在页面中每个条目的后面。

至此，“学习笔记” 已具备了需要的大部分功能。用户可添加主题和条目，还可根据需要查看任何条目。后续将实现一个用户注册
系统，让任何人都可向 “学习笔记” 申请账户，并创建自己的主题和条目。

"""