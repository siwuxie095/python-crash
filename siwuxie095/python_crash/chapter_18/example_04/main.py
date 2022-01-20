"""

创建页面：学习笔记主页


使用 Django 创建页面的过程分三个阶段：定义 URL，编写视图和编写模板。按什么顺序完成这三个阶段无关紧要，但在本项目中，
总是先定义 URL 模式。URL 模式描述了 URL 是如何设计的，让 Django 知道如何将浏览器请求与网站 URL 匹配，以确定返回
哪个页面。

每个 URL 都被映射到特定的视图 —— 视图函数获取并处理页面所需的数据。视图函数通常使用模板来渲染页面，而模板定义页面的
总体结构。为明白其中的工作原理，这里来创建学习笔记的主页。这包括定义该主页的 URL，编写其视图函数并创建一个简单的模板。

只是要确保 “学习笔记” 按要求的那样工作，因此暂时让这个页面尽可能简单。Web 应用程序能够正常运行后，设置样式可使其更
有趣，但中看不中用的应用程序毫无意义。就目前而言，主页只显示标题和简单的描述。



1、映射 URL

用户通过在浏览器中输入 URL 以及单击链接来请求页面，因此要确定项目需要哪些 URL。主页的 URL 最重要，它是用户用来访问
项目的基础 URL。当前，基础 URL（http://localhost:8000/）返回默认的 Django 网站，让你知道正确地建立了项目。下
面修改这一点，将这个基础 URL 映射到 “学习笔记” 的主页。

打开项目主文件夹 learning_log 中的文件 urls.py，你将看到如下代码：

❶ from django.contrib import admin
from django.urls import path

❷ urlpatterns = [
❸    path('admin/', admin.site.urls),
]

前两行导入了一个模块和一个函数，以便对管理网站的 URL 进行管理（见❶）。这个文件的主体定义了变量 urlpatterns（见❷）。
在这个针对整个项目的 urls.py 文件中，变量 urlpatterns 包含项目中应用程序的 URL。❸处的代码包含模 块admin.site
.urls，该模块定义了可在管理网站中请求的所有 URL。

这里需要包含 learning_logs 的 URL，因此添加如下代码：

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
❶    path('', include('learning_logs.urls')),
]

在❶处，添加一行代码来包含模块 learning_logs.urls。

默认的 urls.py 包含在文件夹 learning_log 中，现在需要在文件夹 learning_logs 中再创建一个 urls.py 文件。为此，
新建一个文件，使用文件名 urls.py 将其存储到文件夹 learning_logs 中，再在这个文件中输入如下代码：

❶ \"""定义learning_logs的URL模式。\"""

❷ from django.urls import path

❸ from . import views

❹ app_name = 'learning_logs'
❺ urlpatterns = [
    # 主页
❻    path('', views.index, name='index'),
]

为指出当前位于哪个 urls.py 文件中，在该文件开头添加一个文档字符串（见❶）。接下来，导入了函数 path，因为需要使用它
将 URL 映射到视图（见❷）。这里还导入了模块views（见❸），其中的句点让 Python 从当前 urls.py 模块所在的文件夹导
入 views.py。变量 app_name 让 Django 能够将这个 urls.py 文件同项目内其他应用程序中的同名文件区分开来（见❹）。
在这个模块中，变量 urlpatterns 是一个列表，包含可在应用程序 learning_logs 中请求的页面。

实际的 URL 模式是对函数 path() 的调用，这个函数接受三个实参（见❺）。第一个是一个字符串，帮助 Django 正确地路由
（route）请求。收到请求的 URL 后，Django 力图将请求路由给一个视图。为此，它搜索所有的 URL 模式，找到与当前请求
匹配的那个。Django 忽略项目的基础 URL（http://localhost:8000/），因此空字符串（''）与基础 URL 匹配。其他
URL 都与这个模式不匹配。如果请求的 URL 与任何既有的 URL 模式都不匹配，Django 将返回一个错误页面。

path() 的第二个实参（见❻）指定了要调用 view.py 中的哪个函数。请求的 URL 与前述正则表达式匹配时，Django 将调用
view.py 中的函数 index()（这个视图函数将在下面编写）。第三个实参将这个 URL 模式的名称指定为 index，使得能够在
代码的其他地方引用它。每当需要提供到这个主页的链接时，都将使用这个名称，而不编写 URL。



2、编写视图

视图函数接受请求中的信息，准备好生成页面所需的数据，再将这些数据发送给浏览器 —— 这通常是使用定义页面外观的模板实现的。

learning_logs 中的文件 views.py 是执行命令 python manage.py startapp 时自动生成的，当前其内容如下：

from django.shortcuts import render

# 在这里创建视图。

当前，这个文件只导入了函数 render()，它根据视图提供的数据渲染响应。请在这个文件中添加为主页编写视图的代码，如下所示：

from django.shortcuts import render

def index(request):
    \"""学习笔记的主页。\"""
    return render(request, 'learning_logs/index.html')

URL 请求与刚才定义的模式匹配时，Django 将在文件 views.py 中查找函数 index()，再将对象 request 传递给这个视图
函数。这里不需要处理任何数据，因此这个函数只包含调用 render() 的代码。这里向函数 render() 提供了两个实参：对象
request 以及一个可用于创建页面的模板。下面来编写这个模板。



3、编写模板

模板定义页面的外观，而每当页面被请求时，Django 将填入相关的数据。模板让你能够访问视图提供的任何数据。这里的主页视图
没有提供任何数据，因此相应的模板非常简单。

在文件夹 learning_logs 中新建一个文件夹，并将其命名为 templates。在文件夹 templates 中，再新建一个文件夹，并
将其命名为 learning_logs。这好像有点多余（在文件夹 learning_logs 中创建文件夹 templates，又在这个文件夹中创
建文件夹 learning_logs），但是建立了 Django 能够明确解读的结构，即便项目很大、包含很多应用程序亦如此。在最里面
的文件夹 learning_logs 中，新建一个文件，并将其命名为 index.html（这个文件的路径为 learning_log/learning-
_logs/templates/learning_logs/index.html），再在其中编写如下代码：

<p>Learning Log</p>
<p>Learning Log helps you keep track of your learning, for any topic you're learning about.</p>

这个文件非常简单。这里向不熟悉 HTML 的解释一下：标签 <p></p> 标识段落。标签 <p> 指出段落的开头位置，而标签 </p>
指出段落的结束位置。这里定义了两个段落：第一个充当标题，第二个阐述了用户可使用 “学习笔记” 来做什么。

现在，如果请求这个项目的基础URL http://localhost:8000/，将看到刚才创建的页面，而不是默认的 Django 页面。

Django接受请求的 URL，发现该URL与模式 '' 匹配，因此调用函数 views.index()。这将使用 index.html 包含的模板来
渲染页面。

创建页面的过程看起来可能很复杂，但将 URL、视图和模板分离的效果很好。这让你能够分别考虑项目的不同方面，在项目很大时，
可让各个参与者专注于最擅长的方面。例如，数据库专家专注于模型，程序员专注于视图代码，而 Web 设计人员专注于模板。

注意，可能出现如下错误消息：

ModuleNotFoundError: No module named 'learning_logs.urls'

如果确实如此，请在执行命令 python manage.py runserver 的终端窗口中按 Ctrl + C 停用服务器，再重新执行这个命令。
这样做后，应该能够看到主页。每当遇到类似的错误时，都尝试停用并重启服务器，看看是否管用。

"""