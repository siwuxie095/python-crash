"""

创建应用程序


Django 项目由一系列应用程序组成，它们协同工作让项目成为一个整体。这里只创建一个应用程序，它将完成项目的大部分工作。
后续将添加一个管理用户账户的应用程序。

当前，在之前打开的终端窗口中应该还运行着 runserver。请再打开一个终端窗口（或标签页），并切换到 manage.py 所在
的目录。激活虚拟环境，再执行命令 startapp：

learning_log$ source ll_env/bin/activate
(ll_env)learning_log$ python manage.py startapp learning_logs
❶ (ll_env)learning_log$ ls
db.sqlite3 learning_log learning_logs ll_env manage.py
❷ (ll_env)learning_log$ ls learning_logs/
__init__.py admin.py apps.py migrations models.py tests.py views.py

命令 startapp appname 让 Django 搭建创建应用程序所需的基础设施。如果现在查看项目目录，将看到其中新增了文件夹
learning_logs（见❶）。打开这个文件夹，看看 Django 都创建了什么（见❷），其中最重要的文件是 models.py、ad-
min.py 和 views.py。这里将使用 models.py 来定义要在应用程序中管理的数据，稍后再介绍 admin.py 和 views.py。



1、定义模型

这里来想想涉及的数据。每位用户都需要在学习笔记中创建很多主题。用户输入的每个条目都与特定主题相关联，这些条目将以文本
的方式显示。还需要存储每个条目的时间戳，以便告诉用户各个条目都是什么时候创建的。

打开文件 models.py，看看它当前包含哪些内容：

from django.db import models

# 在这里创建模型。

这里导入了模块 models，并让你创建自己的模型。模型告诉 Django 如何处理应用程序中存储的数据。在代码层面，模型就是
一个类，就像前面讨论的每个类一样，包含属性和方法。下面是表示用户将存储的主题的模型：

from django.db import models

class Topic(models.Model):
    \"""用户学习的主题。\"""
❶    text = models.CharField(max_length=200)
❷    date_added = models.DateTimeField(auto_now_add=True)

❸    def __str__(self):
        \"""返回模型的字符串表示。\"""
        return self.text

这里创建了一个名为 Topic 的类，它继承 Model，即 Django 中定义了模型基本功能的类。这里给 Topic 类添加了两个
属性：text 和 date_added。

属性 text 是一个 CharField —— 由字符组成的数据，即文本（见❶）。需要存储少量文本，如名称、标题或城市时，可使用
CharField。定义 CharField 属性时，必须告诉 Django 该在数据库中预留多少空间。这里将 max_length 设置成了 200
（即 200 字符），这对存储大多数主题名来说足够了。

属性 date_added 是一个 DateTimeField ——记录日期和时间的数据（见❷）。这里传递了实参 auto_now_add=True，
每当用户创建新主题时，Django 都会将这个属性自动设置为当前日期和时间。

注意：要获悉可在模型中使用的各种字段，请参阅 Django Model Field Reference。就当前而言，你无须全面了解其中的
所有内容，但自己开发应用程序时，这些内容将提供极大的帮助。

需要告诉 Django，默认使用哪个属性来显示有关主题的信息。Django 调用方法 __str__() 来显示模型的简单表示。这里
编写了方法 __str__()，它返回存储在属性 text 中的字符串（见❸）。



2、激活模型

要使用这些模型，必须让 Django 将前述应用程序包含到项目中。为此，打开 settings.py（它位于目录 learning_log/
learning_log 中），其中有个片段告诉 Django 哪些应用程序被安装到了项目中并将协同工作：

--snip--
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
--snip--

请将 INSTALLED_APPS 修改成下面这样，将前面的应用程序添加到这个列表中：

--snip--
INSTALLED_APPS = [
    # 我的应用程序
    'learning_logs',
    # 默认添加的应用程序
    'django.contrib.admin',
    --snip--
]
--snip--

通过将应用程序编组，在项目不断增大，包含更多的应用程序时，有助于对应用程序进行跟踪。这里新建了一个名为 “我的应用程序”
的片段，当前它只包含应用程序 learning_logs。务必将自己创建的应用程序放在默认应用程序前面，这样能够覆盖默认应用程序
的行为。

接下来，需要让 Django 修改数据库，使其能够存储与模型 Topic 相关的信息。为此，在终端窗口中执行下面的命令：

(ll_env)learning_log$ python manage.py makemigrations learning_logs
Migrations for 'learning_logs':
  learning_logs/migrations/0001_initial.py
    - Create model Topic
(ll_env)learning_log$

命令 makemigrations 让 Django 确定该如何修改数据库，使其能够存储与前面定义的新模型相关联的数据。输出表明 Django
创建了一个名为 0001_initial.py 的迁移文件，这个文件将在数据库中为模型 Topic 创建一个表。

下面应用这种迁移，让 Django 替你修改数据库：

(ll_env)learning_log$ python manage.py migrate
Operations to perform:
   Apply all migrations: admin, auth, contenttypes, learning_logs, sessions
Running migrations:
❶  Applying learning_logs.0001_initial... OK

这个命令的大部分输出与首次执行命令 migrate 的输出相同。需要检查的是❶处的输出行。在这里，Django 指出为 learning-
_logs 应用迁移时一切正常。

每当需要修改 “学习笔记” 管理的数据时，都采取如下三个步骤：修改 models.py，对 learning_logs 调用 makemigrations，
以及让 Django 迁移项目。



3、Django 管理网站

Django 提供的管理网站（admin site）让你能够轻松地处理模型。网站管理员可以使用管理网站，但普通用户不能使用。这里将
建立管理网站，并通过它使用模型 Topic 来添加一些主题。


a. 创建超级用户

Django 允许创建具备所有权限的用户，即超级用户。权限决定了用户可执行的操作。最严格的权限设置只允许用户阅读网站的公开
信息。注册用户通常可阅读自己的私有数据，还可查看一些只有会员才能查看的信息。为有效地管理 Web 应用程序，网站所有者通
常需要访问网站存储的所有信息。优秀的管理员会小心对待用户的敏感信息，因为用户极其信任自己访问的应用程序。

为在 Django 中创建超级用户，请执行下面的命令并按提示做：

(ll_env)learning_log$ python manage.py createsuperuser
❶ Username (leave blank to use 'eric'): ll_admin
❷ Email address:
❸ Password:
Password (again):
Superuser created successfully.
(ll_env)learning_log$

你执行命令 createsuperuser 时，Django 提示输入超级用户的用户名（见❶）。这里输入的是 ll_admin，但可输入任何用
户名。如果你愿意，可以输入电子邮箱地址，也可让这个字段为空（见❷）。需要输入密码两次（见❸）。

注意：一些敏感信息可能会向网站管理员隐藏。例如，Django 并不存储你输入的密码，而是存储从该密码派生出来的一个字符串，
称为散列值。每当你输入密码时，Django 都计算其散列值，并将结果与存储的散列值进行比较。如果这两个散列值相同，你就通过
了身份验证。由于存储的是散列值，即便黑客获得了网站数据库的访问权，也只能获取其中存储的散列值，无法获得密码。在网站配
置正确的情况下，几乎无法根据散列值推导出原始密码。


b. 向管理网站注册模型

Django 自动在管理网站中添加了一些模型，如 User 和 Group，但对于自己创建的模型，必须手工进行注册。

之前创建应用程序 learning_logs 时，Django 在 models.py 所在的目录中创建了一个名为 admin.py 的文件：

from django.contrib import admin

# 在这里注册你的模型。

为向管理网站注册 Topic，请输入下面的代码：

from django.contrib import admin

❶ from .models import Topic

❷ admin.site.register(Topic)

这些代码首先导入要注册的模型 Topic（见❶）。models 前面的句点让 Django 在 admin.py 所在的目录中查找 models
.py。admin.site.register() 让 Django 通过管理网站管理模型（见❷）。

现在，使用超级用户账户访问管理网站：访问 http://localhost:8000/admin/，并输入刚创建的超级用户的用户名和密码。
你将看到的这个页面让你能够添加和修改用户和用户组，还可管理与刚才定义的模型 Topic 相关的数据。

注意：如果在浏览器中看到一条消息，指出访问的网页不可用，请确认在终端窗口中运行着 Django 服务器。如果没有，请激活
虚拟环境，并执行命令 python manage.py runserver。在开发过程中，如果无法通过浏览器访问项目，首先应采取的故障
排除措施是，关闭所有打开的终端，再打开终端并执行命令 runserver。


c. 添加主题

向管理网站注册 Topic 后，下面来添加第一个主题。为此，单击 Topics 进入主题页面，它几乎是空的，因为还没有添加任何
主题。单击 Add，将出现一个用于添加新主题的表单。在第一个方框中输入 Chess，再单击 Save 回到主题管理页面，其中包
含刚创建的主题。

下面再创建一个主题，以便有更多的数据可供使用。再次单击 Add，并输入 Rock Climbing，然后单击 Save 回到主题管理
页面。现在，你可以看到其中包含了主题 Chess 和 Rock Climbing。



4、定义模型 Entry

要记录学到的国际象棋和攀岩知识，用户必须能够在学习笔记中添加条目。为此，需要定义相关的模型。每个条目都与特定主题相
关联，这种关系称为多对一关系，即多个条目可关联到同一个主题。

下面是模型 Entry 的代码，请将这些代码放在文件 models.py 中：

from django.db import models

# Create your models here.
from django.db import models

class Topic(models.Model):
    --snip--

❶ class Entry(models.Model):
    \"""学到的有关某个主题的具体知识。\"""
❷    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
❸    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

❹    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        \"""返回模型的字符串表示。\"""
❺        return f"{self.text[:50]}..."

像 Topic 一样，Entry 也继承了 Django 基类 Model（见❶）。第一个属性 topic 是个 ForeignKey 实例（见❷）。
外键（foreign key）是一个数据库术语，它指向数据库中的另一条记录，这里是将每个条目关联到特定主题。创建每个主题
时，都分配了一个键（ID）。需要在两项数据之间建立联系时，Django 使用与每项信息相关联的键。稍后将根据这些联系获取
与特定主题相关联的所有条目。实参 on_delete=models.CASCADE 让 Django 在删除主题的同时删除所有与之相关联的
条目，这称为级联删除（cascading delete）。

接下来是属性 text，它是一个 TextField 实例（见❸）。这种字段的长度不受限制，因为这里不想限制条目的长度。属性
date_added 能够按创建顺序呈现条目，并在每个条目旁边放置时间戳。

在❹处，在 Entry 类中嵌套了 Meta 类。Meta 存储用于管理模型的额外信息。在这里，它让你能够设置一个特殊属性，让
Django 在需要时使用 Entries 来表示多个条目。如果没有这个类，Django 将使用 Entrys 来表示多个条目。

方法 __str__() 告诉 Django，呈现条目时应显示哪些信息。条目包含的文本可能很长，因此让 Django 只显示 text
的前50字符（见❺）。这里还添加了一个省略号，指出显示的并非整个条目。



5、迁移模型 Entry

添加新模型后，需要再次迁移数据库。你将慢慢地对这个过程了如指掌：修改 models.py，执行命令 python manage.py
makemigrations app_name，再执行命令 python manage.py migrate。

请使用如下命令迁移数据库并查看输出：

(ll_env)learning_log$ python manage.py makemigrations learning_logs
Migrations for 'learning_logs':
❶  learning_logs/migrations/0002_entry.py
    - Create model Entry
(ll_env)learning_log$ python manage.py migrate
Operations to perform:
  --snip--
❷  Applying learning_logs.0002_entry... OK

生成了一个新的迁移文件 0002_entry.py，它告诉 Django 如何修改数据库，使其能够存储与模型 Entry 相关的信息
（见❶）。在❷处执行命令 migrate，不难发现 Django 应用了该迁移且一切顺利。



6、向管理网站注册 Entry

这里还需要注册模型 Entry。为此，需要将 admin.py 修改成类似于下面这样：

from django.contrib import admin

from .models import Topic, Entry

admin.site.register(Topic)
admin.site.register(Entry)

返回到 http://localhost/admin/，你将看到 Learning_Logs 下列出了 Entries。单击 Entries 的 Add 链接，
或者单击 Entries 再选择 Add entry，将看到一个下拉列表，供你选择要为哪个主题创建条目，以及一个用于输入条目的
文本框。从下拉列表中选择 Chess，并添加一个条目。下面是添加的第一个条目。

The opening is the first part of the game, roughly the first ten moves or so. In the opening,
it's a good idea to do three things— bring out your bishops and knights, try to control the
center of the board, and castle your king.（国际象棋的第一个阶段是开局，大致是前 10 步左右。在开局阶段，
最好做三件事情：将象和马调出来，努力控制棋盘的中间区域，以及用车将王护住。）

Of course, these are just guidelines. It will be important to learn when to follow these
guidelines and when to disregard these suggestions.（当然，这些只是指导原则。学习什么情况下遵守这些
原则、什么情况下不用遵守很重要。）

当你单击 Save 时，将返回到主条目管理页面。在这里，你将发现使用 text[:50] 作为条目的字符串表示的好处：在管理
界面中只显示了条目的开头部分而不是其所有文本，这使得管理多个条目容易得多。

再来创建一个国际象棋条目，并创建一个攀岩条目，以提供一些初始数据。下面是第二个国际象棋条目。

In the opening phase of the game, it's important to bring out your bishops and knights.
These pieces are powerful and maneuverable enough to play a significant role in the
beginning moves of a game.（在国际象棋的开局阶段，将象和马调出来很重要。这些棋子威力大，机动性强，在开局
阶段扮演着重要角色。）

下面是第一个攀岩条目。

One of the most important concepts in climbing is to keep your weight on your feet as
much as possible. There's a myth that climbers can hang all day on their arms. In reality,
good climbers have practiced specific ways of keeping their weight over their feet
whenever possible.（最重要的攀岩概念之一是尽可能让双脚承受体重。有人误认为攀岩者能依靠手臂的力量坚持一整天。
实际上，优秀的攀岩者都经过专门训练，能够尽可能让双脚承受体重。）

接着往下开发 “学习笔记” 时，这三个条目提供了可供使用的数据。



7、Django shell

输入一些数据后，就可通过交互式终端会话以编程方式查看这些数据了。这种交互式环境称为 Django shell，是测试项目
和排除故障的理想之地。下面是一个交互式 shell 会话示例：

(ll_env)learning_log$ python manage.py shell
❶ >>> from learning_logs.models import Topic
>>> Topic.objects.all()
 <QuerySet [<Topic: Chess>, <Topic: Rock Climbing>]>

在活动状态的虚拟环境中执行时，命令 python manage.py shell 启动 Python 解释器，让你能够探索存储在项目
数据库中的数据。这里导入了模块 learning_logs.models 中的模型 Topic（见❶），再使用方法 Topic.objects.
all() 获取模型 Topic 的所有实例，这将返回一个称为查询集（queryset）的列表。

可以像遍历列表一样遍历查询集。下面演示了如何查看分配给每个主题对象的 ID：

>>> topics = Topic.objects.all()
>>> for topic in topics:
... print(topic.id, topic)
...
1 Chess
2 Rock Climbing

将返回的查询集存储在 topics 中，再打印每个主题的 id 属性和字符串表示。从输出可知，主题 Chess 的 ID 为 1，
而 Rock Climbing 的 ID 为 2。

知道主题对象的 ID 后，就可使用方法 Topic.objects.get() 获取该对象并查看其属性。下面来看看主题 Chess 的
属性 text 和 date_added 的值：

>>> t = Topic.objects.get(id=1)
>>> t.text
'Chess'
>>> t.date_added
datetime.datetime(2019, 2, 19, 1, 55, 31, 98500, tzinfo=<UTC>)

还可以查看与主题相关联的条目。前面给模型 Entry 定义了属性 topic。这是一个 ForeignKey，将条目与主题关联
起来。利用这种关联，Django 能够获取与特定主题相关联的所有条目，如下所示：

❶ >>> t.entry_set.all()
<QuerySet [<Entry: The opening is the first part of the game, roughly...>, <Entry:
In the opening phase of the game, it's important t...>]>

要通过外键关系获取数据，可使用相关模型的小写名称、下划线和单词 set（见❶）。例如，假设有模型 Pizza 和 Top-
ping，而 Topping 通过一个外键关联到 Pizza。

如果有一个名为 my_pizza 的 Pizza 对象，就可使用代码 my_pizza.topping_set.all() 来获取这张比萨的
所有配料。

编写用户可请求的页面时，将使用这种语法。确认代码能获取所需的数据时，shell 很有帮助。如果代码在 shell 中的行为
符合预期，那么它们在项目文件中也能正确地工作。如果代码引发了错误或获取的数据不符合预期，那么在简单的 shell 环境
中排除故障要比在生成页面的文件中排除故障容易得多。这里不会太多地使用 shell，但应继续使用它来熟悉对存储在项目中
的数据进行访问的 Django 语法。

注意：每次修改模型后，都需要重启 shell，这样才能看到修改的效果。要退出 shell 会话，可按 Ctr + D。如果你使用
的是 Windows 系统，应按 Ctr + Z，再按回车键。

"""