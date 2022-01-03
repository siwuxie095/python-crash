"""

写入文件


保存数据的最简单的方式之一是将其写入文件中。通过将输出写入文件，即便关闭包含程序输出的终端窗口，这些输出也
依然存在：可以在程序结束运行后查看这些输出，可以与别人分享输出文件，还可以编写程序来将这些输出读取到内存中
并进行处理。



1、写入空文件

要将文本写入文件，你在调用 open() 时需要提供另一个实参，告诉 Python 你要写入打开的文件。为明白其中的工
作原理，这里来将一条简单的消息存储到文件中，而不是将其打印到屏幕上：

filename = 'programming.txt'

❶ with open(filename, 'w') as file_object:
❷   file_object.write("I love programming.")

在本例中，调用 open() 时提供了两个实参（见❶）。第一个实参也是要打开的文件的名称。第二个实参（'w'）告诉
Python，要以写入模式打开这个文件。打开文件时，可指定读取模式（'r'）、写入模式（'w'）、附加模式（'a'）
或读写模式（'r+'）。如果省略了模式实参，Python 将以默认的只读模式打开文件。

如果要写入的文件不存在，函数 open() 将自动创建它。然而，以写入模式（'w'）打开文件时千万要小心，因为如果
指定的文件已经存在，Python 将在返回文件对象前清空该文件的内容。

在❷处，使用文件对象的方法 write() 将一个字符串写入文件。这个程序没有终端输出，但如果打开文件 programming
.txt，将看到其中包含如下一行内容：

I love programming.

相比于计算机中的其他文件，这个文件没有什么不同。你可以打开它、在其中输入新文本、复制其内容、将内容粘贴到其中，
等等。

注意：Python 只能将字符串写入文本文件。要将数值数据存储到文本文件中，必须先使用函数 str() 将其转换为字符
串格式。



2、写入多行

函数 write() 不会在写入的文本末尾添加换行符，因此如果写入多行时没有指定换行符，文件看起来可能不是你希望的
那样：

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.")
    file_object.write("I love creating new games.")

如果你打开 programming.txt，将发现两行内容挤在一起：

I love programming.I love creating new games.

要让每个字符串都单独占一行，需要在方法调用 write() 中包含换行符：

filename = 'programming.txt'

with open(filename, 'w') as file_object:
    file_object.write("I love programming.\n")
    file_object.write("I love creating new games.\n")

现在，输出出现在不同的行中：

I love programming.
I love creating new games.

像显示到终端的输出一样，还可以使用空格、制表符和空行来设置这些输出的格式。



3、附加到文件

如果要给文件添加内容，而不是覆盖原有的内容，可以以附加模式打开文件。以附加模式打开文件时，Python 不会在返回
文件对象前清空文件的内容，而是将写入文件的行添加到文件末尾。如果指定的文件不存在，Python 将为你创建一个空文
件。

下面来修改 write_message.py，在既有文件 programming.txt 中再添加一些你酷爱编程的原因：

filename = 'programming.txt'

❶ with open(filename, 'a') as file_object:
❷   file_object.write("I also love finding meaning in large datasets.\n")
    file_object.write("I love creating apps that can run in a browser.\n")

在❶处，打开文件时指定了实参 'a'，以便将内容附加到文件末尾，而不是覆盖文件原来的内容。在❷处，又写入了两行，
它们被添加到文件 programming.txt 末尾：

I love programming.
I love creating new games.
I also love finding meaning in large datasets.
I love creating apps that can run in a browser.

最终的结果是，文件原来的内容还在，后面则是刚添加的内容。

"""