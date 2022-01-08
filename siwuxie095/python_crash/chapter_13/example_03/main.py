"""

创建第一个外星人


在屏幕上放置外星人与放置飞船类似。每个外星人的行为都由 Alien 类控制，这里将像创建 Ship 类那样创建这个类。
出于简化考虑，也将使用位图来表示外星人。这幅图像的背景为灰色，与屏幕背景色一致。请务必将选择的图像文件保存
到文件夹 images 中（PS：你也可以自己寻找表示外星人的图像）。



1、创建 Alien 类

下面来编写 Alien 类并将其保存为文件 alien.py：

import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    \"""表示单个外星人的类。\"""

    def __init__(self, ai_game):
        \"""初始化外星人并设置其起始位置。\"""
        super().__init__()
        self.screen = ai_game.screen

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load("images/alien.bmp")
        self.rect = self.image.get_rect()

        # 每个外星人最初都在屏幕左上角附近。
❶        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # 存储外星人的精确水平位置。
❷        self.x = float(self.rect.x)

除位置不同外，这个类的大部分代码与 Ship 类相似。每个外星人最初都位于屏幕左上角附近。将每个外星人的左边距
都设置为外星人的宽度，并将上边距设置为外星人的高度（见❶），这样更容易看清。这里主要关心的是外星人的水平速
度，因此精确地记录了每个外星人的水平位置（见❷）。

Alien 类不需要一个在屏幕上绘制外星人的方法，因为这里将使用一个 Pygame 编组方法，自动在屏幕上绘制编组中
的所有元素。



2、创建 Alien 实例

要让第一个外星人在屏幕上现身，需要创建一个 Alien 实例。这属于设置工作，因此将把这些代码放在 AlienInvasion
类的方法 __init__() 末尾。这里最终会创建一群外星人，涉及的工作量不少，因此将新建一个名为 _create_fleet()
的辅助方法。

在类中，方法的排列顺序无关紧要，只要按统一的标准排列就行。这里将把 _create_fleet() 放在 _update_screen()
前面，不过放在 AlienInvasion 类的任何地方其实都可行。首先，需要导入 Alien 类。

下面是 alien_invasion.py 中修改后的 import 语句：

--snip--
from bullet import Bullet

from alien import Alien

下面是修改后的方法 __init__()：

def __init__(self):
    --snip--
    self.ship = Ship(self)
    self.bullets = pygame.sprite.Group()
    self.aliens = pygame.sprite.Group()

    self._create_fleet()

创建了一个用于存储外星人群的编组，还调用了接下来将编写的方法 _create_fleet()。

    def _create_fleet(self):
        \"""创建外星人群。\"""
        # 创建一个外星人。
        alien = Alien(self)
        self.aliens.add(alien)

在这个方法中，创建了一个 Alien 实例，再将其添加到用于存储外星人群的编组中。外星人默认放在屏幕左上角附近，对第
一个外星人来说，这样的位置非常合适。

要让外星人现身，需要在 _update_screen() 中对外星人编组调用方法 draw()：

    def _update_screen(self):
        --snip--
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.aliens.draw(self.screen)

        pygame.display.flip()

对编组调用 draw() 时，Pygame 将把编组中的每个元素绘制到属性 rect 指定的位置。方法 draw() 接受一个参数，
这个参数指定了要将编组中的元素绘制到哪个 surface 上。

运行代码，第一个外星人正确地现身了，后续来编写绘制一群外星人的代码。

"""