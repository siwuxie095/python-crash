"""

数


在编程中，经常使用数来记录得分、表示可视化数据、存储 Web 应用信息，等等。Python 能根据数的用法以不同的方式处理它们。
鉴于整数使用起来最简单，下面就先来看看 Python 是如何管理它们的。



整数

在 Python 中，可对整数执行加（+）减（-）乘（*）除（/）运算。

>>> 2 + 3
5
>>> 3 - 2
1
>>> 2 * 3
6
>>> 3 / 2
1.5

在终端会话中，Python 直接返回运算结果。Python 使用两个乘号表示乘方运算：

>>> 3 ** 2
9
>>> 3 ** 3
27
>>> 10 ** 6
1000000

Python 还支持运算次序，因此可在同一个表达式中使用多种运算。还可以使用圆括号来修改运算次序，让 Python 按你指定的
次序执行运算，如下所示：

>>> 2 + 3*4
14
>>> (2 + 3) * 4
20

在这些示例中，空格不影响 Python 计算表达式的方式。它们的存在旨在让你在阅读代码时能迅速确定先执行哪些运算。



浮点数

Python 将所有带小数点的数称为浮点数。大多数编程语言使用了这个术语，它指出了这样一个事实：小数点可出现在数的任何
位置。每种编程语言都必须细心设计，以妥善地处理浮点数，确保不管小数点出现在什么位置，数的行为都是正常的。

从很大程度上说，使用浮点数时无须考虑其行为。你只需输入要使用的数，Python 通常会按你期望的方式处理它们：

>>> 0.1 + 0.1
0.2
>>> 0.2 + 0.2
0.4
>>> 2 * 0.1
0.2
>>> 2 * 0.2
0.4

但需要注意的是，结果包含的小数位数可能是不确定的：

>>> 0.2 + 0.1
0.30000000000000004
>>> 3 * 0.1
0.30000000000000004

所有语言都存在这种问题，没有什么可担心的。Python 会尽力找到一种精确表示结果的方法，但鉴于计算机内部表示数的方式，
这在有些情况下很难。就现在而言，暂时忽略多余的小数位数即可。后续你将学习处理多余小数位的方式。



整数和浮点数

将任意两个数相除时，结果总是浮点数，即便这两个数都是整数且能整除：

>>> 4/2
2.0

在其他任何运算中，如果一个操作数是整数，另一个操作数是浮点数，结果也总是浮点数：

>>> 1 + 2.0
3.0
>>> 2 * 3.0
6.0
>>> 3.0 ** 2
9.0

无论是哪种运算，只要有操作数是浮点数，Python 默认得到的总是浮点数，即便结果原本为整数也是如此。



数中的下划线

书写很大的数时，可使用下划线将其中的数字分组，使其更清晰易读：

>>> universe_age = 14_000_000_000

当你打印这种使用下划线定义的数时，Python 不会打印其中的下划线：

>>> print(universe_age)
14000000000

这是因为存储这种数时，Python 会忽略其中的下划线。将数字分组时，即便不是将每三位分成一组，也不会影响最终的值。
在 Python 看来，1000 与 1_000 没什么不同，1_000 与 10_00 也没什么不同。这种表示法适用于整数和浮点数，但
只有 Python 3.6 和更高的版本支持。



同时给多个变量赋值

可在一行代码中给多个变量赋值，这有助于缩短程序并提高其可读性。这种做法最常用于将一系列数赋给一组变量。

例如，下面演示了如何将变量 x 、y 和 z 都初始化为零：

>>> x, y, z = 0, 0, 0

这样做时，需要用逗号将变量名分开；对于要赋给变量的值，也需同样处理。Python 将按顺序将每个值赋给对应的变量。
只要变量和值的个数相同，Python 就能正确地将它们关联起来。



常量

常量类似于变量，但其值在程序的整个生命周期内保持不变。Python 没有内置的常量类型，但 Python 程序员会使用
全大写来指出应将某个变量视为常量，其值应始终不变：

MAX_CONNECTIONS = 5000

在代码中，要指出应将特定的变量视为常量，可将其字母全部大写。

"""