"""

定义函数


下面是一个打印问候语的简单函数，名为 greet_user()：

❶ def greet_user():
❷    \"""显示简单的问候语。\"""
❸    print("Hello!")
    
❹ greet_user()

本例演示了最简单的函数结构。❶处的代码行使用关键字 def 来告诉 Python，你要定义一个函数。这是函数定义，向
Python 指出了函数名，还可能在圆括号内指出函数为完成任务需要什么样的信息。在这里，函数名为 greet_user()，
它不需要任何信息就能完成工作，因此括号是空的（即便如此，括号也必不可少）。最后，定义以冒号结尾。

紧跟在 def greet_user(): 后面的所有缩进行构成了函数体。❷处的文本是称为文档字符串（docstring）的注释，
描述了函数是做什么的。文档字符串用三引号括起，Python 使用它们来生成有关程序中函数的文档。

代码行 print("Hello!")（见❸）是函数体内的唯一一行代码，因此 greet_user() 只做一项工作：打印 Hello!。

要使用这个函数，可调用它。函数调用让 Python 执行函数的代码。要调用函数，可依次指定函数名以及用圆括号括起
的必要信息，如❹处所示。由于这个函数不需要任何信息，调用它时只需输入 greet_user() 即可。和预期一样，它
打印 Hello!：

Hello!



1、向函数传递信息

只需稍作修改，就可让函数 greet_user() 不仅向用户显示 Hello!，还将用户的名字作为抬头。为此，可在函数
定义 def greet_user() 的括号内添加 username。通过在这里添加 username，可让函数接受你给 username
指定的任何值。现在，这个函数要求你调用它时给 username 指定一个值。调用 greet_user() 时，可将一个名字
传递给它，如下所示：

def greet_user(username):
    \"""显示简单的问候语。\"""
    print(f"Hello, {username.title()}!")

greet_user('jesse')

代码 greet_user('jesse') 调用函数 greet_user()，并向它提供执行函数调用 print() 所需的信息。这个
函数接受你传递给它的名字，并向这个人发出问候：

Hello, Jesse!

同样，greet_user('sarah') 调用函数 greet_user() 并向它传递 'sarah'，从而打印 Hello, Sarah!。
可根据需要调用函数 greet_user() 任意次，调用时无论传入什么名字，都将生成相应的输出。



2、实参和形参

前面定义函数 greet_user() 时，要求给变量 username 指定一个值。调用这个函数并提供这种信息（人名）时，
它将打印相应的问候语。

在函数 greet_user() 的定义中，变量 username 是一个形参（parameter），即函数完成工作所需的信息。
在代码 greet_user('jesse') 中，值 'jesse' 是一个实参（argument），即调用函数时传递给函数的信息。
调用函数时，将要让函数使用的信息放在圆括号内。在 greet_user('jesse') 中，将实参 'jesse' 传递给了
函数 greet_user()，这个值被赋给了形参 username。

注意：大家有时候会形参、实参不分，因此如果你看到有人将函数定义中的变量称为实参或将函数调用中的变量称为
形参，不要大惊小怪。

"""