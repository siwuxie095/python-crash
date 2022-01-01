"""

while 循环简介


for 循环用于针对集合中的每个元素都执行一个代码块，而 while 循环则不断运行，直到指定的条件不满足为止。



1、使用 while 循环

可使用 while 循环来数数。例如，下面的 while 循环从 1 数到 5：

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1

在第一行，将 1 赋给变量 current_number，从而指定从 1 开始数。将接下来的 while 循环设置成：只要
current_number 小于或等于 5，就接着运行这个循环。循环中的代码打印 current_number 的值，再使用
代码 current_number += 1 将其值加 1。

PS：current_number += 1 即代码 current_number = current_number + 1 的简写。

只要满足条件 current_number <= 5，Python 就接着运行这个循环。因为 1 小于 5，所以 Python 打印
1 并将 current_number 加 1，使其为 2；因为 2 小于 5，所以 Python 打印 2 并将 current_number
加 1，使其为 3；依此类推。一旦 current_number 大于 5，循环就将停止，整个程序也将结束：

1
2
3
4
5

你每天使用的程序很可能就包含 while 循环。例如，游戏使用 while 循环，确保在玩家想玩时不断运行，并在
玩家想退出时停止运行。如果程序在用户没有让它停止时停止运行，或者在用户要退出时还继续运行，那就太没有意
思了。因此，while 循环很有用。



2、让用户选择何时退出

可以使用 while 循环让程序在用户愿意时不断运行，如下面的程序 parrot.py 所示。在其中定义了一个退出值，
只要用户输入的不是这个值，程序就将接着运行：

❶ prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
❷ message = ""

❸ while message != 'quit':
    message = input(prompt)
    print(message)

❶处定义了一条提示消息，告诉用户有两个选择：要么输入一条消息，要么输入退出值（这里为 'quit'）。接下来，
创建变量 message（见❷），用于记录用户输入的值。这里将变量 message 的初始值设置为空字符串 ""，让
Python 首次执行 while 代码行时有可供检查的东西。Python 首次执行 while 语句时，需要将 message
的值与 'quit' 进行比较，但此时用户还没有输入。如果没有可供比较的东西，Python 将无法继续运行程序。为
解决这个问题，必须给变量 message 指定初始值。虽然这个初始值只是一个空字符串，但符合要求，能够让 Python
执行 while 循环所需的比较。只要 message 的值不是 'quit'，这个循环（见❸）就会不断运行。

首次遇到这个循环时，message 是一个空字符串，因此 Python 进入该循环。执行到代码行 message = input(prompt)
时，Python 显示提示消息，并等待用户输入。不管用户输入是什么，都将赋给变量 message 并打印出来。接下来，Python
重新检查 while 语句中的条件。只要用户输入的不是单词 'quit'，Python 就会再次显示提示消息并等待用户输入。等到
用户终于输入 'quit' 后，Python 停止执行 while 循环，整个程序也到此结束：

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit
quit

这个程序很好，唯一美中不足的是，它将单词 'quit' 也作为一条消息打印了出来。为修复这种问题，只需使用一个简单的
if 测试：

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "
message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)

现在，程序在显示消息前将做简单的检查，仅在消息不是退出值时才打印它：

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello everyone!
Hello everyone!

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. Hello again.
Hello again.

Tell me something, and I will repeat it back to you:
Enter 'quit' to end the program. quit



3、使用标志

在前一个示例中，让程序在满足指定条件时执行特定的任务。但在更复杂的程序中，很多不同的事件会导致程序停止
运行。在这种情况下，该怎么办呢？

例如，有多种事件可能导致游戏结束，如玩家失去所有飞船、时间已用完，或者要保护的城市被全部摧毁。导致程序
结束的事件有很多时，如果在一条 while 语句中检查所有这些条件，将既复杂又困难。

在要求很多条件都满足才继续运行的程序中，可定义一个变量，用于判断整个程序是否处于活动状态。这个变量称为
标志（flag），充当程序的交通信号灯。可以让程序在标志为 True 时继续运行，并在任何事件导致标志的值为
False 时让程序停止运行。这样，在 while 语句中就只需检查一个条件：标志的当前值是否为 True。然后将
所有其他测试（是否发生了应将标志设置为 False 的事件）都放在其他地方，从而让程序更整洁。

下面在之前的程序 parrot.py 中添加一个标志。将其命名为 active（你可给它指定任何名称），用于判断程序
是否应继续运行：

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

❶ active = True
❷ while active:
        message = input(prompt)

❸        if message == 'quit':
             active = False
❹        else:
            print(message)

将变量 active 设置为 True（见❶），让程序最初处于活动状态。这样做简化了 while 语句，因为不需要在
其中做任何比较 —— 相关的逻辑由程序的其他部分处理。只要变量 active 为 True，循环就将继续运行（见❷）。

在 while 循环中，在用户输入后使用一条 if 语句来检查变量 message 的值。如果用户输入的是 'quit'
（见❸），就将变量 active 设置为 False。这将导致 while 循环不再继续执行。如果用户输入的不是 'quit'
（见❹），就将输入作为一条消息打印出来。

这个程序的输出与前一个示例相同。前一个示例将条件测试直接放在了 while 语句中，而这个程序则使用一个标志
来指出程序是否处于活动状态。这样，如果要添加测试（如 elif 语句）以检查是否发生了其他导致 active 变为
False 的事件，就会很容易。在复杂的程序（如很多事件会导致程序停止运行的游戏）中，标志很有用：在任意一个
事件导致活动标志变成 False 时，主游戏循环将退出，此时可显示一条游戏结束消息，并让用户选择是否要重新玩。



4、使用 break 退出循环

要立即退出 while 循环，不再运行循环中余下的代码，也不管条件测试的结果如何，可使用 break 语句。break
语句用于控制程序流程，可用来控制哪些代码行将执行、哪些代码行不执行，从而让程序按你的要求执行你要执行的代码。

例如，来看一个让用户指出他到过哪些地方的程序。在这个程序中，可在用户输入 'quit' 后使用 break 语句立即
退出 while 循环：

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

❶ while True:
        city = input(prompt)

        if city == 'quit':
             break
        else:
            print(f"I'd love to go to {city.title()}!")

以 while True（见❶）打头的循环将不断运行，直到遇到 break 语句。这个程序中的循环不断让用户输入他到过
的城市的名字，直到用户输入 'quit' 为止。用户输入 'quit' 后，将执行 break 语句，导致 Python 退出
循环：

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) New York
I'd love to go to New York!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) San Francisco
I'd love to go to San Francisco!

Please enter the name of a city you have visited:
(Enter 'quit' when you are finished.) quit

注意：在任何 Python 循环中都可使用 break 语句。例如，可使用 break 语句来退出遍历列表或字典的 for
循环。



5、在循环中使用 continue

要返回循环开头，并根据条件测试结果决定是否继续执行循环，可使用 continue 语句，它不像 break 语句那样
不再执行余下的代码并退出整个循环。例如，来看一个从 1 数到 10 但只打印其中奇数的循环：

current_number = 0
while current_number < 10:
❶    current_number += 1
    if current_number % 2 == 0:
        continue
    print(current_number)

首先将 current_number 设置为 0，由于它小于 10，Python 进入 while 循环。进入循环后，以步长 1 的
方式往上数（见❶），因此 current_number 为 1。接下来，if 语句检查 current_number 与 2 的求模运
算结果。如果结果为 0（意味着 current_number 可被 2 整除），就执行 continue 语句，让 Python 忽略
余下的代码，并返回循环的开头。如果当前的数不能被 2 整除，就执行循环中余下的代码，将这个数打印出来：

1
3
5
7
9



6、避免无限循环

每个 while 循环都必须有停止运行的途径，这样才不会没完没了地执行下去。例如，下面的循环从 1 数到 5：

x = 1
while x <= 5:
    print(x)
    x += 1


但如果像下面这样不小心遗漏了代码行 x += 1，这个循环将没完没了地运行：

# 这个循环将没完没了地运行！
x = 1
while x <= 5:
    print(x)

在这里，x 的初始值为 1，但根本不会变。因此条件测试 x <= 5 始终为 True，导致 while 循环没完没了地
打印 1，如下所示：

1
1
1
1
--snip--

每个程序员都会偶尔因不小心而编写出无限循环，在循环的退出条件比较微妙时尤其如此。如果程序陷入无限循环，
可按 Ctrl + C，也可关闭显示程序输出的终端窗口。

要避免编写无限循环，务必对每个 while 循环进行测试，确保其按预期那样结束。如果你希望程序在用户输入特定
值时结束，可运行程序并输入这样的值。如果在这种情况下程序没有结束，请检查程序处理这个值的方式，确认程序
至少有一个这样的地方能让循环条件为 False，或者让 break 语句得以执行。

注意：Sublime Text 等一些编辑器内嵌了输出窗口，这可能导致难以结束无限循环，不得不通过关闭编辑器来
结束。在这种情况下，可在输出窗口中单击鼠标，再按 Ctrl + C，这样应该能够结束无限循环。

"""