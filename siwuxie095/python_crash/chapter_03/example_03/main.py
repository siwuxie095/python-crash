"""

组织列表


在你创建的列表中，元素的排列顺序常常是无法预测的，因为你并非总能控制用户提供数据的顺序。这虽然在大多数情况下
是不可避免的，但你经常需要以特定的顺序呈现信息。有时候，你希望保留列表元素最初的排列顺序，而有时候又需要调整
排列顺序。Python 提供了很多组织列表的方式，可根据具体情况选用。



1、使用方法 sort() 对列表永久排序

Python 方法 sort() 让你能够较为轻松地对列表进行排序。假设你有一个汽车列表，并要让其中的汽车按字母顺序排列。
为简化这项任务，假设该列表中的所有值都是小写的。

cars = ['bmw', 'audi', 'toyota', 'subaru']
❶ cars.sort()
print(cars)

方法sort()（见❶）永久性地修改列表元素的排列顺序。现在，汽车是按字母顺序排列的，再也无法恢复到原来的排列顺序：

['audi', 'bmw', 'subaru', 'toyota']

还可以按与字母顺序相反的顺序排列列表元素，只需向 sort() 方法传递参数 reverse=True 即可。下面的示例将汽车
列表按与字母顺序相反的顺序排列：

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)

同样，对列表元素排列顺序的修改是永久性的：

['toyota', 'subaru', 'bmw', 'audi']



2、使用函数 sorted() 对列表临时排序

要保留列表元素原来的排列顺序，同时以特定的顺序呈现它们，可使用函数 sorted()。函数 sorted() 让你能够按特定
顺序显示列表元素，同时不影响它们在列表中的原始排列顺序。

下面尝试来对汽车列表调用这个函数。

cars = ['bmw', 'audi', 'toyota', 'subaru']

❶ print("Here is the original list:")
 print(cars)

❷ print("\nHere is the sorted list:")
 print(sorted(cars))

❸ print("\nHere is the original list again:")
 print(cars)

首先按原始顺序打印列表（见❶），再按字母顺序显示该列表（见❷）。以特定顺序显示列表后，进行核实，确认列表元素
的排列顺序与以前相同（见❸）。

Here is the original list:
['bmw', 'audi', 'toyota', 'subaru']

Here is the sorted list:
['audi', 'bmw', 'subaru', 'toyota']

❹ Here is the original list again:
['bmw', 'audi', 'toyota', 'subaru']

注意，调用函数 sorted() 后，列表元素的排列顺序并没有变（见❹）。如果要按与字母顺序相反的顺序显示列表，也可
向函数 sorted() 传递参数 reverse=True。

注意：在并非所有的值都是小写时，按字母顺序排列列表要复杂些。决定排列顺序时，有多种解读大写字母的方式，要指定
准确的排列顺序，可能比这里所做的要复杂。然而，大多数排序方式是以这里介绍的知识为基础的。



3、倒着打印列表

要反转列表元素的排列顺序，可使用方法 reverse()。假设汽车列表是按购买时间排列的，可轻松地按相反的顺序排列
其中的汽车：

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

注意，reverse() 不是按与字母顺序相反的顺序排列列表元素，而只是反转列表元素的排列顺序：

['bmw', 'audi', 'toyota', 'subaru']
['subaru', 'toyota', 'audi', 'bmw']

方法reverse() 永久性地修改列表元素的排列顺序，但可随时恢复到原来的排列顺序，只需对列表再次调用 reverse()
即可。



4、确定列表的长度

使用函数 len() 可快速获悉列表的长度。在下面的示例中，列表包含四个元素，因此其长度为 4：

>>> cars = ['bmw', 'audi', 'toyota', 'subaru']
>>> len(cars)
4

需要完成如下任务时，len() 很有用：明确还有多少个外星人未被射杀，确定需要管理多少项可视化数据，计算网站有
多少注册用户，等等。

注意：Python 计算列表元素数时从 1 开始，因此确定列表长度时，你应该不会遇到差一错误。

"""