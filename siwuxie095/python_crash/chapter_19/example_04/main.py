"""

让用户拥有自己的数据


用户应该能够输入其专有的数据，因此这里将创建一个系统，确定各项数据所属的用户，再限制对页面的访问，让用户只能使用
自己的数据。

这里将修改模型 Topic，让每个主题都归属于特定用户。这也将影响条目，因为每个条目都属于特定的主题。下面先来限制对
一些页面的访问。



1、使用 @login_required 限制访问

Django 提供了装饰器 @login_required，让你能够轻松地只允许已登录用户访问某些页面。装饰器（decorator）是放
在函数定义前面的指令，Python 在函数运行前根据它来修改函数代码的行为。下面来看一个示例。


α. 限制访问显示所有主题的页面

每个主题都归特定用户所有，因此应只允许已登录的用户请求显示所有主题的页面。为此，在 learning_logs/views.py
中添加如下代码：

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from .models import Topic, Entry
--snip--

@login_required
def topics(request):
    \"""显示所有的主题。\"""
    --snip--

首先导入函数 login_required()。将 login_required() 作为装饰器应用于视图函数 topics() —— 在它前面加上
符号 @ 和 login_required，让 Python 在运行 topics() 的代码之前运行 login_required() 的代码。

login_required() 的代码检查用户是否已登录，仅当用户已登录时，Django 才运行 topics() 的代码。如果用户未登
录，就重定向到登录页面。

为实现这种重定向，需要修改 settings.py，让 Django 知道到哪里去查找登录页面。请在 settings.py 末尾添加如
下代码：

--snip--

# 我的设置
LOGIN_URL = 'users:login'

现在，如果未登录的用户请求装饰器 @login_required 保护的页面，Django 将重定向到 settings.py 中的 LOGIN-
_URL 指定的 URL。

要测试这个设置，可注销并进入主页，再单击链接 Topics，这将重定向到登录页面。然后，使用你的账户登录，并再次单击
主页中的 Topics 链接，你将看到显示所有主题的页面。


β. 全面限制对项目 “学习笔记” 的访问

Django 让你能够轻松地限制对页面的访问，但你必须确定要保护哪些页面。最好先确定项目的哪些页面不需要保护，再限制对
其他所有页面的访问。你可轻松地修改过于严格的访问限制。比起不限制对敏感页面的访问，这样做的风险更低。

在项目 “学习笔记” 中，将不限制对主页和注册页面的访问，并限制对其他所有页面的访问。

在下面的 learning_logs/views.py 中，对除 index() 外的每个视图都应用了装饰器 @login_required：

@login_required
def topics(request):
    --snip--

@login_required
def topic(request, topic_id):
    --snip--

@login_required
def new_topic(request):
    --snip--

@login_required
def new_entry(request, topic_id):
    --snip--

@login_required
def edit_entry(request, entry_id):
    --snip--

如果你在未登录的情况下尝试访问这些页面，将被重定向到登录页面。另外，你还不能单击到 new_topic 等页面的链接。如果
你输入 URL http://localhost:8000/new_topic/，将被重定向到登录页面。对于所有与私有用户数据相关的 URL，都
应限制访问。



2、将数据关联到用户

现在，需要将数据关联到提交它们的用户。只需将最高层的数据关联到用户，更低层的数据就会自动关联到用户。例如，在项目
“学习笔记” 中，应用程序的最高层数据是主题，而所有条目都与特定主题相关联。只要每个主题都归属于特定用户，就能确定
数据库中每个条目的所有者。

下面来修改模型 Topic，在其中添加一个关联到用户的外键。这样做之后，必须对数据库进行迁移。最后，必须修改某些视图，
使其只显示与当前登录的用户相关联的数据。


α. 修改模型 Topic

对 models.py 的修改只涉及两行代码：

from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
    \"""用户学习的主题。\"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        \"""返回模型的字符串表示。\"""
        return self.text

class Entry(models.Model):
    --snip--

首先导入 django.contrib.auth 中的模型 User，然后在 Topic 中添加字段 owner，它建立到模型 User 的外键关系。
用户被删除时，所有与之相关联的主题也会被删除。


β. 确定当前有哪些用户

迁移数据库时，Django 将对数据库进行修改，使其能够存储主题和用户之间的关联。为执行迁移，Django 需要知道该将各个
既有主题关联到哪个用户。最简单的办法是，将既有主题都关联到同一个用户，如超级用户。为此，需要知道该用户的 ID。

下面来查看已创建的所有用户的 ID。为此，启动一个 Django shell 会话，并执行如下命令：

(ll_env)learning_log$ python manage.py shell
❶ >>> from django.contrib.auth.models import User
❷ >>> User.objects.all()
 <QuerySet [<User: ll_admin>, <User: eric>, <User: willie>]>
❸ >>> for user in User.objects.all():
... print(user.username, user.id)
...
ll_admin 1
eric 2
willie 3
>>>

在❶处，在 shell 会话中导入模型 User。然后，查看到目前为止都创建了哪些用户（见❷）。输出中列出了三个用户：
ll_admin、eric 和 willie。

在❸处，遍历用户列表并打印每位用户的用户名和 ID。Django 询问要将既有主题关联到哪个用户时，将指定其中一个 ID 值。


γ. 迁移数据库

知道用户 ID 后，就可迁移数据库了。这样做时，Python 将询问你是要暂时将模型 Topic 关联到特定用户，还是在文件 mo-
dels.py 中指定默认用户。请选择第一个选项。

❶ (ll_env)learning_log$ python manage.py makemigrations learning_log
❷ You are trying to add a non-nullable field 'owner' to topic without a default; we can't do
 that (the database needs something to populate existing rows).
❸ Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
❹ Select an option: 1
❺ Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
❻ >>> 1
Migrations for 'learning_logs':
  learning_logs/migrations/0003_topic_owner.py
    - Add field owner to topic
(ll_env)learning_log$

首先执行命令 makemigrations（见❶）。在❷处的输出中，Django 指出你试图给既有模型 Topic 添加一个必不可少（不可
为空）的字段，而该字段没有默认值。在❸处，Django 提供了两种选择：要么现在提供默认值，要么退出并在 models.py 中
添加默认值。在❹处，选择了第一个选项，因此 Django 让你输入默认值（见❺）。

为将所有既有主题都关联到管理用户 ll_admin，这里输入用户 ID 值 1（见❻）。可以使用已创建的任何用户的 ID，而非必
须是超级用户。接下来，Django 使用这个值来迁移数据库，并生成了迁移文件 0003_topic_owner.py，它在模型 Topic
中添加字段 owner。

现在可以执行迁移了。为此，在活动状态的虚拟环境中执行如下命令：

(ll_env)learning_log$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
❶  Applying learning_logs.0003_topic_owner... OK
(ll_env)learning_log$

Django 应用新的迁移，结果一切顺利（见❶）。

为验证迁移符合预期，可在 shell 会话中像下面这样做：

❶ >>> from learning_logs.models import Topic
❷ >>> for topic in Topic.objects.all():
...       print(topic, topic.owner)
...
Chess ll_admin
Rock Climbing ll_admin
>>>

PS：可用 python manage.py shell 启动 shell。

这里从 learning_logs.models 中导入 Topic（见❶），再遍历所有的既有主题，并打印每个主题及其所属的用户（见❷）。
如你所见，现在每个主题都属于用户 ll_admin。如果你在运行这些代码时出错，请尝试退出并重启 shell。

注意：你可以重置数据库而不是迁移它，但如果这样做，既有的数据都将丢失。一种不错的做法是，学习如何在迁移数据库的同时
确保用户数据的完整性。如果你确实想要一个全新的数据库，可执行命令 python manage.py flush，这将重建数据库的结构。
如果这样做，就必须重新创建超级用户，且原来的所有数据都将丢失。



3、只允许用户访问自己的主题

当前，不管以哪个用户的身份登录，都能够看到所有的主题。下面改变这一点，只向用户显示属于其自己的主题。

在 views.py 中，对函数 topics() 做如下修改：

--snip--
@login_required
def topics(request):
    \"""显示所有的主题。\"""
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)
--snip--

用户登录后，request 对象将有一个 user 属性，其中存储了有关该用户的信息。查询 Topic.objects.filter(owner
=request.user) 让 Django 只从数据库中获取 owner 属性为当前用户的 Topic 对象。由于没有修改主题的显示方式，
无须对显示所有主题的页面的模板做任何修改。

要查看结果，以所有既有主题关联到的用户的身份登录，并访问显示所有主题的页面，你将看到所有的主题。然后，注销并以另
一个用户的身份登录，该页面将不列出任何主题。



4、保护用户的主题

这里还没有限制对显示单个主题的页面的访问，因此任何已登录的用户都可输入类似于 http://localhost:8000/topics
/1/ 的 URL，来访问显示相应主题的页面。

你自己试一试就明白了。以拥有所有主题的用户的身份登录，访问特定的主题，并复制该页面的 URL 或将其中的 ID 记录下来。
然后，注销并以另一个用户的身份登录，再输入显示前述主题的页面的 URL。虽然你是作为另一个用户登录的，但依然能够查看
该主题中的条目。

为修复这种问题，在视图函数 topic() 获取请求的条目前执行检查：

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
❶ from django.http import Http404

--snip--
@login_required
def topic(request, topic_id):
    \"""显示单个主题及其所有的条目。\"""
    topic = Topic.objects.get(id=topic_id)
    # 确认请求的主题属于当前用户。
❷    if topic.owner != request.user:
        raise Http404
    
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)
--snip--

服务器上没有请求的资源时，标准的做法是返回 404 响应。这里导入了异常 Http404（见❶），并在用户请求其不应查看的
主题时引发这个异常。收到主题请求后，在渲染页面前检查该主题是否属于当前登录的用户。如果请求的主题不归当前用户所有，
就引发 Http404 异常（见❷），让 Django 返回一个 404 错误页面。

现在，如果你试图查看其他用户的主题条目，将看到 Django 发送的消息 Page Not Found。后续将对这个项目进行配置，
让用户看到更合适的错误页面。



5、保护页面 edit_entry

页面 edit_entry 的 URL 形式为 http://localhost:8000/edit_entry/entry_id/，其中 entry_id 是一个
数。下面来保护这种页面，禁止用户通过输入类似于前面的 URL 来访问其他用户的条目：

--snip--
@login_required
def edit_entry(request, entry_id):
    \"""编辑既有条目。\"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    if topic.owner != request.user:
        raise Http404

    if request.method != 'POST':
        --snip--

首先获取指定的条目以及与之相关联的主题，再检查主题的所有者是否是当前登录的用户。如果不是，就引发 Http404 异常。



6、将新主题关联到当前用户

当前，用于添加新主题的页面存在问题 —— 没有将新主题关联到特定用户。如果你尝试添加新主题，将看到错误消息 Inte-
grityError，指出 learning_logs_topic.user_id 不能为 NULL（NOT NULL constraint failed: learn-
ing_logs_topic.owner_id）。Django 的意思是说，创建新主题时，必须给 owner 字段指定值。

可通过 request 对象获悉当前用户，因此有一个修复该问题的简单方案。请添加下面的代码，将新主题关联到当前用户：

--snip--
@login_required
def new_topic(request):
    \"""添加新主题。\"""
    if request.method != 'POST':
        # 未提交数据：创建一个新表单。
        form = TopicForm()
    else:
        # POST提交的数据：对数据进行处理。
        form = TopicForm(data=request.POST)
        if form.is_valid():
❶            new_topic = form.save(commit=False)
❷            new_topic.owner = request.user
❸            new_topic.save()
            return redirect('learning_logs:topics')

    # 显示空表单或指出表单数据无效。
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
--snip--

首先调用 form.save() 并传递实参 commit=False（见❶），因为要先修改新主题，再将其保存到数据库。接下来，将
新主题的 owner 属性设置为当前用户（见❷）。最后，对刚定义的主题实例调用 save()（见❸）。现在，主题包含所有
必不可少的数据，将被成功保存。

这个项目现在允许任何用户注册，而每个用户想添加多少新主题都可以。每个用户都只能访问自己的数据，无论是查看数据、
输入新数据还是修改旧数据时都如此。

"""