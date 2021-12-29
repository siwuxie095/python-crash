"""

使用字典


在 Python 中，字典是一系列键值对 。每个键都与一个值相关联，你可使用键来访问相关联的值。与键
相关联的值可以是数、字符串、列表乃至字典。事实上，可将任何 Python 对象用作字典中的值。

在 Python 中，字典用放在花括号（{}）中的一系列键值对表示，如前面的示例所示：

alien_0 = {'color': 'green', 'points': 5}

键值对是两个相关联的值。指定键时，Python 将返回与之相关联的值。键和值之间用冒号分隔，而键值
对之间用逗号分隔。在字典中，想存储多少个键值对都可以。

最简单的字典只有一个键值对，如下述修改后的字典 alien_0 所示：

alien_0 = {'color': 'green'}

这个字典只存储了一项有关 alien_0 的信息，具体地说是这个外星人的颜色。在该字典中，字符串
'color' 是一个键，与之相关联的值为 'green'。



1、访问字典中的值

要获取与键相关联的值，可依次指定字典名和放在方括号内的键，如下所示：

alien_0 = {'color': 'green'}

print(alien_0['color'])

这将返回字典 alien_0 中与键 'color' 相关联的值：

green

字典中可包含任意数量的键值对。例如，下面是最初的字典 alien_0，其中包含两个键值对：

alien_0 = {'color': 'green', 'points': 5}

现在，你可访问外星人 alien_0 的颜色和分数。如果玩家射杀了这个外星人，就可以使用下面的代码来
确定应获得多少分：

alien_0 = {'color': 'green', 'points': 5}

❶ new_points = alien_0['points']
❷ print(f"You just earned {new_points} points!")

上述代码首先定义了一个字典。然后，从这个字典中获取与键 'points' 相关联的值（见❶），并将这个
值赋给变量 new_points。接下来，将这个整数转换为字符串，并打印一条消息，指出玩家获得了多少分
（见❷）：

You just earned 5 points!

如果在外星人被射杀时运行这段代码，就将获取该外星人的分数。



2、添加键值对

字典是一种动态结构，可随时在其中添加键值对。要添加键值对，可依次指定字典名、用方括号括起的键和
相关联的值。

下面来在字典 alien_0 中添加两项信息：外星人的坐标和坐标，使得能够在屏幕的特定位置显示该外星
人。这里将这个外星人放在屏幕左边缘，且离屏幕顶部 25 像素的地方。由于屏幕坐标系的原点通常为左
上角，要将该外星人放在屏幕左边缘，可将 x 坐标设置为 0；要将该外星人放在离屏幕顶部 25 像素的
地方，可将 y 坐标设置为 25，如下所示：

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

❶ alien_0['x_position'] = 0
❷ alien_0['y_position'] = 25
print(alien_0)

首先定义前面一直在使用的字典，然后打印这个字典，以显示其信息快照。在❶处，在这个字典中新增了一
个键值对，其中的键为 'x_position'，值为 0。在❷处重复这样的操作，但使用的键为 'y_position'。
打印修改后的字典时，将看到这两个新增的键值对：

{'color': 'green', 'points': 5}
{'color': 'green', 'points': 5, 'x_position': 0, 'y_position': 25}

这个字典的最终版本包含四个键值对：原来的两个指定外星人的颜色和分数，而新增的两个指定其位置。

注意：在 Python 3.7 中，字典中元素的排列顺序与定义时相同。如果将字典打印出来或遍历其元素，
将发现元素的排列顺序与添加顺序相同。



3、先创建一个空字典

在空字典中添加键值对有时候可提供便利，而有时候必须这样做。为此，可先使用一对空花括号定义一个
字典，再分行添加各个键值对。例如，下面演示了如何以这种方式创建字典 alien_0：

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

这里首先定义了空字典 alien_0，再在其中添加颜色和分数，得到前述示例一直在使用的字典：

{'color': 'green', 'points': 5}

使用字典来存储用户提供的数据或在编写能自动生成大量键值对的代码时，通常需要先定义一个空字典。



4、修改字典中的值

要修改字典中的值，可依次指定字典名、用方括号括起的键，以及与该键相关联的新值。例如，假设随着
游戏的进行，需要将一个外星人从绿色改为黄色：

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}.")

首先定义一个表示外星人 alien_0 的字典，其中只包含这个外星人的颜色。接下来，将与键 'color'
相关联的值改为 'yellow'。输出表明，这个外星人确实从绿色变成了黄色：

The alien is green.
The alien is now yellow.

来看一个更有趣的例子，对一个能够以不同速度移动的外星人进行位置跟踪。为此，需要将存储该外星人
的当前速度，并据此确定该外星人将向右移动多远：

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# 向右移动外星人。
# 根据当前速度确定将外星人向右移动多远。
❶ if alien_0['speed'] == 'slow':
         x_increment = 1
elif alien_0['speed'] == 'medium':
         x_increment = 2
else:
        # 这个外星人的移动速度肯定很快。
        x_increment = 3

# 新位置为旧位置加上移动距离。
❷ alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

首先定义一个外星人，其中包含初始 x 坐标和 y 坐标，还有速度 'medium'。出于简化考虑，省略了
颜色和分数，但即便包含这些键值对，本例的工作原理也不会有任何变化。这里还打印了 x_position
的初始值，旨在让用户知道这个外星人向右移动了多远。

❶处使用一个 if-elif-else 结构来确定外星人应向右移动多远，并将这个值赋给变量 x_increment。
如果外星人的速度为 'slow'，它将向右移动一个单位；如果速度为 'medium'，将向右移动两个单位；
如果为 'fast'，将向右移动三个单位。确定移动距离后，将其与 x_position 的当前值相加（见❷），
再将结果关联到字典中的键 x_position。

因为这是一个速度中等的外星人，所以其位置将向右移两个单位：

Original position: 0
New position: 2

这种技术很棒：通过修改外星人字典中的值，可改变外星人的行为。例如，要将这个速度中等的外星人变成
速度很快的外星人，可添加如下代码行：

alien_0['speed'] = 'fast'

这样，再次运行这些代码时，其中的 if-elif-else 结构将把一个更大的值赋给变量 x_increment。



5、删除键值对

对于字典中不再需要的信息，可使用 del 语句将相应的键值对彻底删除。使用 del 语句时，必须指定字典
名和要删除的键。

例如，下面的代码从字典 alien_0 中删除键 'points' 及其值：

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

❶ del alien_0['points']
print(alien_0)

❶处的代码行让 Python 将键 'points' 从字典 alien_0 中删除，同时删除与这个键相关联的值。输出
表明，键 'points' 及其值 5 已从字典中删除，但其他键值对未受影响：

{'color': 'green', 'points': 5}
{'color': 'green'}

注意：删除的键值对会永远消失。



6、由类似对象组成的字典

在前面的示例中，字典存储的是一个对象（游戏中的一个外星人）的多种信息，但你也可以使用字典来存储众多
对象的同一种信息。例如，假设你要调查很多人，询问他们最喜欢的编程语言，可使用一个字典来存储这种简单
调查的结果，如下所示：

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

如你所见，这里将一个较大的字典放在了多行中。每个键都是一个被调查者的名字，而每个值都是被调查者喜欢
的语言。确定需要使用多行来定义字典时，要在输入左花括号后按回车键。在下一行缩进四个空格，指定第一个
键值对，并在它后面加上一个逗号。此后再按回车键时，文本编辑器将自动缩进后续键值对，且缩进量与第一个
键值对相同。

定义好字典后，在最后一个键值对的下一行添加一个右花括号，并缩进四个空格，使其与字典中的键对齐。一种
不错的做法是，在最后一个键值对后面也加上逗号，为以后在下一行添加键值对做好准备。

注意：对于较长的列表和字典，大多数编辑器提供了以类似方式设置格式的功能。对于较长的字典，还有其他一
些可行的格式设置方式，因此在你的编辑器或其他源代码中，你可能会看到稍微不同的格式设置方式。

给定被调查者的名字，可使用这个字典轻松地获悉他喜欢的语言：

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

❶ language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

为获悉 Sarah 喜欢的语言，使用如下代码：

favorite_languages['sarah']

在❶处，使用这种语法获取 Sarah 喜欢的语言，并将其赋给变量 language。创建这个新变量让函数调用
print() 变得整洁得多。输出指出了 Sarah 喜欢的语言：

Sarah's favorite language is C.

这种语法可用来从字典中获取任何人喜欢的语言。



7、使用 get() 来访问值

使用放在方括号内的键从字典中获取感兴趣的值时，可能会引发问题：如果指定的键不存在就会出错。

如果你要求获取外星人的分数，而这个外星人没有分数，结果将如何呢？下面来看一看：

alien_0 = {'color': 'green', 'speed': 'slow'}
print(alien_0['points'])

这将导致 Python 显示 traceback，指出存在键值错误（KeyError）：

Traceback (most recent call last):
  File "alien_no_points.py", line 2, in <module>
    print(alien_0['points'])
KeyError: 'points'

后续将详细介绍如何处理类似的错误，但就字典而言，可使用方法 get() 在指定的键不存在时返回一个默认
值，从而避免这样的错误。

方法 get() 的第一个参数用于指定键，是必不可少的；第二个参数为指定的键不存在时要返回的值，是可选
的：

alien_0 = {'color': 'green', 'speed': 'slow'}
point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)

如果字典中有键 'points'，将获得与之相关联的值；如果没有，将获得指定的默认值。虽然这里没有键
'points'，但将获得一条清晰的消息，不会引发错误：

No point value assigned.

如果指定的键有可能不存在，应考虑使用方法 get()，而不要使用方括号表示法。

注意：调用 get() 时，如果没有指定第二个参数且指定的键不存在，Python 将返回值 None。这个特殊
值表示没有相应的值。None 并非错误，而是一个表示所需值不存在的特殊值，后续将介绍它的其他用途。

"""