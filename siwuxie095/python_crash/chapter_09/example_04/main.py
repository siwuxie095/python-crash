"""

继承


编写类时，并非总是要从空白开始。如果要编写的类是另一个现成类的特殊版本，可使用继承。一个类继承另一个类时，
将自动获得另一个类的所有属性和方法。原有的类称为父类，而新类称为子类。子类继承了父类的所有属性和方法，同
时还可以定义自己的属性和方法。



1、子类的方法 __init__()

在既有类的基础上编写新类时，通常要调用父类的方法 __init__()。这将初始化在父类 __init__() 方法中定义
的所有属性，从而让子类包含这些属性。

例如，下面来模拟电动汽车。电动汽车是一种特殊的汽车，因此可在之前创建的 Car 类的基础上创建新类 ElectricCar。
这样就只需为电动汽车特有的属性和行为编写代码。

下面来创建 ElectricCar 类的一个简单版本，它具备 Car 类的所有功能：

❶ class Car:
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


❷ class ElectricCar(Car):
    \"""电动汽车的独特之处。\"""

❸    def __init__(self, make, model, year):
        \"""初始化父类的属性。\"""
❹        super().__init__(make, model, year)


❺ my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())

首先是 Car 类的代码（见❶）。创建子类时，父类必须包含在当前文件中，且位于子类前面。在❷处，定义了子类
ElectricCar。定义子类时，必须在圆括号内指定父类的名称。方法 __init__() 接受创建 Car 实例所需的
信息（见❸）。

❹处的 super() 是一个特殊函数，让你能够调用父类的方法。这行代码让 Python 调用父类 Car 类的方法
__init__()，让 ElectricCar 实例包含这个方法中定义的所有属性。父类也称为超类（superclass），
名称 super 由此而来。

为测试继承能够正确地发挥作用，这里尝试创建一辆电动汽车，但提供的信息与创建普通汽车时相同。在❺处，创建
ElectricCar 类的一个实例，并将其赋给变量 my_tesla。这行代码调用 ElectricCar 类中定义的方法
__init__()，后者让 Python 调用父类 Car 中定义的方法 __init__()。

这里提供了实参 'tesla'、'model s' 和 2019。

除方法 __init___() 外，电动汽车没有其他特有的属性和方法。当前，只想确认电动汽车具备普通汽车的行为：

2019 Tesla Model S

ElectricCar 实例的行为与 Car 实例一样，现在可以开始定义电动汽车特有的属性和方法了。



2、给子类定义属性和方法

让一个类继承另一个类后，就可以添加区分子类和父类所需的新属性和新方法了。

下面来添加一个电动汽车特有的属性（电瓶），以及一个描述该属性的方法。这里将存储电瓶容量，并编写一个打印
电瓶描述的方法：

class Car:
    --snip--

class ElectricCar(Car):
    \"""电动汽车的独特之处。\"""
    
    def __init__(self, make, model, year):
        \"""
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        \"""
        super().__init__(make, model, year) 
❶        self.battery_size = 75

❷        def describe_battery(self):
        \"""打印一条描述电瓶容量的消息。\"""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.describe_battery()

在❶处，添加了新属性 self.battery_size，并设置其初始值（75）。根据 ElectricCar 类创建的所有实例
都将包含该属性，但所有 Car 实例都不包含它。在❷处，还添加了一个名为 describe_battery() 的方法，打
印有关电瓶的信息。调用这个方法时，将看到一条电动汽车特有的描述：

2019 Tesla Model S
This car has a 75-kWh battery.

对于 ElectricCar 类的特殊程度没有任何限制。模拟电动汽车时，可根据所需的准确程度添加任意数量的属性和
方法。如果一个属性或方法是任何汽车都有的，而不是电动汽车特有的，就应将其加入到 Car 类而非 ElectricCar
类中。这样，使用 Car 类的人将获得相应的功能，而 ElectricCar 类只包含处理电动汽车特有属性和行为的代码。



3、重写父类的方法

对于父类的方法，只要它不符合子类模拟的实物的行为，都可以进行重写。为此，可在子类中定义一个与要重写的父类
方法同名的方法。这样，Python 将不会考虑这个父类方法，而只关注你在子类中定义的相应方法。

假设 Car 类有一个名为 fill_gas_tank() 的方法，它对全电动汽车来说毫无意义，因此你可能想重写它。下面
演示了一种重写方式：

class ElectricCar(Car):
    --snip--

    def fill_gas_tank(self):
        \"""电动汽车没有油箱。\"""
        print("This car doesn't need a gas tank!")

现在，如果有人对电动汽车调用方法 fill_gas_tank()，Python 将忽略 Car 类中的方法 fill_gas_tank()，
转而运行上述代码。使用继承时，可让子类保留从父类那里继承而来的精华，并剔除不需要的糟粕。



4、将实例用作属性

使用代码模拟实物时，你可能会发现自己给类添加的细节越来越多：属性和方法清单以及文件都越来越长。在这种情况
下，可能需要将类的一部分提取出来，作为一个独立的类。可以将大型类拆分成多个协同工作的小类。

例如，不断给 ElectricCar 类添加细节时，可能发现其中包含很多专门针对汽车电瓶的属性和方法。在这种情况下，
可将这些属性和方法提取出来，放到一个名为 Battery 的类中，并将一个 Battery 实例作为 ElectricCar 类
的属性：

class Car:
    --snip--

❶ class Battery:
    \"""一次模拟电动汽车电瓶的简单尝试。\"""
    
❷    def __init__(self, battery_size=75):
        \"""初始化电瓶的属性。\""" 
        self.battery_size = battery_size
    
❸    def describe_battery(self):
        \"""打印一条描述电瓶容量的消息。\"""
        print(f"This car has a {self.battery_size}-kWh battery.")

class ElectricCar(Car):
    \"""电动汽车的独特之处。\"""
    
    def __init__(self, make, model, year):
        \"""
        初始化父类的属性。
        再初始化电动汽车特有的属性。
        \"""
        super().__init__(make, model, year) 
❹        self.battery = Battery()
        
my_tesla = ElectricCar('tesla', 'model s', 2019)

print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

❶处定义一个名为 Battery 的新类，它没有继承任何类。❷处的方 法 __init__() 除 self 外，还有另一个
形参 battery_size。这个形参是可选的：如果没有给它提供值，电瓶容量将被设置为 75。另外，还有一个方法
describe_battery() 也移到了这个类中（见❸）。

在 ElectricCar 类中，添加了一个名为 self.battery 的属性（见❹）。这行代码让 Python 创建一个新
的 Battery 实例（因为没有指定容量，所以为默认值 75），并将该实例赋给属性 self.battery。每当方法
__init__() 被调用时，都将执行该操作，因此现在每个 ElectricCar 实例都包含一个自动创建的 Battery
实例。

这里创建一辆电动汽车，并将其赋给变量 my_tesla。描述电瓶时，需要使用电动汽车的属性 battery：

my_tesla.battery.describe_battery()

这行代码让 Python 在实例 my_tesla 中查找属性 battery，并对存储在该属性中的 Battery 实例调用方
法 describe_battery()。

输出与你在前面看到的相同：

2019 Tesla Model S
This car has a 75-kWh battery.

这看似做了很多额外的工作，但是现在想多详细地描述电瓶都可以，且不会导致 ElectricCar 类混乱不堪。下面
再给 Battery 类添加一个方法，它根据电瓶容量报告汽车的续航里程：

class Car:
    --snip--

class Battery:
    --snip--

❶    def get_range(self):
        \"""打印一条消息，指出电瓶的续航里程。\"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")
    
class ElectricCar(Car):
    --snip--

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
❷ my_tesla.battery.get_range()

❶处新增的方法 get_range() 做了一些简单的分析：如果电瓶的容量为75 kWh，就将续航里程设置为 260 英
里；如果容量为 100 kWh，就将续航里程设置为 315 英里，然后报告这个值。为使用这个方法，也需要通过汽车
的属性 battery 来调用（见❷）。

输出指出了汽车的续航里程（这取决于电瓶的容量）：

2019 Tesla Model S
This car has a 75-kWh battery.
This car can go about 260 miles on a full charge.



5、模拟实物

模拟较复杂的物件（如电动汽车）时，需要解决一些有趣的问题。续航里程是电瓶的属性还是汽车的属性呢？如果只描述
一辆汽车，将方法 get_range() 放在 Battery 类中也许是合适的，但如果要描述一家汽车制造商的整个产品线，
也许应该将方法 get_range() 移到 ElectricCar 类中。在这种情况下，get_range() 依然根据电瓶容量来确
定续航里程，但报告的是一款汽车的续航里程。也可以这样做：仍将方法 get_range() 留在 Battery 类中，但向
它传递一个参数，如 car_model。在这种情况下，方法 get_range() 将根据电瓶容量和汽车型号报告续航里程。

这让你进入了程序员的另一个境界：解决上述问题时，从较高的逻辑层面（而不是语法层面）考虑；考虑的不是 Python，
而是如何使用代码来表示实物。达到这种境界后，你会经常发现，对现实世界的建模方法没有对错之分。有些方法的效率
更高，但要找出效率最高的表示法，需要经过一定的实践。只要代码像你希望的那样运行，就说明你做得很好！即便发现
自己不得不多次尝试使用不同的方法来重写类，也不必气馁。要编写出高效、准确的代码，都得经过这样的过程。

"""