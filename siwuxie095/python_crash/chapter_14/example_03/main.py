"""

提高等级


当前，将整群外星人消灭干净后，玩家将提高一个等级，但游戏的难度没变。下面来增加一点趣味性：每当玩家将屏幕上的外星人
消灭干净后，都加快游戏的节奏，让游戏玩起来更难。



1、修改速度设置

首先重新组织 Settings 类，将游戏设置划分成静态和动态两组。对于随着游戏进行而变化的设置，还要确保在开始新游戏时进
行重置。settings.py 的方法 __init__() 如下：

    def __init__(self):
        \"""初始化游戏的设置。\"""
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_limit = 3

        # 子弹设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # 外星人设置
        self.fleet_drop_speed = 10

        # 加快游戏节奏的速度。
❶        self.speedup_scale = 1.1

❷        self.initialize_dynamic_settings()

依然在 __init__() 中初始化静态设置。在❶处，添加设置 speedup_scale，用于控制游戏节奏的加快速度：2 表示玩家每
提高一个等级，游戏的节奏就翻一倍；1 表示游戏节奏始终不变。将其设置为 1.1 能够将游戏节奏提高到足够快，让游戏既有难
度又并非不可完成。最后，调用 initialize_dynamic_settings() 初始化随游戏进行而变化的属性（见❷）。

initialize_dynamic_settings() 的代码如下：

    def initialize_dynamic_settings(self):
        \"""初始化随游戏进行而变化的设置。\"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction为1表示向右，为-1表示向左。
        self.fleet_direction = 1

这个方法设置飞船、子弹和外星人的初始速度。随着游戏的进行，将提高这些速度。每当玩家开始新游戏时，都将重置这些速度。
在这个方法中，还设置了 fleet_direction，使得游戏刚开始时，外星人总是向右移动。不需要增大 fleet_drop_speed
的值，因为外星人移动的速度越快，到达屏幕底端所需的时间越短。

为在玩家的等级提高时提高飞船、子弹和外星人的速度，编写一个名为 increase_speed() 的新方法：

    def increase_speed(self):
        \"""提高速度设置\"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

为提高这些游戏元素的速度，将每个速度设置都乘以 speedup_scale 的值。

在 _check_bullet_alien_collisions() 中，在整群外星人都被消灭后调用 increase_speed() 来加快游戏的节奏：

    def _check_bullet_alien_collisions(self):
        --snip--
        if not self.aliens:
            # 删除现有的所有子弹，并创建一群新的外星人。
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()

通过修改速度设置 ship_speed、alien_speed 和 bullet_speed 的值，足以加快整个游戏的节奏！



2、重置速度

每当玩家开始新游戏时，都需要将发生了变化的设置重置为初始值，否则新游戏开始时，速度设置将为前一次提高后的值：

    def _check_play_button(self, mouse_pos):
        \"""玩家单击Play按钮时开始新游戏。\"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            # 重置游戏设置。
            self.settings.initialize_dynamic_settings()
            --snip--

现在，游戏《外星人入侵》玩起来更有趣，也更有挑战性了。每当玩家将屏幕上的外星人消灭干净后，游戏都将加快节奏，因此难
度更大。如果游戏的难度提高得太快，可降低 settings.speedup_scale 的值；如果游戏的挑战性不足，可稍微提高这个设
置的值。找出这个设置的最佳值，让难度的提高速度相对合理：一开始的几群外星人很容易消灭干净，接下来的几群消灭起来有一
定难度，但也不是不可能，而要将之后的外星人群消灭干净几乎不可能。

"""