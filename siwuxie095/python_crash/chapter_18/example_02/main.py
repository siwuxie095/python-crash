"""

建立项目


建立项目时，首先需要以规范的方式对项目进行描述，再建立虚拟环境，以便在其中创建项目。



1、制定规范

完整的规范详细说明了项目的目标，阐述了项目的功能，并讨论了项目的外观和用户界面。与任何良好的项目规划和商业计划书
一样，规范应突出重点，帮助避免项目偏离轨道。这里不会制定完整的项目规划，只列出一些明确的目标，以突出开发的重点。
制定的规范如下：

这里要编写一个名为 “学习笔记” 的 Web 应用程序，让用户能够记录感兴趣的主题，并在学习每个主题的过程中添加日志条
目。“学习笔记” 的主页对这个网站进行描述，并邀请用户注册或登录。用户登录后，可以创建新主题、添加新条目以及阅读既
有的条目。

学习新的主题时，记录学到的知识可帮助跟踪和复习这些知识。优秀的应用程序让这个记录过程简单易行。



2、建立虚拟环境

要使用 Django，首先需要建立一个虚拟工作环境。虚拟环境是系统的一个位置，可在其中安装包，并将之与其他 Python 包
隔离。将项目的库与其他项目分离是有益的，并且为了在后续将 “学习笔记” 部署到服务器，这也是必需的。

为项目新建一个目录，将其命名为 learning_log，再在终端中切换到这个目录，并执行如下命令创建一个虚拟环境：

learning_log$ python -m venv ll_env
learning_log$

这里运行了模块 venv，并使用它创建了一个名为 ll_env 的虚拟环境（请注意，ll_env 的开头是两个小写字母 l，而不
是数字 1）。如果你运行程序或安装包时使用的是命令 python3，这里也务必使用同样的命令。如下：

python3 -m venv ll_env



3、激活虚拟环境

现在需要使用下面的命令激活虚拟环境：

learning_log$ source ll_env/bin/activate
❶ (ll_env)learning_log$

这个命令运行 ll_env/bin 中的脚本 activate。环境处于活动状态时，环境名将包含在圆括号内，如❶处所示。在这种情
况下，你可以在环境中安装包，并使用已安装的包。在 ll_env 中安装的包仅在该环境处于活动状态时才可用。

注意：如果你使用的是 Windows 系统，请使用命令 ll_env\Scripts\activate（不包含 source）来激活这个虚拟环
境。如果你使用的是 PowerShell，可能需要将 Activate 的首字母大写。

要停止使用虚拟环境，可执行命令 deactivate：

(ll_env)learning_log$ deactivate
learning_log$

如果关闭运行虚拟环境的终端，虚拟环境也将不再处于活动状态。



4、安装 Django

(ll_env)learning_log$ pip install django
Collecting django
 --snip--
Installing collected packages: pytz, django
Successfully installed django-2.2.0 pytz-2018.9 sqlparse-0.2.4
(ll_env)learning_log$

由于是在虚拟环境（独立的环境）中工作，在各种系统中安装 Django 的命令都相同：不需要指定标志 --user，也不需要
使用像 python -m pip install package_name 这样较长的命令。

别忘了，Django 仅在虚拟环境 ll_env 处于活动状态时才可用。

注意：每隔大约 8 个月，Django 新版本就会发布，因此在你安装 Django 时，看到的可能是更新的版本。即便你使用的
是更新的 Django 版本，这个项目也可行。如果要使用这里所示的 Django 版本，请使用命令 pip install django
==2.2.* 安装 Django 2.2 的最新版本。



5、在 Django 中创建项目

在虚拟环境依然处于活动状态的情况下（ll_env 包含在圆括号内），执行如下命令新建一个项目：

❶ (ll_env)learning_log$ django-admin startproject learning_log .
❷ (ll_env)learning_log$ ls
 learning_log ll_env manage.py
❸ (ll_env)learning_log$ ls learning_log
__init__.py settings.py urls.py wsgi.py

PS：实际只需要执行 django-admin startproject learning_log .

❶处的命令让 Django 新建一个名为 learning_log 的项目。这个命令末尾的句点让新项目使用合适的目录结构，这样
开发完成后可轻松地将应用程序部署到服务器。

注意：千万别忘了这个句点，否则部署应用程序时将遭遇一些配置问题。如果忘记了这个句点，要删除已创建的文件和文件夹
（ll_env 除外），再重新运行这个命令。

在❷处，运行命令 ls（在 Windows 系统上为 dir），结果表明 Django 新建了一个名为 learning_log 的目录，还
创建了文件 manage.py。后者是一个简单的程序，接受命令并将其交给 Django 的相关部分运行。这里将使用这些命令来
管理使用数据库和运行服务器等任务。

目录 learning_log 包含 4 个文件（见❸），最重要的是 settings.py、urls.py 和 wsgi.py。文件 settings
.py 指定 Django 如何与系统交互以及如何管理项目。在开发项目的过程中，将修改其中一些设置，并添加一些设置。文件
urls.py 告诉 Django，应创建哪些页面来响应浏览器请求。文件 wsgi.py 帮助 Django 提供它创建的文件，这个文件
名是 Web 服务器网关接口（Web server gateway interface）的首字母缩写。



6、创建数据库

Django 将大部分与项目相关的信息存储在数据库中，因此需要创建一个供 Django 使用的数据库。为给项目 “学习笔记”
创建数据库，请在虚拟环境处于活动状态的情况下执行下面的命令：

(ll_env)learning_log$ python manage.py migrate
❶ Operations to perform:
   Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  --snip--
  Applying sessions.0001_initial... OK
❷ (ll_env)learning_log$ ls
 db.sqlite3 learning_log ll_env manage.py

PS：实际只需要执行 python manage.py migrate

这里将修改数据库称为迁移（migrate）数据库。首次执行命令 migrate 时，将让 Django 确保数据库与项目的当前状态
匹配。在使用 SQLite（后续将详细介绍）的新项目中首次执行这个命令时，Django 将新建一个数据库。在❶处，Django
指出它将准备好数据库，用于存储执行管理和身份验证任务所需的信息。

在❷处运行命令 ls，其输出表明 Django 又创建了一个文件 db.sqlite3。SQLite 是一种使用单个文件的数据库，是编
写简单应用程序的理想选择，因为它让你不用太关注数据库管理的问题。

注意：在虚拟环境中运行 manage.py 时，务必使用命令 python，即便你在运行其他程序时使用的是另外的命令，
如 python3。在虚拟环境中，命令 python 指的是在虚拟环境中安装的 Python 版本。



7、查看项目

下面来核实 Django 正确地创建了项目。为此，可使用命令 runserver 查看项目的状态，如下所示：

(ll_env)learning_log$ python manage.py runserver
Watchman unavailable: pywatchman not installed.
Watching for file changes with StatReloader
Performing system checks...

❶ System check identified no issues (0 silenced).
 February 18, 2019 - 16:26:07
❷ Django version 2.2.0, using settings 'learning_log.settings'
❸ Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

Django 启动了一个名为 development server 的服务器，让你能够查看系统中的项目，了解其工作情况。如果你在浏览
器中输入 URL 以请求页面，该 Django 服务器将进行响应：生成合适的页面，并将其发送给浏览器。

Django 在❶处通过检查确认正确地创建了项目，在❷处指出使用的 Django 版本以及当前使用的设置文件的名称，并在❸处
指出项目的 URL。URL http://127.0.0.1:8000/ 表明项目将在你的计算机（即 localhost）的端口 8000 上侦听
请求。localhost 指的是只处理当前系统发出的请求，而不允许其他任何人查看你正在开发的页面的服务器。

现在打开一款 Web 浏览器，并输入 URL http://localhost:8000/（如果这不管用，请输入 http://127.0.0.1:
8000/）。看到的这个页面是 Django 创建的，让你知道到目前为止一切正常。现在暂时不要关闭这个服务器，等你要关闭
这个服务器时，可切换到执行命令 runserver 时所在的终端窗口，再按 Ctrl + C。

注意：如果出现错误消息 That port is already in use（指定端口被占用），请执行命令 python manage.py
runserver 8001，让 Diango 使用另一个端口。如果这个端口也不可用，请不断执行上述命令，并逐渐增大其中的端口号，
直到找到可用的端口。

"""