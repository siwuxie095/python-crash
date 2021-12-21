"""

使用列表的一部分


之前，你一直在学习如何处理列表的所有元素。你还可以处理列表的部分元素，Python 称之为切片。



1、切片

要创建切片，可指定要使用的第一个元素和最后一个元素的索引。与函数 range() 一样，Python
在到达第二个索引之前的元素后停止。要输出列表中的前三个元素，需要指定索引 0 和 3，这将返回
索引为 0、1 和 2 的元素。

下面的示例处理的是一个运动队成员列表：

players = ['charles', 'martina', 'michael', 'florence', 'eli']
❶ print(players[0:3])

❶处的代码打印该列表的一个切片，其中只包含三名队员。输出也是一个列表，其中包含前三名队员：

['charles', 'martina', 'michael']

你可以生成列表的任意子集。例如，如果要提取列表的第二、第三 和第四个元素，可将起始索引指定
为 1，并将终止索引指定为 4：

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

此时，切片始于 'martina'、终于 'florence'。

['martina', 'michael', 'florence']

如果没有指定第一个索引，Python 将自动从列表开头开始：

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

由于没有指定起始索引，Python 从列表开头开始提取：

['charles', 'martina', 'michael', 'florence']

要让切片终止于列表末尾，也可使用类似的语法。例如，如果要提取从第三个元素到列表末尾的所有
元素，可将起始索引指定为 2，并省略终止索引：

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

Python 将返回从第三个元素到列表末尾的所有元素：

['michael', 'florence', 'eli']

无论列表多长，这种语法都能够让你输出从特定位置到列表末尾的所有元素。之前说过，负数索引
返回离列表末尾相应距离的元素，因此你可以输出列表末尾的任意切片。例如，如果要输出名单上
的最后三名队员，可使用切片 players[-3:]：

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

上述代码打印最后三名队员的名字，即便队员名单长度发生变化，也依然如此。

注意：可在表示切片的方括号内指定第三个值。这个值告诉 Python 在指定范围内每隔多少元素
提取一个。



2、遍历切片

如果要遍历列表的部分元素，可在 for 循环中使用切片。下面的示例遍历前三名队员，并打印他们
的名字：

players = ['charles', 'martina', 'michael', 'florence', 'eli']

 print("Here are the first three players on my team:")
 ❶ for player in players[:3]:
       print(player.title())

❶处的代码没有遍历整个队员列表，而只遍历前三名队员：

Here are the first three players on my team:
Charles
Martina
Michael

在很多情况下，切片都很有用。例如，编写游戏时，你可以在玩家退出游戏时将其最终得分加入一个
列表中，然后将该列表按降序排列以获取三个最高得分，再创建一个只包含前三个得分的切片；处理
数据时，可使用切片来进行批量处理；编写 Web 应用程序时，可使用切片来分页显示信息，并在每
页显示数量合适的信息。



3、复制列表

经常需要根据既有列表创建全新的列表。下面来介绍复制列表的工作原理，以及复制列表可提供极大
帮助的一种情形。

要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]）。这让
Python 创建一个始于第一个元素、终止于最后一个元素的切片，即整个列表的副本。

例如，假设有一个列表包含你最喜欢的四种食品，而你想再创建一个列表，并在其中包含一位朋友喜
欢的所有食品。不过，你喜欢的食品，这位朋友也都喜欢，因此可通过复制来创建这个列表：

❶ my_foods = ['pizza', 'falafel', 'carrot cake']
❷ friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

首先，创建一个你喜欢的食品列表，名为 my_foods（见❶）。然后创建一个名为 friend_foods
的新列表（见❷）。在不指定任何索引的情况下从列表 my_foods 中提取一个切片，从而创建这个
列表的副本，并将该副本赋给变量 friend_foods。打印这两个列表后，发现其包含的食品相同：

My favorite foods are:
['pizza', 'falafel', 'carrot cake']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake']

为核实确实有两个列表，下面在每个列表中都添加一种食品，并核实每个列表都记录了相应人员喜欢
的食品：

my_foods = ['pizza', 'falafel', 'carrot cake']
❶ friend_foods = my_foods[:]

❷ my_foods.append('cannoli')
❸ friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

与前一个示例一样，首先将 my_foods 的元素复制到新列表 friend_foods 中（见❶）。接下来，
在每个列表中都添加一种食品：在列表 my_foods 中添加 'cannoli'（见❷），而在 friend_foods
中添加 'ice cream'（见❸）。最后，打印这两个列表，核实这两种食品分别包含在正确的列表中。

My favorite foods are:
❹ ['pizza', 'falafel', 'carrot cake', 'cannoli']

My friend's favorite foods are:
❺ ['pizza', 'falafel', 'carrot cake', 'ice cream']

❹处的输出表明，'cannoli' 包含在你喜欢的食品列表中，而 'ice cream' 不在。❺处的输出表明，
'ice cream' 包含在你朋友喜欢的食品列表中，而 'cannoli' 不在。如果只是将 my_foods 赋给
friend_foods，就不能得到两个列表。例如，下面演示了在不使用切片的情况下复制列表的情况：

my_foods = ['pizza', 'falafel', 'carrot cake']

# 行不通
❶ friend_foods = my_foods

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

这里将 my_foods 赋给 friend_foods，而不是将 my_foods 的副本赋给 friend_foods（见❶）。
这种语法实际上是让 Python 将新变量 friend_foods 关联到已与 my_foods 相关联的列表，因此
这两个变量指向同一个列表。

有鉴于此，当将 'cannoli' 添加到 my_foods 中时，它也将出现在 friend_foods 中。同样，虽然
'ice cream' 好像只被加入到了 friend_foods 中，但它也将出现在这两个列表中。

输出表明，两个列表是相同的，这并非想要的结果：

My favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

My friend's favorite foods are:
['pizza', 'falafel', 'carrot cake', 'cannoli', 'ice cream']

注意：暂时不要考虑这个示例中的细节。当试图使用列表的副本时结果出乎意料，基本上都要确认你是否像
第一个示例那样使用切片复制了列表。

"""