"""

一个简单示例


下面是一个简短的示例，演示了如何使用if 语句来正确地处理特殊情形。假设你有一个汽车列表，并想将其中
每辆汽车的名称打印出来。对于大多数汽车，应以首字母大写的方式打印其名称，但对于汽车名 'bmw'，应以
全大写的方式打印。下面的代码遍历这个列表，并以首字母大写的方式打印其中的汽车名，不过对于 'bmw'，
则以全大写的方式打印：

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
❶    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

这个示例中的循环首先检查当前的汽车名是否是'bmw'（见❶）。 如果是，就以全大写方式打印，否则以首字母
大写的方式打印：

Audi
BMW
Subaru
Toyota

这个示例涵盖了将要介绍的很多概念。后续会先介绍可用来在程序中检查条件的测试。

"""