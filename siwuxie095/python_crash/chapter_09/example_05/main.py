"""

导入类


随着不断给类添加功能，文件可能变得很长，即便妥善地使用了继承亦如此。为遵循 Python 的总体理念，应让文件尽可能整洁。
Python 在这方面提供了帮助，允许将类存储在模块中，然后在主程序中导入所需的模块。



1、导入单个类

下面来创建一个只包含 Car 类的模块。这就面临一个微妙的命名问题：之前已经有一个名为 car.py 的文件，但这个模块也应
命名为 car.py，因为它包含表示汽车的代码。这里将这样解决这个命名问题：将 Car 类存储在一个名为 car.py 的模块中，
该模块将覆盖前面使用的文件 car.py。从现在开始，使用该模块的程序都必须使用更具体的文件名，如 my_car.py。下面是
模块 car.py，其中只包含 Car 类的代码：

❶ \"""一个可用于表示汽车的类。\"""

class Car:
    \"""一次模拟汽车的简单尝试。\"""

    def __init__(self, make, model, year):
        \"""初始化描述汽车的属性。\"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        \"""返回整洁的描述性信息。\"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        \"""打印一条指出汽车里程的消息。\"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        \"""
        将里程表读数设置为指定的值。
        禁止将里程表读数往回调。
        \"""
        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        \"""将里程表读数增加指定的量。\"""
        self.odometer_reading += miles

❶处包含一个模块级文档字符串，对该模块的内容做了简要的描述。你应为自己创建的每个模块编写文档字符串。

下面来创建另一个文件 my_car.py，在其中导入 Car 类并创建其实例：

❶ from car import Car

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

❶处的 import 语句让 Python 打开模块 car 并导入其中的 Car 类。这样，就可以使用 Car 类，就像它是在这个文件中
定义的一样。输出与在前面看到的一样：

2019 Audi A4
This car has 23 miles on it.

导入类是一种有效的编程方式。如果这个程序包含整个 Class 类，它该有多长啊！通过将这个类移到一个模块中并导入该模块，
依然可以使用其所有功能，但主程序文件变得整洁而易于阅读了。这还让你能够将大部分逻辑存储在独立的文件中。确定类像你
希望的那样工作后，就可以不管这些文件，而专注于主程序的高级逻辑了。



2、在一个模块中存储多个类

虽然同一个模块中的类之间应存在某种相关性，但可根据需要在一个模块中存储任意数量的类。Battery 类和 ElectricCar
类都可帮助模拟汽车，下面将它们都加入模块 car.py 中（新建一个 car_02.py）：

\"""一组用于表示燃油汽车和电动汽车的类。\"""

class Car:
    --snip--

class Battery:
    \"""一次模拟电动汽车电瓶的简单尝试。\"""

    def __init__(self, battery_size=75):
        \"""初始化电瓶的属性。\"""
        self.battery_size = battery_size

    def describe_battery(self):
        \"""打印一条描述电瓶容量的消息。\"""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        \"""打印一条消息，指出电瓶的续航里程。\"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectricCar(Car):
    \"""电动汽车的独特之处。\"""

    def __init__(self, make, model, year):
        \"""
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        \"""
        super().__init__(make, model, year)
        self.battery = Battery()

现在，可以新建一个名为 my_electric_car.py 的文件，导入 ElectricCar 类，并创建一辆电动汽车了：

from car_02 import ElectricCar
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

输出与在前面看到的相同，但大部分逻辑隐藏在一个模块中：

2019 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.



3、从一个模块中导入多个类

可根据需要在程序文件中导入任意数量的类。如果要在同一个程序中创建普通汽车和电动汽车，就需要将 Car 类和
ElectricCar 类都导入：

❶ from car_02 import Car, ElectricCar

❷ my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

❸ my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

在❶处从一个模块中导入多个类时，用逗号分隔了各个类。导入必要的类后，就可根据需要创建每个类的任意数量实例。

在本例中，在❷处创建了一辆大众甲壳虫普通汽车，并在❸处创建了一辆特斯拉 Roadster 电动汽车：

2019 Volkswagen Beetle
2019 Tesla Roadster



4、导入整个模块

还可以导入整个模块，再使用句点表示法访问需要的类。这种导入方式很简单，代码也易于阅读。因为创建类实例的代码都包含
模块名，所以不会与当前文件使用的任何名称发生冲突。

❶ import car_02

❷ my_beetle = car_02.Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

❸ my_tesla = car_02.ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

在❶处，导入了整个 car 模块。接下来，使用语法 module_name.ClassName 访问需要的类。像前面一样，在❷处创建一
辆大众甲壳虫汽车，并在❸处创建一辆特斯拉 Roadster 汽车。



5、导入模块中的所有类

要导入模块中的每个类，可使用下面的语法：

from module_name import *

不推荐使用这种导入方式，原因有二。第一，如果只看文件开头的 import 语句，就能清楚地知道程序使用了哪些类，将大有
裨益。然而这种导入方式没有明确地指出使用了模块中的哪些类。第二，这种方式还可能引发名称方面的迷惑。如果不小心导入
了一个与程序文件中其他东西同名的类，将引发难以诊断的错误。这里之所以介绍这种导入方式，是因为虽然不推荐使用，但你
可能在别人编写的代码中见到它。

需要从一个模块中导入很多类时，最好导入整个模块，并使用 module_name.ClassName 语法来访问类。这样做时，虽然
文件开头并没有列出用到的所有类，但你清楚地知道在程序的哪些地方使用了导入的模块。这也避免了导入模块中的每个类可能
引发的名称冲突。



6、在一个模块中导入另一个模块

有时候，需要将类分散到多个模块中，以免模块太大或在同一个模块中存储不相关的类。将类存储在多个模块中时，你可能会
发现一个模块中的类依赖于另一个模块中的类。在这种情况下，可在前一个模块中导入必要的类。

下面将 Car 类存储在一个模块中，并将 ElectricCar 类和 Battery 类存储在另一个模块中。将第二个模块命名为
electric_car.py（这将覆盖前面创建的文件 electric_car.py），并将 Battery 类和 ElectricCar 类复制
到这个模块中：

\"""一组可用于表示电动汽车的类。\"""

from car import Car

class Battery:
    --snip--

class ElectricCar(Car):
    --snip--

ElectricCar 类需要访问其父类 Car，因此在❶处直接将 Car 类导入该模块中。如果忘记了这行代码，Python 将在
试图创建 ElectricCar 实例时引发错误。还需要更新模块 car，使其只包含 Car 类：

\"""一个可用于表示汽车的类。\"""

class Car:
    --snip--

现在可以分别从每个模块中导入类，以根据需要创建任何类型的汽车了：

❶ from car import Car
from electric_car import ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2019)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2019)
print(my_tesla.get_descriptive_name())

在❶处，从模块 car 中导入了 Car 类，并从模块 electric_car 中导入 ElectricCar 类。接下来，创建了一辆
普通汽车和一辆电动汽车。这两种汽车都被正确地创建出来了：

2019 Volkswagen Beetle
2019 Tesla Roadster



7、使用别名

之前说过，使用模块来组织项目代码时，别名大有裨益。导入类时，也可为其指定别名。

例如，要在程序中创建大量电动汽车实例，需要反复输入 ElectricCar，非常烦琐。为避免这种烦恼，可在 import
语句中给 ElectricCar 指定一个别名：

from electric_car import ElectricCar as EC

现在每当需要创建电动汽车实例时，都可使用这个别名：

my_tesla = EC('tesla', 'roadster', 2019)



8、自定义工作流程

如你所见，在组织大型项目的代码方面，Python 提供了很多选项。熟悉所有这些选项很重要，这样你才能确定哪种项目
组织方式是最佳的，并能理解别人开发的项目。

一开始应让代码结构尽可能简单。先尽可能在一个文件中完成所有的工作，确定一切都能正确运行后，再将类移到独立的
模块中。如果你喜欢模块和文件的交互方式，可在项目开始时就尝试将类存储到模块中。先找出让你能够编写出可行代码
的方式，再尝试改进代码。

"""