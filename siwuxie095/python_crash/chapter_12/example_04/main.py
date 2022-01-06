"""

开始游戏项目


开始开发游戏《外星人入侵》吧。首先要创建一个空的 Pygame 窗口，供之后用来绘制游戏元素，如飞船和外星人。这里还将让这个
游戏响应用户输入，设置背景色，以及加载飞船图像。



1、创建 Pygame 窗口及响应用户输入

下面创建一个表示游戏的类，以创建空的 Pygame 窗口。为此，在文本编辑器中新建一个文件，将其保存为 alien_invasion.py，
再在其中输入如下代码：

import sys

import pygame

class AlienInvasion:
    \"""管理游戏资源和行为的类\"""

    def __init__(self):
        \"""初始化游戏并创建游戏资源。\"""
❶        pygame.init()

❷        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        \"""开始游戏的主循环\"""
❸        while True:
            # 监视键盘和鼠标事件。
❹            for event in pygame.event.get():
❺                if event.type == pygame.QUIT:
                    sys.exit()

            # 让最近绘制的屏幕可见。
❻            pygame.display.flip()


if __name__ == '__main__':
    # 创建游戏实例并运行游戏。
    ai = AlienInvasion()
    ai.run_game()

首先，导入模块 sys 和 pygame。模块 pygame 包含开发游戏所需的功能。玩家退出时，将使用模块 sys 中的工具来退出游戏。

为开发游戏《外星人入侵》，这里创建了一个表示它的类，名为 AlienInvasion。在这个类的方法 __init__() 中，调用函数
pygame.init() 来初始化背景设置，让 Pygame 能够正确地工作（见❶）。在❷处，调用 pygame.display.set_mode()
来创建一个显示窗口，游戏的所有图形元素都将在其中绘制。实参 (1200, 800) 是一个元组，指定了游戏窗口的尺寸——宽 1200
像素、高 800 像素（你可以根据自己的显示器尺寸调整这些值）。将这个显示窗口赋给属性 self.screen，让这个类中的所有
方法都能够使用它。

赋给属性 self.screen 的对象是一个 surface。在 Pygame 中，surface 是屏幕的一部分，用于显示游戏元素。在这个游
戏中，每个元素（如外星人或飞船）都是一个 surface。display.set_mode() 返回的 surface 表示整个游戏窗口。激活
游戏的动画循环后，每经过一次循环都将自动重绘这个 surface，将用户输入触发的所有变化都反映出来。

这个游戏由方法 run_game() 控制。该方法包含一个不断运行的 while 循环（见❸），而这个循环包含一个事件循环以及管理
屏幕更新的代码。事件是用户玩游戏时执行的操作，如按键或移动鼠标。为程序响应事件，可编写一个事件循环，以侦听事件并根据
发生的事件类型执行合适的任务。❹处的 for 循环就是一个事件循环。

为访问 Pygame 检测到的事件，这里使用了函数 pygame.event.get()。这个函数返回一个列表，其中包含它在上一次被调用
后发生的所有事件。所有键盘和鼠标事件都将导致这个 for 循环运行。在这个循环中，将编写一系列 if 语句来检测并响应特定
的事件。例如，当玩家单击游戏窗口的关闭按钮时，将检测到 pygame.QUIT 事件，进而调用 sys.exit() 来退出游戏（见❺）。

❻处调用了 pygame.display.flip()，命令 Pygame 让最近绘制的屏幕可见。在这里，它在每次执行 while 循环时都绘制
一个空屏幕，并擦去旧屏幕，使得只有新屏幕可见。移动游戏元素时，pygame.display.flip() 将不断更新屏幕，以显示元素
的新位置，并且在原来的位置隐藏元素，从而营造平滑移动的效果。

在这个文件末尾，创建一个游戏实例并调用 run_game()。这些代码放在一个 if 代码块中，仅当直接运行该文件时，它们才会
执行。如果此时运行 alien_invasion.py，将看到一个空的 Pygame 窗口。



2、设置背景色

Pygame 默认创建一个黑色屏幕，这太乏味了。下面来将背景设置为另一种颜色，这是在方法 __init__() 末尾进行的：

def __init__(self):
    --snip--
    pygame.display.set_caption("Alien Invasion")

    # 设置背景色。
    self.bg_color = (230, 230, 230)

def run_game(self):
    --snip--
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    # 每次循环时都重绘屏幕。
    self.screen.fill(self.bg_color)

    # 让最近绘制的屏幕可见。
    pygame.display.flip()

在 Pygame 中，颜色是以 RGB 值指定的。这种颜色由红色、绿色和蓝色值组成，其中每个值的可能取值范围都是 0～255。颜色
值 (255,0, 0) 表示红色，(0, 255, 0) 表示绿色，而 (0, 0, 255) 表示蓝色。通过组合不同的 RGB 值，可创建 1600
万种颜色。

在颜色值 (230, 230, 230) 中，红色、绿色和蓝色的量相同，它生成一种浅灰色。将这种颜色赋给了 self.bg_color（见❶）。

在❷处，调用方法 fill() 用这种背景色填充屏幕。方法 fill() 用于处理 surface，只接受一个实参：一种颜色。



3、创建设置类

每次给游戏添加新功能时，通常也将引入一些新设置。下面来编写一个名为 settings 的模块，在其中包含一个名为 Settings
的类，用于将所有设置都存储在一个地方，以免在代码中到处添加设置。这样，每当需要访问设置时，只需使用一个设置对象。另外，
在项目增大时，这使得修改游戏的外观和行为更容易：要修改游戏，只需修改（接下来将创建的）settings.py 中的一些值，而
无须查找散布在项目中的各种设置。

在文件夹 alien_invasion 中，新建一个名为 settings.py 的文件，并在其中添加如下 Settings 类：

class Settings:
    \"""存储游戏《外星人入侵》中所有设置的类\"""

    def __init__(self):
        \"""初始化游戏的设置。\"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

为在项目中创建 Settings 实例并用它来访问设置，需要将 alien_invasion.py 修改成下面这样：

--snip--
import pygame

from settings import Settings

class AlienInvasion:
    \"""管理游戏资源和行为的类\"""

    def __init__(self):
        \"""初始化游戏并创建游戏资源。\"""
        pygame.init()
❶        self.settings = Settings()

❷        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        --snip--
        # 每次循环时都重绘屏幕。
❸        self.screen.fill(self.settings.bg_color)

        # 让最近绘制的屏幕可见。
        pygame.display.flip()

--snip--

在主程序文件中，导入 Settings 类，调用 pygame.init()，再创建一个 Settings 实例并将其赋给 self.settings
（见❶）。创建屏幕时（见❷），使用了 self.settings 的属性 screen_width 和 screen_height。接下来填充屏幕
时，也使用了 self.settings 来访问背景色（见❸）。

如果此时运行 alien_invasion.py，结果不会有任何不同，因为这里只是将设置移到了不同的地方。现在可以在屏幕上添加
新元素了。

"""