"""

将函数存储在模块中


使用函数的优点之一是可将代码块与主程序分离。通过给函数指定描述性名称，可让主程序容易理解得多。你还可以
更进一步，将函数存储在称为模块的独立文件中，再将模块导入到主程序中。import 语句允许在当前运行的程序文
件中使用模块中的代码。

通过将函数存储在独立的文件中，可隐藏程序代码的细节，将重点放在程序的高层逻辑上。这还能让你在众多不同的
程序中重用函数。将函数存储在独立文件中后，可与其他程序员共享这些文件而不是整个程序。知道如何导入函数还
能让你使用其他程序员编写的函数库。

导入模块的方法有多种，下面对每种进行简要的介绍。



1、导入整个模块

要让函数是可导入的，得先创建模块。模块是扩展名为 .py 的文件，包含要导入到程序中的代码。下面来创建一个
包含函数 make_pizza() 的模块。为此，将文件 pizza.py 中除函数 make_pizza() 之外的其他代码删除：

def make_pizza(size, *toppings):
    \"""概述要制作的比萨。\"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

接下来，在 pizza.py 所在的目录中创建一个名为 making_pizzas.py 的文件。这个文件导入刚创建的模块，
再调用 make_pizza() 两次：

import pizza

❶ pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

Python 读取这个文件时，代码行 import pizza 让 Python 打开文件 pizza.py，并将其中的所有函数都
复制到这个程序中。你看不到复制的代码，因为在这个程序即将运行时，Python 在幕后复制了这些代码。你只需
知道，在 making_pizzas.py 中，可使用 pizza.py 中定义的所有函数。

要调用被导入模块中的函数，可指定被导入模块的名称 pizza 和函数名 make_pizza()，并用句点分隔（见❶）。
这些代码的输出与没有导入模块的原始程序相同：

Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese

这就是一种导入方法：只需编写一条 import 语句并在其中指定模块名，就可在程序中使用该模块中的所有函数。
如果使用这种 import 语句导入了名为 module_name.py 的整个模块，就可使用下面的语法来使用其中任何
一个函数：

module_name.function_name()



2、导入特定的函数

还可以导入模块中的特定函数，这种导入方法的语法如下：

from module_name import function_name

通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数：

from module_name import function_0, function_1, function_2

对于前面的 making_pizzas.py 示例，如果只想导入要使用的函数，代码将类似于下面这样：

from pizza import make_pizza

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

使用这种语法时，调用函数时无须使用句点。由于在 import 语句中显式地导入了函数 make_pizza()，调用
时只需指定其名称即可。



3、使用 as 给函数指定别名

如果要导入函数的名称可能与程序中现有的名称冲突，或者函数的名称太长，可指定简短而独一无二的别名：函数
的另一个名称，类似于外号。要给函数取这种特殊外号，需要在导入它时指定。

下面给函数 make_pizza() 指定了别名 mp()。这是在 import 语句中使用 make_pizza as mp 实现的，
关键字 as 将函数重命名为指定的别名：

from pizza import make_pizza as mp

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')

上面的 import 语句将函数 make_pizza() 重命名为 mp()。在这个程序中，每当需要调用 make_pizza()
时，都可简写成 mp()。

Python 将运行 make_pizza() 中的代码，避免与这个程序可能包含的函数 make_pizza() 混淆。

指定别名的通用语法如下：

from module_name import function_name as fn



4、使用 as 给模块指定别名

还可以给模块指定别名。通过给模块指定简短的别名（如给模块 pizza 指定别名 p），让你能够更轻松地调用
模块中的函数。相比于 pizza.make_pizza()，p.make_pizza() 更为简洁：

import pizza as p

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

上述 import 语句给模块 pizza 指定了别名 p，但该模块中所有函数的名称都没变。要调用函数 make_pizza()，
可编写代码 p.make_pizza() 而非 pizza.make_pizza()。这样不仅代码更简洁，还让你不用再关注模块名，
只专注于描述性的函数名。这些函数名明确指出了函数的功能，对于理解代码而言，比模块名更重要。

给模块指定别名的通用语法如下：

import module_name as mn



5、导入模块中的所有函数

使用星号（*）运算符可让 Python 导入模块中的所有函数：

from pizza import *

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

import 语句中的星号让 Python 将模块 pizza 中的每个函数都复制到这个程序文件中。由于导入了每个函数，
可通过名称来调用每个函数，而无须使用句点表示法。然而，使用并非自己编写的大型模块时，最好不要采用这种导
入方法。这是因为如果模块中有函数的名称与当前项目中使用的名称相同，可能导致意想不到的结果：Python 可能
遇到多个名称相同的函数或变量，进而覆盖函数，而不是分别导入所有的函数。

最佳的做法是，要么只导入需要使用的函数，要么导入整个模块并使用句点表示法。这让代码更清晰，更容易阅读和
理解。这里之所以介绍这种导入方法，只是想让你在阅读别人编写的代码时，能够理解类似于下面的 import 语句：

from module_name import *

"""