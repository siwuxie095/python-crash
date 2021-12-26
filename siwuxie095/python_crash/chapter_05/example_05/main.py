"""

使用 if 语句处理列表


通过结合使用 if 语句和列表，可完成一些有趣的任务：对列表中特定的值做特殊处理；高效地管理不断
变化的情形，如餐馆是否还有特定的食材；证明代码在各种情形下都将按预期那样运行。



1、检查特殊元素

之前开头通过一个简单示例演示了如何处理特殊值 'bmw' —— 它需要采用不同的格式进行打印。现在你
对条件测试和 if 语句有了大致的认识，下面就来进一步研究如何检查列表中的特殊值，并对其做合适的
处理。

继续使用前面的比萨店示例。这家比萨店在制作比萨时，每添加一种配料都打印一条消息。通过创建一个
列表，在其中包含顾客点的配料，并使用一个循环来指出添加到比萨中的配料，能以极高的效率编写这样
的代码：

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

输出很简单，因为上述代码不过是一个简单的 for 循环：

Adding mushrooms.
Adding green peppers.
Adding extra cheese.

Finished making your pizza!

然而，如果比萨店的青椒用完了，该如何处理呢？为妥善地处理这种情况，可在 for 循环中包含一条
if 语句：

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
❶    if requested_topping == 'green peppers':
        print("Sorry, we are out of green peppers right now.")
❷    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")

这里在比萨中添加每种配料前都进行检查。❶处的代码检查顾客是否点了青椒。如果是，就显示一条消息，
指出不能点青椒的原因。 ❷处的 else 代码块确保其他配料都将添加到比萨中。

输出表明，已经妥善地处理了顾客点的每种配料：

Adding mushrooms.
Sorry, we are out of green peppers right now.
Adding extra cheese.

Finished making your pizza!



2、确定列表不是空的

到目前为止，对于处理的每个列表都做了一个简单的假设 —— 假设它们都至少包含一个元素。因为马上
就要让用户来提供存储在列表中的信息，所以不能再假设循环运行时列表不是空的。有鉴于此，在运行
for 循环前确定列表是否为空很重要。

下面在制作比萨前检查顾客点的配料列表是否为空。如果列表为空，就向顾客确认是否要点原味比萨；
如果列表不为空，就像前面的示例那样制作比萨：

❶ requested_toppings = []
❷ if requested_toppings:
      for requested_topping in requested_toppings:
            print(f"Adding {requested_topping}.")
      print("\nFinished making your pizza!")
❸ else:
      print("Are you sure you want a plain pizza?")

首先创建一个空列表，其中不包含任何配料（见❶）。❷处进行简单的检查，而不是直接执行 for 循环。
在 if 语句中将列表名用作条件表达式时，Python 将在列表至少包含一个元素时返回 True，并在列表
为空时返回 False。如果 requested_toppings 不为空，就运行与前一个示例相同的 for 循环；
否则，就打印一条消息，询问顾客是否确实要点不加任何配料的原味比萨（见❸）。

在这里，这个列表为空，因此输出如下——询问顾客是否确实要点原味比萨：

Are you sure you want a plain pizza?

如果这个列表不为空，输出将显示在比萨中添加的各种配料。



3、使用多个列表

顾客的要求往往五花八门，在比萨配料方面尤其如此。如果顾客要在比萨中添加炸薯条，该怎么办呢？可
使用列表和 if 语句来确定能否满足顾客的要求。

来看看在制作比萨前如何拒绝怪异的配料要求。下面的示例定义了两个列表，其中第一个列表包含比萨店
供应的配料，而第二个列表包含顾客点的配料。这次对于 requested_toppings 中的每个元素，都
检查它是否是比萨店供应的配料，再决定是否在比萨中添加它：

❶ available_toppings = ['mushrooms', 'olives', 'green peppers',
 'pepperoni', 'pineapple', 'extra cheese']

❷ requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

❸ for requested_topping in requested_toppings:
❹       if requested_topping in available_toppings:
            print(f"Adding {requested_topping}.")
        ❺ else:
            print(f"Sorry, we don't have {requested_topping}.")

print("\nFinished making your pizza!")

❶处定义了一个列表，其中包含比萨店供应的配料。请注意，如果比萨店供应的配料是固定的，也可使用
一个元组来存储它们。❷处又创建了一个列表，其中包含顾客点的配料。请注意那个不同寻常的配料 ——
'french fries'。在❸处遍历顾客点的配料列表。在这个循环中，对于顾客点的每种配料，都检查它
是否包含在供应的配料列表中（见❹）。如果答案是肯定的，就将其加入比萨中，否则将运行 else 代
码块（见❺）：打印一条消息，告诉顾客不供应这种配料。

这些代码的输出整洁而翔实：

Adding mushrooms.
Sorry, we don't have french fries.
Adding extra cheese.

Finished making your pizza!

这里通过为数不多的几行代码，高效地处理了一种真实的情形！

"""