"""

添加飞船图像


下面将飞船加入游戏中。为了在屏幕上绘制玩家的飞船，这里将加载一幅图像，再使用 Pygame 方法 blit() 绘制它。

为游戏选择素材时，务必要注意许可。最安全、最不费钱的方式是使用 Pixabay 等网站提供的免费图形，无须授权许可
即可使用并修改。

在游戏中几乎可以使用任何类型的图像文件，但使用位图（.bmp）文件最为简单，因为 Pygame 默认加载位图。虽然可
配置 Pygame 以使用其他文件类型，但有些文件类型要求你在计算机上安装相应的图像库。大多数图像为 .jpg、.png
或 .gif 格式，但可使用 Photoshop、GIMP 和 Paint 等工具将其转换为位图。

选择图像时，要特别注意背景色。请尽可能选择背景为透明或纯色的图像，便于使用图像编辑器将其背景替换为任意颜色。
图像的背景色与游戏的背景色匹配时，游戏看起来最漂亮。你也可以将游戏的背景色设置成图像的背景色。

就游戏《外星人入侵》而言，可使用文件 ship.bmp。这个文件的背景色与项目使用的设置相同。请在项目文件夹中新建
一个名为 images 的文件夹，并将文件 ship.bmp 保存在其中。

PS：项目文件夹 即 alien_invasion。



1、创建 Ship 类

选择用于表示飞船的图像后，需要将其显示到屏幕上。这里创建一个名为 ship 的模块，其中包含 Ship 类，负责管理
飞船的大部分行为。

import pygame

class Ship:
    \"""管理飞船的类\"""

    def __init__(self, ai_game):
        \"""初始化飞船并设置其初始位置。\"""
❶        self.screen = ai_game.screen
❷        self.screen_rect = ai_game.screen.get_rect()

        # 加载飞船图像并获取其外接矩形。
❸        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # 对于每艘新飞船，都将其放在屏幕底部的中央。
❹        self.rect.midbottom = self.screen_rect.midbottom

❺    def blitme(self):
        \"""在指定位置绘制飞船。\"""
        self.screen.blit(self.image, self.rect)

Pygame 之所以高效，是因为它让你能够像处理矩形（rect 对象）一样处理所有的游戏元素，即便其形状并非矩形。像
处理矩形一样处理游戏元素之所以高效，是因为矩形是简单的几何形状。例如，通过将游戏元素视为矩形，Pygame 能够
更快地判断出它们是否发生了碰撞。这种做法的效果通常很好，游戏玩家几乎注意不到处理的并不是游戏元素的实际形状。
在这个类中，将把飞船和屏幕作为矩形进行处理。

定义这个类之前，导入了模块 pygame。Ship 的方法 __init__() 接受两个参数：引用 self 和指向当前 Alien-
Invasion 实例的引用。这让 Ship 能够访问 AlienInvasion 中定义的所有游戏资源。在❶处，将屏幕赋给了 Ship
的一个属性，以便在这个类的所有方法中轻松访问。在❷处，使用方法 get_rect() 访问屏幕的属性 rect，并将其赋
给了 self.screen_rect，这使得能够将飞船放到屏幕的正确位置。

调用 pygame.image.load() 加载图像，并将飞船图像的位置传递给它（见❸）。该函数返回一个表示飞船的 surface，
而这里将这个 surface 赋给了 self.image。加载图像后，使用 get_rect() 获取相应 surface 的属性 rect，
以便后面能够使用它来指定飞船的位置。

处理 rect 对象时，可使用矩形四角和中心的 x 坐标和 y 坐标。可通过设置这些值来指定矩形的位置。要让游戏元素
居中，可设置相应 rect 对象的属性 center、centerx 或 centery；要让游戏元素与屏幕边缘对齐，可使用属性
top、bottom、left 或 right。除此之外，还有一些组合属性，如 midbottom、midtop 、midleft 和 mid-
right。要调整游戏元素的水平或垂直位置，可使用属性 x 和 y，分别是相应矩形左上角的 x 坐标和 y 坐标。这些
属性让你无须做游戏开发人员原本需要手工完成的计算，因此会经常用到。

注意：在 Pygame 中，原点 (0, 0) 位于屏幕左上角，向右下方移动时，坐标值将增大。在 1200 × 800 的屏幕上，
原点位于左上角，而右下角的坐标为 (1200, 800)。这些坐标对应的是游戏窗口，而不是物理屏幕。

这里要将飞船放在屏幕底部的中央。为此，将 self.rect.midbottom 设置为表示屏幕的矩形的属性 midbottom（见❹）。
Pygame 使用这些 rect 属性来放置飞船图像，使其与屏幕下边缘对齐并水平居中。

在❺处，定义了方法 blitme()，它将图像绘制到 self.rect 指定的位置。




2、在屏幕上绘制飞船

下面更新 alien_invasion.py，创建一艘飞船并调用其方法 blitme()：

--snip--
from settings import Settings
from ship import Ship


class AlienInvasion:
    \"""管理游戏资源和行为的类\"""

    def __init__(self):
        --snip--
        pygame.display.set_caption("Alien Invasion")

❶        self.ship = Ship(self)

    def run_game(self):
            --snip--
            # 每次循环时都重绘屏幕。
            self.screen.fill(self.settings.bg_color)
❷            self.ship.blitme()

            # 让最近绘制的屏幕可见。
            pygame.display.flip()

--snip--

导入 Ship 类，并在创建屏幕后创建一个 Ship 实例（见❶）。调用 Ship() 时，必须提供一个参数：一个 Alien-
Invasion 实例。在这里，self 指向的是当前 AlienInvasion 实例。这个参数让 Ship 能够访问游戏资源，如
对象 screen。这里将这个 Ship 实例赋给了 self.ship。

填充背景后，调用 ship.blitme() 将飞船绘制到屏幕上，确保它出现在背景前面（见❷）。

现在如果运行 alien_invasion.py，将看到飞船位于空游戏屏幕底部的中央。

"""