"""

添加 Play 按钮


这里将添加一个 Play 按钮，它在游戏开始前出现，并在游戏结束后再次出现，让玩家能够开始新游戏。

当前，这个游戏在玩家运行 alien_invasion.py 时就开始了。下面让游戏一开始处于非活动状态，并提示玩家单击 Play
按钮来开始游戏。为此，像下面这样修改 GameStats 类的方法 __init__()：

    def __init__(self, ai_game):
        \"""初始化统计信息。\"""
        self.settings = ai_game.settings
        self.reset_stats()

        # 让游戏一开始处于非活动状态。
        self.game_active = False

现在，游戏一开始将处于非活动状态，待创建 Play 按钮后，玩家才能开始游戏。



1、创建 Button 类

由于 Pygame 没有内置创建按钮的方法，这里将编写一个 Button 类，用于创建带标签的实心矩形。你可在游戏中使用这些
代码来创建任何按钮。下面是 Button 类的第一部分，请将这个类保存为文件 button.py：

import pygame.font

class Button:

❶    def __init__(self, ai_game, msg):
        \"""初始化按钮的属性。\"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # 设置按钮的尺寸和其他属性。
❷        self.width, self.height = 200, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
❸        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中。
❹        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需创建一次。
❺        self._prep_msg(msg)

首先，导入模块 pygame.font，它让 Pygame 能够将文本渲染到屏幕上。方法 __init__() 接受参数 self、对象 ai-
_game 和 msg，其中 msg 是要在按钮中显示的文本（见❶）。设置按钮的尺寸（见❷），再通过设置 button_color，让
按钮的 rect 对象为亮绿色，并通过设置 text_color 让文本为白色。

在❸处，指定使用什么字体来渲染文本。实参 None 让 Pygame 使用默认字体，而 48 指定了文本的字号。为让按钮在屏幕
上居中，创建一个表示按钮的 rect 对象（见❹），并将其 center 属性设置为屏幕的 center 属性。

Pygame 处理文本的方式是，将要显示的字符串渲染为图像。在❺处，调用了 _prep_msg() 来处理这样的渲染。

_prep_msg() 的代码如下：

    def _prep_msg(self, msg):
        \"""将msg渲染为图像，并使其在按钮上居中。\"""
❶        self.msg_image = self.font.render(msg, True, self.text_color,
                                          self.button_color)
❷        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


方法 _prep_msg() 接受实参 self 以及要渲染为图像的文本（msg）。调用 font.render() 将存储在 msg 中的文本
转换为图像，再将该图像存储在 self.msg_image 中（见❶）。方法 font.render() 还接受一个布尔实参，该实参指定
开启还是关闭反锯齿功能（反锯齿让文本的边缘更平滑）。余下的两个实参分别是文本颜色和背景色。这里启用了反锯齿功能，
并将文本的背景色设置为按钮的颜色。（如果没有指定背景色，Pygame 渲染文本时将使用透明背景。）

在❷处，让文本图像在按钮上居中：根据文本图像创建一个 rect，并将其 center 属性设置为按钮的 center 属性。

最后，创建方法 draw_button()，用于将这个按钮显示到屏幕上：

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本。
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

这里调用 screen.fill() 来绘制表示按钮的矩形，再调用 screen.blit() 并向它传递一幅图像以及与该图像相关联的
rect，从而在屏幕上绘制文本图像。至此，Button 类便创建好了。



2、在屏幕上绘制按钮

这里将在 AlienInvasion 中使用 Button 类来创建一个 Play 按钮。首先，更新 import 语句：

--snip--
from game_stats import GameStats
from button import Button

只需要一个 Play 按钮，因此在 AlienInvasion 类的方法 __init__() 中创建它。可将这些代码放在方法 __init__()
的末尾：

    def __init__(self):
        --snip--
        self._create_fleet()

        # 创建Play按钮。
        self.play_button = Button(self, "Play")

这些代码创建一个标签为 Play 的 Button 实例，但没有将它显示到屏幕上。为显示该按钮，在 _update_screen() 对
其调用方法 draw_button()：

    def _update_screen(self):
        --snip--
        self.aliens.draw(self.screen)

        # 如果游戏处于非活动状态，就绘制Play按钮。
        if not self.stats.game_active:
            self.play_button.draw_button()

        pygame.display.flip()

为让 Play 按钮位于其他所有屏幕元素上面，在绘制其他所有游戏元素后再绘制这个按钮，然后切换到新屏幕。将这些代码放
在一个 if 代码块中，让按钮仅在游戏出于非活动状态时才出现。

如果现在运行这个游戏，将在屏幕中央看到一个 Play 按钮。



3、开始游戏

为在玩家单击 Play 按钮时开始新游戏，在 _check_events() 末尾 添加如下 elif 代码块，以监视与该按钮相关的鼠
标事件：

    def _check_events(self):
        \"""响应按键和鼠标事件。\"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                --snip--
❶            elif event.type == pygame.MOUSEBUTTONDOWN:
❷                mouse_pos = pygame.mouse.get_pos()
❸                self._check_play_button(mouse_pos)

无论玩家单击屏幕的什么地方，Pygame 都将检测到一个 MOUSEBUTTONDOWN 事件（见❶），但这里只想让这个游戏在玩家
用鼠标单击 Play 按钮时做出响应。为此，使用了 pygame.mouse.get_pos()，它返回一个元组，其中包含玩家单击时
鼠标的 x 坐标和 y 坐标（见❷）。将这些值传递给新方法 _check_play_button()（见❸）。

方法 _check_play_button() 的代码如下，将它放在 _check_events() 后面：

    def _check_play_button(self, mouse_pos):
        \"""在玩家单击Play按钮时开始新游戏。\"""
❶        if self.play_button.rect.collidepoint(mouse_pos):
            self.stats.game_active = True

这里使用了 rect 的方法 collidepoint() 检查鼠标单击位置是否在 Play 按钮的 rect 内（见❶）。如果是，就将
game_active 设置为 True，让游戏开始！

至此，现在应该能够开始这个游戏了。游戏结束时，应将 game_active 设置为 False，并重新显示 Play 按钮。



4、重置游戏

前面编写的代码只处理了玩家第一次单击 Play 按钮的情况，而没有处理游戏结束的情况，因为没有重置导致游戏结束的条件。

为在玩家每次单击 Play 按钮时都重置游戏，需要重置统计信息、删除现有的外星人和子弹、创建一群新的外星人并让飞船居
中，如下所示：

    def _check_play_button(self, mouse_pos):
        \"""在玩家单击Play按钮时开始新游戏。\"""
        if self.play_button.rect.collidepoint(mouse_pos):
            # 重置游戏统计信息。
❶            self.stats.reset_stats()
            self.stats.game_active = True

            # 清空余下的外星人和子弹。
❷            self.aliens.empty()
            self.bullets.empty()

            # 创建一群新的外星人并让飞船居中。
❸            self._create_fleet()
            self.ship.center_ship()

在❶处，重置游戏统计信息，给玩家提供三艘新飞船。接下来，将 game_active 设置为 True。这样，这个方法的代码执
行完毕后，游戏就将开始。清空编组 aliens 和 bullets（见❷），然后创建一群新的外星人并将飞船居中（见❸）。

现在，每当玩家单击 Play 按钮时，这个游戏都将正确地重置，让玩家想玩多少次就玩多少次！



5、将 Play 按钮切换到非活动状态

当前存在一个问题：即便 Play 按钮不可见，玩家单击其所在的区域时，游戏依然会做出响应。游戏开始后，如果玩家不小
心单击了 Play 按钮所处的区域，游戏将重新开始！

为修复这个问题，可让游戏仅在 game_active 为 False 时才开始：

    def _check_play_button(self, mouse_pos):
        \"""玩家单击Play按钮时开始新游戏。\"""
❶        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
❷        if button_clicked and not self.stats.game_active:
            # 重置游戏统计信息。
            self.stats.reset_stats()

            --snip--

标志 button_clicked 的值为 True 或 False（见❶）。仅当玩家单击了 Play 按钮且游戏当前处于非活动状态时，
游戏才重新开始（见❷）。要测试这种行为，可开始新游戏，并不断单击 Play 按钮所在的区域。如果一切都像预期的那样
工作，单击 Play 按钮所处的区域应该没有任何影响。



6、隐藏鼠标光标

为让玩家能够开始游戏，要让鼠标光标可见，但游戏开始后，光标只会添乱。为修复这种问题，需要在游戏处于活动状态时
让光标不可见。可在方法 _check_play_button() 末尾的 if 代码块中完成这项任务：

    def _check_play_button(self, mouse_pos):
        \"""玩家单击Play按钮时开始新游戏。\"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            --snip--
            # 隐藏鼠标光标。
            pygame.mouse.set_visible(False)

通过向 set_visible() 传递 False，让 Pygame 在光标位于游戏窗口内时将其隐藏起来。

游戏结束后，将重新显示光标，让玩家能够单击 Play 按钮来开始新游戏。相关的代码如下：

    def _ship_hit(self):
        \"""响应飞船被外星人撞到。\"""
        if self.stats.ships_left > 0:
            --snip--
        else:
            self.stats.game_active = False
            pygame.mouse.set_visible(True)

在 _ship_hit() 中，在游戏进入非活动状态后，立即让光标可见。关注这样的细节让游戏显得更专业，也让玩家能够专
注于玩游戏而不是去费力理解用户界面。

"""