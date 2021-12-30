"""

遍历字典


一个 Python 字典可能只包含几个键值对，也可能包含数百万个键值对。鉴于字典可能包含大量数据，Python
支持对字典进行遍历。字典可用于以各种方式存储信息，因此有多种遍历方式：可遍历字典的所有键值对，也可仅
遍历键或值。



1、遍历所有键值对

探索各种遍历方法前，先来看一个新字典，它用于存储有关网站用户的信息。下面的字典存储一名用户的用户名、
名和姓：

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

利用之前介绍过的知识，可访问 user_0 的任何一项信息，但如果要获悉该用户字典中的所有信息，该如何办呢？
可使用 for 循环来遍历这个字典：

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

❶ for key, value in user_0.items():
❷    print(f"\nKey: {key}")
❸    print(f"Value: {value}")

如❶所示，要编写遍历字典的 for 循环，可声明两个变量，用于存储键值对中的键和值。这两个变量可以使用任意
名称。下面的代码使用了简单的变量名，这完全可行：

for k, v in user_0.items()

for 语句的第二部分包含字典名和方法 items()（见❶），它返回一个键值对列表。接下来，for 循环依次将
每个键值对赋给指定的两个变量。在本例中，使用这两个变量来打印每个键（见❷）及其相关联的值（见❸）。第
一个函数调用 print() 中的 "\n" 确保在输出每个键值对前都插入一个空行：

Key: username
Value: efermi

Key: first
Value: enrico

Key: last
Value: fermi

在之前的示例 favorite_languages.py 中，字典存储的是不同人的同一种信息。对于类似这样的字典，遍历
所有的键值对很合适。如果遍历字典 favorite_languages，将得到其中每个人的姓名和喜欢的编程语言。由于
该字典中的键都是人名，值都是语言，因此在循环中使用变量 name 和 language，而不是 key 和 value。
这让人更容易明白循环的作用：

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

❶ for name, language in favorite_languages.items():
❷     print(f"{name.title()}'s favorite language is {language.title()}.")

❶处的代码让 Python 遍历字典中的每个键值对，并将键赋给变量 name，将值赋给变量 language。这些描述
性名称能够让人非常轻松地明白函数调用 print()（见❷）是做什么的。

仅使用几行代码，就将全部调查结果显示出来了：

Jen's favorite language is Python.
Sarah's favorite language is C.
Edward's favorite language is Ruby.
Phil's favorite language is Python.

即便字典存储的是上千乃至上百万人的调查结果，这种循环也管用。



2、遍历字典中的所有键

在不需要使用字典中的值时，方法 keys() 很有用。下面来遍历字典 favorite_languages，并将每个被调查
者的名字都打印出来：

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

❶ for name in favorite_languages.keys():
    print(name.title())

❶处的代码行让 Python 提取字典 favorite_languages 中的所有键，并依次将它们赋给变量 name。输出
列出了每个被调查者的名字：

Jen
Sarah
Edward
Phil

遍历字典时，会默认遍历所有的键。因此，如果将上述代码中的：

for name in favorite_languages.keys():

替换为：

for name in favorite_languages:

输出将不变。

显式地使用方法 keys() 可让代码更容易理解，你可以选择这样做，但是也可以省略它。

在这种循环中，可使用当前键来访问与之相关联的值。下面来打印两条消息，指出两位朋友喜欢的语言。像前面一样
遍历字典中的名字，但在名字为指定朋友的名字时，打印一条消息，指出其喜欢的语言：

favorite_languages = {
    --snip--
    }

❶ friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

❷    if name in friends:
❸        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

PS：这里的 --snip-- 表示省略的意思。

❶处创建了一个列表，其中包含要收到打印消息的朋友。在循环中，打印每个人的名字，并检查当前的名字是否在列表
friends 中（见❷）。如果在，就打印一句特殊的问候语，其中包含这位朋友喜欢的语言。为获悉朋友喜欢的语言，
这里使用了字典名，并将变量 name 的当前值作为键（见❸）。

每个人的名字都会被打印，但只对朋友打特殊消息：

Hi Jen.
Hi Sarah.
	Sarah, I see you love C!
Hi Edward.
Hi Phil.
	Phil, I see you love Python!

还可使用方法 keys() 确定某个人是否接受了调查。下面的代码确定 Erin 是否接受了调查：

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

❶ if 'erin' not in favorite_languages.keys():
      print("Erin, please take our poll!")

方法 keys() 并非只能用于遍历：实际上，它返回一个列表，其中包含字典中的所有键。因此❶处的代码行只核实
'erin' 是否包含在这个列表中。因为她并不包含在这个列表中，所以打印一条消息，邀请她参加调查：

Erin, please take our poll!



3、按特定顺序遍历字典中的所有键

从 Python 3.7 起，遍历字典时将按插入的顺序返回其中的元素。不过在有些情况下，你可能要按与此不同的顺序
遍历字典。

要以特定顺序返回元素，一种办法是在 for 循环中对返回的键进行排序。为此，可使用函数 sorted() 来获得按
特定顺序排列的键列表的副本：

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

这条 for 语句类似于其他 for 语句，不同之处是对方法 dictionary.keys() 的结果调用了函数 sorted()。
这让 Python 列出字典中的所有键，并在遍历前对这个列表进行排序。输出表明，按顺序显示了所有被调查者的名字：

Edward, thank you for taking the poll.
Jen, thank you for taking the poll.
Phil, thank you for taking the poll.
Sarah, thank you for taking the poll.



4、遍历字典中的所有值

如果主要对字典包含的值感兴趣，可使用方法 values() 来返回一个值列表，不包含任何键。例如，假设想获得一个
列表，其中只包含被调查者选择的各种语言，而不包含被调查者的名字，可以这样做：

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

这条 for 语句提取字典中的每个值，并将其依次赋给变量 language。通过打印这些值，就获得了一个包含被调查
者所选择语言的列表：

The following languages have been mentioned:
Python
C
Ruby
Python

这种做法提取字典中所有的值，而没有考虑是否重复。涉及的值很少时，这也许不是问题，但如果被调查者很多，最终
的列表可能包含大量重复项。为剔除重复项，可使用集合（set）。集合中的每个元素都必须是独一无二的：

favorite_languages = {
    --snip--
    }

print("The following languages have been mentioned:")
 ❶ for language in set(favorite_languages.values()):
        print(language.title())

通过对包含重复元素的列表调用 set()，可让 Python 找出列表中独一无二的元素，并使用这些元素来创建一个集合。
❶处使用 set() 来提取 favorite_languages.values() 中不同的语言。

结果是一个不重复的列表，其中列出了被调查者提及的所有语言：

The following languages have been mentioned:
C
Python
Ruby

随着你更深入地学习 Python，经常会发现它内置的功能可帮助你以希望的方式处理数据。

注意可使：用一对花括号直接创建集合，并在其中用逗号分隔元素：

>>> languages = {'python', 'ruby', 'python', 'c'}
>>> languages
{'ruby', 'python', 'c'}

集合和字典很容易混淆，因为它们都是用一对花括号定义的。当花括号内没有键值对时，定义的很可能是集合。不同于
列表和字典，集合不会以特定的顺序存储元素。

"""