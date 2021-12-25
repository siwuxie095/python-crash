"""

if 语句


理解条件测试后，就可以开始编写 if 语句了。if 语句有很多种，选择使用哪种取决于要测试的条件数。
前面讨论条件测试时，列举了多个 if 语句示例，下面更深入地讨论这个主题。



1、简单的 if 语句

最简单的 if 语句只有一个测试和一个操作：

if conditional_test:
    do something

第一行可包含任何条件测试，而在紧跟在测试后面的缩进代码块中，可执行任何操作。如果条件测试的结果
为 True，Python 就会执行紧跟在 if 语句后面的代码，否则 Python 将忽略这些代码。

假设有一个表示某人年龄的变量，而你想知道这个人是否符合投票的年龄，可使用如下代码：

age = 19
❶ if age >= 18:
❷     print("You are old enough to vote!")

在❶处，Python 检查变量 age 的值是否大于或等于 18。答案是肯定的，因此 Python 执行❷处缩进
的函数调用 print()：

You are old enough to vote!

在 if 语句中，缩进的作用与在 for 循环中相同。如果测试通过了，将执行 if 语句后面所有缩进的代
码行，否则将忽略它们。

在紧跟 if 语句后面的代码块中，可根据需要包含任意数量的代码行。下面在一个人符合投票年龄时再打印
一行输出，问他是否登记了：

age = 19
if age >= 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")

条件测试通过了，而且两个函数调用 print() 都缩进了，因此它们都将执行：

You are old enough to vote!
Have you registered to vote yet?

如果 age 的值小于 18，这个程序将不会有任何输出。



2、if-else 语句

经常需要在条件测试通过时执行一个操作，在没有通过时执行另一个操作。在这种情况下，可使用 Python
提供的 if-else 语句。if-else 语句块类似于简单的 if 语句，但其中的 else 语句让你能够指定
条件测试未通过时要执行的操作。

下面的代码在一个人符合投票年龄时显示与前面相同的消息，在不符合时显示一条新消息：

age = 17
❶ if age >= 18:
      print("You are old enough to vote!")
      print("Have you registered to vote yet?")
❷ else:
     print("Sorry, you are too young to vote.")
     print("Please register to vote as soon as you turn 18!")

如果❶处的条件测试通过了，就执行第一组缩进的函数调用 print()。如果测试结果为 False，就执行
❷处的 else 代码块。这次 age 小于 18，条件测试未通过，因此执行 else 代码块中的代码：

Sorry, you are too young to vote.
Please register to vote as soon as you turn 18!

上述代码之所以可行，是因为只存在两种情形：要么符合投票年龄，要么不符合。if-else 结构非常适合
用于让 Python 执行两种操作之一的情形。在这样简单的 if-else 结构中，总是会执行两个操作中的
一个。



3、if-elif-else 结构

经常需要检查超过两个的情形，为此可使用 Python 提供的 if-elif-else 结构。Python 只执行
if-elif-else 结构中的一个代码块。它依次检查每个条件测试，直到遇到通过了的条件测试。测试通
过后，Python 将执行紧跟在它后面的代码，并跳过余下的测试。

在现实世界中，很多情况下需要考虑的情形超过两个。例如，来看一个根据年龄段收费的游乐场：

age = 12

❶ if age < 4:
      print("Your admission cost is $0.")
❷ elif age < 18:
      print("Your admission cost is $25.")
❸ else:
      print("Your admission cost is $40.")

❶处的 if 测试检查一个人是否不满 4 岁。如果是，Python 就打印一条合适的消息，并跳过余下测试。
❷处的 elif 代码行其实是另一个 if 测试，仅在前面的测试未通过时才会运行。在这里，已经知道这个
人不小于 4 岁，因为第一个测试未通过。如果这个人未满 18 岁，Python 将打印相应的消息，并跳过
else 代码块。如果 if 测试和 elif 测试都未通过，Python 将运行❸处 else 代码块中的代码。

在本例中，❶处测试的结果为 False，因此不执行其代码块。然而，第二个测试的结果为 True（12 小于
18），因此执行其代码块。输出为一个句子，向用户指出门票价格：

Your admission cost is $25.

只要年龄超过 17 岁，前两个测试就都不能通过。在这种情况下，将执行 else 代码块，指出门票价格为
40 美元。

为了让代码更简洁，可不在 if-elif-else 代码块中打印门票价格，而只在其中设置门票价格，并在它
后面添加一个简单的函数调用 print()：

age = 12

if age < 4:
❶    price = 0
elif age < 18:
❷    price = 25
else:
❸    price = 40

❹ print(f"Your admission cost is ${price}.")

❶处、❷处和❸处的代码行像前一个示例那样，根据人的年龄设置变量 price 的值。在 if-elif-else
结构中设置 price 的值后，一条未缩进的函数调用 print() ❹会根据这个变量的值打印一条消息，指出
门票的价格。

这些代码的输出与前一个示例相同，但 if-elif-else 结构的作用更小：它只确定门票价格，而不是在确定
门票价格的同时打印一条消息。除效率更高外，这些修订后的代码还更容易修改：要调整输出消息的内容，只
需修改一个而不是三个函数调用 print()。



4、使用多个 elif 代码块

可根据需要使用任意数量的 elif 代码块。例如，假设前述游乐场要给老年人打折，可再添加一个条件测试，
判断顾客是否符合打折条件。下面假设对于 65 岁（含）以上的老人，可半价（即 20 美元） 购买门票：

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
❶ elif age < 65:
    price = 40
❷ else:
    price = 20

print(f"Your admission cost is ${price}.")

这些代码大多未变。第二个 elif 代码块（见❶）通过检查确定年龄不到 65 岁后，才将门票价格设置为
全票价格——40 美元。请注意，在 else 代码块（见❷）中，必须将所赋的值改为 20，因为仅当年龄超过
65岁（含）时，才会执行这个代码块。



5、省略 else 代码块

Python 并不要求 if-elif 结构后面必须有 else 代码块。在有些情况下，else 代码块很有用；而
在其他一些情况下，使用一条 elif 语句来处理特定的情形更清晰：

age = 12

if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
❶ elif age >= 65:
    price = 20

print(f"Your admission cost is ${price}.")

❶处的 elif 代码块在顾客的年龄超过65岁（含）时，将价格设置为 20 美元。这比使用 else 代码块
更清晰些。经过这样的修改后，每个代码块都仅在通过了相应的测试时才会执行。

else 是一条包罗万象的语句，只要不满足任何 if 或 elif 中的条件测试，其中的代码就会执行。这
可能引入无效甚至恶意的数据。如果知道最终要测试的条件，应考虑使用一个 elif 代码块来代替 else
代码块。这样就可以肯定，仅当满足相应的条件时，代码才会执行。



6、测试多个条件

if-elif-else 结构功能强大，但仅适合用于只有一个条件满足的情况：遇到通过了的测试后，Python
就跳过余下的测试。这种行为很好，效率很高，让你能够测试一个特定的条件。

然而，有时候必须检查你关心的所有条件。在这种情况下，应使用一系列不包含 elif 和 else 代码块
的简单 if 语句。在可能有多个条件为 True 且需要在每个条件为 True 时都采取相应措施时，适合
使用这种方法。

下面再来看看前面的比萨店示例。如果顾客点了两种配料，就需要确保在其比萨中包含这些配料：

❶ requested_toppings = ['mushrooms', 'extra cheese']

❷ if 'mushrooms' in requested_toppings:
      print("Adding mushrooms.")
❸ if 'pepperoni' in requested_toppings:
      print("Adding pepperoni.")
❹ if 'extra cheese' in requested_toppings:
      print("Adding extra cheese.")

print("\nFinished making your pizza!")

首先创建一个列表，其中包含顾客点的配料（见❶）。❷处的 if 语句检查顾客是否点了配料蘑菇
（mushrooms）。如果点了，就打印一条确认消息。❸处检查配料辣香肠（pepperoni）的代码
也是一个简单的 if 语句，而不是 elif 或 else 语句。因此不管前一个测试是否通过，都将
进行这个测试。❹处的代码检查顾客是否要求多加芝士（extra cheese）。不管前两个测试的
结果如何，都会执行这些代码。每当这个程序运行时，都会执行这三个独立的测试。

因为本例检查了每个条件，所以将在比萨中添加蘑菇并多加芝士：

Adding mushrooms.
Adding extra cheese.

Finished making your pizza!

如果像下面这样转而使用 if-elif-else 结构，代码将不能正确运行，因为有一个测试通过后，
就会跳过余下的测试：

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")

第一个测试检查列表中是否包含 'mushrooms'。它通过了，因此将在比萨中添加蘑菇。然而，
Python 将跳过 if-elif-else 结构中余下的测试，不再检查列表中是否包含 'pepperoni'
和 'extra cheese'。结果是，将添加顾客点的第一种配料，但不会添加其他配料：

Adding mushrooms.

Finished making your pizza!

总之，如果只想执行一个代码块，就使用 if-elif-else 结构；如果要执行多个代码块，就使用
一系列独立的 if 语句。

"""