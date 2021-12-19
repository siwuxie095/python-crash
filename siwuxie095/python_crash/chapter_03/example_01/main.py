"""

列表是什么


列表 由一系列按特定顺序排列的元素组成。你可以创建包含字母表中所有字母、数字 0～9 或所有家庭成员姓名的列表；
也可以将任何东西加入列表中，其中的元素之间可以没有任何关系。列表通常包含多个元素，因此给列表指定一个表示复
数的名称（如letters 、digits 或 names ）是个不错的主意。

在 Python 中，用方括号（[]）表示列表，并用逗号分隔其中的元素。下面是一个简单的列表示例，其中包含几种自行车：

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

如果让 Python 将列表打印出来，Python 将打印列表的内部表示，包括方括号：

['trek', 'cannondale', 'redline', 'specialized']

鉴于这不是你要让用户看到的输出，下面来学习如何访问列表元素。



1、访问列表元素

列表是有序集合，因此要访问列表的任意元素，只需将该元素的位置（索引）告诉 Python 即可。要访问列表元素，可
指出列表的名称，再指出元素的索引，并将后者放在方括号内。

例如，下面的代码从列表 bicycles 中提取第一款自行车：

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
❶ print(bicycles[0])

❶处演示了访问列表元素的语法。当你请求获取列表元素时，Python 只返回该元素，而不包括方括号：

trek

这正是你要让用户看到的结果——整洁、干净的输出。


你还可以对任意列表元素调用字符串方法。例如，可使用方法 title() 让元素 'trek' 的格式更整洁：

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0].title())

这个示例的输出与前一个示例相同，只是首字母 T 是大写的。



2、索引从 0 而不是 1 开始

在 Python 中，第一个列表元素的索引为 0，而不是 1。多数编程语言是如此规定的，这与列表操作的底层实现相关。
如果结果出乎意料，请看看你是否犯了简单的差一错误。

第二个列表元素的索引为 1。根据这种简单的计数方式，要访问列表的任何元素，都可将其位置减 1，并将结果作为索
引。例如，要访问第四个列表元素，可使用索引 3。

下面的代码访问索引 1 和索引 3 处的自行车：

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[1])
print(bicycles[3])

这些代码返回列表中的第二个和第四个元素：

cannondale
specialized

Python 为访问最后一个列表元素提供了一种特殊语法。通过将索引指定为 -1，可让 Python 返回最后一个列表元素：

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[-1])

这段代码返回 'specialized'。这种语法很有用，因为你经常需要在不知道列表长度的情况下访问最后的元素。这种
约定也适用于其他负数索引。例如，索引 -2 返回倒数第二个列表元素，索引 -3 返回倒数第三个列表元素，依此类推。



3、使用列表中的各个值

你可以像使用其他变量一样使用列表中的各个值。例如，可以使用 f 字符串根据列表中的值来创建消息。

下面尝试从列表中提取第一款自行车，并使用这个值创建一条消息：

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
❶ message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

这里使用 bicycles[0] 的值生成了一个句子，并将其赋给变量 message（见❶）。输出是一个简单的句子，其中
包含列表中的第一款自行车：

My first bicycle was a Trek.

"""