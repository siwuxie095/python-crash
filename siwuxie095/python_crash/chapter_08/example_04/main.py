"""

返回值


函数并非总是直接显示输出，它还可以处理一些数据，并返回一个或一组值。函数返回的值称为返回值。在函数中，可使用
return 语句将值返回到调用函数的代码行。返回值让你能够将程序的大部分繁重工作移到函数中去完成，从而简化主程序。



1、返回简单值

下面来看一个函数，它接受名和姓并返回整洁的姓名：

❶ def get_formatted_name(first_name, last_name):
    \"""返回整洁的姓名。\"""
❷    full_name = f"{first_name} {last_name}"
❸    return full_name.title()

❹ musician = get_formatted_name('jimi', 'hendrix')
print(musician)

函数 get_formatted_name() 的定义通过形参接受名和姓（见❶）。它将姓和名合而为一，在中间加上一个空格，并
将结果赋给变量 full_name（见❷）。然后，将 full_name 的值转换为首字母大写格式，并将结果返回到函数调用行
（见❸）。

调用返回值的函数时，需要提供一个变量，以便将返回的值赋给它。在这里，将返回值赋给了变量 musician（见❹）。
输出为整洁的姓名：

Jimi Hendrix

原本只需编写下面的代码就可输出整洁的姓名，相比于此，前面做的工作好像太多了：

print("Jimi Hendrix")

但在需要分别存储大量名和姓的大型程序中，像 get_formatted_name() 这样的函数非常有用。可以分别存储名和姓，
每当需要显示姓名时都调用这个函数。



2、让实参变成可选的

有时候，需要让实参变成可选的，这样使用函数的人就能只在必要时提供额外的信息。可使用默认值来让实参变成可选的。

例如，假设要扩展函数 get_formatted_name()，使其同时处理中间名。为此，可将其修改成类似于下面这样：

def get_formatted_name(first_name, middle_name, last_name):
    \"""返回整洁的姓名。\"""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

只要同时提供名、中间名和姓，这个函数就能正确运行。它根据这三部分创建一个字符串，在适当的地方加上空格，并将
结果转换为首字母大写格式：

John Lee Hooker

并非所有的人都有中间名，但如果调用这个函数时只提供了名和姓，它将不能正确运行。为了让中间名变成可选的，可给
形参 middle_name 指定一个空的默认值，并在用户没有提供中间名时不使用这个形参。为让 get_formatted_name()
在没有提供中间名时依然可行，可将形参 middle_name 的默认值设置为空字符串，并将其移到形参列表的末尾：

❶ def get_formatted_name(first_name, last_name, middle_name=''):
    \"""返回整洁的姓名。\"""
❷    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
❸    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

musician = get_formatted_name('jimi', 'hendrix')
print(musician)

❹ musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)

在本例中，姓名是根据三个可能提供的部分创建的。由于人都有名和姓，因此在函数定义中首先列出了这两个形参。中间
名是可选的，因此在函数定义中最后列出该形参，并将其默认值设置为空字符串（见❶）。

在函数体中，检查是否提供了中间名。Python 将非空字符串解读为 True，因此如果函数调用中提供了中间名，if
middle_name 将为 True（见❷）。如果提供了中间名，就将名、中间名和姓合并为姓名，再将其修改为首字母大写
格式，并返回到函数调用行。在函数调用行，将返回的值赋给变量 musician，然后这个变量的值被打印出来。如果没
有提供中间名，middle_name 将为空字符串，导致 if 测试未通过，进而执行 else 代码块（见❸）：只使用名和
姓来生成姓名，并将格式设置好的姓名返回给函数调用行。在函数调用行，将返回的值赋给变量 musician，然后这个
变量的值被打印出来。

调用这个函数时，如果只想指定名和姓，调用起来将非常简单。如果还要指定中间名，就必须确保它是最后一个实参，
这样 Python 才能正确地将位置实参关联到形参（见❹）。

这个修改后的版本不仅适用于只有名和姓的人，而且适用于还有中间名的人：

Jimi Hendrix
John Lee Hooker

可选值让函数能够处理各种不同的情形，同时确保函数调用尽可能简单。



3、返回字典

函数可返回任何类型的值，包括列表和字典等较复杂的数据结构。例如，下面的函数接受姓名的组成部分，并返回一个
表示人的字典：

def build_person(first_name, last_name):
    \"""返回一个字典，其中包含有关一个人的信息。\"""
❶    person = {'first': first_name, 'last': last_name}
❷    return person

musician = build_person('jimi', 'hendrix')
❸ print(musician)

函数 build_person() 接受名和姓，并将这些值放到字典中（见❶）。存储 first_name 的值时，使用的键为
'first'，而存储 last_name 的值时，使用的键为 'last'。最后，返回表示人的整个字典（见❷）。在❸处，
打印这个返回的值，此时原来的两项文本信息存储在一个字典中：

{'first': 'jimi', 'last': 'hendrix'}

这个函数接受简单的文本信息，并将其放在一个更合适的数据结构中，让你不仅能打印这些信息，还能以其他方式处
理它们。当前，字符串 'jimi' 和 'hendrix' 被标记为名和姓。你可以轻松地扩展这个函数，使其接受可选值，
如中间名、年龄、职业或其他任何要存储的信息。例如，下面的修改让你能存储年龄：

def build_person(first_name, last_name, age=None):
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

在函数定义中，新增了一个可选形参 age，并将其默认值设置为特殊值 None（表示变量没有值）。可将 None
视为占位值。在条件测试中，None 相当于 False。如果函数调用中包含形参 age 的值，这个值将被存储到字典
中。在任何情况下，这个函数都会存储人的姓名，但可进行修改，使其同时存储有关人的其他信息。



4、结合使用函数和 while 循环

可将函数同之前介绍的任何 Python 结构结合起来使用。例如，下面将结合使用函数 get_formatted_name()
和 while 循环，以更正式的方式问候用户。下面尝试使用名和姓跟用户打招呼：

def get_formatted_name(first_name, last_name):
    \"""返回整洁的姓名。\"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 这是一个无限循环！
while True:
❶    print("\nPlease tell me your name:")
    f_name = input("First name: ")
    l_name = input("Last name: ")

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

在本例中，使用的是 get_formatted_name() 的简单版本，不涉及中间名。while 循环让用户输入姓名：依次
提示用户输入名和姓（见❶）。

但这个 while 循环存在一个问题：没有定义退出条件。请用户提供一系列输入时，该在什么地方提供退出途径呢？
要让用户能够尽可能容易地退出，因此每次提示用户输入时，都应提供退出途径。每次提示用户输入时，都使用
break 语句提供退出循环的简单途径：

def get_formatted_name(first_name, last_name):
    \"""返回整洁的姓名。\"""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# 这是一个无限循环！
while True:
    print("\nPlease tell me your name:")
    print("(enter 'q' at any time to quit)")

    f_name = input("First name: ")
    if f_name == 'q':
        break

    l_name = input("Last name: ")
    if l_name == 'q':
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"\nHello, {formatted_name}!")

这里添加了一条消息来告诉用户如何退出，然后在每次提示用户输入时，都检查他输入的是否是退出值。如果是，就
退出循环。现在，这个程序将不断地问候，直到用户输入的姓或名为 'q'：

Please tell me your name:
(enter 'q' at any time to quit)
First name: eric
Last name: matthes

Hello, Eric Matthes!

Please tell me your name:
(enter 'q' at any time to quit) First name: q

"""