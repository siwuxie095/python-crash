"""

传递实参


函数定义中可能包含多个形参，因此函数调用中也可能包含多个实参。向函数传递实参的方式很多：可使用位置实参，这要求
实参的顺序与形参的顺序相同；也可使用关键字实参，其中每个实参都由变量名和值组成；还可使用列表和字典。下面依次介
绍这些方式。



1、位置实参

调用函数时，Python 必须将函数调用中的每个实参都关联到函数定义中的一个形参。为此，最简单的关联方式是基于实参
的顺序。这种关联方式称为位置实参。

为明白其中的工作原理，来看一个显示宠物信息的函数。这个函数指出一个宠物属于哪种动物以及它叫什么名字，如下所示：

❶ def describe_pet(animal_type, pet_name):
    \"""显示宠物的信息。\"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

❷ describe_pet('hamster', 'harry')

这个函数的定义表明，它需要一种动物类型和一个名字（见❶）。 调用 describe_pet() 时，需要按顺序提供一种动物
类型和一个名字。例如，在刚才的函数调用中，实参 'hamster' 被赋给形参 animal_type，而实参 'harry' 被赋
给形参 pet_name（见❷）。在函数体内，使用了这两个形参来显示宠物的信息。

输出描述了一只名为 Harry 的仓鼠：

I have a hamster.
My hamster's name is Harry.


a. 多次调用函数

可以根据需要调用函数任意次。要再描述一个宠物，只需再次调用 describe_pet() 即可：

def describe_pet(animal_type, pet_name):
    \"""显示宠物的信息。\"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')
describe_pet('dog', 'willie')

第二次调用 describe_pet() 函数时，向它传递了实参 'dog' 和 'willie'。与第一次调用时一样，Python 将
实参 'dog' 关联到形参 animal_type，并将实参 'willie' 关联到形参 pet_name。与前面一样，这个函数完成
了任务，但打印的是一条名为 Willie 的小狗的信息。至此，有一只名为 Harry 的仓鼠，还有一条名为 Willie 的
小狗：

I have a hamster.
My hamster's name is Harry.

I have a dog.
My dog's name is Willie.

多次调用函数是一种效率极高的工作方式。只需在函数中编写一次描述宠物的代码，然后每当需要描述新宠物时，都调用
该函数并向它提供新宠物的信息。即便描述宠物的代码增加到了 10 行，依然只需使用一行调用函数的代码，就可描述
一个新宠物。

在函数中，可根据需要使用任意数量的位置实参，Python 将按顺序将函数调用中的实参关联到函数定义中相应的形参。


b. 位置实参的顺序很重要

使用位置实参来调用函数时，如果实参的顺序不正确，结果可能出乎意料：

def describe_pet(animal_type, pet_name):
    \"""显示宠物的信息。\"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')

在这个函数调用中，先指定名字，再指定动物类型。由于实参 'harry' 在前，这个值将赋给形参 animal_type。
同理，'hamster' 将赋给形参 pet_name。结果是有一个名为 Hamster 的 harry：

I have a harry.
My harry's name is Hamster.

如果你得到的结果像上面一样可笑，请确认函数调用中实参的顺序与函数定义中形参的顺序一致。



2、关键字实参

关键字实参是传递给函数的名称值对。因为直接在实参中将名称和值关联起来，所以向函数传递实参时不会混淆（不会得到
名为 Hamster 的 harry 这样的结果）。关键字实参让你无须考虑函数调用中的实参顺序，还清楚地指出了函数调用中
各个值的用途。

下面来重新编写 pets.py，在其中使用关键字实参来调用 describe_pet()：

def describe_pet(animal_type, pet_name):
    \"""显示宠物的信息。\"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(animal_type='hamster', pet_name='harry')

函数 describe_pet() 还和之前一样，但调用这个函数时，向 Python 明确地指出了各个实参对应的形参。看到这个
函数调用时，Python 知道应该将实参 'hamster' 和 'harry' 分别赋给形参 animal_type 和 pet_name。输
出正确无误，指出有一只名为 Harry 的仓鼠。

关键字实参的顺序无关紧要，因为 Python 知道各个值该赋给哪个形参。下面两个函数调用是等效的：

describe_pet(animal_type='hamster', pet_name='harry')
describe_pet(pet_name='harry', animal_type='hamster')

注意：使用关键字实参时，务必准确指定函数定义中的形参名。



3、默认值

编写函数时，可给每个形参指定默认值。在调用函数中给形参提供了实参时，Python 将使用指定的实参值；否则，将使用
形参的默认值。因此，给形参指定默认值后，可在函数调用中省略相应的实参。使用默认值可简化函数调用，还可清楚地指
出函数的典型用法。

例如，如果你发现调用 describe_pet() 时，描述的大多是小狗，就可将形参 animal_type 的默认值设置为 'dog'。
这样，调用 describe_pet() 来描述小狗时，就可不提供这种信息：

def describe_pet(pet_name, animal_type='dog'):
    \"""显示宠物的信息。\"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')

这里修改了函数 describe_pet() 的定义，在其中给形参 animal_type 指定了默认值 'dog'。这样，调用这个函数
时，如果没有给 animal_type 指定值，Python 就将把这个形参设置为 'dog'：

I have a dog.
My dog's name is Willie.

请注意，在这个函数的定义中，修改了形参的排列顺序。因为给 animal_type 指定了默认值，无须通过实参来指定动物
类型，所以在函数调用中只包含一个实参 —— 宠物的名字。然而，Python 依然将这个实参视为位置实参，因此如果函数
调用中只包含宠物的名字，这个实参将关联到函数定义中的第一个形参。这就是需要将 pet_name 放在形参列表开头的
原因。

现在，使用这个函数的最简单方式是在函数调用中只提供小狗的名字：

describe_pet('willie')

这个函数调用的输出与前一个示例相同。只提供了一个实参 'willie'，这个实参将关联到函数定义中的第一个形参
pet_name。由于没有给 animal_type 提供实参，Python 将使用默认值 'dog'。

如果要描述的动物不是小狗，可使用类似于下面的函数调用：

describe_pet(pet_name='harry', animal_type='hamster')

由于显式地给 animal_type 提供了实参，Python 将忽略这个形参的默认值。

注意：使用默认值时，必须先在形参列表中列出没有默认值的形参，再列出有默认值的实参。这让 Python 依然能够正确
地解读位置实参。



4、等效的函数调用

鉴于可混合使用位置实参、关键字实参和默认值，通常有多种等效的函数调用方式。请看下面对函数 describe_pet()
的定义，其中给一个形参提供了默认值：

def describe_pet(pet_name, animal_type='dog'):

基于这种定义，在任何情况下都必须给 pet_name 提供实参。指定该实参时可采用位置方式，也可采用关键字方式。如果
要描述的动物不是小狗，还必须在函数调用中给 animal_type 提供实参。同样，指定该实参时可以采用位置方式，也可
采用关键字方式。

下面对这个函数的所有调用都可行：

# 一条名为Willie的小狗。
describe_pet('willie')
describe_pet(pet_name='willie')

# 一只名为Harry的仓鼠。
describe_pet('harry', 'hamster')
describe_pet(pet_name='harry', animal_type='hamster')
describe_pet(animal_type='hamster', pet_name='harry')

这些函数调用的输出与前面的示例相同。

注意：使用哪种调用方式无关紧要，只要函数调用能生成你期望的输出就行。使用对你来说最容易理解的调用方式即可。



5、避免实参错误

等你开始使用函数后，如果遇到实参不匹配错误，不要大惊小怪。你提供的实参多于或少于函数完成工作所需的信息时，将
出现实参不匹配错误。例如，如果调用函数 describe_pet() 时没有指定任何实参，结果将如何呢？

def describe_pet(animal_type, pet_name):
    \"""显示宠物的信息。\"""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet()

Python 发现该函数调用缺少必要的信息，traceback 指出了这一点：

 Traceback (most recent call last):
❶  File "pets.py", line 6, in <module>
❷    describe_pet()
❸ TypeError: describe_pet() missing 2 required positional arguments: 'animal_type' and 'pet_name'

在❶处，traceback 指出了问题出在什么地方，使得能够回过头去找出函数调用中的错误。在❷处，指出了导致问题的函数
调用。在❸处，traceback 指出该函数调用少了两个实参，并指出了相应形参的名称。如果这个函数存储在一个独立的文件
中，也许无须打开这个文件并查看函数的代码，就能重新正确地编写函数调用。

Python 读取函数的代码并指出需要为哪些形参提供实参，这提供了极大的帮助。这也是应该给变量和函数指定描述性名称
的另一个原因：如果这样做了，那么无论对于你，还是可能使用你编写的代码的其他任何人来说，Python 提供的错误消息
都将更帮助。

如果提供的实参太多，将出现类似的 traceback，帮助你确保函数调用和函数定义匹配。

"""