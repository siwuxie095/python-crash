"""

创建用户账户


这里将建立用户注册和身份验证系统，让用户能够注册账户，进而登录和注销。为此，将新建一个应用程序，其中包含与处理用户账户
相关的所有功能。这个应用程序将尽可能使用 Django 自带的用户身份验证系统来完成工作。这里还将对模型 Topic 稍做修改，让
每个主题都归属于特定用户。



1、应用程序 users

首先使用命令 startapp 创建一个名为 users 的应用程序：

(ll_env)learning_log$ python manage.py startapp users
(ll_env)learning_log$ ls
❶ db.sqlite3 learning_log learning_logs ll_env manage.py users
(ll_env)learning_log$ ls users
❷ __init__.py admin.py apps.py migrations models.py tests.py views.py

这个命令新建一个名为 users 的目录（见❶），其结构与应用程序 learning_logs 相同（见❷）。



2、将 users 添加到 settings.py 中

在 settings.py 中，需要将这个新的应用程序添加到 INSTALLED_APPS 中，如下所示：

--snip--
INSTALLED_APPS = [
    # 我的应用程序
    'learning_logs',
    'users',
    # 默认添加的应用程序
    --snip--
]

这样，Django 将把应用程序 users 包含到项目中。



3、包含 users 的 URL

接下来，需要修改项目根目录中的 urls.py，使其包含将为应用程序 users 定义的 URL：

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learning_logs.urls')),
    path('users/', include('users.urls')),
]

这里添加了一行代码，以包含应用程序 users 中的文件 urls.py。这行代码与任何以单词 users 打头的 URL（如 http://
localhost:8000/users/login/）都匹配。



4、登录页面

首先来实现登录页面。这里将使用 Django 提供的默认视图 login，因此这个应用程序的 URL 模式稍有不同。在目录 learning-
_log/users/ 中，新建一个名为 urls.py 的文件，并在其中添加如下代码：

\"""为应用程序users定义URL模式。\"""

from django.urls import path, include

❶ app_name = 'users'

urlpatterns = [
    # 包含默认的身份验证URL。
❷    path('', include('django.contrib.auth.urls')),
]

导入函数 path 和 include，以便包含 Django 定义的一些默认的身份验证 URL。这些默认的 URL 包含具名的 URL 模式，
如 'login' 和 'logout'。这里将变量 app_name 设置成 'users'，让 Django 能够将这些 URL 与其他应用程序的
URL 区分开来（见❶）。即便是 Django 提供的默认 URL，将其包含在应用程序 users 的文件中后，也可通过命名空间 users
进行访问。

登录页面的 URL 模式与 URL http://localhost:8000/users/login/ 匹配（见❷）。这个 URL 中的单词 users 让
Django 在 users/urls.py 中查找，而单词 login 让它将请求发送给 Django 的默认视图 login。


α. 模板 login.html

用户请求登录页面时，Django 将使用一个默认的视图函数，但依然需要为这个页面提供模板。默认的身份验证视图在文件夹 reg-
istration 中查找模板，因此需要创建这个文件夹。为此，在目录 learning_log/users/ 中新建一个名为 templates 的
目录，再在这个目录中新建一个名为 registration 的目录。下面是模板 login.html，应将其存储到目录 learning_log/
users/templates/registration 中：

{% extends "learning_logs/base.html" %}

{% block content %}

❶    {% if form.errors %}
        <p>Your username and password didn't match. Please try again.</p>
    {% endif %}

❷    <form method="post" action="{% url 'users:login' %}">
        {% csrf_token %}
❸        {{ form.as_p }}
❹        <button name="submit">Log in</button>
❺        <input type="hidden" name="next" value="{% url 'learning_logs:index' %}"/>
    </form>

{% endblock content %}

这个模板继承了 base.html，旨在确保登录页面的外观与网站的其他页面相同。请注意，一个应用程序中的模板可继承另一个应用
程序中的模板。

如果设置表单的 errors 属性，就显示一条错误消息（见❶），指出输入的用户名密码对与数据库中存储的任何用户名密码对都不
匹配。

这里要让登录视图对表单进行处理，因此将实参 action 设置为登录页面的 URL（见❷）。登录视图将一个表单发送给模板。在模
板中，显示这个表单（见❸）并添加一个提交按钮（见❹）。在❺处，包含了一个隐藏的表单元素 'next'，其中的实参 value 告
诉 Django 在用户成功登录后将其重定向到什么地方。在本例中，用户将返回主页。


β. 链接到登录页面

下面在 base.html 中添加到登录页面的链接，让所有页面都包含它。用户已登录时，这里不想显示这个链接，因此将它嵌套在一
个 {% if %} 标签中：

<p>
    <a href="{% url 'learning_logs:index' %}">Learning Log</a> -
    <a href="{% url 'learning_logs:topics' %}">Topics</a> -
❶    {% if user.is_authenticated %}
❷    Hello, {{ user.username }}.
    {% else %}
❸        <a href="{% url 'users:login' %}">Log in</a>
  {% endif %}
</p>

{% block content %}{% endblock content %}

在 Django 身份验证系统中，每个模板都可使用变量 user。这个变量有一个 is_authenticated 属性：如果用户已登录，该
属性将为 True，否则为 False。这让你能够向已通过身份验证的用户显示一条消息，而向未通过身份验证的用户显示另一条消息。

这里向已登录的用户显示问候语（见❶）。对于已通过身份验证的用户，还设置了属性 username。这里使用该属性来个性化问候语，
让用户知道自己已登录（见❷）。在❸处，对于尚未通过身份验证的用户，显示到登录页面的链接。


γ. 使用登录页面

前面建立了一个用户账户，下面来登录一下，看看登录页面是否管用。请访问 http://localhost:8000/admin/，如果你依然
是以管理员身份登录的，请在页眉上找到注销链接并单击它。

注销后，访问 http://localhost:8000/users/login/ 将看到登录页面。输入你在前面设置的用户名和密码，将进入索引页
面。在这个主页的页眉中，显示了一条个性化问候语，其中包含你的用户名。



5、注销

现在需要提供一个让用户注销的途径。为此，将在 base.html 中添加一个注销链接。用户单击这个链接时，将进入一个确认其已
注销的页面。


α. 在 base.html 中添加注销链接

下面在 base.html 中添加注销链接，让每个页面都包含它。将注销链接放在 {% if user.is_authenticated %} 部分中，
这样只有已登录的用户才能看到它：

--snip--
    {% if user.is_authenticated %}
    Hello, {{ user.username }}.
        <a href="{% url 'users:logout' %}">Log out</a>
    {% else %}
--snip--

默认的具名注销 URL 模式为 'logout'。


β. 注销确认页面

成功注销后，用户希望获悉这一点。因此默认的注销视图使用模板 logged_out.html 渲染注销确认页面，现在就来创建该模板。
下面这个简单的页面确认用户已注销，请将其存储到目录 templates/registration（login.html 所在的目录）中：

{% extends "learning_logs/base.html" %}

{% block content %}
    <p>You have been logged out. Thank you for visiting!</p>
{% endblock content %}

在这个页面中，不需要提供其他内容，因为 base.html 提供了到主页和登录页面的链接。

这样就能显示用户单击 Log out 链接后出现的注销确认页面。这里的重点是创建能够正确工作的网站，因此几乎没有设置样式。
确定所需的功能都能正确运行后，将设置这个网站的样式，使其看起来更专业。



6、注册页面

下面来创建一个页面供新用户注册。这里将使用 Django 提供的表单 UserCreationForm，但需要编写自己的视图函数和模
板。


α. 注册页面的 URL 模式

下面的代码定义了注册页面的 URL 模式，它也包含在 users/urls.py 中：

\"""为应用程序users定义URL模式。\"""

from django.urls import path, include

from . import views

app_name = 'users'

urlpatterns = [
    # 包含默认的身份验证URL。
    path('', include('django.contrib.auth.urls')),
    # 注册页面
    path('register/', views.register, name='register'),
]

这里从 users 中导入模块 views。为何需要这样做呢？因为需要将为注册页面编写视图函数。注册页面的 URL 模式与 URL
http://localhost:8000/users/register/ 匹配，并将请求发送给即将编写的函数 register()。


β. 视图函数 register()

在注册页面首次被请求时，视图函数 register() 需要显示一个空的注册表单，并在用户提交填写好的注册表单时对其进行处
理。如果注册成功，这个函数还需让用户自动登录。请在 users/views.py 中添加如下代码：

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    \"""注册新用户。\"""
    if request.method != 'POST':
        # 显示空的注册表单。
❶        form = UserCreationForm()
    else:
        # 处理填写好的表单。
❷        form = UserCreationForm(data=request.POST)

❸        if form.is_valid():
❹            new_user = form.save()
            # 让用户自动登录，再重定向到主页。
❺            login(request, new_user)
❻            return redirect('learning_logs:index')

    # 显示空表单或指出表单无效。
    context = {'form': form}
    return render(request, 'registration/register.html', context)

首先导入函数 render() 和 redirect()，然后导入函数 login()，以便在用户正确填写了注册信息时让其自动登录。还
导入了默认表单 UserCreationForm。在函数 register() 中，检查要响应的是否是 POST 请求。如果不是，就创建一
个 UserCreationForm 实例，且不给它提供任何初始数据（见❶）。

如果响应的是 POST 请求，就根据提交的数据创建一个 UserCreationForm 实例（见❷），并检查这些数据是否有效（见❸）。
就本例而言，有效是指用户名未包含非法字符，输入的两个密码相同，以及用户没有试图做恶意的事情。

如果提交的数据有效，就调用表单的方法 save()，将用户名和密码的散列值保存到数据库中（见❹）。方法 save() 返回新
创建的用户对象，这里将它赋给了 new_user。保存用户的信息后，调用函数 login() 并传入对象 request 和 new_user，
为用户创建有效的会话，从而让其自动登录（见❺）。最后，将用户重定向到主页（见❻），而主页的页眉中显示了一条个性化的
问候语，让用户知道注册成功了。

在这个函数的末尾，渲染了注册页面：它要么显示一个空表单，要么显示提交的无效表单。


γ. 注册模板

下面来创建注册页面的模板，它与登录页面的模板类似。请务必将其保存到 login.html 所在的目录中：

{% extends "learning_logs/base.html" %}

{% block content %}

    <form method="post" action="{% url 'users:register' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button name="submit">Register</button>
        <input type="hidden" name="next" value="{% url 'learning_logs:index' %}"/>
    </form>

{% endblock content %}

这里也使用了方法 as_p，让 Django 在表单中正确地显示所有的字段，包括错误消息 —— 如果用户没有正确地填写表单。


δ. 链接到注册页面

--snip--
    {% if user.is_authenticated %}
    Hello, {{ user.username }}.
        <a href="{% url 'users:logout' %}">Log out</a>
    {% else %}
        <a href="{% url 'users:register' %}">Register</a> -
        <a href="{% url 'users:login' %}">Log in</a>
  {% endif %}
--snip--

现在，已登录的用户看到的是个性化的问候语和注销链接，而未登录的用户看到的是注册链接和登录链接。请尝试使用注册页面
创建几个用户名各不相同的用户账户。

后续会将一些页面限制为仅让已登录的用户访问，还将确保每个主题都归属于特定用户。

注意：这里的注册系统允许用户创建任意数量的账户。有些系统要求用户确认其身份：发送一封确认邮件，用户回复后账户才生
效。通过这样做，这些系统会比本例的简单系统生成更少的垃圾账户。然而，学习创建应用程序时，完全可以像这里所做的那样，
使用简单的用户注册系统。

"""