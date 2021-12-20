"""

遍历整个列表


你经常需要遍历列表的所有元素，对每个元素执行相同的操作。例如，在游戏中，可能需要将每个界面元素平移
相同的距离；对于包含数字的列表，可能需要对每个元素执行相同的统计运算；在网站中，可能需要显示文章列
表中的每个标题。需要对列表中的每个元素都执行相同的操作时，可使用 Python 中的 for 循环。

假设有一个魔术师名单，需要将其中每个魔术师的名字都打印出来。为此，可以分别获取名单中的每个名字，但
这种做法会导致多个问题。例如，如果名单很长，将包含大量重复的代码。另外，每当名单的长度发生变化时，
都必须修改代码。通过使用 for 循环，可以让 Python 去处理这些问题。

下面使用 for 循环来打印魔术师名单中的所有名字：

❶ magicians = ['alice', 'david', 'carolina']
❷ for magician in magicians:
❸     print(magician)

首先，定义一个列表（见❶）。接下来，定义一个 for 循环（见❷）。这行代码让 Python 从列表 magicians
中取出一个名字，并将其与变量 magician 相关联。最后，让 Python 打印前面赋给变量 magician 的名字
（见❸）。这样，对于列表中的每个名字，Python 都将重复执行❷处和❸处的代码行。你可以这样解读这些代码：
对于列表 magicians 中的每位魔术师，都将其名字打印出来。输出很简单，就是列表中所有的名字：

alice
david
carolina



1、深入研究循环

循环这种概念很重要，因为它是让计算机自动完成重复工作的常见方式之一。例如，在前面 magicians.py 中
使用的简单循环里，Python 将首先读取其中的第一行代码：

for magician in magicians:

这行代码让 Python 获取列表 magicians 中的第一个值 'alice'，并将其与变量 magician 相关联。
接下来，Python 读取下一行代码：

print(magician)

它让 Python 打印 magician 的值，依然是 'alice'。鉴于该列表还包含其他值，Python 返回到循环
的第一行：

for magician in magicians:

Python 获取列表中的下一个名字 'david'，并将其与变量 magician 相关联，再执行下面这行代码：

print(magician)

Python 再次打印变量 magician 的值，当前为 'david'。接下来， Python 再次执行整个循环，对列表
中的最后一个值 'carolina' 进行处理。至此，列表中没有其他的值了，因此 Python 接着执行程序的下一
行代码。在这个示例中，for 循环后面没有其他代码，因此程序就此结束。

刚开始使用循环时请牢记，对列表中的每个元素，都将执行循环指定的步骤，而不管列表包含多少个元素。如果
列表包含一百万个元素，Python 就重复执行指定的步骤一百万次，且通常速度非常快。

另外，编写 for 循环时，可以给依次与列表中每个值相关联的临时变量指定任意名称。然而，选择描述单个列表
元素的有意义名称大有裨益。例如，对于小猫列表、小狗列表和一般性列表，像下面这样编写 for 循环的第一行
代码是不错的选择：

for cat in cats:
for dog in dogs:
for item in list_of_items:

这些命名约定有助于你明白 for 循环中将对每个元素执行的操作。使用单数和复数式名称，可帮助你判断代码段
处理的是单个列表元素还是整个列表。



2、在 for 循环中执行更多操作

在 for 循环中，可对每个元素执行任何操作。下面来扩展前面的示例，对于每位魔术师，都打印一条消息，指出
他的表演太精彩了。

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
❶    print(f"{magician.title()}, that was a great trick!")

相比于前一个示例，唯一的不同是为每位魔术师打印了一条以其名字为抬头的消息（见❶）。这个循环第一次迭代
时，变量 magician 的值为 'alice'，因此 Python 打印的第一条消息的抬头为 'Alice'；第二次迭代
时，消息的抬头为 'David'；第三次迭代时，抬头为 'Carolina'。

下面的输出表明，对于列表中的每位魔术师，都打印了一条个性化消息：

Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!

在 for 循环中，想包含多少行代码都可以。在代码行 for magician in magicians 后面，每个缩进的
代码行都是循环的一部分，将针对列表中的每个值都执行一次。因此，可对列表中的每个值执行任意次数的操作。

下面再添加一行代码，告诉每位魔术师，我们期待他的下一次表演：

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
❶    print(f"I can't wait to see your next trick, {magician.title()}.\n")

两个函数调用 print() 都缩进了，因此它们都将针对列表中的每位魔术师执行一次。第二个函数调用 print()
中的换行符 "\n"（见❶）在每次迭代结束后都插入一个空行，从而整洁地将针对各位魔术师的消息编组：

Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

在 for 循环中，想包含多少行代码都可以。实际上，你会发现使用 for 循环对每个元素执行众多不同的操作
很有用。



3、在 for 循环结束后执行一些操作

for 循环结束后怎么办呢？通常，你需要提供总结性输出或接着执行程序必须完成的其他任务。

在 for 循环后面，没有缩进的代码都只执行一次，不会重复执行。下面来打印一条向全体魔术师致谢的消息，
感谢他们的精彩表演。想要在打印给各位魔术师的消息后面打印一条给全体魔术师的致谢消息，需要将相应的
代码放在 for 循环后面，且不缩进：

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")

❶ print("Thank you, everyone. That was a great magic show!")

你在前面看到了，开头两个函数调用 print() 针对列表中的每位魔术师重复执行。然而，第三个函数调用
print() 没有缩进（见❶），因此只执行一次：

Alice, that was a great trick!
I can't wait to see your next trick, Alice.

David, that was a great trick!
I can't wait to see your next trick, David.

Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!

使用 for 循环处理数据是一种对数据集执行整体操作的不错方式。例如，你可能使用 for 循环来初始化
游戏：遍历角色列表，将每个角色显示到屏幕上。然后在循环后面添加一个不缩进的代码块，在屏幕上绘制
所有角色后显示一个 Play Now 按钮。

"""