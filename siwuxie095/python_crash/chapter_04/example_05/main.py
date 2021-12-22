"""

元组


列表非常适合用于存储在程序运行期间可能变化的数据集。列表是可以修改的，这对处理网站的用户列表或游戏中的角色
列表至关重要。然而，有时候你需要创建一系列不可修改的元素，元组可以满足这种需求。Python 将不能修改的值称为
不可变的，而不可变的列表被称为元组。



1、定义元组

元组看起来很像列表，但使用圆括号而非中括号来标识。定义元组后，就可使用索引来访问其元素，就像访问列表元素
一样。

例如，如果有一个大小不应改变的矩形，可将其长度和宽度存储在一个元组中，从而确保它们是不能修改的：

❶ dimensions = (200, 50)
❷ print(dimensions[0])
 print(dimensions[1])

首先定义元组 dimensions（见❶），为此使用了圆括号而不是方括号。接下来，分别打印该元组的各个元素，使用的
语法与访问列表元素时使用的语法相同（见❷）：

200
50

下面来尝试修改元组 dimensions 的一个元素，看看结果如何：

dimensions = (200, 50)
❶ dimensions[0] = 250

❶处的代码试图修改第一个元素的值，导致 Python 返回类型错误消息。由于试图修改元组的操作是被禁止的，因此
Python 指出不能给元组的元素赋值：

Traceback (most recent call last):
  File "dimensions.py", line 2, in <module>
    dimensions[0] = 250
TypeError: 'tuple' object does not support item assignment

这很好，因为这里希望 Python 在代码试图修改矩形的尺寸时引发错误。

注意：严格地说，元组是由逗号标识的，圆括号只是让元组看起来更整洁、更清晰。如果你要定义只包含一个元素的
元组，必须在这个元素后面加上逗号：

my_t = (3,)

创建只包含一个元素的元组通常没有意义，但自动生成的元组有可能只有一个元素。



2、遍历元组中的所有值

像列表一样，也可以使用 for 循环来遍历元组中的所有值：

dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

就像遍历列表时一样，Python 返回元组中所有的元素：

200
50



3、修改元组变量

虽然不能修改元组的元素，但可以给存储元组的变量赋值。因此，如果要修改前述矩形的尺寸，可重新定义整个元组：

❶ dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

❷ dimensions = (400, 100)
❸ print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

首先定义一个元组，并将其存储的尺寸打印出来（见❶）。接下来，将一个新元组关联到变量 dimensions（见❷）。
然后，打印新的尺寸（见❸）。这次，Python 不会引发任何错误，因为给元组变量重新赋值是合法的：

Original dimensions:
200
50

Modified dimensions:
400
100

相比于列表，元组是更简单的数据结构。如果需要存储的一组值在程序的整个生命周期内都不变，就可以使用元组。

"""