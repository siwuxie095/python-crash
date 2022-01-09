"""

结束游戏


如果玩家根本不会输，游戏还有什么趣味和挑战性可言？如果玩家没能在足够短的时间内将整群外星人消灭干净，导致有外星人
撞到了飞船或抵达屏幕底端，飞船将被摧毁。与此同时，限制玩家可使用的飞船数，在玩家用光所有的飞船后，游戏将结束。



1、检测外星人和飞船碰撞

首先检查外星人和飞船之间的碰撞，以便在外星人撞上飞船时做出合适的响应。为此，在 AlienInvasion 中更新每个外星人
的位置后，立即检测外星人和飞船之间的碰撞：

    def _update_aliens(self):
        --snip--
        self.aliens.update()

        # 检测外星人和飞船之间的碰撞。
❶        if pygame.sprite.spritecollideany(self.ship, self.aliens):
❷            print("Ship hit!!!")

函数 spritecollideany() 接受两个实参：一个精灵和一个编组。它检查编组是否有成员与精灵发生了碰撞，并在找到与
精灵发生碰撞的成员后停止遍历编组。在这里，它遍历编组 aliens，并返回找到的第一个与飞船发生碰撞的外星人。

如果没有发生碰撞，spritecollideany() 将返回 None，因此❶处的 if 代码块不会执行。如果找到了与飞船发生碰撞
的外星人，它就返回这个外星人，因此 if 代码块将执行：打印 “Ship hit!!!”（见❷）。有外星人撞到飞船时，需要执
行很多任务：删除余下的外星人和子弹，让飞船重新居中，以及创建一群新的外星人。编写完成这些任务的代码之前，需要确
定检测外星人和飞船碰撞的方法是否可行。为此，最简单的方式就是调用函数 print()。

现在如果运行这个游戏，则每当有外星人撞到飞船时，终端窗口都将显示 “Ship hit!!!”。测试这项功能时，请将 alien-
_drop_speed 设置为较大的值，如 50 或 100，这样外星人将更快地撞到飞船。



2、响应外星人和飞船碰撞

现在需要确定当外星人与飞船发生碰撞时该做些什么。这里不销毁 Ship 实例并创建新的，而是通过跟踪游戏的统计信息来
记录飞船被撞了多少次（跟踪统计信息还有助于记分）。

下面来编写一个用于跟踪游戏统计信息的新类 GameStats，并将其保存为文件 game_stats.py：

class GameStats:
    \"""跟踪游戏的统计信息。\"""

    def __init__(self, ai_game):
        \"""初始化统计信息。\"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        \"""初始化在游戏运行期间可能变化的统计信息。\"""
        self.ships_left = self.settings.ship_limit

在游戏运行期间，只创建一个 GameStats 实例，但每当玩家开始新游戏时，需要重置一些统计信息。为此，在方法 reset-
_stats() 中初始化大部分统计信息，而不是在 __init__() 中直接初始化。这里在 __init__() 中调用这个方法，这
样创建 GameStats 实例时将妥善地设置这些统计信息，在玩家开始新游戏时也能调用 reset_stats()。

当前，只有一项统计信息 ships_left，其值在游戏运行期间不断变化。一开始玩家拥有的飞船数存储在 settings.py 的
ship_limit 中：

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

还需对 alien_invasion.py 做些修改，以创建一个 GameStats 实例。 首先，更新这个文件开头的 import 语句：

import sys
from time import sleep

import pygame

from settings import Settings
from game_stats import GameStats
from ship import Ship
--snip--

从 Python 标准库的模块 time 中导入函数 sleep()，以便在飞船被外星人撞到后让游戏暂停片刻。这里还导入了 Game-
Stats。

接下来，在 __init__() 中创建一个 GameStats 实例：

    def __init__(self):
        --snip--
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")

        # 创建一个用于存储游戏统计信息的实例。
        self.stats = GameStats(self)

        self.ship = Ship(self)
        --snip--

在创建游戏窗口后、定义诸如飞船等其他游戏元素前，创建一个 GameStats 实例。

有外星人撞到飞船时，将余下的飞船数减 1，创建一群新的外星人，并将飞船重新放到屏幕底端的中央。另外，让游戏暂停片刻，
让玩家在新外星人群出现前注意到发生了碰撞并将重新创建外星人群。

下面将实现这些功能的大部分代码放到新方法 _ship_hit() 中。 在 _update_aliens() 中，将在有外星人撞到飞船时
调用这个方法：

    def _ship_hit(self):
        \"""响应飞船被外星人撞到。\"""
        # 将ships_left减1。
❶        self.stats.ships_left -= 1

        # 清空余下的外星人和子弹。
❷        self.aliens.empty()
        self.bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端的中央。
❸        self._create_fleet()
        self.ship.center_ship()

        # 暂停。
❹        sleep(0.5)

新方法 _ship_hit() 在飞船被外星人撞到时做出响应。在这个方法中，将余下的飞船数减 1（见❶），再清空编组 aliens
和 bullets（见❷）。

接下来，创建一群新的外星人，并将飞船居中（见❸）。（稍后将在 Ship 类中添加方法 center_ship()）最后，在更新所
有元素后（但在将修改显示到屏幕前）暂停，让玩家知道飞船被撞到了（见❹）。这里的函数调用 sleep() 让游戏暂停半秒钟，
让玩家能够看到外星人撞到了飞船。函数 sleep() 执行完毕后，将接着执行方法 _update_screen()，将新的外星人群绘
制到屏幕上。

在 _update_aliens() 中，当有外星人撞到飞船时，不调用函数 print()，而调用 _ship_hit()：

    def _update_aliens(self):
        --snip--
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

下面是新方法 center_ship()，请将其添加到 ship.py 的末尾：

    def center_ship(self):
        \"""让飞船在屏幕底端居中。\"""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)


这里像 __init__() 中那样让飞船在屏幕底端居中。让飞船在屏幕底端居中后，重置用于跟踪飞船确切位置的属性 self.x。

注意：这里根本没有创建多艘飞船。在整个游戏运行期间，只创建了一个飞船实例，并在该飞船被撞到时将其居中。统计信息
ships_left 指出玩家是否用完了所有的飞船。

请运行这个游戏，射杀几个外星人，并让一个外星人撞到飞船。游戏暂停片刻后，将出现一群新的外星人，而飞船将在屏幕底端
居中。



3、有外星人到达屏幕底端

如果有外星人到达屏幕底端，这里将像有外星人撞到飞船那样做出响应。为检测这种情况，在 alien_invasion.py 中添加
一个新方法：

    def _check_aliens_bottom(self):
        \"""检查是否有外星人到达了屏幕底端。\"""
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
❶            if alien.rect.bottom >= screen_rect.bottom:
                # 像飞船被撞到一样处理。
                self._ship_hit()
                break

方法 _check_aliens_bottom() 检查是否有外星人到达了屏幕底端。到达屏幕底端后，外星人的属性 rect.bottom
大于或等于屏幕的属性 rect.bottom（见❶）。如果有外星人到达屏幕底端，就调用 _ship_hit()。只要检测到一个外星
人到达屏幕底端，就无须检查其他外星人了，因此在调用 _ship_hit() 后退出循环。

然后在 _update_aliens() 中调用 _check_aliens_bottom()：

    def _update_aliens(self):
        --snip--
        # 检测外星人和飞船之间的碰撞。
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()

        # 检查是否有外星人到达了屏幕底端。 
        self._check_aliens_bottom()

在更新所有外星人的位置并检测是否有外星人和飞船发生碰撞后调用 _check_aliens_bottom()。现在，每当有外星人撞到
飞船或抵达屏幕底端时，都将出现一群新的外星人。



4、游戏结束

现在这个游戏看起来更完整了，但它永远都不会结束，只是 ships_left 不断变成越来越小的负数。下面在 GameStats 中
添加一个作为标志的属性 game_active，以便在玩家的飞船用完后结束游戏。首先，在 GameStats 类的方法 __init__()
末尾设置这个标志：

    def __init__(self, ai_game):
        --snip--
        # 游戏刚启动时处于活动状态。
        self.game_active = True

接下来在 _ship_hit() 中添加代码，在玩家的飞船用完后将 game_active 设置为 False：

    def _ship_hit(self):
        \"""响应飞船被外星人撞到。\"""
        if self.stats.ships_left > 0:
            # 将ships_left减1。
            self.stats.ships_left -= 1
            --snip--
            # 暂停。
            sleep(0.5)
        else:
            self.stats.game_active = False

_ship_hit() 的大部分代码没有变。这里将原来的代码都移到了一个 if 语句块中，它检查玩家是否至少还有一艘飞船。
如果是，就创建一群新的外星人，暂停片刻，再接着往下执行。如果玩家没有了飞船，就将 game_active 设置为 False。

"""