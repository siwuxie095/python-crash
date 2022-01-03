"""

存储数据


很多程序都要求用户输入某种信息，如让用户存储游戏首选项或提供要可视化的数据。不管关注点是什么，
程序都把用户提供的信息存储在列表和字典等数据结构中。用户关闭程序时，几乎总是要保存他们提供的
信息。一种简单的方式是使用模块 json 来存储数据。

模块 json 让你能够将简单的 Python 数据结构转储到文件中，并在程序再次运行时加载该文件中的
数据。你还可以使用 json 在 Python 程序之间分享数据。更重要的是，JSON 数据格式并非 Python
专用的，这让你能够将以 JSON 格式存储的数据与使用其他编程语言的人分享。这是一种轻便而有用的
格式，也易于学习。

注意：JSON（JavaScript Object Notation）格式最初是为 JavaScript 开发的，但随后成了
一种常见格式，被包括 Python 在内的众多语言采用。



1、使用 json.dump() 和 json.load()

下面来编写一个存储一组数的简短程序，再编写一个将这些数读取到内存中的程序。第一个程序将使用
json.dump() 来存储这组数，而第二个程序将使用 json.load()。

函数 json.dump() 接受两个实参：要存储的数据，以及可用于存储数据的文件对象。下面演示了如
何使用 json.dump() 来存储数字列表：

import json

numbers = [2, 3, 5, 7, 11, 13]

❶ filename = 'numbers.json'
❷ with open(filename, 'w') as f:
❸   json.dump(numbers, f)

先导入模块 json，再创建一个数字列表。在❶处，指定了要将该数字列表存储到哪个文件中。通常使用
文件扩展名.json 来指出文件存储的数据为 JSON 格式。接下来，以写入模式打开这个文件，让 json
能够将数据写入其中（见❷）。在❸处，使用函数 json.dump() 将数字列表存储到文件 numbers.json
中。

这个程序没有输出，但可以打开文件 numbers.json 来看看内容。数据的存储格式与 Python 中一样：

[2, 3, 5, 7, 11, 13]

下面再编写一个程序，使用 json.load() 将列表读取到内存中：

import json

❶ filename = 'numbers.json'
❷ with open(filename) as f:
❸   numbers = json.load(f)

print(numbers)

在❶处，确保读取的是前面写入的文件。这次以读取方式打开该文件，因为 Python 只需要读取它（见❷）。
在❸处，使用函数 json.load() 加载存储在 numbers.json 中的信息，并将其赋给变量 numbers。
最后，打印恢复的数字列表，看看是否与 number_writer.py 中创建的数字列表相同：

[2, 3, 5, 7, 11, 13]

这是一种在程序之间共享数据的简单方式。



2、保存和读取用户生成的数据

使用 json 保存用户生成的数据大有裨益，因为如果不以某种方式存储，用户的信息会在程序停止运行时
丢失。下面来看一个这样的例子：提示用户首次运行程序时输入自己的名字，并在再次运行程序时记住他。

先来存储用户的名字：

import json

❶ username = input("What is your name? ")

filename = 'username.json'

with open(filename, 'w') as f:
❷    json.dump(username, f)
❸    print(f"We'll remember you when you come back, {username}!")

在❶处，提示输入用户名并将其赋给一个变量。接下来，调用 json.dump()，并将用户名和一个文件对象
传递给它，从而将用户名存储到文件中（见❷）。然后，打印一条消息，指出存储了用户输入的信息（见❸）：

What is your name? Eric
We'll remember you when you come back, Eric!

现在再编写一个程序，向已存储了名字的用户发出问候：

import json

filename = 'username.json'

with open(filename) as f:
❶    username = json.load(f)
❷    print(f"Welcome back, {username}!")

在❶处，使用 json.load() 将存储在 username.json 中的信息读取到变量 username 中。恢复
用户名后，就可以欢迎用户回来了（见❷）：

Welcome back, Eric!

需要将这两个程序合并到一个程序（remember_me.py）中。这个程序运行时，将尝试从文件 username
.json 中获取用户名。因此，首先编写一个尝试恢复用户名的 try 代码块。如果这个文件不存在，就在
except 代码块中提示用户输入用户名，并将其存储到 username.json 中，以便程序再次运行时能够
获取：

import json
# 如果以前存储了用户名，就加载它。
# 否则，提示用户输入用户名并存储它。
filename = 'username.json'

try:
❶    with open(filename) as f:
❷        username = json.load(f)
❸ except FileNotFoundError:
❹    username = input("What is your name? ")
❺    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")
else:
    print(f"Welcome back, {username}!")

这里没有任何新代码，只是将前两个示例的代码合并到了一个程序中。在❶处，尝试打开文件 username
.json。如果该文件存在，就将其中的用户名读取到内存中（见❷），再执行 else 代码块，打印一条
欢迎用户回来的消息。

用户首次运行该程序时，文件 username.json 不存在，将引发 FileNotFoundError 异常（见❸）。
因此 Python 将执行 except 代码块，提示用户输入用户名（见❹），再使用 json.dump() 存储
该用户名并打印一句问候语（见❺）。

无论执行的是 except 还是 else 代码块，都将显示用户名和合适的问候语。如果这个程序是首次运行，
输出将如下：

What is your name? Eric
We'll remember you when you come back, Eric!

否则，输出将如下：

Welcome back, Eric!

这是程序之前至少运行了一次时的输出。



3、重构

你经常会遇到这样的情况：代码能够正确地运行，但通过将其划分为一系列完成具体工作的函数，还可以改进。
这样的过程称为重构。重构让代码更清晰、更易于理解、更容易扩展。

要重构 remember_me.py，可将其大部分逻辑放到一个或多个函数中。remember_me.py 的重点是问候
用户，因此将其所有代码都放到一个名为 greet_user() 的函数中：

import json

def greet_user():
❶    \"""问候用户，并指出其名字。\"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
             json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")
    else:
        print(f"Welcome back, {username}!")

greet_user()

考虑到现在使用了一个函数，删除原注释，转而使用一个文档字符串来指出程序的作用（见❶）。这个程序更加
清晰，但函数 greet_user() 所做的不仅仅是问候用户，还在存储了用户名时获取它、在没有存储用户名时
提示用户输入。

下面来重构 greet_user()，减少其任务。为此，首先将获取已存储用户名的代码移到另一个函数中：

import json

def get_stored_username():
❶    \"""如果存储了用户名，就获取它。\"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
❷        return None
    else:
        return username

def greet_user():
    \"""问候用户，并指出其名字。\"""
    username = get_stored_username()
❸    if username:
        print(f"Welcome back, {username}!")
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print(f"We'll remember you when you come back, {username}!")

greet_user()

新增的函数 get_stored_username() 目标明确，❶处的文档字符串指出了这一点。如果存储了用户名，该
函数就获取并返回它；如果文件 username.json 不存在，该函数就返回 None（见❷）。这是一种不错的做
法：函数要么返回预期的值，要么返回 None。这使得能够使用函数的返回值做简单的测试。在❸处，如果成功
地获取了用户名，就打印一条欢迎用户回来的消息，否则提示用户输入用户名。

还需要重构 greet_user() 中的另一个代码块，将没有存储用户名时提示用户输入的代码放在一个独立的函数
中：

import json

def get_stored_username():
    \"""如果存储了用户名，就获取它。\"""
    --snip--

def get_new_username():
    \"""提示用户输入用户名。\"""
    username = input("What is your name? ")
    filename = 'username.json'
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    \"""问候用户，并指出其名字。\"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()

在 remember_me.py 的这个最终版本中，每个函数都执行单一而清晰的任务。这里调用 greet_user()，
它打印一条合适的消息：要么欢迎老用户回来，要么问候新用户。为此，它首先调用 get_stored_username()，
该函数只负责获取已存储的用户名（如果存储了的话）。最后在必要时调用 get_new_username()，该函数
只负责获取并存储新用户的用户名。要编写出清晰而易于维护和扩展的代码，这种划分必不可少。

"""