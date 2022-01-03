"""

Python 标准库


Python 标准库是一组模块，一般安装的 Python 都包含它。你现在对函数和类的工作原理已有大致的了解，可以开始
使用其他程序员编写好的模块了。可以使用标准库中的任何函数和类，只需在程序开头包含一条简单的 import 语句即可。
下面来看看模块 random，它在你模拟很多现实情况时很有用。

在这个模块中，一个有趣的函数是 randint()。它将两个整数作为参数，并随机返回一个位于这两个整数之间（含）的
整数。下面演示了如何生成一个位于 1 和 6 之间的随机整数：

>>> from random import randint
>>> randint(1, 6)
3

在模块 random 中，另一个有用的函数是 choice()。它将一个列表或元组作为参数，并随机返回其中的一个元素：

>>> from random import choice
>>> players = ['charles', 'martina', 'michael', 'florence', 'eli']
>>> first_up = choice(players)
>>> first_up
'florence'

创建与安全相关的应用程序时，请不要使用模块 random，但该模块可以很好地用于创建众多有趣的项目。

注意：还可以从其他地方下载外部模块。后续的每个项目都需要使用外部模块，届时你将看到很多此类示例。

"""