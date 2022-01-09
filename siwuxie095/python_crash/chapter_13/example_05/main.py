"""

让外星人群移动


下面来让外星人群在屏幕上向右移动，撞到屏幕边缘后下移一定的量，再沿相反的方向移动。这里将不断移动所有的外星人，直到
外星人被全部消灭，或者有外星人撞上飞船或抵达屏幕底端。下面先让外星人向右移动。



1、向右移动外星人群

为移动外星人群，将使用 alien.py 中的方法 update()。对于外星人群中的每个外星人，都要调用它。首先，添加一个控制
外星人速度的设置：

    def __init__(self):
        --snip--
        # 外星人设置
        self.alien_speed = 1.0

再使用这个设置来实现 update()：

    def __init__(self, ai_game):
        \"""初始化外星人并设置其起始位置。\"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        --snip--

    def update(self):
        \"""向右移动外星人。\"""
❶        self.x += self.settings.alien_speed
❷        self.rect.x = self.x

在 __init__() 中添加了属性 settings，以便能够在 update() 中访问外星人的速度。每次更新外星人时，都将它向右
移动，移动量为 alien_speed 的值。这里使用属性 self.x 跟踪每个外星人的准确位置，该属性可存储小数值（见❶）。
然后，使用 self.x 的值来更新外星人的 rect 的位置（见❷）。

主 while 循环中已调用了更新飞船和子弹的方法，现在还需更调用更新每个外星人位置的方法：

        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_bullets()
            self._update_aliens()
            self._update_screen()

需要编写一些代码来管理外星人群的移动，因此新建一个名为 _update_aliens() 的方法。这里在更新子弹后再更新外星人
的位置，因为稍后要检查是否有子弹击中了外星人。

将这个方法放在模块的什么地方都无关紧要，但为确保代码组织有序，这里将它放在方法 _update_bullets() 的后面，以
便与 while 循环中的调用顺序一致。下面是 _update_aliens() 的第一版：

    def _update_aliens(self):
        \"""更新外星人群中所有外星人的位置。\"""
        self.aliens.update()

对编组调用方法 update()，这将自动对每个外星人调用方法 update()。如果现在运行这个游戏，你将看到外星人群向右移
动，并在屏幕右边缘消失。



2、创建表示外星人移动方向的设置

下面来创建让外星人撞到屏幕右边缘后向下移动、再向左移动的设置。实现这种行为的代码如下：

        # 外星人设置
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # fleet_direction为1表示向右移，为-1表示向左移。
        self.fleet_direction = 1

设置 fleet_drop_speed 指定有外星人撞到屏幕边缘时，外星人群向下移动的速度。将这个速度与水平速度分开是有好处的，
便于分别调整这两个速度。

要实现设置 fleet_direction，可将其设置为文本值，如 'left' 或 'right'，但这样就必须编写 if-elif 语句来检
查外星人群的移动方向。鉴于只有两个可能的方向，这里使用值 1 和 -1 来表示，并在外星人群改变方向时在这两个值之间切
换。（向右移时需要增大每个外星人的坐标，而向左移时需要减小每个外星人的坐标，因此使用数字来表示方向十分合理。）



3、检查外星人是否撞到了屏幕边缘

现在需要编写一个方法来检查外星人是否撞到了屏幕边缘，还需修改 update() 让每个外星人都沿正确的方向移动。这些代码
位于 Alien 类中：

    def check_edges(self):
        \"""如果外星人位于屏幕边缘，就返回True。\"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True

    def update(self):
        \"""向左或向右移动外星人。\"""
        self.x += (self.settings.alien_speed *
                   self.settings.fleet_direction)
        self.rect.x = self.x

可对任意外星人调用新方法 check_edges()，看其是否位于屏幕左边缘或右边缘。如果外星人的 rect 的属性 right 大于
或等于屏幕的 rect 的 right 属性，就说明外星人位于屏幕右边缘；如果外星人的 rect 的 left 属性小于或等于 0，就
说明外星人位于屏幕左边缘（见❶）。

这里修改方法 update()，将移动量设置为外星人速度和 fleet_direction 的乘积，让外星人向左或向右移动（见❷）。
如果 fleet_direction 为 1，就将外星人的当前坐标增大 alien_speed，从而将外星人向右移；如果 fleet_direc-
tion 为 -1，就将外星人的当前坐标减去 alien_speed，从而将外星人向左移。



4、向下移动外星人群并改变移动方向

有外星人到达屏幕边缘时，需要将整群外行星下移，并改变它们的移动方向。为此，需要在 AlienInvasion 中添加一些代码，
因为要在这里检查是否有外星人到达了左边缘或右边缘。这里编写方法 _check_fleet_edges() 和 _change_fleet_dir-
ection()，并且修改 _update_aliens()。这些新方法将放在 _create_alien() 后面，但其实放在 AlienInvasion
类中的什么位置都无关紧要：

    def _check_fleet_edges(self):
        \"""有外星人到达边缘时采取相应的措施。\"""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        \"""将整群外星人下移，并改变它们的方向。\"""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

在 _check_fleet_edges() 中，遍历外星人群并对其中的每个外星人调用 check_edges()（见❶）。如果 check_edges()
返回 True，就表明相应的外星人位于屏幕边缘，需要改变外星人群的方向，因此调用 _change_fleet_direction() 并退出
循环（见❷）。在 _change_fleet_direction() 中，遍历所有外星人，将每个外星人下移设置 fleet_drop_speed 的值
（见❸）。然后，将 fleet_direction 的值改为其当前值与 -1 的乘积。调整外星人群移动方向的代码行没有包含在 for 循
环中，因为要调整每个外星人的垂直位置，但只想调整外星人群移动方向一次。

下面显示了对 _update_aliens() 所做的修改：

    def _update_aliens(self):
        \"""
        检查是否有外星人位于屏幕边缘，
        并更新整群外星人的位置。
        \"""
        self._check_fleet_edges()
        self.aliens.update()

这里将方法 _update_aliens() 修改成了先调用 _check_fleet_edges()，再更新每个外星人的位置。

如果现在运行这个游戏，外星人群将在屏幕上来回移动，并在抵达屏幕边缘后向下移动。现在可以开始射杀外星人，并检查是否有外
星人撞到飞船或抵达了屏幕底端。



















"""