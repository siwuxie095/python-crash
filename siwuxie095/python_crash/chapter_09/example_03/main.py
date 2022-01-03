"""

使用类和实例


可使用类来模拟现实世界中的很多情景。类编写好后，你的大部分时间将花在根据类创建的实例上。你需要执行的一个重要
任务是修改实例的属性。可以直接修改实例的属性，也可以编写方法以特定的方式进行修改。



1、Car 类

下面来编写一个表示汽车的类。它存储了有关汽车的信息，还有一个汇总这些信息的方法：

class Car:
    \"""一次模拟汽车的简单尝试。\"""

❶    def __init__(self, make, model, year):
        \"""初始化描述汽车的属性。\"""
        self.make = make
        self.model = model
        self.year = year

❷    def get_descriptive_name(self):
        \"""返回整洁的描述性信息。\"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

❸ my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

在❶处，定义了方法 __init__()。与前面的 Dog 类中一样，这个方法的第一个形参为 self。该方法还包含另外三个
形参：make、model 和 year。方法 __init__() 接受这些形参的值，并将它们赋给根据这个类创建的实例的属性。
创建新的 Car 实例时，需要指定其制造商、型号和生产年份。

在❷处，定义了一个名为 get_descriptive_name() 的方法。它使用属性 year 、make 和 model 创建一个对
汽车进行描述的字符串，使得无须分别打印每个属性的值。为在这个方法中访问属性的值，使用了 self.make 、self
.model 和 self.year。在❸处， 根据 Car 类创建了一个实例，并将其赋给变量 my_new_car。接下来，调用方
法 get_descriptive_name()，指出拥有一辆什么样的汽车：

2019 Audi A4

为了让这个类更有趣，下面给它添加一个随时间变化的属性，用于存储汽车的总里程。



2、给属性指定默认值

创建实例时，有些属性无须通过形参来定义，可在方法 __init__() 中为其指定默认值。

下面来添加一个名为 odometer_reading 的属性，其初始值总是为 0。还添加了一个名为 read_odometer() 的
方法，用于读取汽车的里程表：

class Car:
    def __init__(self, make, model, year):
        \"""初始化描述汽车的属性。\"""
        self.make = make
        self.model = model
        self.year = year
❶        self.odometer_reading = 0

    def get_descriptive_name(self):
        --snip--

❷    def read_odometer(self):
        \"""打印一条指出汽车里程的消息。\"""
        print(f"This car has {self.odometer_reading} miles on it.")

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

现在，当 Python 调用方法 __init__() 来创建新实例时，将像前一个示例一样以属性的方式存储制造商、型号和生产
年份。接下来，Python 将创建一个名为 odometer_reading 的属性，并将其初始值设置为 0（见❶）。在❷处，定义
一个名为 read_odometer() 的方法，让你能够轻松地获悉汽车的里程。

PS：此处里程的单位为英里（mile），1英里 ≈ 1.6千米。

一开始汽车的里程为 0：

2019 Audi A4
This car has 0 miles on it.

出售时里程表读数为 0 的汽车不多，因此需要一种方式来修改该属性的值。



3、修改属性的值

能以三种方式修改属性的值：直接通过实例进行修改，通过方法进行设置，以及通过方法进行递增（增加特定的值）。下面
依次介绍这些方式。


a. 直接修改属性的值

要修改属性的值，最简单的方式是通过实例直接访问它。下面的代码直接将里程表读数设置为 23：

class Car:
    --snip--

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

❶ my_new_car.odometer_reading = 23
my_new_car.read_odometer()

在❶处，使用句点表示法直接访问并设置汽车的属性 odometer_reading。这行代码让 Python 在实例 my_new_car
中找到属性 odometer_reading，并将其值设置为 23：

2019 Audi A4
This car has 23 miles on it.

有时候需要像这样直接访问属性，但其他时候需要编写对属性进行更新的方法。


b. 通过方法修改属性的值

如果有方法能替你更新属性，将大有裨益。这样就无须直接访问属性，而可将值传递给方法，由它在内部进行更新。

下面的示例演示了一个名为 update_odometer() 的方法：

class Car:
    --snip--

    def update_odometer(self, mileage):
        \"""将里程表读数设置为指定的值。\"""
        self.odometer_reading = mileage

my_new_car = Car('audi', 'a4', 2019)
print(my_new_car.get_descriptive_name())

❷ my_new_car.update_odometer(23)
my_new_car.read_odometer()

对 Car 类所做的唯一修改是在❶处添加了方法 update_odometer()。这个方法接受一个里程值，并将其赋给 self
.odometer_reading 。在❷处，调用 update_odometer()，并向它提供了实参 23（该实参对应于方法定义中的
形参 mileage）。它将里程表读数设置为 23， 而方法 read_odometer() 打印该读数：

2019 Audi A4
This car has 23 miles on it.

可对方法 update_odometer() 进行扩展，使其在修改里程表读数时做些额外的工作。下面来添加一些逻辑，禁止任
何人将里程表读数往回调：

class Car:
    --snip--

    def update_odometer(self, mileage):
        \"""
        将里程表读数设置为指定的值。
        禁止将里程表读数往回调。
        \"""
❶        if mileage >= self.odometer_reading:
             self.odometer_reading = mileage
        else:
❷            print("You can't roll back an odometer!")

现在，update_odometer() 在修改属性前检查指定的读数是否合理。如果新指定的里程（mileage）大于或等于原来
的里程（self.odometer_reading），就将里程表读数改为新指定的里程（见❶）；否则发出警告，指出不能将里程表
往回调（见❷）。


c. 通过方法对属性的值进行递增

有时候需要将属性值递增特定的量，而不是将其设置为全新的值。假设购买了一辆二手车，且从购买到登记期间增加了 100
英里的里程。下面的方法能够传递这个增量，并相应地增大里程表读数：

class Car:
    --snip--

    def update_odometer(self, mileage):
        --snip--

    def increment_odometer(self, miles):
        \"""将里程表读数增加指定的量。\"""
        self.odometer_reading += miles

❷ my_used_car = Car('subaru', 'outback', 2015)
print(my_used_car.get_descriptive_name())

❸ my_used_car.update_odometer(23_500)
my_used_car.read_odometer()

❹ my_used_car.increment_odometer(100)
my_used_car.read_odometer()

在❶处，新增的方法 increment_odometer() 接受一个单位为英里的数，并将其加入 self.odometer_reading
中。在❷处，创建一辆二手车 my_used_car。在❸处，调用方法 update_odometer() 并传入 23_500，将这辆二
手车的里程表读数设置为 23 500。在❹处，调用 increment_odometer() 并传入 100，以增加从购买到登记期间
行驶的 100 英里：

2015 Subaru Outback
This car has 23500 miles on it.
This car has 23600 miles on it.

你可以轻松地修改这个方法，以禁止增量为负值，从而防止有人利用它来回调里程表。

注意：你可以使用类似于上面的方法来控制用户修改属性值（如里程表读数）的方式，但能够访问程序的人都可以通过直接
访问属性来将里程表修改为任何值。要确保安全，除了进行类似于前面的基本检查外，还需特别注意细节。

"""