"""

驾驶飞船


下面来让玩家能够左右移动飞船。这里将编写代码，在用户按左或右箭头键时做出响应。这里将首先专注于向右移动，再使用
同样的原理来控制向左移动。通过这样做，你将学会如何控制屏幕图像的移动。



1、响应按键

每当用户按键时，都将在 Pygame 中注册一个事件。事件都是通过方法 pygame.event.get() 获取的，因此需要在方法
_check_events() 中指定要检查哪些类型的事件。每次按键都被注册为一个 KEYDOWN 事件。

Pygame 检测到 KEYDOWN 事件时，需要检查按下的是否是触发行动的键。例如，如果玩家按下的是右箭头键，就增大飞船的
rect.centerx 值，将飞船向右移动：

def _check_events(self):
    \"""响应按键和鼠标事件。\"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
❶        elif event.type == pygame.KEYDOWN:
❷            if event.key == pygame.K_RIGHT:
                # 向右移动飞船。
❸                self.ship.rect.x += 1

在方法 _check_events() 中，为事件循环添加一个 elif 代码块，以便在 Pygame 检测到 KEYDOWN 事件时做出响应
（见❶）。这里检查按下键（event.key）是否是右箭头键（pygame.K_RIGHT）（见❷）。如果是，就将 self.ship.
rect.centerx 的值加 1，从而将飞船向右移动（见❸）。

如果现在运行 alien_invasion.py，则每按右箭头键一次，飞船都将向右移动 1 像素。这是一个开端，但并非控制飞船的
高效方式。下面来改进控制方式，允许持续移动。



2、允许持续移动

玩家按住右箭头键不放时，希望飞船不断向右移动，直到玩家松开为止。这里将让游戏检测 pygame.KEYUP 事件，以便知道
玩家何时松开右箭头键。然后，结合使用 KEYDOWN 和 KEYUP 事件以及一个名为 moving_right 的标志来实现持续移动。

当标志 moving_right 为 False 时，飞船不会移动。玩家按下右箭头键时，将该标志设置为 True，在玩家松开时将该
标志重新设置为 False。

飞船的属性都由 Ship 类控制，因此要给这个类添加一个名为 moving_right 的属性和一个名为 update() 的方法。方
法 update() 检查标志 moving_right 的状态。如果该标志为 True，就调整飞船的位置。这里将在 while 循环中调
用这个方法，以调整飞船的位置。

class Ship:
    \"""管理飞船的类\"""

    def __init__(self, ai_game):
        --snip--
        # 对于每艘新飞船，都将其放在屏幕底部的中央。
        self.rect.midbottom = self.screen_rect.midbottom

        # 移动标志。
❶        # self.moving_right = False

❷    def update(self):
        \"""根据移动标志调整飞船的位置。\"""
        if self.moving_right:
            self.rect.x += 1

    def blitme(self):
        --snip--

在方法 __init__() 中，添加属性 self.moving_right，并将其初始值设置为 False（见❶）。接下来，添加方法
update()，在前述标志为 True 时向右移动飞船（见❷）。方法 update() 将通过 Ship 实例来调用，因此不是辅助
方法。

接下来，需要修改 _check_events()，使其在玩家按下右箭头键时将 moving_right 设置为 True，并在玩家松开时
将 moving_right 设置为 False：

def _check_events(self):
    \"""响应按键和鼠标事件。\"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
❶                self.ship.moving_right = True
❷        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False

在❶处，修改游戏在玩家按下右箭头键时响应的方式：不直接调整飞船的位置，而只是将 moving_right 设置为 True。
在❷处，添加一个新的 elif 代码块，用于响应 KEYUP 事件：玩家松开右箭头键（K_RIGHT）时，将 moving_right
设置为 False。

最后，需要修改 run_game() 中的 while 循环，以便每次执行循环时都调用飞船的方法 update()：

def run_game(self):
    \"""开始游戏主循环。\"""
    while True:
        self._check_events()
        self.ship.update()
        self._update_screen()

飞船的位置将在检测到键盘事件后（但在更新屏幕前）更新。这样，玩家输入时，飞船的位置将更新，从而确保使用更新后的
位置将飞船绘制到屏幕上。

如果现在运行 alien_invasion.py 并按住右箭头键，飞船将持续向右移动，直到松开为止。



3、左右移动

现在飞船能够持续向右移动了，添加向左移动的逻辑也很容易。这里将再次修改 Ship 类和方法 _check_events()。下面
显示了对 Ship 类的方法 __init__() 和 update() 所做的相关修改：

    def __init__(self, ai_game):
        --snip--
        # 移动标志。
        self.moving_right = False
        self.moving_left = False

    def update(self):
        \"""根据移动标志调整飞船的位置。\"""
        if self.moving_right:
            self.rect.x += 1
        if self.moving_left:
            self.rect.x -= 1

在方法 __init__() 中，添加标志 self.moving_left。在方法 update() 中，添加一个 if 代码块而不是 elif
代码块，这样如果玩家同时按下了左右箭头键，将先增加再减少飞船的 rect.x 值，即飞船的位置保持不变。如果使用一个
elif 代码块来处理向左移动的情况，右箭头键将始终处于优先地位。从向左移动切换到向右移动时，玩家可能同时按住左右
箭头键，此时前面的做法让移动更准确。

还需对 _check_events() 做两方面的调整：

def _check_events(self):
    \"""响应按键和鼠标事件。\"""
    for event in pygame.event.get():
        --snip--
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right = False
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left = False

如果因玩家按下 K_LEFT 键而触发了 KEYDOWN 事件，就将 moving_left 设置为 True。如果因玩家松开 K_LEFT 而
触发了 KEYUP 事件，就将 moving_left 设置为 False。这里之所以可以使用 elif 代码块，是因为每个事件都只与一
个键相关联。如果玩家同时按下左右箭头键，将检测到两个不同的事件。

如果此时运行 alien_invasion.py，将能够持续左右移动飞船。如果同时按下左右箭头键，飞船将纹丝不动。

下面来进一步优化飞船的移动方式：调整飞船的速度，以及限制飞船的移动距离，以免其消失在屏幕之外。



4、调整飞船的速度

当前，每次执行 while 循环时，飞船最多移动 1 像素，但可在 Settings 类中添加属性 ship_speed，用于控制飞船
的速度。这里将根据这个属性决定飞船在每次循环时最多移动多远。下面演示了如何在 settings.py 中添加这个新属性：

class Settings:
    \"""存储游戏《外星人入侵》中所有设置的类\"""

    def __init__(self):
        --snip--
        
        # 飞船设置 
        self.ship_speed = 1.5

将 ship_speed 的初始值设置为 1.5。现在需要移动飞船时，每次循环将移动 1.5 像素而不是 1 像素。

通过将速度设置指定为小数值，可在后面加快游戏节奏时更细致地控制飞船的速度。然而，rect 的 x 等属性只能存储整数值，
因此需要对 Ship 类做些修改：

import pygame

class Ship:
    \"""管理飞船的类\"""

❶    def __init__(self, ai_game):
        \"""初始化飞船并设置其初始位置。\"""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        --snip--
       
        # 对于每艘新飞船，都将其放在屏幕底部的中央。
        --snip--

        # 在飞船的属性x中存储小数值。
❷        self.x = float(self.rect.x)

        # 移动标志。
        self.moving_right = False
        self.moving_left = False

    def update(self):
        \"""根据移动标志调整飞船的位置。\"""
        # 更新飞船而不是rect对象的x值。
        if self.moving_right:
❸            self.x += self.settings.ship_speed
        if self.moving_left:
            self.x -= self.settings.ship_speed

        # 根据self.x更新rect对象。
❹        self.rect.x = self.x

    def blitme(self):
        --snip--

在❶处，给 Ship 类添加属性 settings，以便能够在 update() 中使用它。鉴于现在调整飞船的位置时，将增减一个单位
为像素的小数值，因此需要将位置赋给一个能够存储小数值的变量。可使用小数来设置 rect 的属性，但 rect 将只存储这个
值的整数部分。为准确存储飞船的位置，定义一个可存储小数值的新属性 self.x（见❷）。使用函数 float() 将 self.
rect.x 的值转换为小数，并将结果赋给 self.x。

现在在 update() 中调整飞船的位置时，将 self.x 的值增减 settings.ship_speed 的值（见❸）。更新 self.x
后，再根据它来更新控制飞船位置的 self.rect.x（见❹）。self.rect.x 只存储 self.x 的整数部分，但对显示飞船
而言，这问题不大。

现在可以修改 ship_speed 的值了。只要它的值大于 1，飞船的移动速度就会比以前更快。这有助于让飞船的反应速度足够快，
以便射杀外星人，还能够随着游戏的进行加快游戏的节奏。

注意：如果你使用的是 macOS，可能发现即便 ship_speed 的值很大，飞船的移动速度还是很慢。要修复这种问题，可在全
屏模式下运行游戏，稍后就将实现这种功能。



5、限制飞船的活动范围

当前，如果玩家按住箭头键的时间足够长，飞船将飞到屏幕之外，消失得无影无踪。下面来修复这种问题，让飞船到达屏幕边缘
后停止移动。为此，将修改 Ship 类的方法 update()：

    def update(self):
        \"""根据移动标志调整飞船的位置。\"""
        # 更新飞船而不是rect对象的x值。
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        # 根据self.x更新rect对象。
        self.rect.x = self.x

上述代码在修改 self.x 的值之前检查飞船的位置。self.rect.right 返回飞船外接矩形右边缘的坐标。如果这个值小于
self.screen_rect.right 的值，就说明飞船未触及屏幕右边缘（见❶）。左边缘的情况与此类似：如果 rect 左边缘的
坐标大于零，就说明飞船未触及屏幕左边缘（见❷）。这确保仅当飞船在屏幕内时，才调整 self.x 的值。

如果此时运行 alien_invasion.py，飞船将在触及屏幕左边缘或右边缘后停止移动。真是太神奇了！只在 if 语句中添加
一个条件测试，就让飞船在到达屏幕左右边缘时像被墙挡住了一样。



6、重构 _check_events()

随着游戏的开发，方法 _check_events() 将越来越长。因此将其部分代码放在两个方法中，其中一个处理 KEYDOWN 事件，
另一个处理 KEYUP 事件：

def _check_events(self):
    \"""响应按键和鼠标事件。\"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            self._check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            self._check_keyup_events(event)

def _check_keydown_events(self, event):
    \"""响应按键。\"""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True

def _check_keyup_events(self, event):
    \"""响应松开。\"""
    if event.key == pygame.K_RIGHT:
        self.ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = False

这里创建了两个新的辅助方法：_check_keydown_events() 和 _check_keyup_events()。它们都包含形参 self
和 event。这两个方法的代码是从 _check_events() 中复制而来的，因此将方法 _check_events() 中相应的代码
替换成了对这两个新方法的调用。现在，方法 _check_events() 更简单，代码结构也更清晰，在其中响应玩家输入时将
更容易。



7、按 Q 键退出

能够高效地响应按键后，下面来添加另一种退出游戏的方式。当前，每次测试新功能时，都需要单击游戏窗口顶部的 X 按钮
来结束游戏，实在是太麻烦了。因此，这里来添加一个结束游戏的键盘快捷键 —— Q 键：

def _check_keydown_events(self, event):
    --snip--
    elif event.key == pygame.K_LEFT:
        self.ship.moving_left = True
    elif event.key == pygame.K_q:
        sys.exit()

在 _check_keydown_events() 中，添加一个代码块，用于在玩家按 Q 键时结束游戏。现在测试该游戏时，你可按 Q
键来结束游戏，而无须使用鼠标将窗口关闭。



8、在全屏模式下运行游戏

Pygame 支持全屏模式，你可能会更喜欢在这种模式下而非常规窗口中运行游戏。有些游戏在全屏模式下看起来更舒服，而在
macOS 系统中用全屏模式运行会提升性能。

要在全屏模式下运行该游戏，可在 __init__() 中做如下修改：

    def __init__(self):
        \"""初始化游戏并创建游戏资源。\"""
        pygame.init()
        self.settings = Settings()

❶        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
❷        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

创建屏幕时，传入了尺寸 (0, 0) 以及参数 pygame.FULLSCREEN（见❶）。这让 Pygame 生成一个覆盖整个显示器的
屏幕。由于无法预先知道屏幕的宽度和高度，要在创建屏幕后更新这些设置（见❷）：使用屏幕的 rect 的属性 width 和
height 来更新对象 settings。

如果你喜欢这款游戏在全屏模式下的外观和行为，请保留这些设置。如果你更喜欢这款游戏在独立的窗口中运行，可恢复到原
来采用的方法 —— 将屏幕尺寸设置为特定的值。

注意：在全屏模式下运行这款游戏之前，请确认能够按 Q 键退出，因为 Pygame 默认不提供在全屏模式下退出游戏的方式。

"""