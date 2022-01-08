"""

简单回顾


后续将添加射击功能，为此需要新增一个名为 bullet.py 的文件，并修改一些既有文件。当前有三个文件，其中包含很多类
和方法。添加其他功能之前，先来回顾一下这些文件，让你清楚这个项目的组织结构。



1、alien_invasion.py

主文件 alien_invasion.py 包含 AlienInvasion 类。这个类创建一系列贯穿整个游戏都要用到的属性：赋给 self
.settings 的设置，赋给 screen 中的主显示 surface，以及一个飞船实例。这个模块还包含游戏的主循环，即一个调
用 _check_events()、ship.update() 和 _update_screen() 的 while 循环。


方法 _check_events() 检测相关的事件（如按下和松开键盘），并通过调用方法 _check_keydown_events() 和
_check_keyup_events() 处理这些事件。当前，这些方法负责管理飞船的移动。AlienInvasion 类还包含方法
_update_screen()，该方法在每次主循环中重绘屏幕。

要玩游戏《外星人入侵》，只需运行文件 alien_invasion.py，其他文件（settings.py 和 ship.py）包含的代码会
被导入这个文件中。



2、settings.py

文件 settings.py 包含 Settings 类，这个类只包含方法 __init__()，用于初始化控制游戏外观和飞船速度的属性。



3、ship.py

文件 ship.py 包含 Ship 类，这个类包含方法 __init__()、管理飞船位置的方法 update() 和在屏幕上绘制飞船的
方法 blitme()。表示飞船的图像存储在文件夹 images 下的文件 ship.bmp 中。

"""