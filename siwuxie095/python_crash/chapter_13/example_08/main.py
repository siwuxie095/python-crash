"""

确定应运行游戏的哪些部分


这里需要确定游戏的哪些部分在任何情况下都应运行，哪些部分仅在游戏处于活动状态时才运行：

    def run_game(self):
        \"""开始游戏主循环。\"""
        while True:
            self._check_events()

            if self.stats.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()

在主循环中，在任何情况下都需要调用 _check_events()，即便游戏处于非活动状态。例如，这里需要知道玩家
是否按了Q 键以退出游戏，或者是否单击了关闭窗口的按钮。还需要不断更新屏幕，以便在等待玩家是否选择开始
新游戏时修改屏幕。其他的函数仅在游戏处于活动状态时才需要调用，因为游戏处于非活动状态时，不用更新游戏
元素的位置。

现在运行这个游戏，它将在飞船用完后停止不动。

"""