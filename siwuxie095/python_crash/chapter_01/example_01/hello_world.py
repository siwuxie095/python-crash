"""
在终端窗口（或命令行）中可以使用如下命令来检测是否安装了 python：
（1）python
（2）python --version
（3）python3
（4）python3 --version

其中：
（1）（2）用于检测是否安装了 Python 2
（3）（4）用于检测是否安装了 Python 3

另外：在终端窗口中输入（1）（3）会启动对应版本 Python 解释器，同时出现 Python 提示符，即 >>>，
让你输入 Python 命令，然后由 Python 解释器执行。

如果要退出 Python 并返回到终端窗口，可执行命令 exit()。



使用 Python 编写程序，文件名和文件夹名称最好使用小写字母，并使用下划线代替空格，因为 Python 采用
了这些命名约定。

当程序存在严重错误时，Python 将显示 traceback，即 错误报告。Python 会仔细研究文件，试图找出其中
的问题。traceback 可能会提供线索，让你知道是什么问题让程序无法运行。



从终端运行 Python 程序：

你编写的大多数程序将直接在文本编辑器中运行，但有时候从终端运行程序很有用。例如，你可能想直接运行既有
的程序。

在任何安装了 Python 的系统上都可以这样做，前提是你知道如何进入程序文件所在的目录。

大多数程序可直接从编辑器运行，但待解决的问题比较复杂时，你编写的程序可能需要从终端运行。

要运行 Python 程序，只需使用命令 python（或 python3）即可。如：python hello_word.py

PS：
（1）在 Windows 系统的命令窗口中，可以使用终端命令 cd（表示 change directory，即切换目录）在文件
系统中导航。使用命令 dir（表示 directory，即目录）可以显示当前目录中的所有文件。
（2）在 Linux 和 macOS 系统中，从终端运行 Python 程序的方式相同。在终端会话中，可以使用终端命令 cd
（表示 change directory，即切换目录 ）在文件系统中导航。使用命令 ls（表示 list，即列表）可以显示
当前目录中所有未隐藏的文件。

"""
print("Hello Python world!")