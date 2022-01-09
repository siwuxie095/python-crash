"""

射击


下面来添加射击功能。这里将编写在玩家按空格键时发射子弹（用小矩形表示）的代码。子弹将在屏幕中向上飞行，抵达
屏幕上边缘后消失。



1、添加子弹设置

首先，更新 settings.py，在方法 __init__() 末尾存储新类 Bullet 所需的值：

    def __init__(self):
        --snip--
        # 子弹设置
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)

这些设置创建宽 3 像素、高 15 像素的深灰色子弹。子弹的速度比飞船稍低。



2、创建 Bullet 类

下面来创建存储 Bullet 类的文件 bullet.py，其前半部分如下：

import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    \"""管理飞船所发射子弹的类\"""

    def __init__(self, ai_game):
        \"""在飞船当前位置创建一个子弹对象。\"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在(0,0)处创建一个表示子弹的矩形，再设置正确的位置。
❶        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
❷        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储用小数表示的子弹位置。
❸        self.y = float(self.rect.y)

Bullet 类继承了从模块 pygame.sprite 导入的 Sprite 类。通过使用精灵（sprite），可将游戏中相关的元素
编组，进而同时操作编组中的所有元素。为创建子弹实例，__init__() 需要当前的 AlienInvasion 实例，这里还
调用了 super() 来继承 Sprite。另外，还定义了用于存储屏幕以及设置对象和子弹颜色的属性。

在❶处，创建子弹的属性 rect。子弹并非基于图像，因此必须使用 pygame.Rect() 类从头开始创建一个矩形。创建
这个类的实例时，必须提供矩形左上角的 x 坐标和 y 坐标，以及矩形的宽度和高度。这里在 (0, 0) 处创建这个矩形，
但下一行代码将其移到了正确的位置，因为子弹的初始位置取决于飞船当前的位置。子弹的宽度和高度是从 self.settings
中获取的。

在❷处，将子弹的 rect.midtop 设置为飞船的 rect.midtop。这样子弹将从飞船顶部出发，看起来像是从飞船中射
出的。这里将子弹的 y 坐标存储为小数值，以便能够微调子弹的速度（见❸）。

下面是 bullet.py 的第二部分，包括方法 update() 和 draw_bullet()：

    def update(self):
        \"""向上移动子弹。\"""
        # 更新表示子弹位置的小数值。
❶        self.y -= self.settings.bullet_speed
        # 更新表示子弹的rect的位置。
❷        self.rect.y = self.y

    def draw_bullet(self):
        \"""在屏幕上绘制子弹。\"""
❸        pygame.draw.rect(self.screen, self.color, self.rect)

方法 update() 管理子弹的位置。发射出去后，子弹向上移动，意味着其坐标将不断减小。为更新子弹的位置，从 self
.y 中减去 settings.bullet_speed 的值（见❶）。接下来，将 self.rect.y 设置为 self.y 的值（见❷）。

属性 bullet_speed 使得能够随着游戏的进行或根据需要提高子弹的速度，以调整游戏的行为。子弹发射后，其坐标始
终不变，因此子弹将沿直线垂直向上飞行。

需要绘制子弹时，调用 draw_bullet()。draw.rect() 函数使用存储在 self.color 中的颜色填充表示子弹的
rect 占据的屏幕部分（见❸）。



3、将子弹存储到编组中

定义 Bullet 类和必要的设置后，便可编写代码在玩家每次按空格键时都射出一发子弹了。这里将在 AlienInvasion
中创建一个编组（group），用于存储所有有效的子弹，以便管理发射出去的所有子弹。这个编组是 pygame.sprite.
Group 类的一个实例。pygame.sprite.Group 类似于列表，但提供了有助于开发游戏的额外功能。在主循环中，将
使用这个编组在屏幕上绘制子弹以及更新每颗子弹的位置。

首先，在 __init__() 中创建用于存储子弹的编组：

    def __init__(self):
        --snip--
        self.ship = Ship(self)

        self.bullets = pygame.sprite.Group()

然后在 while 循环中更新子弹的位置：

    def run_game(self):
        \"""开始游戏主循环。\"""
        while True:
            self._check_events()
            self.ship.update()
❶            self.bullets.update()
            self._update_screen()

对编组调用 update() 时（见❶），编组自动对其中的每个精灵调用 update()。因此代码行 bullets.update()
将为编组 bullets 中的每颗子弹调用 bullet.update()。



4、开火

在 AlienInvasion 中，需要修改 _check_keydown_events()，以便在玩家按空格键时发射一颗子弹。无须修改
_check_keyup_events()，因为玩家松开空格键时什么都不会发生。还需要修改 _update_screen()，确保在调用
flip() 前在屏幕上重绘每颗子弹。

为发射子弹，需要做的工作不少，因此编写一个新方法 _fire_bullet() 来完成这项任务：

--snip--
from ship import Ship
❶ from bullet import Bullet

class AlienInvasion:
    --snip--

    def _check_keydown_events(self, event):
        --snip--
        elif event.key == pygame.K_q:
            sys.exit()
❷        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        --snip--

    def _fire_bullet(self):
        \"""创建一颗子弹，并将其加入编组bullets中。\"""
❸        new_bullet = Bullet(self)
❹        self.bullets.add(new_bullet)

    def _update_screen(self):
        \"""更新屏幕上的图像，并切换到新屏幕。\"""
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

❺        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        pygame.display.flip()

--snip--

首先导入 Bullet 类（见❶），再在玩家按空格键时调用 _fire_bullet()（见❷）。在 _fire_bullet() 中，
创建一个 Bullet 实例并将其赋给 new_bullet（见❸），再使用方法 add() 将其加入编组 bullets 中（见❹）。
方法 add() 类似于 append()，不过是专门为 Pygame 编组编写的。

方法 bullets.sprites() 返回一个列表，其中包含编组 bullets 中的所有精灵。为在屏幕上绘制发射的所有子弹，
遍历编组 bullets 中的精灵，并对每个精灵调用 draw_bullet()（见❺）。

如果此时运行 alien_invasion.py，将能够左右移动飞船，并发射任意数量的子弹。子弹在屏幕上向上飞行，抵达屏
幕顶部后消失得无影无踪。你可在 settings.py 中修改子弹的尺寸、颜色和速度。



5、删除消失的子弹

当前，子弹在抵达屏幕顶端后消失，但这仅仅是因为 Pygame 无法在屏幕外面绘制它们。这些子弹实际上依然存在，其
y 坐标为负数且越来越小。这是个问题，因为它们将继续消耗内存和处理能力。

需要将这些消失的子弹删除，否则游戏所做的无谓工作将越来越多，进而变得越来越慢。为此，需要检测表示子弹的 rect
的 bottom 属性是否为零。如果是，则表明子弹已飞过屏幕顶端：

    def run_game(self):
        \"""开始游戏主循环。\"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()

            # 删除消失的子弹。
❶            for bullet in self.bullets.copy():
❷                 if bullet.rect.bottom <= 0:
❸                    self.bullets.remove(bullet)
❹            print(len(self.bullets))
            
            self._update_screen()

使用 for 循环遍历列表（或 Pygame 编组）时，Python 要求该列表的长度在整个循环中保持不变。因为不能从 for
循环遍历的列表或编组中删除元素，所以必须遍历编组的副本。这里使用方法 copy()来设置 for 循环（见❶），从而
能够在循环中修改 bullets。这里检查每颗子弹，看看它是否从屏幕顶端消失（见❷）。如果是，就将其从 bullets
中删除（见❸）。在❹处，使用函数调用 print() 显示当前还有多少颗子弹，以核实确实删除了消失的子弹。

如果这些代码没有问题，发射子弹后查看终端窗口时，将发现随着子弹一颗颗地在屏幕顶端消失，子弹数将逐渐降为零。
运行该游戏并确认子弹被正确删除后，请将这个函数调用 print() 删除。如果不删除，游戏的速度将大大降低，因为
将输出写入终端花费的时间比将图形绘制到游戏窗口花费的时间还要多。



6、限制子弹数量

很多射击游戏对可同时出现在屏幕上的子弹数量进行了限制，以鼓励玩家有目标地射击。下面在游戏《外星人入侵》中做
这样的限制。

首先，在 settings.py 中存储最大子弹数：

        # 子弹设置
        --snip--
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

这将未消失的子弹数限制为三颗。在 AlienInvasion 的 _fire_bullet() 中，在创建新子弹前检查未消失的子弹
数是否小于该设置：

    def _fire_bullet(self):
        \"""创建一颗子弹，并将其加入编组bullets中。\"""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)


玩家按空格键时，检查 bullets 的长度。如果 len(bullets) 小于 3，就创建一颗新子弹；但如果有三颗未消失的
子弹，则玩家按空格键时什么都不会发生。如果现在运行这个游戏，屏幕上最多只能有三颗子弹。



7、创建方法 _update_bullets()

编写并检查子弹管理代码后，可将其移到一个独立的方法中，确保 AlienInvasion 类组织有序。为此，创建一个名为
_update_bullets() 的新方法，并将其放在 _update_screen() 前面：

    def _update_bullets(self):
        \"""更新子弹的位置并删除消失的子弹。\"""
        # 更新子弹的位置。
        self.bullets.update()

        # 删除消失的子弹。
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

_update_bullets() 的代码是从 run_game() 剪切并粘贴而来的，这里只是让注释更清晰了。

run_game() 中的 while 循环又变得简单了：

        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()

让主循环包含尽可能少的代码，这样只要看方法名就能迅速知道游戏中发生的情况。主循环检查玩家的输入，并更新飞船的
位置和所有未消失子弹的位置。然后，使用更新后的位置来绘制新屏幕。

请再次运行 alien_invasion.py，确认发射子弹时没有错误。

"""