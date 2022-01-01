"""

传递任意数量的实参


有时候，预先不知道函数需要接受多少个实参，好在 Python 允许函数从调用语句中收集任意数量的实参。

例如，来看一个制作比萨的函数，它需要接受很多配料，但无法预先确定顾客要多少种配料。下面的函数只有一个形参
*toppings，但不管调用语句提供了多少实参，这个形参会将它们统统收入囊中：

def make_pizza(*toppings):
    \"""打印顾客点的所有配料。\"""
    print(toppings)

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

形参名 *toppings 中的星号让 Python 创建一个名为 toppings 的空元组，并将收到的所有值都封装到这个
元组中。函数体内的函数调用 print() 通过生成输出，证明 Python 能够处理使用一个值来调用函数的情形，
也能处理使用三个值来调用函数的情形。它以类似的方式处理不同的调用。注意，Python 将实参封装到一个元组中，
即便函数只收到一个值：

('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')

现在，可以将函数调用 print() 替换为一个循环，遍历配料列表并对顾客点的比萨进行描述：

不管收到一个值还是三个值，这个函数都能妥善处理：

def make_pizza(*toppings):
    \"""概述要制作的比萨。\"""
    print("\nMaking a pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

不管收到一个值还是三个值，这个函数都能妥善处理：

Making a pizza with the following toppings:
- pepperoni

Making a pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese

不管函数收到的实参是多少个，这种语法都管用。



1、结合使用位置实参和任意数量实参

如果要让函数接受不同类型的实参，必须在函数定义中将接纳任意数量实参的形参放在最后。Python 先匹配位置
实参和关键字实参，再将余下的实参都收集到最后一个形参中。

例如，如果前面的函数还需要一个表示比萨尺寸的形参，必须将其放在形参 *toppings 的前面：

def make_pizza(size, *toppings):
    \"""概述要制作的比萨。\"""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

基于上述函数定义，Python 将收到的第一个值赋给形参 size，并将其他所有值都存储在元组 toppings 中。
在函数调用中，首先指定表示比萨尺寸的实参，再根据需要指定任意数量的配料。

现在，每个比萨都有了尺寸和一系列配料，而且这些信息按正确的顺序打印出来了——首先是尺寸，然后是配料：

Making a 16-inch pizza with the following toppings:
- pepperoni

Making a 12-inch pizza with the following toppings:
- mushrooms
- green peppers
- extra cheese

注意：你经常会看到通用形参名 *args，它也收集任意数量的位置实参。



2、使用任意数量的关键字实参

有时候，需要接受任意数量的实参，但预先不知道传递给函数的会是什么样的信息。在这种情况下，可将函数编写成
能够接受任意数量的键值对 —— 调用语句提供了多少就接受多少。一个这样的示例是创建用户简介：你知道将收到
有关用户的信息，但不确定会是什么样的信息。在下面的示例中，函数 build_profile() 接受名和姓，还接受
任意数量的关键字实参：

def build_profile(first, last, **user_info):
    \"""创建一个字典，其中包含已经知道的有关用户的一切。\"""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')

print(user_profile)

函数 build_profile() 的定义要求提供名和姓，同时允许根据需要提供任意数量的名称值对。其中，形参
**user_info 中的两个星号让 Python 创建一个名为 user_info 的空字典，并将收到的所有名称值对
都放到这个字典中。在这个函数中，可以像访问其他字典那样访问 user_info 中的名称值对。

在 build_profile() 的函数体内，将名和姓加入了字典 user_info 中（见❶），因为总是会从用户那里
收到这两项信息，而这两项信息没有放到这个字典中。接下来，将字典 user_info 返回到函数调用行。

这里调用 build_profile()，向它传递名（'albert'）、姓（'einstein'）和两个键值对（location
='princeton' 和 field='physics'），并将返回的 user_info 赋给变量 user_profile，再打印
该变量：

{'location': 'princeton', 'field': 'physics',
'first_name': 'albert', 'last_name': 'einstein'}

在这里，返回的字典包含用户的名和姓，还有求学的地方和所学专业。调用这个函数时，不管额外提供多少个
键值对，它都能正确地处理。

编写函数时，能以各种方式混合使用位置实参、关键字实参和任意数量的实参。知道这些实参类型大有裨益，
因为阅读别人编写的代码时经常会见到它们。要正确地使用这些类型的实参并知道其使用时机，需要经过一
定的练习。就目前而言，牢记使用最简单的方法来完成任务就好了。继续往下阅读，你就会知道在各种情况
下哪种方法的效率最高。

注意：你经常会看到形参名 **kwargs，它用于收集任意数量的关键字实参。

PS：
（1）*args 称之为 Non-keyword Variable Arguments，无关键字参数。
（2）**kwargs 称之为 keyword Variable Arguments，有关键字参数。

"""