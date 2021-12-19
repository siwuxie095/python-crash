"""

修改、添加和删除元素


你创建的大多数列表将是动态的，这意味着列表创建后，将随着程序的运行增删元素。例如，你创建一个游戏，要求玩家射杀
从天而降的外星人。为此，可在开始时将一些外星人存储在列表中，然后每当有外星人被射杀时，都将其从列表中删除，而每
次有新的外星人出现在屏幕上时，都将其添加到列表中。在整个游戏运行期间，外星人列表的长度将不断变化。



1、修改列表元素

修改列表元素的语法与访问列表元素的语法类似。要修改列表元素，可指定列表名和要修改的元素的索引，再指定该元素的新值。

例如，假设有一个摩托车列表，其中的第一个元素为 'honda'，如何修改它的值呢？

❶ motorcycles = ['honda', 'yamaha', 'suzuki']
 print(motorcycles)

 ❷ motorcycles[0] = 'ducati'
 print(motorcycles)

首先定义一个摩托车列表，其中的第一个元素为 'honda'（见❶）。接下来，将第一个元素的值改为 'ducati'（见❷）。输出
表明，第一个元素的值确实变了，但其他列表元素的值没变：

['honda', 'yamaha', 'suzuki']
['ducati', 'yamaha', 'suzuki']

你可以修改任意列表元素的值，而不仅仅是第一个元素的值。



2、在列表中添加元素

你可能出于众多原因要在列表中添加新元素。例如，你可能希望游戏中出现新的外星人、添加可视化数据或给网站添加新注册的用户。
Python 提供了多种在既有列表中添加新数据的方式。


（1）在列表末尾添加元素

在列表中添加新元素时，最简单的方式是将元素附加（append）到列表。给列表附加元素时，它将添加到列表末尾。继续使用前一
个示例中的列表，在其末尾添加新元素'ducati'：

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

❶ motorcycles.append('ducati')
 print(motorcycles)

方法 append() 将元素 'ducati' 添加到列表末尾（见❶），而不影响列表中的其他所有元素：

['honda', 'yamaha', 'suzuki']
['honda', 'yamaha', 'suzuki', 'ducati']

方法 append() 让动态地创建列表易如反掌。例如，你可以先创建一个空列表，再使用一系列函数调用 append() 来添加元素。
下面来创建一个空列表，再在其中添加元素 'honda'、'yamaha' 和 'suzuki'：

motorcycles = []

motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

最终的列表与前述示例中的列表完全相同：

['honda', 'yamaha', 'suzuki']

这种创建列表的方式极其常见，因为经常要等程序运行后，你才知道用户要在程序中存储哪些数据。为控制用户，可首先创建一个
空列表，用于存储用户将要输入的值，然后将用户提供的每个新值附加到列表中。


（2）在列表中插入元素

使用方法 insert() 可在列表的任何位置添加新元素。为此，你需要指定新元素的索引和值。

motorcycles = ['honda', 'yamaha', 'suzuki']

❶ motorcycles.insert(0, 'ducati')
 print(motorcycles)

在这个示例中，值 'ducati' 被插入到了列表开头（见❶）。方法 insert() 在索引 0 处添加空间，并将值 'ducati' 存储
到这个地方。这种操作将列表中既有的每个元素都右移一个位置：

['ducati', 'honda', 'yamaha', 'suzuki']



3、从列表中删除元素

你经常需要从列表中删除一个或多个元素。例如，玩家将空中的一个外星人射杀后，你很可能要将其从存活的外星人列表中删除；
当用户在你创建的 Web 应用中注销账户时，你就需要将该用户从活动用户列表中删除。你可以根据位置或值来删除列表中的元素。


（1）使用 del 语句删除元素

如果知道要删除的元素在列表中的位置，可使用 del 语句。

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

❶ del motorcycles[0]
print(motorcycles)

❶处的代码使用 del 删除了列表 motorcycles 中的第一个元素 'honda'：

['honda', 'yamaha', 'suzuki']
['yamaha', 'suzuki']

使用 del 可删除任意位置处的列表元素，条件是知道其索引。例如，下面演示了如何删除前述列表中的第二个元素 'yamaha'：

motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

下面的输出表明，已经将第二款摩托车从列表中删除了：

['honda', 'yamaha', 'suzuki']
['honda', 'suzuki']

在这两个示例中，使用 del 语句将值从列表中删除后，你就无法再访问它了。


（2）使用方法 pop() 删除元素

有时候，你要将元素从列表中删除，并接着使用它的值。例如，你可能需要获取刚被射杀的外星人的 x 坐标和 y 坐标，以便在
相应的位置显示爆炸效果；在 Web 应用程序中，你可能要将用户从活跃成员列表中删除，并将其加入到非活跃成员列表中。

方法 pop() 删除列表末尾的元素，并让你能够接着使用它。术语弹出（pop）源自这样的类比：列表就像一个栈，而删除列表
末尾的元素相当于弹出栈顶元素。

下面来从列表 motorcycles 中弹出一款摩托车：

❶ motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

❷ popped_motorcycle = motorcycles.pop()
❸ print(motorcycles)
❹ print(popped_motorcycle)

首先定义并打印列表 motorcycles（见❶）。接下来，从这个列表中弹出一个值，并将其赋给变量 popped_motorcycle 中
（见❷）。然后打印这个列表，以核实从中删除了一个值（见❸）。最后打印弹出的值，以证明依然能够访问被删除的值（见❹）。

输出表明，列表末尾的值 'suzuki' 已删除，它现在被赋给了变量 popped_motorcycle：

['honda', 'yamaha', 'suzuki']
['honda', 'yamaha']
suzuki

方法 pop() 有什么用处呢？假设列表中的摩托车是按购买时间存储的，就可使用方法 pop() 打印一条消息，指出最后购买的
是哪款摩托车：

motorcycles = ['honda', 'yamaha', 'suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

输出是一个简单的句子，指出了最新购买的是哪款摩托车：

The last motorcycle I owned was a Suzuki.


（3）弹出列表中任何位置处的元素

实际上，可以使用 pop() 来删除列表中任意位置的元素，只需在圆括号中指定要删除元素的索引即可。

motorcycles = ['honda', 'yamaha', 'suzuki']

❶ first_owned = motorcycles.pop(0)
❷ print(f"The first motorcycle I owned was a {first_owned.title()}.")

首先弹出列表中的第一款摩托车（见❶），然后打印一条有关这辆摩托车的消息（见❷）。输出是一个简单的句子，描述了购买的
第一辆摩托车：

The first motorcycle I owned was a Honda.

别忘了，每当你使用 pop() 时，被弹出的元素就不再在列表中了。

如果你不确定该使用 del 语句还是 pop() 方法，下面是一个简单的判断标准：如果你要从列表中删除一个元素，且不再以
任何方式使用它，就使用 del 语句；如果你要在删除元素后还能继续使用它，就使用方法 pop()。


（4）根据值删除元素

有时候，你不知道要从列表中删除的值所处的位置。如果只知道要删除的元素的值，可使用方法 remove()。

例如，假设要从列表 motorcycles 中删除值 'ducati'。

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

❶ motorcycles.remove('ducati')
 print(motorcycles)

❶处的代码让 Python 确定 'ducati' 出现在列表的什么地方，并将该元素删除：

['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

使用 remove() 从列表中删除元素时，也可接着使用它的值。下面删除值 'ducati' 并打印一条消息，指出要将其从列表中
删除的原因：

❶ motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)

❷ too_expensive = 'ducati'
❸ motorcycles.remove(too_expensive)
 print(motorcycles)
❹ print(f"\nA {too_expensive.title()} is too expensive for me.")

定义列表（见❶）后，将值 'ducati' 赋给变量 too_expensive（见❷）。接下来，使用这个变量来告诉 Python 将哪个
值从列表中删除（见❸）。最后，值 'ducati' 已经从列表中删除，但可通过变量 too_expensive 来访问它（见❹）。这
使得能够打印一条消息，指出将 'ducati' 从列表 motorcycles 中删除的原因：

['honda', 'yamaha', 'suzuki', 'ducati']
['honda', 'yamaha', 'suzuki']

A Ducati is too expensive for me.

注意：方法 remove() 只删除第一个指定的值。如果要删除的值可能在列表中出现多次，就需要使用循环来确保将每个值都
删除。

"""