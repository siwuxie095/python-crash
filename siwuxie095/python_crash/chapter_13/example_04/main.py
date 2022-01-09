"""

创建一群外星人


要绘制一群外星人，需要确定一行能容纳多少个外星人以及要绘制多少行。这里将首先计算外星人的水平间距并创建一行
外星人，再确定可用的垂直空间并创建整群外星人。



1、确定一行可容纳多少个外星人

为确定一行可容纳多少个外星人，来看看可用的水平空间有多大。屏幕宽度存储在 settings.screen_width 中，但
需要在屏幕两边都留下一定的边距（将其设置为外星人的宽度）。因为有两个边距，所以可用于放置外星人的水平空间为
屏幕宽度减去外星人宽度的两倍：

available_space_x = settings.screen_width – (2 * alien_width)

还需要在外星人之间留出一定的空间，不妨将其定为外星人的宽度。因此，显示一个外星人所需的水平空间为外星人宽度
的两倍：一个宽度用于放置外星人，另一个宽度为外星人右边的空白区域。为确定一行可容纳多少个外星人，将可用空间
除以外星人宽度的两倍。这里使用整除（floor division）运算符 //，它将两个数相除并丢弃余数，得到一个表示
外星人个数的整数。

number_aliens_x = available_space_x // (2 * alien_width)

这里将在创建外星人群时使用这些公式。

注意：令人欣慰的是，在程序中执行计算时，无须在一开始确定公式是正确的，而是可以尝试运行程序，看看结果是否符
合预期。即便是在最坏的情况下，也只是屏幕上显示的外星人太多或太少。随后可根据在屏幕上看到的情况调整计算公式。



2、创建一行外星人

现在可以创建整行外星人了。由于创建单个外星人的代码管用，这里重写 _create_fleet() 使其创建一行外星人：

    def _create_fleet(self):
        \"""创建外星人群。\"""
        # 创建一个外星人并计算一行可容纳多少个外星人。
        # 外星人的间距为外星人宽度。
❶        alien = Alien(self)
❷        alien_width = alien.rect.width
❸        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 创建第一行外星人。
❹        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行。
            alien = Alien(self)
❺            alien.x = alien_width + 2 * alien_width * alien_number
            alien.rect.x = alien.x
            self.aliens.add(alien)

这些代码大多在前面详细介绍过。为放置外星人，需要知道外星人的宽度和高度，因此在执行计算前，创建一个外星人
（见❶）。这个外星人不是外星人群的成员，因此没有将其加入编组 aliens 中。在❷处，从外星人的 rect 属性
中获取外星人宽度，并将这个值存储到 alien_width 中，以免反复访问属性 rect。在❸处，计算可用于放置外星
人的水平空间以及其中可容纳多少个外星人。

接下来，编写一个循环，从零数到要创建的外星人数（见❹）。在这个循环中，创建一个新的外星人，并通过设置 x
坐标将其加入当前行（见❺）。将每个外星人都往右推一个外星人宽度。接下来，将外星人宽度乘以 2，得到每个外星
人占据的空间（其中包括右边的空白区域），再据此计算当前外星人在当前行的位置。这里使用外星人的属性 x 来设
置其 rect 的位置。最后，将每个新创建的外星人都添加到编组 aliens 中。

如果现在运行这个游戏，将看到第一行外星人。

这行外星人在屏幕上稍微偏向了左边、这实际上是有好处的，因为后面将让外星人群往右移，触及屏幕边缘后稍微往下
移，再往左移，依此类推。就像经典游戏《太空入侵者》，相比于只往下移，这种移动方式更为有趣。这里将让外星人
群不断这样移动，直到所有外星人都被击落，或者有外星人撞上飞船或抵达屏幕底端。



3、重构 _create_fleet()

倘若只需使用前面的代码就能创建外星人群，也许应该让 _create_fleet() 保持原样，但鉴于创建外星人群的工
作还未完成，这里稍微整理一下这个方法。为此，添加辅助方法 _create_alien()，并在 _create_fleet()
中调用它：

    def _create_fleet(self):
        --snip--
        # 创建第一行外星人。
        for alien_number in range(number_aliens_x):
            self._create_alien(alien_number)

    def _create_alien(self, alien_number):
        \"""创建一个外星人并将其放在当前行。\"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        self.aliens.add(alien)

除 self 外，方法 _create_alien() 还接受另一个参数，即要创建的外星人的编号。该方法的代码与 _create-
_fleet() 相同，但在内部获取外星人宽度，而不是将其作为参数传入。这样重构后，添加新行进而创建整群外星人将
更容易。



4、添加行

要创建外星人群，需要计算屏幕可容纳多少行，并将创建一行外星人的循环重复执行相应的次数。为计算可容纳的行数，
要先计算可用的垂直空间：用屏幕高度减去第一行外星人的上边距（外星人高度）、飞船的高度以及外星人群最初与飞
船之间的距离（外星人高度的两倍）：

available_space_y = settings.screen_height – (3 * alien_height) – ship_height

这将在飞船上方留出一定的空白区域，给玩家留出射杀外星人的时间。

每行下方都要留出一定的空白区域，不妨将其设置为外星人的高度。为计算可容纳的行数，将可用的垂直空间除以外星
人高度的两倍。这里使用整除，因为行数只能是整数。（同样，如果这样的计算不对，马上就能发现，继而将间距调整
为合理的值。）

number_rows = available_space_y // (2 * alien_height)

知道可容纳多少行之后，便可重复执行创建一行外星人的代码了：

    def _create_fleet(self):
        --snip--
        alien = Alien(self)
❶        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        # 计算屏幕可容纳多少行外星人。
        ship_height = self.ship.rect.height
❷        available_space_y = (self.settings.screen_height -
                              (3 * alien_height) - ship_height)
        number_rows = available_space_y // (2 * alien_height)

        # 创建外星人群。
❸        for row_number in range(number_rows):
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

    def _create_alien(self, alien_number, row_number):
        \"""创建一个外星人并将其放在当前行。\"""
        alien = Alien(self)
        alien_width = alien.rect.width
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
❹        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
        self.aliens.add(alien)

需要知道外星人的宽度和高度，因此在❶处使用了属性 size。该属性是一个元组，包含 rect 对象的宽度和高度。为
计算屏幕可容纳多少行外星人，在计算 available_space_x 的代码后面添加了计算 available_space_y 的代
码（见❷）。此处将计算公式用圆括号括起来，以便将代码分成两行，遵循每行不超过 79 字符的建议。

为创建多行外星人，使用了两个嵌套在一起的循环：一个外部循环和一个内部循环（见❸）。内部循环创建一行外星人，
而外部循环从零数到要创建的外星人行数：Python 将重复执行创建单行外星人的代码，重复次数为 number_rows。

为嵌套循环，编写了一个新的 for 循环，并缩进了要重复执行的代码。（在大多数文本编辑器中，缩进代码块和取消
缩进都很容易）。现在调用 _create_alien() 时，传递了一个表示行号的实参，将每行都沿屏幕依次向下放置。

在_create_alien() 的定义中，需要一个用于存储行号的形参。在 _create_alien() 中，修改外星人的坐标
（见❹）并在第一行外星人上方留出与外星人等高的空白区域。相邻外星人行的 y 坐标相差外星人高度的两倍，因此
将外星人高度乘以 2，再乘以行号。第一行的行号为 0，因此第一行的垂直位置不变，而其他行都沿屏幕依次向下放
置。

如果现在运行这个游戏，将看到一群外星人。后续将让外星人群动起来！

"""