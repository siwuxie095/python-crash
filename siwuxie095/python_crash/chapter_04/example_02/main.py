"""

避免缩进错误


Python 根据缩进来判断代码行与前一个代码行的关系。在前面的示例中，向各位魔术师显示消息的代码行是
 for 循环的一部分，因为它们缩进了。Python 通过使用缩进让代码更易读。简单地说，它要求你使用缩进
让代码整洁而结构清晰。在较长的 Python 程序中，你将看到缩进程度各不相同的代码块，从而对程序的组
织结构有大致的认识。

开始编写必须正确缩进的代码时，需要注意一些常见的缩进错误。例如，程序员有时候会将不需要缩进的代码
块缩进，而对于必须缩进的代码块却忘了缩进。查看这样的错误示例有助于你以后避开它们，以及在它们出现
在程序中时进行修复。

下面来看一些较为常见的缩进错误。



1、忘记缩进

对于位于 for 语句后面且属于循环组成部分的代码行，一定要缩进。如果忘记缩进， Python 会提醒你：

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
❶ print(magician)

函数调用 print()（见❶）应缩进却没有缩进。Python 没有找到期望缩进的代码块时，会让你知道哪行
代码有问题。

File "magicians.py", line 3
 print(magician)
 ^
IndentationError: expected an indented block

通常，将紧跟在 for 语句后面的代码行缩进，可消除这种缩进错误。



2、忘记缩进额外的代码行

有时候，循环能够运行且不会报告错误，但结果可能出人意料。试图在循环中执行多项任务，却忘记缩进其中
的一些代码行时，就会出现这种情况。

例如，如果忘记缩进循环中的第二行代码（它告诉每位魔术师，期待其下次表演），就会出现这种情况：

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
❶ print(f"I can't wait to see your next trick, {magician.title()}.\n")

第二个函数调用 print()（见❶）原本需要缩进，但 Python 发现 for 语句后面有一行代码是缩进的，
因此没有报告错误。最终的结果是，对于列表中的每位魔术师，都执行了第一个函数调用 print()，因为
它缩进了；而第二个函数调用 print() 没有缩进，因此只在循环结束后执行一次。由于变量 magician
的终值为 'carolina'，结果只有她收到了消息 “looking forward to the next trick”：

Alice, that was a great trick!
David, that was a great trick!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

这是一个逻辑错误。从语法上看，这些 Python 代码是合法的，但由于存在逻辑错误，结果并不符合预期。
如果你预期某项操作将针对每个列表元素都执行一次，但它总共只执行了一次，请确定需要将一行还是多行
代码缩进。



3、不必要的缩进

如果你不小心缩进了无须缩进的代码行，Python 将指出这一点：

message = "Hello Python world!"
❶    print(message)

函数调用 print()（见❶）无须缩进，因为它并非循环的组成部分。因此 Python 将指出这种错误：

 File "hello_world.py", line 2
 print(message)
 ^
IndentationError: unexpected indent

为避免意外缩进错误，请只缩进需要缩进的代码。在前面编写的程序中，只有要在 for 循环中对每个
元素执行的代码需要缩进。



4、循环后不必要的缩进

如果不小心缩进了应在循环结束后执行的代码，这些代码将针对每个列表元素重复执行。在有些情况下，
这可能导致 Python 报告语法错误，但在大多数情况下，这只会导致逻辑错误。

例如，如果不小心缩进了感谢全体魔术师精彩表演的代码行，结果将如何呢？

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
❶    print("Thank you, everyone. That was a great magic show!")

由于❶处的代码行缩进了，它将针对列表中的每位魔术师执行一次，如下所示：

Alice, that was a great trick!
I can't wait to see your next trick, Alice.

Thank you, everyone. That was a great magic show!
David, that was a great trick!
I can't wait to see your next trick, David.

Thank you, everyone. That was a great magic show!
Carolina, that was a great trick!
I can't wait to see your next trick, Carolina.

Thank you, everyone. That was a great magic show!

这也是一个逻辑错误，与上面的错误类似。Python 不知道你的本意，只要代码符合语法，它就会运行。
如果原本只应执行一次的操作执行了多次，可能要对执行该操作的代码取消缩进。



5、遗漏了冒号

for 语句末尾的冒号告诉 Python，下一行是循环的第一行。

magicians = ['alice', 'david', 'carolina']
❶ for magician in magicians
    print(magician)

如果不小心遗漏了冒号，如❶所示，将导致语法错误，因为 Python 不知道你意欲何为。这种错误虽然
易于消除，但并不那么容易发现。程序员为找出这样的单字符错误，花费的时间多得令人惊讶。此类错误
之所以难以发现，是因为通常在人们的意料之外。

"""