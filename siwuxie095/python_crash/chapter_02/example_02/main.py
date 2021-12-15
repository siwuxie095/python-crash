"""

字符串


大多数程序定义并收集某种数据，然后使用它们来做些有意义的事情。有鉴于此，对数据进行分类大有裨益。这里将介绍的第一种
数据类型是字符串。字符串虽然看似简单，但能够以很多不同的方式使用。

字符串就是一系列字符。在 Python 中，用引号括起的都是字符串，其中的引号可以是单引号，也可以是双引号，如下所示：

"This is a string."
'This is also a string.'

这种灵活性让你能够在字符串中包含引号和撇号：

'I told my friend, "Python is my favorite language!"'
"The language 'Python' is named after Monty Python, not the snake."
"One of Python's strengths is its diverse and supportive community."

下面来看一些使用字符串的方式。



1、使用方法修改字符串的大小写

对于字符串，可执行的最简单的操作之一是修改其中单词的大小写。请看下面的代码，并尝试判断其作用：

name = "ada lovelace"
print(name.title())

将这个文件保存为 name.py，再运行它。你将看到如下输出：

Ada Lovelace

在这个示例中，变量 name 指向小写的字符串 "ada lovelace"。在函数调用 print() 中，方法 title() 出现在这个变量的
后面。方法是 Python 可对数据执行的操作。在 name.title() 中，name 后面的句点（.）让 Python 对变量 name 执行方法
title() 指定的操作。每个方法后面都跟着一对圆括号，这是因为方法通常需要额外的信息来完成其工作。这种信息是在圆括号内
提供的。函数title() 不需要额外的信息，因此它后面的圆括号是空的。

方法 title() 以首字母大写的方式显示每个单词，即将每个单词的首字母都改为大写。这很有用，因为你经常需要将名字视为信息。
例如，你可能希望程序将值 Ada、ADA 和 ada 视为同一个名字，并将它们都显示为 Ada。

还有其他几个很有用的大小写处理方法。例如，要将字符串改为全部大写或全部小写，可以像下面这样做：

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

存储数据时，方法 lower() 很有用。很多时候，你无法依靠用户来提供正确的大小写，因此需要将字符串先转换为小写，再存储
它们。以后需要显示这些信息时，再将其转换为最合适的大小写方式。



2、在字符串中使用变量

在有些情况下，你可能想在字符串中使用变量的值。例如，你可能想使用两个变量分别表示名和姓，然后合并这两个值以显示姓名：

first_name = "ada"
last_name = "lovelace"
❶ full_name = f"{first_name} {last_name}"
print(full_name)

要在字符串中插入变量的值，可在前引号前加上字母 f（见❶），再将要插入的变量放在花括号内。这样，当 Python 显示字符串
时，将把每个变量都替换为其值。

这种字符串名为 f 字符串 。f 是format（设置格式）的简写，因为 Python 通过把花括号内的变量替换为其值来设置字符串
的格式。上述代码的输出如下：

ada lovelace

使用 f 字符串可完成很多任务，如利用与变量关联的信息来创建完整的消息，如下所示：

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
❶ print(f"Hello, {full_name.title()}!")

在这里，一个问候用户的句子中使用了完整的姓名（见❶），并使用方法 title() 来将姓名设置为合适的格式。这些代码显示
一条格式良好的简单问候语：

Hello, Ada Lovelace!

还可以使用 f 字符串来创建消息，再把整条消息赋给变量：

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
❶ message = f"Hello, {full_name.title()}!"
❷ print(message)

上述代码也显示消息 Hello, Ada Lovelace!，但将这条消息赋给了一个变量（见❶），这让最后的函数调用 print() 变得
简单得多（见❷）。


注意：f 字符串是 Python 3.6 引入的。如果你使用的是 Python 3.5 或更早的版本，需要使用 format() 方法，而非这种
 f 语法。要使用方法 format()，可在圆括号内列出要在字符串中使用的变量。对于每个变量，都通过一对花括号来引用。这样
将按顺序将这些花括号替换为圆括号内列出的变量的值，如下所示：

full_name = "{} {}".format(first_name, last_name)



3、使用制表符或换行符来添加空白

在编程中，空白泛指任何非打印字符，如空格、制表符和换行符。你可以使用空白来组织输出，让用户阅读起来更容易。

要在字符串中添加制表符，可使用字符组合 \t，如下述代码的❶处所示：

 >>> print("Python")
 Python
❶ >>> print("\tPython")
 Python

要在字符串中添加换行符，可使用字符组合 \n：

>>> print("Languages:\nPython\nC\nJavaScript")
Languages:
Python
C JavaScript

还可在同一个字符串中同时包含制表符和换行符。字符串 "\n\t" 让 Python 换到下一行，并在下一行开头添加一个制表符。
下面的示例演示了如何使用一个单行字符串来生成四行输出：

>>> print("Languages:\n\tPython\n\tC\n\tJavaScript")
Languages:
    Python
    C
    JavaScript



4、删除空白

在程序中，额外的空白可能令人迷惑。对程序员来说，'python' 和 'python ' 看起来几乎没什么两样，但对程序来说，它们
却是两个不同的字符串。Python 能够发现 'python ' 中额外的空白，并认为它意义重大 —— 除非你告诉它不是这样的。

空白很重要，因为你经常需要比较两个字符串是否相同。一个重要的示例是，在用户登录网站时检查其用户名。不过在非常简单的
情形下，额外的空格也可能令人迷惑。所幸，在 Python 中删除用户输入数据中的多余空白易如反掌。

Python 能够找出字符串开头和末尾多余的空白。要确保字符串末尾没有空白，可使用方法 rstrip()。

❶ >>> favorite_language = 'python '
❷ >>> favorite_language
 'python '
❸ >>> favorite_language.rstrip()
 'python'
❹ >>> favorite_language
'python '

与变量 favorite_language 相关联的字符串末尾有多余的空白（见❶）。你在终端会话中向 Python 询问这个变量的值时，
可看到末尾的空格（见❷）。对变量 favorite_language 调用方法 rstrip() 后（见❸），这个多余的空格被删除了。
然而，这种删除只是暂时的，接下来再次询问 favorite_language 的值时，你会发现这个字符串与输入时一样，依然包含
多余的空白（见❹）。

要永久删除这个字符串中的空白，必须将删除操作的结果关联到变量：

>>> favorite_language = 'python '
❶ >>> favorite_language = favorite_language.rstrip()
 >>> favorite_language
 'python'

为删除这个字符串中的空白，要将其末尾的空白剔除，再将结果关联到原来的变量（见❶）。在编程中，经常需要修改变量的值，
再将新值关联到原来的变量。这就是变量的值可能随程序的运行或用户输入数据而发生变化的原因所在。

你还可以剔除字符串开头的空白，或者同时剔除字符串两边的空白。为此，可分别使用方法 lstrip() 和 strip()：

❶ >>> favorite_language = ' python '
❷ >>> favorite_language.rstrip()
 ' python'
❸ >>> favorite_language.lstrip()
 'python '
❹ >>> favorite_language.strip()
 'python'

在这个示例中，首先创建了一个开头和末尾都有空白的字符串（见❶）。接下来，分别删除末尾（见❷）、开头（见❸）和两边（见❹）
的空白。尝试使用这些剥除函数有助于你熟悉字符串操作。在实际程序中，这些剥除函数最常用于在存储用户输入前对其进行清理。



5、使用字符串时避免语法错误

语法错误是一种你时不时会遇到的错误。程序中包含非法的 Python 代码时，就会导致语法错误。例如，在用单引号括起的字符串中，
如果包含撇号，就将导致错误。这是因为这会导致 Python 将第一个单引号和撇号之间的内容视为一个字符串，进而将余下的文本视
为 Python 代码，从而引发错误。

下面演示了如何正确地使用单引号和双引号。请将该程序保存为 apostrophe.py，再运行它：

message = "One of Python's strengths is its diverse community."
print(message)

撇号位于两个双引号之间，因此Python解释器能够正确地理解这个字符串。

然而，如果使用单引号，Python 将无法正确地确定字符串的结束位置：

message = 'One of Python's strengths is its diverse community.'
print(message)

你将看到如下输出：

 File "apostrophe.py", line 1
 message = 'One of Python's strengths is its diverse community.'
 ^❶
SyntaxError: invalid syntax

从上述输出可知，错误发生在第二个单引号后面（见❶）。这种语法错误表明，在解释器看来，其中的有些内容不是有效的 Python
代码。错误的原因各种各样，这里将指出一些常见的原因。学习编写 Python 代码时，你可能会经常遇到语法错误。语法错误也是
最不具体的错误类型，因此可能难以找出并修复。

注意：编写程序时，编辑器的语法高亮功能可帮助你快速找出某些语法错误。看到 Python 代码以普通句子的颜色显示，或者普通
句子以 Python 代码的颜色显示时，就可能意味着文件中存在引号不匹配的情况。

"""