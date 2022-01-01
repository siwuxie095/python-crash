"""

函数 input() 的工作原理


函数 input() 让程序暂停运行，等待用户输入一些文本。获取用户输入后，Python 将其
赋给一个变量，以方便你使用。

例如，下面的程序让用户输入一些文本，再将这些文本呈现给用户：

message = input("Tell me something, and I will repeat it back to you: ")
print(message)

函数 input() 接受一个参数——要向用户显示的提示（prompt）或说明，让用户知道该如何做。
在本例中，Python 运行第一行代码时，用户将看到提示 Tell me something, and I will
repeat it back to you:。程序等待用户输入，并在用户按回车键后继续运行。输入被赋给变量
message，接下来的 print(message) 将输入呈现给用户：

Tell me something, and I will repeat it back to you: Hello everyone!
Hello everyone!

注意：Sublime Text 等众多编辑器不能运行提示用户输入的程序。你可以使用 Sublime Text
来编写提示用户输入的程序，但必须从终端运行它们。



1、编写清晰的程序

每当使用函数 input() 时，都应指定清晰易懂的提示，准确地指出希望用户提供什么样的信息——
指出用户应该输入何种信息的任何提示都行，如下所示：

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

通过在提示末尾（这里是冒号后面）包含一个空格，可将提示与用 户输入分开，让用户清楚地知道
其输入始于何处，如下所示：

Please enter your name: Eric
Hello, Eric!

有时候，提示可能超过一行。例如，你可能需要指出获取特定输入的原因。在这种情况下，可将提示
赋给一个变量，再将该变量传递给函数 input()。这样，即便提示超过一行，input() 语句也会
非常清晰。

prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "

name = input(prompt)
print(f"\nHello, {name}!")

本例演示了一种创建多行字符串的方式。第一行将消息的前半部分赋给变量 prompt 中。在第二行
中，运算符 += 在前面赋给变量 prompt 的字符串末尾附加一个字符串。

最终的提示占据两行，且问号后面有一个空格，这也是为了使其更加清晰：

If you tell us who you are, we can personalize the messages you see.
What is your first name? Eric

Hello, Eric!



2、使用 int() 来获取数值输入

使用函数 input() 时，Python 将用户输入解读为字符串。请看下面让用户输入年龄的解释器会话：

>>> age = input("How old are you? ")
How old are you? 21
>>> age
'21'

用户输入的是数 21，但这里请求 Python 提供变量 age 的值时，它返回的是 '21' —— 用户输入
数值的字符串表示。怎么知道 Python 将输入解读成了字符串呢？因为这个数用引号括起了。如果只想
打印输入，这一点问题都没有；但如果试图将输入作为数来使用，就会引发错误：

 >>> age = input("How old are you? ")
 How old are you? 21
❶ >>> age >= 18
  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
❷ TypeError: unorderable types: str() >= int()

试图将输入用于数值比较时（见❶），Python 会引发错误，因为它无法将字符串和整数进行比较：不
能将赋给 age 的字符串 '21' 与数值 18 进行比较（见❷）。

为解决这个问题，可使用函数 int()，它让 Python 将输入视为数值。函数 int() 将数的字符串
表示转换为数值表示，如下所示：

 >>> age = input("How old are you? ")
 How old are you? 21
❶ >>> age = int(age)
>>> age >= 18
True

在本例中，用户根据提示输入 21 后，Python 将这个数解读为字符串，但随后 int() 将这个字符
串转换成了数值表示（见❶）。这样 Python 就能运行条件测试了：将变量 age（它现在表示的是数
值 21）同 18 进行比较，看它是否大于或等于 18。测试结果为 True。

如何在实际程序中使用函数 int() 呢？请看下面的程序，它判断一个人是否满足坐过山车的身高要求：

height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

在此程序中，为何可以将 height 同 48 进行比较呢？因为在比较前，height = int(height)
将输入转换成了数值表示。如果输入的数大于或等于 48，就指出用户满足身高条件：

How tall are you, in inches? 71

You're tall enough to ride!

将数值输入用于计算和比较前，务必将其转换为数值表示。



3、求模运算符

处理数值信息时，求模运算符（%）是个很有用的工具，它将两个数相除并返回余数：

>>> 4 % 3
1
>>> 5 % 3
2
>>> 6 % 3
0
>>> 7 % 3
1

求模运算符不会指出一个数是另一个数的多少倍，只指出余数是多少。

如果一个数可被另一个数整除，余数就为 0，因此求模运算将返回 0。可利用这一点来判断一个数是
奇数还是偶数：

number = input("Enter a number, and I'll tell you if it's even or odd: ")
number = int(number)

if number % 2 == 0:
    print(f"\nThe number {number} is even.")
else:
    print(f"\nThe number {number} is odd.")

偶数都能被 2 整除，因此如果对一个数和 2 执行求模运算的结果为 0，即 number % 2 == 0，
那么这个数就是偶数；否则就是奇数。

Enter a number, and I'll tell you if it's even or odd: 42

The number 42 is even.

"""