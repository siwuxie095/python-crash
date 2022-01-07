"""

重构：方法 _check_events() 和 _update_screen()


在大型项目中，经常需要在添加新代码前重构既有代码。重构旨在简化既有代码的结构，使其更容易扩展。本节将把越来越长
的方法 run_game() 拆分成两个辅助方法（helper method）。辅助方法在类中执行任务，但并非是通过实例调用的。
在 Python中，辅助方法的名称以单个下划线打头。



1、方法 _check_events()

这里将把管理事件的代码移到一个名为 _check_events() 的方法中，以简化 run_game() 并隔离事件管理循环。通过
隔离事件循环，可将事件管理与游戏的其他方面（如更新屏幕）分离。

下面是新增方法 _check_events() 后的 AlienInvasion 类，只有 run_game() 的代码受到影响：

def run_game(self):
    \"""开始游戏主循环。\"""
    while True:
❶        self._check_events()
        # 每次循环时都重绘屏幕。
        --snip--

❷ def _check_events(self):
    \"""响应按键和鼠标事件。\"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

新增方法 _check_events()（见❷），并将检查玩家是否单击了关闭窗口按钮的代码移到该方法中。

要调用当前类的方法，可使用句点表示法，并指定变量名 self 和要调用的方法的名称（见❶）。在 run_game() 的
while 循环中调用这个新增的方法。



2、方法 _update_screen()

为进一步简化 run_game()，将更新屏幕的代码移到一个名为 _update_screen() 的方法中：

def run_game(self):
    \"""开始游戏主循环。\"""
    while True:
        self._check_events()
        self._update_screen()

def _check_events(self):
    --snip--

def _update_screen(self):
    \"""更新屏幕上的图像，并切换到新屏幕。\"""
    self.screen.fill(self.settings.bg_color)
    self.ship.blitme()

    pygame.display.flip()

这里将绘制背景和飞船以及切换屏幕的代码移到了方法 _update_screen() 中。现在，run_game() 中的主循环简单多
了，很容易看出在每次循环中都检测了新发生的事件并更新了屏幕。

如果你开发过大量的游戏，可能早就开始像这样将代码放到不同的方法中了。不过如果你从未开发过这样的项目，可能不知道
如何组织代码。这里采用的做法是，先编写可行的代码，等代码越来越复杂时再进行重构，以向你展示真正的开发过程：先编
写尽可能简单的代码，等项目越来越复杂后对其进行重构。

对代码进行重构使其更容易扩展后，可以开始处理游戏的动态方面了！

"""