"""

创建和使用类


使用类几乎可以模拟任何东西。下面来编写一个表示小狗的简单类 Dog，它表示的不是特定的小狗，而是任何小狗。对于
大多数宠物狗，大家都知道些什么呢？它们都有名字和年龄。还知道，大多数小狗还会蹲下和打滚。由于大多数小狗都具
备上述两项信息（名字和年龄）和两种行为（蹲下和打滚），这里的 Dog 类将包含它们。这个类让 Python 知道如何
创建表示小狗的对象。编写这个类后，将使用它来创建表示特定小狗的实例。



1、创建 Dog 类

根据 Dog 类创建的每个实例都将存储名字和年龄，赋予了每条小狗蹲下（sit()）和打滚（roll_over()）的能力：

❶ class Dog:
❷    \"""一次模拟小狗的简单尝试。\"""

❸    def __init__(self, name, age):
        \"""初始化属性name和age。\"""
❹        self.name = name
        self.age = age

❺    def sit(self):
        \"""模拟小狗收到命令时蹲下。\"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        \"""模拟小狗收到命令时打滚。\"""
        print(f"{self.name} rolled over!")

这里需要注意的地方很多，但也不用担心，后续内容充斥着这样的结构，你有大把的机会熟悉它。❶处定义了一个名为
Dog 的类。根据约定，在 Python 中，首字母大写的名称指的是类。这个类定义中没有圆括号，因为要从空白创建
这个类。❷处编写了一个文档字符串，对这个类的功能做了描述。


方法 __init__()

类中的函数称为方法。你在前面学到的有关函数的一切都适用于方法，就目前而言，唯一重要的差别是调用方法的方式。
❸处的方法 __init__() 是一个特殊方法，每当你根据 Dog 类创建新实例时，Python 都会自动运行它。在这个
方法的名称中，开头和末尾各有两个下划线，这是一种约定，旨在避免 Python 默认方法与普通方法发生名称冲突。
务必确保 __init__() 的两边都有两个下划线，否则当你使用类来创建实例时，将不会自动调用这个方法，进而引发
难以发现的错误。

这里将方法 __init__() 定义成包含三个形参：self、name 和 age。在这个方法的定义中，形参 self 必不可少，
而且必须位于其他形参的前面。为何必须在方法定义中包含形参 self 呢？因为 Python 调用这个方法来创建 Dog
实例时，将自动传入实参 self。每个与实例相关联的方法调用都自动传递实参 self，它是一个指向实例本身的引用，
让实例能够访问类中的属性和方法。创建 Dog 实例时，Python 将调用 Dog 类的方法 __init__()。这里将通过
实参向 Dog() 传递名字和年龄，self 会自动传递，因此不需要传递它。每当根据 Dog 类创建实例时，都只需给最后
两个形参（name 和 age）提供值。

❹处定义的两个变量都有前缀 self。以 self 为前缀的变量可供类中的所有方法使用，可以通过类的任何实例来访问。
self.name = name 获取与形参 name 相关联的值，并将其赋给变量 name，然后该变量被关联到当前创建的实例。
self.age = age 的作用与此类似。像这样可通过实例访问的变量称为属性。

Dog 类还定义了另外两个方法：sit() 和 roll_over()（见❺）。这些方法执行时不需要额外的信息，因此它们只有
一个形参 self。随后将创建的实例能够访问这些方法，换句话说，它们都会蹲下和打滚。当前，sit() 和 roll_over()
所做的有限，只是打印一条消息，指出小狗正在蹲下或打滚。但可以扩展这些方法以模拟实际情况：如果这个类包含在一个
计算机游戏中，这些方法将包含创建小狗蹲下和打滚动画效果的代码；如果这个类是用于控制机器狗的，这些方法将让机器
狗做出蹲下和打滚的动作。



2、根据类创建实例

可将类视为有关如何创建实例的说明。Dog 类是一系列说明，让 Python 知道如何创建表示特定小狗的实例。

下面来创建一个表示特定小狗的实例：

class Dog:
    --snip--

❶ my_dog = Dog('Willie', 6)

❷ print(f"My dog's name is {my_dog.name}.")
❸ print(f"My dog is {my_dog.age} years old.")

这里使用的是前一个示例中编写的 Dog 类。在❶处，让 Python 创建一条名字为 'Willie'、年龄为 6 的小狗。
遇到这行代码时，Python 使用实参 'Willie' 和 6 调用 Dog 类的方法 __init__()。方 法 __init__()
创建一个表示特定小狗的实例，并使用提供的值来设置属性 name 和 age。接下来，Python 返回一个表示这条小
狗的实例，而这里将这个实例赋给了变量 my_dog。在这里，命名约定很有用：通常可认为首字母大写的名称（如Dog）
指的是类，而小写的名称（如 my_dog）指的是根据类创建的实例。


a. 访问属性

要访问实例的属性，可使用句点表示法。❷处编写了如下代码来访问 my_dog 的属性 name 的值：

my_dog.name

句点表示法在 Python 中很常用，这种语法演示了 Python 如何获悉属性的值。在这里，Python 先找到实例
my_dog，再查找与该实例相关联的属性 name。在 Dog 类中引用这个属性时，使用的是 self.name。在❸处，
使用同样的方法来获取属性 age 的值。

输出是有关 my_dog 的摘要：

My dog's name is Willie.
My dog is 6 years old.


b. 调用方法

根据 Dog 类创建实例后，就能使用句点表示法来调用 Dog 类中定义的任何方法了。下面来让小狗蹲下和打滚：

class Dog:
    --snip--

my_dog = Dog('Willie', 6)
my_dog.sit()
my_dog.roll_over()

要调用方法，可指定实例的名称（这里是 my_dog）和要调用的方法，并用句点分隔。遇到代码 my_dog.sit()
时，Python 在类 Dog 中查找方法 sit() 并运行其代码。同理，Python 也将会以同样的方式解读代码
 my_dog.roll_over()。

Willie 按这里的命令做了：

Willie is now sitting.
Willie rolled over!

这种语法很有用。如果给属性和方法指定了合适的描述性名称，如 name、age、sit() 和 roll_over()，
即便是从未见过的代码块，也能够轻松地推断出它是做什么的。


c. 创建多个实例

可按需求根据类创建任意数量的实例。下面再创建一个名为 your_dog 的小狗实例：

class Dog:
    --snip--

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()

print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()

在本例中创建了两条小狗，分别名为 Willie 和 Lucy。每条小狗都是一个独立的实例，有自己的一组属性，
能够执行相同的操作：

My dog's name is Willie.
My dog is 6 years old.
Willie is now sitting.

Your dog's name is Lucy.
Your dog is 3 years old.
Lucy is now sitting.

即使给第二条小狗指定同样的名字和年龄，Python 依然会根据 Dog 类创建另一个实例。你可按需求根据
一个类创建任意数量的实例，条件是将每个实例都存储在不同的变量中，或者占用列表或字典的不同位置。

"""