"""

测试函数


要学习测试，必须有要测试的代码。下面是一个简单的函数，它接受名和姓并返回整洁的姓名：

def get_formatted_name(first, last):
    \"""生成整洁的姓名。\"""
    full_name = f"{first} {last}"
    return full_name.title()

函数 get_formatted_name() 将名和姓合并成姓名：在名和姓之间加上一个空格并将其首字母大写，再
返回结果。为核实 get_formatted_name() 像期望的那样工作，下面来编写一个使用该函数的程序。程
序 names.py 让用户输入名和姓，并显示整洁的姓名：

from name_function import get_formatted_name

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: ")
    if first == 'q':
        break
    last = input("Please give me a last name: ")
    if last == 'q':
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\tNeatly formatted name: {formatted_name}.")

这个程序从 name_function.py 中导入 get_formatted_name()。用户可输入一系列名和姓，并看
到格式整洁的姓名：

Enter 'q' at any time to quit.

Please give me a first name: janis
Please give me a last name: joplin
	Neatly formatted name: Janis Joplin.

Please give me a first name: bob
Please give me a last name: dylan
	Neatly formatted name: Bob Dylan.

Please give me a first name: q

从上述输出可知，合并得到的姓名正确无误。现在假设要修改 get_formatted_name()，使其还能够处理
中间名。这样做时，要确保不破坏这个函数处理只含有名和姓的姓名的方式。

为此，可在每次修改 get_formatted_name() 后都进行测试：运行程序 names.py，并输入像 Janis
Joplin 这样的姓名。不过这太烦琐了。所幸 Python 提供了一种自动测试函数输出的高效方式。倘若对
get_formatted_name() 进行自动测试，就能始终确信当提供测试过的姓名时，该函数都能正确工作。



1、单元测试和测试用例

Python 标准库中的模块 unittest 提供了代码测试工具。单元测试用于核实函数的某个方面没有问题。
测试用例是一组单元测试，它们一道核实函数在各种情形下的行为都符合要求。良好的测试用例考虑到了
函数可能收到的各种输入，包含针对所有这些情形的测试。全覆盖的测试用例包含一整套单元测试，涵盖了
各种可能的函数使用方式。对于大型项目，要进行全覆盖测试可能很难。通常，最初只要针对代码的重要
行为编写测试即可，等项目被广泛使用时再考虑全覆盖。



2、可通过的测试

你需要一段时间才能习惯创建测试用例的语法，但创建测试用例之后，再添加针对函数的单元测试就很简单
了。要为函数编写测试用例，可先导入模块 unittest 和要测试的函数，再创建一个继承 unittest
.TestCase 的类，并编写一系列方法对函数行为的不同方面进行测试。

下面的测试用例只包含一个方法，它检查函数 get_formatted_name() 在给定名和姓时能否正确工作：

import unittest
from name_function import get_formatted_name

❶ class NamesTestCase(unittest.TestCase):
    \"""测试name_function.py。\"""

    def test_first_last_name(self):
        \"""能够正确地处理像Janis Joplin这样的姓名吗？\"""
❷        formatted_name = get_formatted_name('janis', 'joplin');
❸        self.assertEqual(formatted_name, 'Janis Joplin')

❹ if __name__ == '__main__':
    unittest.main()

首先，导入了模块 unittest 和要测试的函数 get_formatted_name()。在❶处，创建了一个名为
NamesTestCase 的类，用于包含一系列针对 get_formatted_name() 的单元测试。这个类可以
随意命名，但最好让它看起来与要测试的函数相关并包含 Test 字样。这个类必须继承 unittest
.TestCase 类，这样 Python 才知道如何运行你编写的测试。

NamesTestCase 只包含一个方法，用于测试 get_formatted_name() 的一个方面。将该方法命名
为 test_first_last_name()，因为要核实的是只有名和姓的姓名能否被正确格式化。

运行 test_name_function.py 时，所有以 test_ 打头的方法都将自动运行。在这个方法中，调用
了要测试的函数。在本例中，使用实参 'janis' 和 'joplin' 调用 get_formatted_name()，
并将结果赋给变量 formatted_name（见❷）。

在❸处，使用了 unittest 类最有用的功能之一：断言方法。断言方法核实得到的结果是否与期望的结果
一致。在这里，已经知道 get_formatted_name() 应返回名和姓首字母大写且之间有一个空格的姓名，
因此期望 formatted_name 的值为 Janis Joplin。为检查是否确实如此，这里调用 unittest 的
方法 assertEqual()，并向它传递 formatted_name 和 'Janis Joplin'。代码行

self.assertEqual(formatted_name, 'Janis Joplin')

的意思是：“将 formatted_name 的值与字符串 'Janis Joplin' 比较。如果它们相等，那么万事
大吉；如果它们不相等，就告诉我一声！”

这里将直接运行这个文件，但需要指出的是，很多测试框架都会先导入测试文件再运行。导入文件时，解释
器将在导入的同时执行它。❹处的 if 代码块检查特殊变量 __name__，这个变量是在程序执行时设置的。
如果这个文件作为主程序执行，变量 __name__ 将被设置为 '__main__'。在这里，调用 unittest
.main() 来运行测试用例。如果这个文件被测试框架导入，变量 __name__ 的值将不是 '__main__'，
因此不会调用unittest.main()。

运行 test_name_function.py 时，得到的输出如下：

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

第一行的句点表明有一个测试通过了。接下来的一行指出 Python 运行了一个测试，消耗的时间不到
0.001 秒。最后的 OK 表明该测试用例中的所有单元测试都通过了。

上述输出表明，给定包含名和姓的姓名时，函数 get_formatted_name() 总是能正确地处理。修改
get_formatted_name() 后，可再次运行这个测试用例。如果它通过了，就表明给定 Janis Joplin
这样的姓名时，该函数依然能够正确地处理。



3、未通过的测试

测试未通过时结果是什么样的呢？这里来修改 get_formatted_name()，使其能够处理中间名，但同时
故意让该函数无法正确处理像 Janis Joplin 这样只有名和姓的姓名。

下面是函数 get_formatted_name() 的新版本，它要求通过一个实参指定中间名：

def get_formatted_name(first, middle, last):
    \"""生成整洁的姓名。\"""
    full_name = f"{first} {middle} {last}"
    return full_name.title()

这个版本应该能够正确处理包含中间名的姓名，但对其进行测试时，发现它不再能正确处理只有名和姓的姓
名。这次运行程序 test_name_function.py 时，输出如下：

❶ E
 ======================================================================
❷ ERROR: test_first_last_name (__main__.NamesTestCase)
 ----------------------------------------------------------------------
❸ Traceback (most recent call last):
     File "test_name_function.py", line 8, in test_first_last_name
       formatted_name = get_formatted_name('janis', 'joplin')
TypeError: get_formatted_name() missing 1 required positional argument: 'last'

 ----------------------------------------------------------------------
❹ Ran 1 test in 0.000s

❺ FAILED (errors=1)

里面包含很多信息，因为测试未通过时，需要让你知道的事情可能有很多。第一行输出只有一个字母 E（见❶），
指出测试用例中有一个单元测试导致了错误。接下来，看到 NamesTestCase 中的 test_first_last_name()
导致了错误（见❷）。测试用例包含众多单元测试时，知道哪个测试未通过至关重要。在❸处，看到了一个标准
的 traceback，指出函数调用 get_formatted_name('janis', 'joplin') 有问题，因为缺少一个
必不可少的位置实参。

还看到运行了一个单元测试（见❹）。最后是一条消息，指出整个测试用例未通过，因为运行该测试用例时发生
了一个错误（见❺）。这条消息位于输出末尾，让你一眼就能看到。你可不希望为获悉有多少测试未通过而翻阅
长长的输出。



4、测试未通过时怎么办

测试未通过时怎么办呢？如果你检查的条件没错，测试通过意味着函数的行为是对的，而测试未通过意味着
编写的新代码有错。因此，测试未通过时，不要修改测试，而应修复导致测试不能通过的代码：检查刚刚对
函数所做的修改，找出导致函数行为不符合预期的修改。

在本例中，get_formatted_name() 以前只需要名和姓两个实参，但现在要求提供名、中间名和姓。新增
的中间名参数是必不可少的，这导致 get_formatted_name() 的行为不符合预期。就这里而言，最佳的
选择是让中间名变为可选的。这样做后，使用类似于 Janis Joplin 的姓名进行测试时，测试就又能通过
了，而且也可以接受中间名。下面来修改 get_formatted_name()，将中间名设置为可选的，然后再次
运行这个测试用例。如果通过了，就接着确认该函数能够妥善地处理中间名。

要将中间名设置为可选的，可在函数定义中将形参 middle 移到形参列表末尾，并将其默认值指定为一个
空字符串。还需要添加一个 if 测试，以便根据是否提供了中间名相应地创建姓名：

def get_formatted_name(first, last, middle=''):
    \"""生成整洁的姓名。\"""
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}"
    return full_name.title()

在 get_formatted_name() 的这个新版本中，中间名是可选的。如果向该函数传递了中间名，姓名将
包含名、中间名和姓，否则姓名将只包含名和姓。现在，对于两种不同的姓名，这个函数都应该能够正确
地处理。

为确定这个函数依然能够正确处理像 Janis Joplin 这样的姓名，再次运行 test_name_function.py：

.
----------------------------------------------------------------------
Ran 1 test in 0.000s

OK

现在，测试用例通过了。太好了，这意味着这个函数又能正确处理像 Janis Joplin 这样的姓名了，而且
无须手工测试这个函数。这个函数之所以很容易修复，是因为未通过的测试让你得知新代码破坏了函数原来的
行为。



5、添加新测试

确定 get_formatted_name() 又能正确处理简单的姓名后，这里再编写一个测试，用于测试包含中间名
的姓名。为此，在 NamesTestCase 类中再添加一个方法：

--snip--
class NamesTestCase(unittest.TestCase):
    \"""测试name_function.py。\"""

    def test_first_last_name(self):
        --snip--

    def test_first_last_middle_name(self):
        \"""能够正确地处理像Wolfgang Amadeus Mozart这样的姓名吗？\"""
        formatted_name = get_formatted_name('wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

将该方法命名为 test_first_last_middle_name()。方法名必须以 test_ 打头，这样它才会在运行
test_name_function.py 时自动运行。这个方法名清楚地指出了它测试的是 get_formatted_name()
的哪个行为。这样，如果该测试未通过，就能马上知道受影响的是哪种类型的姓名。可以在 TestCase 类中
使用很长的方法名，而且这些方法名必须是描述性的，这样你才能看懂测试未通过时的输出。这些方法由
Python 自动调用，你根本不用编写调用它们的代码。

为测试函数 get_formatted_name()，这里使用名、姓和中间名调用它（见❶），再使用 assertEqual()
检查返回的姓名是否与预期的姓名（名、中间名和姓）一致。再次运行 test_name_function.py 时，
两个测试都通过了：

..
----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK

太好了！现在就知道，这个函数又能正确地处理像 Janis Joplin 这样的姓名了，而且深信它也能够正确地
处理像 Wolfgang Amadeus Mozart 这样的姓名。

"""