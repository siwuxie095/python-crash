"""

变量


print("Hello Python world!")

运行文件 hello_world.py 时，末尾的 .py 指出这是一个 Python 程序，因此编辑器将使用 Python 解释器来运行它。
Python 解释器读取整个程序，确定 其中每个单词的含义。例如，看到后面跟着圆括号的单词 print 时，解释器就将圆括号
中的内容打印到屏幕。

编写程序时，编辑器会以各种方式突出程序的不同部分。例如，它知道 print() 是一个函数的名称，因此将其显示为某种颜色；
它知道 "Hello Python world!" 不是 Python 代码，因此将其显示为另一种颜色。这种功能称为语法高亮，在你刚开始编写
程序时很有帮助。

下面来尝试在 hello_world.py 中使用一个变量。在这个文件开头添加一行代码，并对第二行代码进行修改，如下所示：

message = "Hello Python world!"
print(message)

运行这个程序，你会发现，输出与以前相同。

这里添加了一个名为 message 的变量。每个变量都指向一个值 —— 与该变量相关联的信息。

在这里，指向的值为文本 "Hello Python world!"。

添加变量导致 Python 解释器需要做更多工作。处理第一行代码时，它将变量 message 与文本 "Hello Python world!"
关联起来；处理第二行代码时，它将与变量 message 关联的值打印到屏幕。

下面来进一步扩展这个程序：修改 hello_world.py，使其再打印一条消息。为此，在 hello_world.py 中添加一个空行，
再添加下面两行代码：

message = "Hello Python world!"
print(message)

message = "Hello Python Crash Course world!"
print(message)

在程序中可随时修改变量的值，而 Python 将始终记录变量的最新值。



1、变量的命名和使用

在 Python 中使用变量时，需要遵守一些规则和指南。违反这些规则将引发错误，而指南旨在让你编写的代码更容易阅读和理解。
请务必牢记下 述有关变量的规则。
（1）变量名只能包含字母、数字和下划线。变量名能以字母或下划线打头，但不能以数字打头。例如，可将变量命名为 message_1，
但不能将其命名为 1_message。
（2）变量名不能包含空格，但能使用下划线来分隔其中的单词。例如，变量名 greeting_message 可行，但变量名 greeting message
 会引发错误。
（3）不要将 Python 关键字和函数名用作变量名，即不要使用 Python 保留用于特殊用途的单词，如 print。
（4）变量名应既简短又具有描述性。例如，name 比 n 好，student_name 比 s_n 好，name_length 比 length_of_persons_name 好。
（5）慎用小写字母 l 和大写字母 O，因为它们可能被人错看成数字 1 和 0。


注意：就目前而言，应使用小写的 Python 变量名。虽然在变量名中使用大写字母不会导致错误，但是大写字母在变量名中有特殊含义，
后续将会介绍。



2、使用变量时避免命名错误

下面是拼写不正确的单词 mesage：

message = "Hello Python Crash Course reader!"
print(mesage)

程序存在错误时，Python 解释器将竭尽所能地帮助你找出问题所在。程序无法成功运行时，解释器将提供一个 traceback。traceback
是一条记录，指出了解释器尝试运行代码时，在什么地方陷入了困境。

下面是你不小心错误地拼写了变量名时，Python 解释器提供的 traceback：

Traceback (most recent call last):
❶ File "hello_world.py", line 2, in <module>
❷   print(mesage)
❸ NameError: name 'mesage' is not defined

解释器指出，文件 hello_world.py 的第二行存在错误（见❶）。它列出了这行代码，旨在帮助你快速找出错误（见❷），还指出了它发现
的是什么样的错误（见❸）。在这里，解释器发现了一个名称错误，并报告打印的变量 mesage 未定义：Python 无法识别你提供的变量名。
名称错误通常意味着两种情况：要么是使用变量前忘记给它赋值，要么是输入变量名时拼写不正确。

在这个示例中，第二行的变量名 message 遗漏了字母 s。Python 解释器不会对代码做拼写检查，但要求变量名的拼写一致。例如，如果在
代码的另一个地方也将 message 错误地拼写成了 mesage，结果将如何呢？

mesage = "Hello Python Crash Course reader!"
print(mesage)

在这种情况下，程序将成功运行！

编程语言要求严格，但并不关心拼写是否正确。因此，创建变量名和编写代码时，无须考虑英语中的拼写和语法规则。



3、变量是标签

变量常被描述为可用于存储值的盒子。在你刚接触变量时，这种定义可能很有帮助，但它并没有准确描述 Python 内部表示变量的方式。
一种好得多的定义是，变量是可以赋给值的标签，也可以说变量指向特定的值。

"""