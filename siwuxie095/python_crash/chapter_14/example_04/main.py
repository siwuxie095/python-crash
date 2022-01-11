"""

记分


下面来实现一个记分系统，以实时跟踪玩家的得分，并显示最高得分、等级和余下的飞船数。

得分是游戏的一项统计信息，因此在 GameStats 中添加一个 score 属性：

class GameStats:
    --snip--
    def reset_stats(self):
        \"""初始化在游戏运行期间可能变化的统计信息。\"""
        self.ships_left = self.settings.ship_limit
        self.score = 0

为在每次开始游戏时都重置得分，这里在 reset_stats() 而不是 __init__() 中初始化 score。



1、显示得分

为在屏幕上显示得分，首先创建一个新类 Scoreboard。当前，这个类只显示当前得分，但后面也将使用它来显示最高
得分、等级和余下的飞船数。下面是这个类的前半部分，被保存为文件 scoreboard.py：

import pygame.font

class Scoreboard:
    \"""显示得分信息的类。\"""

❶    def __init__(self, ai_game):
        \"""初始化显示得分涉及的属性。\"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats

        # 显示得分信息时使用的字体设置。
❷        self.text_color = (30, 30, 30)
❸        self.font = pygame.font.SysFont(None, 48)
        # 准备初始得分图像。
❹        self.prep_score()

由于 Scoreboard 在屏幕上显示文本，首先导入模块 pygame.font。接下来，在 __init__() 中包含形参 ai-
_game，以便访问报告跟踪的值所需的对象 settings、screen 和 stats（见❶）。然后，设置文本颜色（见❷）并
实例化一个字体对象（见❸）。

为将要显示的文本转换为图像，调用 prep_score()（见❹），其定义如下：

    def prep_score(self):
        \"""将得分转换为一幅渲染的图像。\"""
❶        score_str = str(self.stats.score)
❷        self.score_image = self.font.render(score_str, True,
                            self.text_color, self.settings.bg_color)

        # 在屏幕右上角显示得分。
❸        self.score_rect = self.score_image.get_rect()
❹        self.score_rect.right = self.screen_rect.right - 20
❺        self.score_rect.top = 20

在 prep_score() 中，将数值 stats.score 转换为字符串（见❶），再将这个字符串传递给创建图像的 render()
（见❷）。为在屏幕上清晰地显示得分，向 render() 传递屏幕背景色和文本颜色。

将得分放在屏幕右上角，并在得分增大导致数变宽时让其向左延伸。为确保得分始终锚定在屏幕右边，创建一个名为 score-
_rect 的 rect（见❸），让其右边缘与屏幕右边缘相距 20 像素（见❹），并让其上边缘与屏幕上边缘也相距20像素（见❺）。

接下来，创建方法 show_score()，用于显示渲染好的得分图像：

    def show_score(self):
        \"""在屏幕上显示得分。\"""
        self.screen.blit(self.score_image, self.score_rect)

这个方法在屏幕上显示得分图像，并将其放在 score_rect 指定的位置。



2、创建记分牌

为显示得分，在 AlienInvasion 中创建一个 Scoreboard 实例。先来更新 import 语句：

--snip--
from game_stats import GameStats
from scoreboard import Scoreboard
--snip--

接下来，在方法 __init__() 中创建一个 Scoreboard 实例：

    def __init__(self):
        --snip--
        pygame.display.set_caption("Alien Invasion")

        # 创建一个用于存储游戏统计信息的实例，
        # 并创建记分牌。 
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)
        --snip--

然后，在 _update_screen() 中将记分牌绘制到屏幕上：

    def _update_screen(self):
        --snip--
        self.aliens.draw(self.screen)

        # 显示得分。 
        self.sb.show_score()

        # 如果游戏处于非活动状态，就绘制Play按钮。
        --snip--

在显示 Play 按钮前调用 show_score()。

如果现在运行这个游戏，将在屏幕右上角看到 0。（当前，只想在进一步开发记分系统前确认得分出现在正确的地方）。

下面来指定每个外星人值多少分！



3、在外星人被消灭时更新得分

为在屏幕上实时显示得分，每当有外星人被击中时，都更新 stats.score 的值，再调用 prep_score() 更新得分图像。
但在此之前，需要指定玩家每击落一个外星人将得到多少分：

    def initialize_dynamic_settings(self):
        --snip--

        # 记分
        self.alien_points = 50

随着游戏的进行，将提高每个外星人的分数。为确保每次开始新游戏时这个值都会被重置，这里在 initialize_dynamic-
_settings() 中设置它。

在 _check_bullet_alien_collisions() 中，每当有外星人被击落时，都更新得分：

    def _check_bullet_alien_collisions(self):
        \"""响应子弹和外星人碰撞。\"""
        # 删除发生碰撞的子弹和外星人。
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if collisions:
            self.stats.score += self.settings.alien_points
            self.sb.prep_score()

        --snip--

有子弹击中外星人时，Pygame返回一个字典（collisions）。检查这个字典是否存在，如果存在，就将得分加上一个外星
人的分数。接下来，调用 prep_score() 来创建一幅包含最新得分的新图像。

如果现在运行这个游戏，得分将不断增加！



4、重置得分

当前，仅在有外星人被射杀之后生成得分。这在大多数情况下可行，但从开始新游戏到有外星人被射杀之间，显示的是上一次
的得分。

为修复这个问题，可在开始新游戏时生成得分：

    def _check_play_button(self, mouse_pos):
        --snip--
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置。
            self.settings.initialize_dynamic_settings()
            # 重置游戏统计信息。
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            --snip--

开始新游戏时，重置游戏统计信息再调用 prep_score()。此时生成的记分牌上显示的得分为零。



5、将消灭的每个外星人都计入得分

当前的代码可能会遗漏一些被消灭的外星人。例如，如果在一次循环中，有两颗子弹击中了外星人，或者因子弹较宽而同时击
中了多个外星人，玩家将只能得到一个外星人的分数。为修复这种问题，下面来调整检测子弹和外星人碰撞的方式。

在 _check_bullet_alien_collisions() 中，与外星人碰撞的子弹都是字典 collisions 中的一个键，而与每颗
子弹相关的值都是一个列表，其中包含该子弹击中的外星人。通过遍历字典 collisions，确保将消灭的每个外星人都计入
得分：

    def _check_bullet_alien_collisions(self):
        --snip--
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
        --snip--

如果字典 collisions 存在，就遍历其中的所有值。别忘了，每个值都是一个列表，包含被同一颗子弹击中的所有外星人。
对于每个列表，都将其包含的外星人数量乘以一个外星人的分数，并将结果加入当前得分。为测试这一点，请将子弹宽度改为
300 像素，并核实得到了其击中的每个外星人的分数，再将子弹宽度恢复正常值。



6、提高分数

鉴于玩家每提高一个等级，游戏都变得更难，因此处于较高的等级时，外星人的分数应更高。为实现这种功能，需要编写在
游戏节奏加快时提高分数的代码：

    def __init__(self):
        --snip--
        # 加快游戏节奏的速度。
        self.speedup_scale = 1.1
        # 外星人分数的提高速度。
❶        self.score_scale = 1.5

        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        --snip--

    def increase_speed(self):
        \"""提高速度设置和外星人分数。\"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

❷        self.alien_points = int(self.alien_points * self.score_scale)
        
这里定义了分数的提高速度，并称之为 score_scale（见❶）。较低的节奏加快速度（1.1）让游戏很快变得极具挑战性，
但为了让记分发生显著的变化，需要将分数的提高速度设置为更大的值（1.5）。现在，在加快游戏节奏的同时，提高了每
个外星人的分数（见❷）。为让分数为整数，使用了函数 int()。

为显示外星人的分数，在 Settings 的方法 increase_speed() 中调用函数 print()：

    def increase_speed(self):
        --snip--
        self.alien_points = int(self.alien_points * self.score_scale)
        print(self.alien_points)

现在每当提高一个等级时，你都将在终端窗口看到新的分数值。

注意：确认分数在不断增加后，一定要删除调用函数 print() 的代码，否则可能影响游戏的性能，分散玩家的注意力。



7、舍入得分

大多数街机风格的射击游戏将得分显示为 10 的整数倍，下面让记分系统遵循这个原则。这里还将设置得分的格式，在大数
中添加用逗号表示的千位分隔符。在 Scoreboard 中执行这种修改：

    def prep_score(self):
        \"""将得分转换为渲染的图像。\"""
        # score_str = str(self.stats.score)
        # self.score_image = self.font.render(score_str, True,
        #                     self.text_color, self.settings.bg_color)

❶        rounded_score = round(self.stats.score, -1)
❷        score_str = "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True,
                            self.text_color, self.settings.bg_color)

        --snip--

函数 round() 通常让小数精确到小数点后某一位，其中小数位数是由第二个实参指定的。然而，如果将第二个实参指定为
负数，round() 将舍入到最近的 10 的整数倍，如 10、100、1000 等。❶处的代码让 Python 将 stats.score
的值舍入到最近的 10 的整数倍，并将结果存储到 rounded_score 中。

在❷处，使用一个字符串格式设置指令，让 Python 将数值转换为字符串时在其中插入逗号。例如，输出为 1,000,000
而不是 1000000。如果现在运行这个游戏，看到的得分将是 10 的整数倍，即便得分很高亦如此。



8、最高得分

每个玩家都想超过游戏的最高得分纪录。下面来跟踪并显示最高得分，给玩家提供要超越的目标。这里将最高得分存储在
GameStats 中：

    def __init__(self, ai_game):
        --snip--
        # 任何情况下都不应重置最高得分。
        self.high_score = 0

因为在任何情况下都不会重置最高得分，所以在 __init__() 而不是 reset_stats() 中初始化 high_score。

下面来修改 Scoreboard 以显示最高得分。先来修改方法 __init__()：

    def __init__(self, ai_game):
        --snip--
        # 准备包含最高得分和当前得分的图像。
        self.prep_score()
❶        self.prep_high_score()

最高得分将与当前得分分开显示，因此需要编写一个新方法 prep_high_score()，用于准备包含最高得分的图像（见❶）。

方法 prep_high_score() 的代码如下：

    def prep_high_score(self):
        \"""将最高得分转换为渲染的图像。\"""
❶        high_score = round(self.stats.high_score, -1)
        high_score_str = "{:,}".format(high_score)
❷        self.high_score_image = self.font.render(high_score_str, True,
                                 self.text_color, self.settings.bg_color)

        # 将最高得分放在屏幕顶部中央。
        self.high_score_rect = self.high_score_image.get_rect()
❸        self.high_score_rect.centerx = self.screen_rect.centerx
❹        self.high_score_rect.top = self.score_rect.top

将最高得分舍入到最近的 10 的整数倍，并添加用逗号表示的千分位分隔符（见❶）。然后，根据最高得分生成一幅图像（见❷），
使其水平居中（见❸），并将其 top 属性设置为当前得分图像的 top 属性（见❹）。

现在，方法 show_score() 需要在屏幕右上角显示当前得分，并在屏幕顶部中央显示最高得分：

    def show_score(self):
        \"""在屏幕上显示得分。\"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)

为检查是否诞生了新的最高得分，在 Scoreboard 中添加一个新方法 check_high_score()：

    def check_high_score(self):
        \"""检查是否诞生了新的最高得分。\"""
        if self.stats.score > self.stats.high_score:
            self.stats.high_score = self.stats.score
            self.prep_high_score()



方法 check_high_score() 比较当前得分和最高得分。如果当前得分更高，就更新 high_score 的值，并调用 prep-
_high_score() 来更新包含最高得分的图像。

在 _check_bullet_alien_collisions() 中，每当有外星人被消灭时，都需要在更新得分后调用 check_high-
_score()：

    def _check_bullet_alien_collisions(self):
        --snip--
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_score()
            self.sb.check_high_score()
        --snip--

如果字典 collisions 存在，就根据消灭了多少外星人更新得分，再调用 check_high_score()。

第一次玩这个游戏时，当前得分就是最高得分，因此两个地方显示的都是当前得分。但再次开始该游戏时，最高得分会出现在
中央，而当前得分则出现在右边。



9、显示等级

为在游戏中显示玩家的等级，首先需要在 GameStats 中添加一个表示当前等级的属性。为确保每次开始新游戏时都重置等
级，在 reset_stats() 中初始化它：

    def reset_stats(self):
        \"""初始化在游戏运行期间可能变化的统计信息。\"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1

为了让 Scoreboard 显示当前等级，在 __init__() 中调用一个新方法 prep_level()：

    def __init__(self, ai_game):
        --snip--
        self.prep_high_score()
        self.prep_level()

prep_level() 的代码如下：

    def prep_level(self):
        \"""将等级转换为渲染的图像。\"""
        level_str = str(self.stats.level)
❶        self.level_image = self.font.render(level_str, True,
                            self.text_color, self.settings.bg_color)

        # 将等级放在得分下方。
        self.level_rect = self.level_image.get_rect()
❷        self.level_rect.right = self.score_rect.right
❸        self.level_rect.top = self.score_rect.bottom + 10

方法 prep_level() 根据存储在 stats.level 中的值创建一幅图像（见❶），并将其 right 属性设置为得分的
right 属性（见❷）。然后，将 top 属性设置为比得分图像的 bottom 属性大 10 像素，以便在得分和等级之间留
出一定的空间（见❸）。

还需要更新 show_score()：

    def show_score(self):
        \"""在屏幕上显示得分和等级。\"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)

新增的代码行在屏幕上显示等级图像。

这里在 _check_bullet_alien_collisions() 中提高等级并更新等级图像：

    def _check_bullet_alien_collisions(self):
        --snip--
        if not self.aliens:
            # 删除现有的所有子弹，并创建一群新的外星人。
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

            # 提高等级。
            self.stats.level += 1 
            self.sb.prep_level()

如果整群外星人都被消灭，就将 stats.level 的值加 1，并调用 prep_level() 确保正确地显示了新等级。

为确保在开始新游戏时更新等级图像，还需在玩家单击按钮 Play 时调用 prep_level()：

    def _check_play_button(self, mouse_pos):
        --snip--
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置。
            self.settings.initialize_dynamic_settings()
            # 重置游戏统计信息。
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            --snip--

这里在调用 prep_score() 后立即调用 prep_level()。


注意：在一些经典游戏中，得分带有标签，如 Score、HighScore 和 Level。这里没有显示这些标签，游戏开始后，
每个数的含义将一目了然。要包含这些标签，只需在 Scoreboard 中 调用 font.render() 前，将它们添加到得分
字符串中。



10、显示余下的飞船数

最后来显示玩家还有多少艘飞船，但使用图形而不是数字。为此，在屏幕左上角绘制飞船图像来指出还余下多少艘飞船，
就像众多经典的街机游戏中那样。

import pygame
from pygame.sprite import Sprite

❶ class Ship(Sprite):
    \"""管理飞船的类\"""

    def __init__(self, ai_game):
        \"""初始化飞船并设置其初始位置。\"""
❷        super().__init__()
        --snip--

这里导入了 Sprite，让 Ship 继承 Sprite（见❶），并在 __init__() 的开头调用 super()（见❷）。接下来，
需要修改 Scoreboard，以创建可供显示的飞船编组。下面是其中的 import 语句：

import pygame.font
from pygame.sprite import Group

from ship import Ship

鉴于需要创建飞船编组，导入 Group 和 Ship 类。

下面是方法__init__()：

    def __init__(self, ai_game):
        \"""初始化显示得分涉及的属性。\"""
        self.ai_game = ai_game
        self.screen = ai_game.screen
        --snip--
        self.prep_level()
        self.prep_ships()

这里将游戏实例赋给一个属性，因为创建飞船时需要用到它。在调用 prep_level() 后调用了 prep_ships()。

prep_ships() 的代码如下：

    def prep_ships(self):
        \"""显示还余下多少艘飞船。\"""
❶        self.ships = Group()
❷        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_game)
❸            ship.rect.x = 10 + ship_number * ship.rect.width
❹            ship.rect.y = 10
❺            self.ships.add(ship)

方法 prep_ships() 创建一个空编组 self.ships，用于存储飞船实例（见❶）。为填充这个编组，根据玩家还有多
少艘飞船以相应的次数运行一个循环（见❷）。在这个循环中，创建新飞船并设置其 x 坐标，让整个飞船编组都位于屏幕
左边，且每艘飞船的左边距都为 10 像素（见❸）。还将 y 坐标设置为离屏幕上边缘10像素，让所有飞船都出现在屏幕
左上角（见❹）。最后，将每艘新飞船都添加到编组 ships 中（见❺）。

现在需要在屏幕上绘制飞船了：

    def show_score(self):
        \"""在屏幕上绘制得分、等级和余下的飞船数。\"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)

为在屏幕上显示飞船，对编组调用 draw()。Pygame 将绘制每艘飞船。

为在游戏开始时让玩家知道自己有多少艘飞船，在开始新游戏时调用 prep_ships()。这是在 AlienInvasion 的
_check_play_button() 中进行的：

    def _check_play_button(self, mouse_pos):
        --snip--
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置。
            self.settings.initialize_dynamic_settings()
            # 重置游戏统计信息。
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_score()
            self.sb.prep_level()
            self.sb.prep_ships()
            --snip--

还要在飞船被外星人撞到时调用 prep_ships()，从而在玩家损失飞船时更新飞船图像：

    def _ship_hit(self):
        \"""响应飞船被外星人撞到。\"""
        if self.stats.ships_left > 0:
            # 将ships_left减1。
            self.stats.ships_left -= 1
            self.sb.prep_ships()
            --snip--

这里在将 ships_left 的值减 1 后调用 prep_ships()。这样每次损失飞船后，显示的飞船数都是正确的。

"""