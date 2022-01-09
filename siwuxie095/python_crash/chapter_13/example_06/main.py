"""

射杀外星人


这里创建了飞船和外星人群，但子弹击中外星人时将穿过外星人，因为还没有检查碰撞。在游戏编程中，碰撞指的是游戏元素
重叠在一起。要让子弹能够击落外星人，这里将使用 sprite.groupcollide() 检测两个编组的成员之间的碰撞。



1、检测子弹与外星人的碰撞

子弹击中外星人时，需要马上知道，以便碰撞发生后让子弹立即消失。为此，这里将在更新子弹的位置后立即检测碰撞。

函数 sprite.groupcollide() 将一个编组中每个元素的 rect 同另一个编组中每个元素的 rect 进行比较。在这里，
是将每颗子弹的 rect 同每个外星人的 rect 进行比较，并返回一个字典，其中包含发生了碰撞的子弹和外星人。在这个
字典中，每个键都是一颗子弹，而关联的值是被该子弹击中的外星人（后续实现记分系统时，也将使用该字典）。

在方法 _update_bullets() 末尾，添加如下检查子弹和外星人碰撞的代码：

    def _update_bullets(self):
        \"""更新子弹的位置并删除消失的子弹。\"""
        --snip--
        # 检查是否有子弹击中了外星人。
        # 如果是，就删除相应的子弹和外星人。
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

这些新增的代码将 self.bullets 中所有的子弹都与 self.aliens 中所有的外星人进行比较，看它们是否重叠在一起。
每当有子弹和外星人的 rect 重叠时，groupcollide() 就在它返回的字典中添加一个键值对。两个实参 True 让 Py-
game 删除发生碰撞的子弹和外星人。（要模拟能够飞行到屏幕顶端、消灭击中的每个外星人的高能子弹，可将第一个布尔实
参设置为 False，并保留第二个布尔参数为 True。这样被击中的外星人将消失，但所有的子弹都始终有效，直到抵达屏幕
顶端后消失。）

如果此时运行这个游戏，被击中的外星人将消失。即 有些外星人被射杀了。



2、为测试创建大子弹

只需运行这个游戏就可测试很多功能，但有些功能在正常情况下测试起来比较烦琐。例如，要测试代码能否正确处理外星人编
组为空的情形，需要花很长时间将屏幕上的外星人全部射杀。

测试有些功能时，可以修改游戏的某些设置，以便能够专注于游戏的特定方面。例如，可以缩小屏幕以减少需要射杀的外星人
数量，也可以提高子弹的速度，以便能够在单位时间内发射大量子弹。

测试这个游戏时，这里喜欢做的一项修改是，增大子弹的尺寸并使其在击中外星人后依然有效。请尝试将 bullet_width
设置为 300 乃至 3000，看看将所有外星人全部射杀有多快！

这样的修改可提高测试效率，还可能激发出如何赋予玩家更大威力的思想火花。（完成测试后，别忘了将设置恢复正常。）



3、生成新的外星人群

这个游戏的一个重要特点是，外星人无穷无尽：一群外星人被消灭后，又会出现另一群外星人。

要在一群外星人被消灭后再显示一群外星人，首先需要检查编组 aliens 是否为空。如果是，就调用 _create_fleet()。
这里将在 _update_bullets() 末尾执行这项任务，因为外星人都是在这里被消灭的：

    def _update_bullets(self):
        --snip--
❶        if not self.aliens:
            # 删除现有的子弹并新建一群外星人。
❷            self.bullets.empty()
            self._create_fleet()

在❶处，检查编组 aliens 是否为空。空编组相当于 False，因此这是一种检查编组是否为空的简单方式。如果编组 ali-
ens 为空，就使用方法 empty() 删除编组中余下的所有精灵，从而删除现有的所有子弹（见❷）。这里还调用了 _create-
_fleet() ，在屏幕上重新显示一群外星人。

现在，当前这群外星人被消灭干净后，将立刻出现一群新的外星人。



4、提高子弹的速度

如果现在尝试在游戏中射杀外星人，可能会发现子弹的速度不太合适（有点快或有点慢），游戏感不好。当前，可通过修改设
置让这款游戏更有意思、更好玩。

        # 子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 3
        --snip--

这项设置的最佳值取决于你使用的系统的速度，请找出适合自己的值。你也可以调整其他设置。



5、重构 _update_bullets()

下面来重构 _update_bullets()，使其不再执行那么多任务。为此，将处理子弹和外星人碰撞的代码移到一个独立的方法
中：

    def _update_bullets(self):
        --snip--
        # 删除消失的子弹。
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        \"""响应子弹和外星人碰撞。\"""
        # 删除发生碰撞的子弹和外星人。
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True)

        if not self.aliens:
            # 删除现有的所有子弹，并创建一群新的外星人。
            self.bullets.empty()
            self._create_fleet()

这里创建了一个新方法 _check_bullet_alien_collisions()，用于检测子弹和外星人之间的碰撞，并在整群外星人
被消灭干净时采取相应的措施。这能避免 _update_bullets() 过长，简化了后续开发工作。

"""