"""

嵌套


有时候，需要将一系列字典存储在列表中，或将列表作为值存储在字典中，这称为嵌套。你可以在列表中
嵌套字典、在字典中嵌套列表甚至在字典中嵌套字典。正如下面的示例将演示的，嵌套是一项强大的功能。



1、字典列表

字典 alien_0 包含一个外星人的各种信息，但无法存储第二个外星人的信息，更别说屏幕上全部外星
人的信息了。如何管理成群结队的外星人呢？一种办法是创建一个外星人列表，其中每个外星人都是一个
字典，包含有关该外星人的各种信息。例如，下面的代码创建一个包含三个外星人的列表：

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

❶ aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

首先创建三个字典，其中每个字典都表示一个外星人。然后在❶处将这些字典都存储到一个名为 aliens
的列表中。最后，遍历这个列表，并将每个外星人都打印出来：

{'color': 'green', 'points': 5}
{'color': 'yellow', 'points': 10}
{'color': 'red', 'points': 15}

更符合现实的情形是，外星人不止三个，且每个外星人都是使用代码自动生成的。在下面的示例中，使用
range() 生成了 30 个外星人：

# 创建一个用于存储外星人的空列表。
aliens = []

 # 创建30个绿色的外星人。
❶ for alien_number in range(30):
        ❷ new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
        ❸ aliens.append(new_alien)

 # 显示前5个外星人。
❹ for alien in aliens[:5]:
         print(alien)
print("...")

 # 显示创建了多少个外星人。
❺ print(f"Total number of aliens: {len(aliens)}")

在本例中，首先创建一个空列表，用于存储接下来将创建的所有外星人。在❶处，range() 返回一系列数，
其唯一的用途是告诉 Python 要重复这个循环多少次。每次执行这个循环时，都创建一个外星人（见❷），
并将其附加到列表 aliens 末尾（见❸）。在❹处，使用一个切片来打印前 5 个外星人。在❺处，打印
列表的长度，以证明确实创建了 30 个外星人：


{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...
Total number of aliens: 30

这些外星人都具有相同的特征，但在 Python 看来，每个外星人都是独立的，这使得能够独立地修改每个
外星人。

在什么情况下需要处理成群结队的外星人呢？想象一下，可能随着游戏的进行，有些外星人会变色且加快
移动速度。必要时，可使用 for 循环和 if 语句来修改某些外形人的颜色。例如，要将前三个外星人
修改为黄色、速度为中等且值 10 分，可这样做：

# 创建一个用于存储外星人的空列表。
aliens = []

# 创建30个绿色的外星人。
for alien_number in range (30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# 显示前5个外星人。
for alien in aliens[:5]:
     print(alien)
print("...")

鉴于要修改前三个外星人，这里遍历一个只包含这些外星人的切片。当前，所有外星人都是绿色的，但情况
并非总是如此，因此编写一条 if 语句来确保只修改绿色外星人。如果外星人是绿色的，就将其颜色改为
'yellow'，将其速度改为 'medium'，并将其分数改为 10，如下面的输出所示：

{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'yellow', 'points': 10, 'speed': 'medium'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
{'color': 'green', 'points': 5, 'speed': 'slow'}
...

可进一步扩展这个循环，在其中添加一个 elif 代码块，将黄色外星人改为移动速度快且值 15 分的红色
外星人，如下所示（这里只列出了循环，而没有列出整个程序）：

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

经常需要在列表中包含大量的字典，而其中每个字典都包含特定对象的众多信息。例如，你可能需要为网站
的每个用户创建一个字典，并将这些字典存储在一个名为 users 的列表中。在这个列表中，所有字典的
结构都相同，因此你可以遍历这个列表，并以相同的方式处理其中的每个字典。



2、在字典中存储列表

有时候，需要将列表存储在字典中，而不是将字典存储在列表中。例如，你如何描述顾客点的比萨呢？如果
使用列表，只能存储要添加的比萨配料；但如果使用字典，就不仅可在其中包含配料列表，还可包含其他有
关比萨的描述。

在下面的示例中，存储了比萨的两方面信息：外皮类型和配料列表。配料列表是一个与键 'toppings'
相关联的值。要访问该列表，我们使用字典名和键 'toppings'，就像访问字典中的其他值一样。这将
返回一个配料列表，而不是单个值：

# 存储所点比萨的信息。
❶ pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# 概述所点的比萨。
❷ print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

❸ for topping in pizza['toppings']:
    print("\t"+topping)

首先创建一个字典，其中存储了有关顾客所点比萨的信息（见❶）。在这个字典中，一个键是 'crust'，
与之相关联的值是字符串 'thick'；下一个键是 'toppings'，与之相关联的值是一个列表，其中存储
了顾客要求添加的所有配料。制作前，概述了顾客所点的比萨（见❷）。如果函数调用 print() 中的字
符串很长，可以在合适的位置分行。只需要在每行末尾都加上引号，同时对于除第一行外的其他各行，都在
行首加上引号并缩进。这样，Python 将自动合并圆括号内的所有字符串。为打印配料，编写一个 for
循环（见❸）。为访问配料列表，使用键 'toppings'，这样 Python 将从字典中提取配料列表。

下面的输出概述了要制作的比萨：

You ordered a thick-crust pizza with the following toppings:
	mushrooms
	extra cheese

每当需要在字典中将一个键关联到多个值时，都可以在字典中嵌套一个列表。在之前有关喜欢的编程语言的
示例中，如果将每个人的回答都存储在一个列表中，被调查者就可选择多种喜欢的语言。在这种情况下，当
遍历字典时，与每个被调查者相关联的都是一个语言列表，而不是一种语言；因此，在遍历该字典的 for
循环中，需要再使用一个 for 循环来遍历与被调查者相关联的语言列表：

❶ favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
    }

❷ for name, languages in favorite_languages.items():
     print(f"\n{name.title()}'s favorite languages are:")
❸    for language in languages:
        print(f"\t{language.title()}")

如你所见，现在与每个名字相关联的值都是一个列表（见❶）。请注意，有些人喜欢的语言只有一种，而有
些人有多种。遍历字典时（见❷），使用变量 languages 来依次存储对字典中每个值的引用，因为已经
知道这些值都是列表。在遍历字典的主循环中，使用了另一个 for 循环（见❸）来遍历每个人喜欢的语言
列表。现在，每个人想列出多少种喜欢的语言都可以：

Jen's favorite languages are:
	Python
	Ruby

Sarah's favorite languages are:
	C

Edward's favorite languages are:
	Ruby
	Go

Phil's favorite languages are:
	Python
	Haskell

为进一步改进这个程序，可在遍历字典的 for 循环开头添加一条 if 语句，通过查看 len(languages)
的值来确定当前的被调查者喜欢的语言是否有多种。如果他喜欢的语言有多种，就像以前一样显示输出；如果
只有一种，就相应修改输出的措辞，如显示 Sarah's favorite language is C。

注意：列表和字典的嵌套层级不应太多。如果嵌套层级比前面的示例多得多，很可能有更简单的解决方案。



3、在字典中存储字典

可在字典中嵌套字典，但这样做时，代码可能很快复杂起来。例如，如果有多个网站用户，每个都有独特的用
户名，可在字典中将用户名作为键，然后将每位用户的信息存储在一个字典中，并将该字典作为与用户名相关
联的值。在下面的程序中，存储了每位用户的三项信息：名、姓和居住地。为访问这些信息，遍历所有的用户
名，并访问与每个用户名相关联的信息字典：

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

❶ for username, user_info in users.items():
❷    print(f"\nUsername: {username}")
❸    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']

❹    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")

首先定义一个名为 users 的字典，其中包含两个键：用户名 'aeinstein' 和 'mcurie'。与每个键盘
相关联的值都是一个字典，其中包含用户的名、姓和居住地。在❶处，遍历字典 users，让 Python 依次将
每个键赋给变量 username，并依次将与当前键相关联的字典赋给变量 user_info。在循环内部的❷处，将
用户名打印出来。

在❸处，开始访问内部的字典。变量 user_info 包含用户信息字典，而该字典包含三个键：'first'、'last'
和 'location'。对于每位用户，都使用这些键来生成整洁的姓名和居住地，然后打印有关用户的简要信息（见❹）：

Username: aeinstein
	Full name: Albert Einstein
	Location: Princeton

Username: mcurie
	Full name: Marie Curie
	Location: Paris


请注意，表示每位用户的字典都具有相同的结构。虽然 Python 并没有这样的要求，但这使得嵌套的字典处理
起来更容易。倘若表示每位用户的字典都包含不同的键，for 循环内部的代码将更复杂。

"""